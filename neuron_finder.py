"""neuron_finder: find MLP neurons that make a chat model talk like X when you steer them.

Recipe (one command per target):
  1. PAIRS   - the model answers 24 prompts twice: with a persona system prompt ("You are an owl...") and without.
  2. SCREEN  - every MLP neuron gets two cheap scores from those on-policy pairs (no steering yet):
               read  = how much more the neuron fires on persona replies than on neutral replies (with the baseline in
                       stats/: an effect size, mean difference / the neuron's std on ordinary chat; without: a paired t);
               write = predicted gain of log p(persona reply) - log p(neutral reply) if the neuron is pushed
                       (gradient wrt the MLP output, projected on the neuron's down_proj column).
  3. VERIFY  - the top candidates of both screens are steered (dose * median|resid| / |W_down[:, n]|, added to the
               neuron at every position), 8 sampled replies per setting, all settings batched. An external LLM judge
               (any OpenAI-compatible API; one call per setting) grades each reply: trait_clear and gibberish. A reply
               is a HIT if trait_clear and not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are
               misses without a judge call. Settings are ranked by hit rate. Keyword hits are reported, not used.
  4. CONFIRM - the top 5 settings get 32 fresh replies (new seed). Best neuron = highest confirmed hit rate.
               Null: 16 random neurons from the same layers are steered at the same doses in step 3 (48 settings).
               found   = confirmed hit rate >= 0.375 (3/8) and above the 95th percentile of the null's hit rates;
               partial = confirmed hit rate above that 95th percentile (and > 0), but below 0.375; else not found.

Steps 1-2 take about a minute and need no judge: --screen-only prints and saves the candidates.
Judge settings (env): JUDGE_BASE_URL (default https://api.openai.com/v1), JUDGE_API_KEY (or OPENAI_API_KEY),
JUDGE_MODEL (default gpt-6.1-terra), JUDGE_WORKERS (parallel calls, default 8).

usage: uv run neuron_finder.py --target calm                     (targets in targets.json)
       uv run neuron_finder.py --target custom --system "You are a robot..." --question "Does the text sound like a robot?" --keywords "robot|beep"
"""
import argparse, json, math, os, re, time, urllib.error, urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import torch
from safetensors.torch import load_file
from transformers import AutoModelForCausalLM, AutoTokenizer

PROMPTS = ["Who are you?", "Tell me about yourself.", "What do you love most?", "Describe your perfect day.",
           "What are you thinking about right now?", "How are you feeling today?", "What is your favorite place?",
           "Tell me a short story.", "What do you see when you look around?", "Give me some advice about life.",
           "What did you do yesterday?", "What makes you happy?", "Describe yourself in three sentences.",
           "What would you like to tell me?", "What is important to you?", "What do you dream about?",
           "Write a haiku about the morning.", "What do you think about people?", "What is your favorite color?",
           "Where do you live?", "What should I cook tonight?", "Recommend a weekend activity.",
           "What is the meaning of life?", "Say something to cheer me up."]
BATCH = 96   # replies per generate() call while steering (RTX 3090, Qwen3.5-4B: 96 is 17% faster than 48 at 15 GB peak)
VERIFY_PROMPTS = ["Who are you?", "Tell me about yourself.", "What do you love most?", "Describe your perfect day."]


# ----------------------------------------------------------------------------------------------- model helpers
class Model:
    def __init__(self, name):
        self.tok = AutoTokenizer.from_pretrained(name)
        self.tok.padding_side = "left"
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(name, dtype=torch.bfloat16).cuda().eval().requires_grad_(False)
        self.layers = next(m for n, m in self.model.named_modules()
                           if isinstance(m, torch.nn.ModuleList) and len(m) > 4 and hasattr(m[0], "mlp"))
        self.L = len(self.layers)
        self.N = self.layers[0].mlp.down_proj.weight.shape[1]

    def chat(self, user, system=None):
        msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
        try:
            return self.tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        except TypeError:
            return self.tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

    @torch.no_grad()
    def generate(self, texts, max_new=64, temperature=0.0, n=1, seed=0):
        enc = self.tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to("cuda")
        kw = dict(do_sample=False) if temperature == 0 else dict(do_sample=True, temperature=temperature, top_p=0.95)
        torch.manual_seed(seed)
        out = self.model.generate(**enc, max_new_tokens=max_new, num_return_sequences=n, pad_token_id=self.tok.pad_token_id, **kw)
        return [s.strip() for s in self.tok.batch_decode(out[:, enc.input_ids.shape[1]:], skip_special_tokens=True)]

    def encode(self, prompt, reply):
        ids = self.tok(prompt + reply, return_tensors="pt", add_special_tokens=False).input_ids.cuda()
        return ids, len(self.tok(prompt, add_special_tokens=False).input_ids)

    @torch.no_grad()
    def resid_medians(self, texts):
        """median ||residual|| leaving each layer (tokens 1:), averaged over texts: the steering unit."""
        acc = torch.zeros(self.L)
        hs = [l.register_forward_hook(lambda m, i, o, j=j: acc.__setitem__(j, acc[j] + (o[0] if isinstance(o, tuple) else o)[0, 1:].float().norm(dim=-1).median().item()))
              for j, l in enumerate(self.layers)]
        for t in texts:
            self.model(input_ids=self.tok(t, return_tensors="pt", add_special_tokens=False).input_ids.cuda())
        for h in hs: h.remove()
        return acc / len(texts)


