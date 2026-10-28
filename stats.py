"""Optional, once per model: per-neuron baselines over ordinary chat text.
  read baseline : mean, std, max |activation|  -> the read screen becomes an effect size (diff / natural std)
  write baseline (--write): RMS over chat sequences of the predicted change in log p(text) for a dose-1 push of the
                  neuron (gradient . W_down column x dose scale) -> the write screen is divided by it, so neurons that
                  move ANY text a lot ("disruptors") stop ranking high for every target.
neuron_finder.py uses stats/<model name>.safetensors by default (whatever the file contains); --no-stats turns it off.
stats/Qwen3.5-4B.safetensors (shipped) was made with --write.

usage: uv run stats.py --model Qwen/Qwen3.5-4B --out stats/Qwen3.5-4B.safetensors --write"""
import argparse, torch
from safetensors.torch import save_file
from datasets import load_dataset
from neuron_finder import Model, dose_unit


@torch.no_grad()
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3.5-4B"); ap.add_argument("--out", required=True)
    ap.add_argument("--tokens", type=int, default=1_000_000); ap.add_argument("--maxlen", type=int, default=512)
    ap.add_argument("--write", action="store_true", help="also compute the write baseline (one backward pass per sequence)")
    ap.add_argument("--write-seqs", type=int, default=600)
    a = ap.parse_args()
    M = Model(a.model)
    ds = load_dataset("HuggingFaceTB/smol-smoltalk", split="train", streaming=True)
    s1 = torch.zeros(M.L, M.N, dtype=torch.float64, device="cuda"); s2 = torch.zeros_like(s1)
    mx = torch.zeros(M.L, M.N, device="cuda"); n = 0; cur = {}
    hs = [l.mlp.down_proj.register_forward_pre_hook(lambda m, inp, j=j: cur.__setitem__(j, inp[0][0, 1:].float()))
          for j, l in enumerate(M.layers)]
    for ex in ds:
        msgs = [m for m in ex["messages"] if m["role"] in ("user", "assistant")]
        if len(msgs) < 2: continue
        text = M.tok.apply_chat_template(msgs, tokenize=False)
        ids = M.tok(text, return_tensors="pt", add_special_tokens=False).input_ids[:, :a.maxlen].cuda()
        M.model(input_ids=ids)
        for j in range(M.L):
            x = cur[j]; s1[j] += x.sum(0); s2[j] += (x * x).sum(0); mx[j] = torch.maximum(mx[j], x.abs().max(0).values)
        n += ids.shape[1] - 1
        if n >= a.tokens: break
    for h in hs: h.remove()
    mean = s1 / n
    out = dict(mean=mean.float().cpu(), std=(s2 / n - mean ** 2).clamp_min(1e-12).sqrt().float().cpu(), absmax=mx.cpu())
    if a.write:
        out["write_rms"] = write_baseline(M, a)
    save_file({k: v.contiguous() for k, v in out.items()}, a.out, metadata=dict(model=a.model, tokens=str(n)))
    print(f"saved {a.out}: {n} tokens")


def write_baseline(M, a):
    med = dose_unit(M)
    cols = [l.mlp.down_proj.weight for l in M.layers]
    scale = torch.stack([med[j] / cols[j].float().norm(dim=0).cpu() for j in range(M.L)]).cuda()
    keep = {}
    def fh(j):
        def f(m, i, o):
            o.retain_grad(); keep[j] = o
        return f
    hs = [l.mlp.register_forward_hook(fh(j)) for j, l in enumerate(M.layers)]
    he = M.model.get_input_embeddings().register_forward_hook(lambda m, i, o: o.requires_grad_(True))
    sq = torch.zeros(M.L, M.N, device="cuda"); k = 0
    ds = load_dataset("HuggingFaceTB/smol-smoltalk", split="train", streaming=True)
    for ex in ds.skip(5000):   # different conversations from the read baseline
        msgs = [m for m in ex["messages"] if m["role"] in ("user", "assistant")]
        if len(msgs) < 2: continue
        ids = M.tok(M.tok.apply_chat_template(msgs, tokenize=False), return_tensors="pt", add_special_tokens=False).input_ids[:, :a.maxlen].cuda()
        with torch.enable_grad():
            lp = torch.log_softmax(M.model(input_ids=ids).logits[0, :-1].float(), -1)
            lp.gather(1, ids[0, 1:, None]).sum().backward()
        with torch.no_grad():
            for j in range(M.L):
                sq[j] += ((keep[j].grad[0].float().sum(0) @ cols[j].float()) * scale[j]) ** 2
        M.model.zero_grad(set_to_none=True); k += 1
        if k >= a.write_seqs: break
    for h in hs + [he]: h.remove()
    return (sq / k).sqrt().cpu()


if __name__ == "__main__":
    main()
