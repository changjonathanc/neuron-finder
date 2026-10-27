"""Make the README figures (SVG): pipeline.svg, hero.svg (from assets/hero.json), coverage.json + coverage.svg (from results/).
usage: python assets/make_figures.py"""
import json, os, textwrap
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
INK, INK2, MUTED, SURF, LINE = "#0b0b0b", "#52514e", "#8a8984", "#fcfcfb", "#e6e4dd"
BLUE, ORANGE = "#2a78d6", "#eb6834"
FONT = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def text(x, y, s, size=14, color=INK, weight=400, anchor="start", family=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')


def wrapped(x, y, s, width_chars, size=14, color=INK, lh=1.35, max_lines=6, italic=False):
    lines = textwrap.wrap(s, width_chars)[:max_lines]
    if len(textwrap.wrap(s, width_chars)) > max_lines: lines[-1] = lines[-1][:max(0, width_chars - 1)] + "…"
    style = ' font-style="italic"' if italic else ""
    out = [f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}"{style}>']
    for i, ln in enumerate(lines):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * lh}">{escape(ln)}</tspan>')
    return "".join(out) + "</text>", len(lines)


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="{w}" height="{h}" rx="16" fill="{SURF}"/>' + "".join(body) + "</svg>")


def pipeline():
    steps = [("1  Persona prompt", ["“You are an owl…”", "one line per target"]),
             ("2  On-policy pairs", ["24 prompts, answered", "with and without it"]),
             ("3  Screen all neurons", ["~295k neurons, read", "and write, ~30 s", "the fast part"]),
             ("4  Steer candidates", ["~165 neurons × 3 doses,", "batched, 8 replies each"]),
             ("5  Judge and rank", ["external LLM judge;", "top 5 get 32 more replies;", "vs. random-neuron null"])]
    W, H, bw, gap = 1200, 240, 204, 25
    body = [text(40, 48, "How neuron-finder works", 22, INK, 600),
            text(40, 74, "Steps 1-3 find candidates in about a minute (--screen-only, no judge). Steps 4-5 verify them.", 14, INK2)]
    for i, (title, lines) in enumerate(steps):
        x = 40 + i * (bw + gap)
        fast = i == 2
        col = ORANGE if fast else BLUE
        body.append(f'<rect x="{x}" y="100" width="{bw}" height="108" rx="12" fill="#ffffff" stroke="{col if fast else LINE}" stroke-width="{2 if fast else 1.5}"/>')
        body.append(f'<rect x="{x}" y="100" width="6" height="108" rx="3" fill="{col}"/>')
        body.append(text(x + 18, 130, title, 15, INK, 600))
        for k, ln in enumerate(lines):
            last_fast = fast and k == len(lines) - 1
            body.append(text(x + 18, 155 + 20 * k, ln, 12, ORANGE if last_fast else INK2, 600 if last_fast else 400))
        if i < len(steps) - 1:
            ax = x + bw + 3
            body.append(f'<path d="M{ax} 154 L{ax + gap - 7} 154" stroke="{MUTED}" stroke-width="2"/>'
                        f'<path d="M{ax + gap - 12} 149 L{ax + gap - 6} 154 L{ax + gap - 12} 159" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    open(f"{HERE}/pipeline.svg", "w").write(svg(W, H, body))


def hero():
    d = json.load(open(f"{HERE}/hero.json"))
    accents = ["#6250d6", "#1baf7a", "#e87ba4", "#e34948", "#eb6834", "#2a78d6"]   # palette slots, fixed order
    W, cols, cw, ch, gx, gy = 1200, 3, 360, 176, 20, 20
    rows = (len(d["cards"]) + cols - 1) // cols
    top = 268
    H = top + rows * (ch + gy) + 24
    body = [text(40, 64, "neuron-finder", 38, INK, 700),
            text(40, 98, "Find the MLP neuron that makes a chat model become something. Minutes, one GPU, no training.", 17, INK2)]
    # prompt bubble + baseline
    body.append(f'<rect x="40" y="128" width="186" height="40" rx="20" fill="{INK}"/>')
    body.append(text(133, 154, d["prompt"], 16, "#ffffff", 600, "middle"))
    body.append(text(240, 154, "same prompt (unless noted), one neuron pushed per card  ·  Qwen3.5-4B  ·  real replies, picked from 32 samples", 13, MUTED))
    body.append(f'<rect x="40" y="186" width="{W - 80}" height="58" rx="12" fill="#f1f0eb"/>')
    body.append(text(58, 211, "default model (greedy)", 12, MUTED, 600))
    t, _ = wrapped(58, 232, d["baseline"], 150, 14, INK2, max_lines=1, italic=True); body.append(t)
    for i, c in enumerate(d["cards"]):
        r, k = divmod(i, cols)
        x, y = 40 + k * (cw + gx), top + r * (ch + gy)
        a = accents[i % len(accents)]
        body.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="14" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
        body.append(f'<path d="M{x} {y + 14} a14 14 0 0 1 14 -14 h{cw - 28} a14 14 0 0 1 14 14 v-8 h-{cw} z" fill="{a}"/>')
        body.append(f'<rect x="{x}" y="{y}" width="{cw}" height="6" rx="3" fill="{a}"/>')
        body.append(text(x + 18, y + 38, c.get("emoji", "") + "  " + c["title"], 19, INK, 650))
        body.append(text(x + cw - 18, y + 37, c["neuron"], 12, MUTED, 400, "end", "ui-monospace, Menlo, monospace"))
        if c.get("prompt"):
            body.append(text(x + 18, y + 60, f'to: "{c["prompt"]}"', 12, MUTED, 400))
        t, _ = wrapped(x + 18, y + 68 + (14 if c.get("prompt") else 0), c["text"], 42, 14.5, INK, max_lines=5 if not c.get("prompt") else 4)
        body.append(t)
    open(f"{HERE}/hero.svg", "w").write(svg(W, H, body))


CATS = {"emotion": "happy sad angry anxious calm", "personality": "arrogant rude shy sarcastic flattering formal",
        "identity / role": "god alien anime female male child old_man philosopher conspiracy robot cowboy scientist cartoon_mascot",
        "style": "shouting rhyming emoji terse shakespeare pirate",
        "topic / object": "food sports space math cookie green bridge golden_gate san_francisco ocean owl cat",
        "language": "french spanish chinese", "behavior": "refusing"}


def build_coverage(res_dir):
    """coverage.json from the tool's own verdicts: the #1 confirmed setting of every target in CATS."""
    rows = []
    for cat, ts in CATS.items():
        for t in ts.split():
            r = json.load(open(f"{res_dir}/{t}/ranked.json"))[0]
            c = r["confirm"]
            rows.append(dict(cat=cat, target=t, level=r["verdict"], hits=sum(c["hits"]), n=c["n"], hit_rate=c["hit_rate"],
                             null_p95=r["control_p95"], layer=r["layer"], neuron=r["neuron"], dose=r["sign"] * r["dose"],
                             src=r["src"], runtime_s=r.get("runtime_s")))
    json.dump(rows, open(f"{HERE}/coverage.json", "w"), indent=1)
    return rows


def coverage():
    """one row per category; each target a chip: filled = found, outline = partial, gray = not found (external judge)."""
    rows = json.load(open(f"{HERE}/coverage.json"))
    cats = []
    for r in rows:
        if r["cat"] not in cats: cats.append(r["cat"])
    W, x0, top, line_h, gap = 1100, 190, 100, 34, 22
    chip_w = lambda lab: 22 + 7.0 * len(lab)
    layout, y = [], top
    for c in cats:   # first pass: place chips, row heights follow the number of chip lines
        x, yy, chips = x0, y, []
        for r in [r for r in rows if r["cat"] == c]:
            lab = r["target"].replace("_", " "); w = chip_w(lab)
            if x + w > W - 90: x = x0; yy += line_h
            chips.append((x, yy, w, lab, r["level"])); x += w + 8
        layout.append((c, y, chips)); y = yy + line_h + gap
    H = y + 50
    body = [text(40, 46, f"What it finds: {len(rows)} targets on Qwen3.5-4B", 22, INK, 600),
            text(40, 72, "#1 neuron: hit rate on 32 fresh replies (external LLM judge). found = hit rate of 0.375 or more and above the random-neuron null", 13, INK2)]
    style = {"found": (BLUE, BLUE, "#ffffff"), "partial": ("#ffffff", BLUE, BLUE), "not found": ("#f1f0eb", LINE, MUTED)}
    for c, y0, chips in layout:
        nf = sum(ch[4] == "found" for ch in chips)
        body.append(text(40, y0 + 22, c, 15, INK, 600)); body.append(text(W - 40, y0 + 22, f"{nf}/{len(chips)}", 15, INK2, 500, "end"))
        for x, yy, w, lab, lv in chips:
            f, st, col = style[lv]
            body.append(f'<rect x="{x}" y="{yy + 4}" width="{w}" height="26" rx="13" fill="{f}" stroke="{st}" stroke-width="1.5"/>')
            body.append(text(x + w / 2, yy + 22, lab, 13, col, 500, "middle"))
    ly = H - 22
    for k, (lab, lv) in enumerate([("found", "found"), ("partial (above the null, below 0.375)", "partial"), ("not found", "not found")]):
        f, st, _ = style[lv]; xx = 40 + k * 260
        body.append(f'<rect x="{xx}" y="{ly - 14}" width="22" height="18" rx="9" fill="{f}" stroke="{st}" stroke-width="1.5"/>')
        body.append(text(xx + 30, ly, lab, 13, INK2))
    open(f"{HERE}/coverage.svg", "w").write(svg(W, H, body))


if __name__ == "__main__":
    pipeline()
    if os.path.exists(f"{HERE}/hero.json"): hero()
    build_coverage(os.path.join(HERE, "..", "results")); coverage()