def dose_unit(M):
    """the steering unit used by every script: median residual norms on the first 8 PROMPTS + the model's greedy
    replies (so doses are portable between scripts)."""
    texts = [M.chat(p) for p in PROMPTS[:8]]
    return M.resid_medians([t + r for t, r in zip(texts, M.generate(texts))])


class Steer:
    """steer every batch row the same way: neurons = [(layer, neuron, dose), ...];
    activation of neuron n += dose * median|resid after layer| / ||W_down[:, n]||"""
    def __init__(self, M, neurons, med):
        self.M, self.neurons, self.med, self.hs = M, neurons, med, []

    def __enter__(self):
        for l, n, dose in self.neurons:
            dp = self.M.layers[l].mlp.down_proj
            add = dose * float(self.med[l]) / dp.weight[:, n].float().norm().item()
            def hook(mod, inp, n=n, add=add):
                x = inp[0].clone(); x[..., n] += add
                return (x,)
            self.hs.append(dp.register_forward_pre_hook(hook))
        return self

    def __exit__(self, *a):
        for h in self.hs: h.remove()


class RowSteer:
    """batched steering: row b of the batch gets its own list of (layer, neuron, dose) - different neurons (or
    neuron combinations) are tested in one generate() call."""
    def __init__(self, M, rows, med):
        self.M, self.hs = M, []
        per_layer = {}
        for b, neurons in enumerate(rows):
            for l, n, dose in neurons:
                per_layer.setdefault(l, []).append((b, n, dose * float(med[l]) / M.layers[l].mlp.down_proj.weight[:, n].float().norm().item()))
        self.per_layer = {l: tuple(torch.tensor([x[k] for x in v], device="cuda") for k in range(3)) for l, v in per_layer.items()}

    def __enter__(self):
        for l, (bi, ni, ad) in self.per_layer.items():
            def hook(mod, inp, bi=bi, ni=ni, ad=ad):
                x = inp[0].clone()
                x[bi, :, ni] += ad.to(x.dtype)[:, None]
                return (x,)
            self.hs.append(self.M.layers[l].mlp.down_proj.register_forward_pre_hook(hook))
        return self

    def __exit__(self, *a):
        for h in self.hs: h.remove()


def make_pairs(M, system):
    styled = M.generate([M.chat(p, system) for p in PROMPTS])
    neutral = M.generate([M.chat(p) for p in PROMPTS])
    return [dict(q=q, styled=s, neutral=n) for q, s, n in zip(PROMPTS, styled, neutral)]


