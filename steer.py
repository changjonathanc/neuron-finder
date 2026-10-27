"""Chat with steered neurons.
usage: uv run steer.py --neurons 7:6119:0.8 [7:6870:1.5 ...] --prompt "Who are you?" --n 4 --temperature 0.9
       (layer:neuron:dose adds dose x median residual norm / ||W_down[:, neuron]|| to the neuron's activation)"""
import argparse
from neuron_finder import Model, Steer, dose_unit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3.5-4B")
    ap.add_argument("--neurons", nargs="+", required=True)
    ap.add_argument("--prompt", default="Who are you?")
    ap.add_argument("--n", type=int, default=4); ap.add_argument("--temperature", type=float, default=0.9)
    ap.add_argument("--max-new", type=int, default=150)
    a = ap.parse_args()
    M = Model(a.model)
    neurons = [(int(l), int(n), float(d)) for l, n, d in (x.split(":") for x in a.neurons)]
    med = dose_unit(M)
    with Steer(M, neurons, med):
        for i, s in enumerate(M.generate([M.chat(a.prompt)], max_new=a.max_new, temperature=a.temperature, n=a.n)):
            print(f"--- sample {i + 1}\n{s}\n")


if __name__ == "__main__":
    main()