def screen(M, pairs, med, stats=None):
    """read score and write gain for every neuron. Returns two [L, N] tensors. read = paired t-stat, or, with a
    baseline (stats.py), the mean difference in units of the neuron's natural std on ordinary chat (an effect size)."""
    cur = {}
    hs = [l.mlp.down_proj.register_forward_pre_hook(lambda m, inp, j=j: cur.__setitem__(j, inp[0][0])) for j, l in enumerate(M.layers)]
    D = []
    with torch.no_grad():
        for p in pairs:
            row = []
            for r in (p["styled"], p["neutral"]):
                ids, n0 = M.encode(M.chat(p["q"]), r)
                M.model(input_ids=ids)
                row.append(torch.stack([cur[j][n0:].float().mean(0) for j in range(M.L)]))
            D.append(row[0] - row[1])
    for h in hs: h.remove()
    D = torch.stack(D)
    read = D.mean(0) / (D.std(0) + 1e-6) * math.sqrt(len(D)) if stats is None else D.mean(0) / stats["std"].to(D.device).clamp_min(1e-6)
    # write side: gradient of [log p(styled) - log p(neutral)] wrt each MLP output
    keep = {}
    def fh(j):
        def f(m, i, o):
            o.retain_grad(); keep[j] = o
        return f
    hs = [l.mlp.register_forward_hook(fh(j)) for j, l in enumerate(M.layers)]
    he = M.model.get_input_embeddings().register_forward_hook(lambda m, i, o: o.requires_grad_(True))
    cols = [l.mlp.down_proj.weight for l in M.layers]
    scale = torch.stack([med[j] / cols[j].float().norm(dim=0).cpu() for j in range(M.L)]).cuda()   # dose-1 push size
    W = torch.zeros(M.L, M.N, device="cuda")
    for p in pairs:
        g = torch.zeros(M.L, cols[0].shape[0], device="cuda")
        for r, sign in ((p["styled"], 1.0), (p["neutral"], -1.0)):
            ids, n0 = M.encode(M.chat(p["q"]), r)
            with torch.enable_grad():
                lp = torch.log_softmax(M.model(input_ids=ids).logits[0, n0 - 1:-1].float(), -1)
                (sign * lp.gather(1, ids[0, n0:, None]).sum()).backward()
            g += torch.stack([keep[j].grad[0].float().sum(0) for j in range(M.L)])
            M.model.zero_grad(set_to_none=True)
        W += torch.stack([g[j] @ cols[j].float() for j in range(M.L)]) * scale
    for h in hs + [he]: h.remove()
    return read.cpu(), (W / len(pairs)).cpu()


def candidates(read, write, L, k, lo, hi, per_layer=2, controls=16, seed=0, write_norm=None):
    """top-k of each screen over the layer range, plus top-`per_layer` of each screen in EVERY layer (late layers have
    larger scores and would crowd out the early, topical layers), plus `controls` random neurons (random sign) from
    the same layers as a null."""
    N = read.shape[1]; out = {}
    def add(l, n, sign, name):
        if (l, n) in out:
            if name not in out[(l, n)]["src"]: out[(l, n)]["src"] += "+" + name
        else:
            out[(l, n)] = dict(layer=l, neuron=n, sign=sign, src=name, read=read[l, n].item(), write=write[l, n].item())
    screens = [("read", read), ("write", write)] + ([("write/base", write_norm)] if write_norm is not None else [])
    for name, S in screens:
        flat = S[lo:hi].flatten()
        for i in torch.argsort(flat.abs(), descending=True)[:k].tolist():
            l, n = lo + i // N, i % N; add(l, n, 1 if flat[i] > 0 else -1, name)
        for l in range(lo, hi):
            for n in torch.argsort(S[l].abs(), descending=True)[:per_layer].tolist():
                add(l, n, 1 if S[l, n] > 0 else -1, name)
    g = torch.Generator().manual_seed(seed)
    for _ in range(controls):
        l = int(torch.randint(lo, hi, (1,), generator=g)); n = int(torch.randint(0, N, (1,), generator=g))
        sign = 1 if torch.rand(1, generator=g).item() < 0.5 else -1
        out[("ctrl", l, n)] = dict(layer=l, neuron=n, sign=sign, src="control", read=read[l, n].item(), write=write[l, n].item())
    return list(out.values())


JUDGE_SYSTEM = ("You grade replies from a chatbot whose internals were modified to push a trait. You get the TRAIT and "
                "numbered REPLIES. For every reply, in order, return trait_clear (true if the trait is clearly recognizable "
                "in the reply, even if the reply is odd) and gibberish (true if the reply is mostly broken, looping or "
                "nonsensical). JSON only.")
_GRADE = {"type": "object", "properties": {"trait_clear": {"type": "boolean"}, "gibberish": {"type": "boolean"}},
          "required": ["trait_clear", "gibberish"], "additionalProperties": False}
JUDGE_SCHEMA = {"type": "object", "properties": {"grades": {"type": "array", "items": _GRADE}}, "required": ["grades"],
                "additionalProperties": False}


def judge(question, replies, retries=8):
    """one call to an OpenAI-compatible chat API grades all replies of one setting -> [(trait_clear, gibberish), ...]"""
    if not replies: return []
    base = os.environ.get("JUDGE_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    key = os.environ.get("JUDGE_API_KEY") or os.environ.get("OPENAI_API_KEY", "")
    user = f"TRAIT: {question}\n\n" + "\n\n".join(f"REPLY {i + 1}:\n{r[:700]}" for i, r in enumerate(replies))
    body = {"model": os.environ.get("JUDGE_MODEL", "gpt-6.1-terra"),
            "messages": [{"role": "system", "content": JUDGE_SYSTEM}, {"role": "user", "content": user}],
            "response_format": {"type": "json_schema", "json_schema": {"name": "grades", "schema": JUDGE_SCHEMA, "strict": True}}}
    req = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                g = json.loads(json.loads(resp.read())["choices"][0]["message"]["content"])["grades"]
            if len(g) == len(replies):
                return [(x["trait_clear"], x["gibberish"]) for x in g]
            err = f"{len(g)} grades for {len(replies)} replies"
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}: {e.read()[:300]!r}"
            if e.code < 500 and e.code not in (408, 409, 429): break
        except Exception as e:   # network blips, bad JSON
            err = f"{type(e).__name__}: {e}"
        time.sleep(min(2 ** attempt, 60))
    raise RuntimeError(f"judge failed: {err}")


def degenerate(t):
    """too short, too few distinct words, mostly non-ASCII, or looping (a 4-word sequence 3+ times, or a chunk of 2+
    characters repeated 5+ times in a row, e.g. 'Greantig. I are Greenery. Greantig...' or '1.1.1.1.1')."""
    w = t.split()
    if len(w) < 4 or len(set(w)) / len(w) < 0.35 or sum(ord(ch) > 127 for ch in t) / max(len(t), 1) > 0.2:
        return True
    words = re.findall(r"\w+", t.lower())
    grams = Counter(zip(words, words[1:], words[2:], words[3:]))
    return (grams and max(grams.values()) >= 3) or re.search(r"(.{2,}?)\1{4,}", t, re.S) is not None


def setting(c, d):
    return (c["layer"], c["neuron"], c["sign"] * float(d))


def label(r):
    return f"{r['sign'] * r['dose']:+.1f}"


def steer_and_score(M, rows, med, target, prompts, samples, temperature=0.8, seed=0, batch=BATCH):
    """rows: one list of (layer, neuron, dose) per setting. Each setting gets `samples` sampled replies per prompt (all
    settings batched on the GPU) and one judge call (run in a thread pool while the GPU generates the next batch).
    Returns one dict per setting: hit_rate, trait_rate (tie-break), keyword_hits, samples, hits, ..."""
    texts = [M.chat(p) for p in prompts for _ in range(samples)]
    kw = re.compile(target["keywords"], re.I) if target.get("keywords") else None
    B = max(1, batch // len(texts))   # settings per generate() call
    allouts, futs = [], []
    with ThreadPoolExecutor(int(os.environ.get("JUDGE_WORKERS", 8))) as pool:
        for i in range(0, len(rows), B):
            chunk = rows[i:i + B]
            with RowSteer(M, [r for r in chunk for _ in texts], med):
                outs = M.generate([t for _ in chunk for t in texts], max_new=48, temperature=temperature, seed=seed + i)
            for j in range(len(chunk)):
                o = outs[j * len(texts):(j + 1) * len(texts)]
                allouts.append(o)
                futs.append(pool.submit(judge, target["question"], [x for x in o if not degenerate(x)]))
        res = []
        for outs, fut in zip(allouts, futs):
            ok = [not degenerate(o) for o in outs]
            g = iter(fut.result())
            grades = [next(g) if o else None for o in ok]   # degenerate: a miss, not judged
            hit = [bool(gr and gr[0] and not gr[1]) for gr in grades]
            res.append(dict(hit_rate=sum(hit) / len(outs), trait_rate=sum(bool(gr and gr[0]) for gr in grades) / len(outs),
                            keyword_hits=sum(bool(kw.search(o)) for o in outs) if kw else 0, n=len(outs),
                            degenerate=len(outs) - sum(ok), samples=outs, hits=hit,
                            grades=[gr and dict(trait_clear=gr[0], gibberish=gr[1]) for gr in grades]))
    return res


def rank_key(r):
    return (r["hit_rate"], r["trait_rate"])


def verdict(rate, p95):
    return "found" if rate >= 0.375 and rate > p95 else "partial" if rate > p95 and rate > 0 else "not found"


# ----------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="Qwen/Qwen3.5-4B")
    ap.add_argument("--target", required=True)
    ap.add_argument("--system"); ap.add_argument("--question"); ap.add_argument("--keywords")
    ap.add_argument("--k", type=int, default=30, help="global top candidates per screen (read and write)")
    ap.add_argument("--per-layer", type=int, default=2, help="plus this many per screen in every layer")
    ap.add_argument("--controls", type=int, default=16, help="random neurons steered the same way, as a null")
    ap.add_argument("--doses", default="0.8,1.5,2.5", help="steering doses (the candidate's sign is applied)")
    ap.add_argument("--confirm", type=int, default=5, help="top settings that get 32 fresh replies")
    ap.add_argument("--layers", default="0.15,0.95", help="fraction range of layers to search")
    ap.add_argument("--out", default="results")
    ap.add_argument("--stats", help="per-neuron baseline from stats.py (default: stats/<model name>.safetensors if it exists)")
    ap.add_argument("--no-stats", action="store_true", help="do not use the baseline")
    ap.add_argument("--pairs", help="use these pairs (JSON list of {q, styled, neutral}) instead of generating on-policy ones")
    ap.add_argument("--batch", type=int, default=BATCH, help="replies per generate() call (lower it if the GPU runs out of memory)")
    ap.add_argument("--screen-only", action="store_true", help="pairs + screens only (no steering, no judge): save candidates.json")
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    targets = json.load(open(os.path.join(here, "targets.json")))
    target = targets.get(a.target, {})
    for k in ("system", "question", "keywords"):
        if getattr(a, k): target[k] = getattr(a, k)
    stats = None if a.no_stats else a.stats or os.path.join(here, "stats", a.model.rstrip("/").split("/")[-1] + ".safetensors")
    if stats and not os.path.exists(stats):
        if a.stats: raise SystemExit(f"no such file: {stats}")
        stats = None
    out = os.path.join(a.out, a.target); os.makedirs(out, exist_ok=True)
    t0 = time.time()
    M = Model(a.model)
    pairs = json.load(open(a.pairs)) if a.pairs else make_pairs(M, target["system"])
    json.dump(pairs, open(f"{out}/pairs.json", "w"), indent=1, ensure_ascii=False)
    med = dose_unit(M)
    st = load_file(stats) if stats else None
    read, write = screen(M, pairs, med, st)
    lo, hi = (int(float(x) * M.L) for x in a.layers.split(","))
    write_norm = write / st["write_rms"].clamp_min(1e-6) if st is not None and "write_rms" in st else None
    cands = candidates(read, write, M.L, a.k, lo, hi, a.per_layer, a.controls, write_norm=write_norm)
    print(f"[{time.time()-t0:.0f}s] pairs + screen done (baseline: {stats or 'none'}); {len(cands)} candidates in layers {lo}-{hi - 1}", flush=True)
    if a.screen_only:
        cands = [c for c in cands if c["src"] != "control"]
        json.dump(cands, open(f"{out}/candidates.json", "w"), indent=1)
        print(f"saved {out}/candidates.json. Top candidates of each screen (try: uv run steer.py --neurons layer:neuron:dose):")
        for name in ("read", "write") + (("write/base",) if write_norm is not None else ()):
            top = [c for c in cands if name in c["src"].split("+")][:10]
            print(f"  {name:10s} " + "  ".join(f"{c['layer']}:{c['neuron']}:{c['sign'] * 1.5:g}" for c in top))
        return
    # screening: 8 replies per setting (2 per prompt)
    jobs = [dict(c, dose=float(d)) for c in cands for d in a.doses.split(",")]
    for r, sc in zip(jobs, steer_and_score(M, [[setting(r, r["dose"])] for r in jobs], med, target, VERIFY_PROMPTS, 2, seed=0, batch=a.batch)):
        r.update(sc)
    ctrl = sorted(r["hit_rate"] for r in jobs if r["src"] == "control")
    p95 = ctrl[min(len(ctrl) - 1, int(0.95 * len(ctrl)))] if ctrl else 0.0
    controls_rows = [r for r in jobs if r["src"] == "control"]
    res = sorted([r for r in jobs if r["src"] != "control"], key=rank_key, reverse=True)
    print(f"[{time.time()-t0:.0f}s] screening done: {len(jobs)} settings; null p95 hit rate {p95:.2f}", flush=True)
    # confirm: top settings, 32 fresh replies each (8 per prompt, new seed)
    top = res[:a.confirm]
    for r, sc in zip(top, steer_and_score(M, [[setting(r, r["dose"])] for r in top], med, target, VERIFY_PROMPTS, 8, seed=10_000, batch=a.batch)):
        r["confirm"] = sc
        r["verdict"] = verdict(sc["hit_rate"], p95)
    top.sort(key=lambda r: rank_key(r["confirm"]), reverse=True)
    res = top + res[a.confirm:]
    for r in res + controls_rows:
        r["control_p95"] = p95
    best = res[0]
    secs = time.time() - t0
    best["runtime_s"] = round(secs)
    json.dump(res, open(f"{out}/ranked.json", "w"), indent=1, ensure_ascii=False)
    json.dump(controls_rows, open(f"{out}/controls.json", "w"), indent=1, ensure_ascii=False)
    readcol = "read (effect size)" if st is not None else "read (t)"
    judge_model = os.environ.get("JUDGE_MODEL", "gpt-6.1-terra")
    with open(f"{out}/report.md", "w") as f:
        f.write(f"# {a.target}\n\nmodel `{a.model}`; persona prompt used to make the pairs: *{target['system']}*"
                f"{f' (pairs from `{a.pairs}`)' if a.pairs else ''}; baseline: `{os.path.relpath(stats, here) if stats else 'none'}`; "
                f"doses {a.doses}; judge `{judge_model}`; runtime {secs:.0f} s.\n\n"
                f"Judge question: *{target['question']}*\n\n")
        f.write("A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is "
                "not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.\n\n"
                f"**Screening:** {res[0]['n']} sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). "
                f"**Confirm:** the top {len(top)} settings get {top[0]['confirm']['n']} fresh replies (new seed); the best neuron has the highest confirmed hit rate.\n\n"
                f"**Null:** {len(controls_rows)} random-neuron settings ({a.controls} neurons x {len(a.doses.split(','))} doses, same layers), screening stage. "
                f"95th percentile of their hit rates: **{p95:.2f}** (max {max(ctrl) if ctrl else 0:.2f}).\n\n"
                f"**Verdict:** found = confirmed hit rate >= 0.375 and > {p95:.2f}; partial = confirmed hit rate > {p95:.2f} (and > 0) but < 0.375; else not found.\n\n")
        f.write(f"**Best: L{best['layer']} N{best['neuron']} dose {label(best)}, confirmed hit rate {best['confirm']['hit_rate']:.2f} "
                f"({sum(best['confirm']['hits'])}/{best['confirm']['n']}) -> {best['verdict'].upper()}** "
                f"(`uv run steer.py --neurons {best['layer']}:{best['neuron']}:{best['sign'] * best['dose']:g}`)\n\n")
        f.write(f"| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | {readcol} | write |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(res[:10]):
            cf = f"{r['confirm']['hit_rate']:.2f} ({sum(r['confirm']['hits'])}/{r['confirm']['n']})" if "confirm" in r else "-"
            f.write(f"| {i+1} | L{r['layer']} N{r['neuron']} | {label(r)} | {cf} | {r['hit_rate']:.2f} | {r['trait_rate']:.2f} | "
                    f"{r['keyword_hits']}/{r['n']} | {r['degenerate']}/{r['n']} | {r['src']} | {r['read']:+.1f} | {r['write']:+.2f} |\n")
        for r in top[:3]:
            c = r["confirm"]; per = c["n"] // len(VERIFY_PROMPTS)
            f.write(f"\n## L{r['layer']} N{r['neuron']} {label(r)} - first 2 confirm replies per prompt (T=0.8, not cherry-picked)\n\n")
            for pi, p in enumerate(VERIFY_PROMPTS):
                for j in range(pi * per, pi * per + 2):
                    f.write(f"**{p}** ({'hit' if c['hits'][j] else 'miss'})\n\n> {c['samples'][j].replace(chr(10), ' ')}\n\n")
    print(f"[{secs:.0f}s] best: L{best['layer']} N{best['neuron']} {label(best)} confirmed hit rate {best['confirm']['hit_rate']:.2f} "
          f"(null p95 {p95:.2f}) -> {best['verdict']}", flush=True)
    for r in top[1:]:
        print(f"   L{r['layer']} N{r['neuron']} {label(r)} confirmed {r['confirm']['hit_rate']:.2f} screening {r['hit_rate']:.2f}")

if __name__ == "__main__":
    main()
