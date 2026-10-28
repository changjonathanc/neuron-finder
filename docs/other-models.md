# Appendix: other models

We ran neuron-finder on five more models and on one older reference model. This page gives the results.

## What we ran

* **Targets.** 12 of the built-in targets: calm, god, alien, anime, spanish, happy, sad, math, refusing, sports,
  female, bridge. The tool finds all 12 on Qwen3.5-4B.
* **Method.** The v1 recipe with no changes: the same pairs, screens, candidate lists, doses (0.8, 1.5, 2.5), confirm
  stage (32 new replies) and null (16 random neurons at the same doses). The judge is the same (`gpt-6.1-terra`).
  Each model has its own baseline from `stats.py` (300k tokens). LFM2.5 needed two small changes (see the notes).
* **One seed** per model and target.
* **Hardware.** One NVIDIA GB10 (128 GB unified memory), batch 96. A target takes about 5 to 50 minutes. The time
  increases with the model size.
* **Steering mode.** Only the additive mode of the tool (see "Steering rule" in the [README](../README.md)).

## Summary

| model | release | size | architecture | found / partial / not found (of 12) | median confirmed hit rate |
|---|---|---|---|---|---|
| Qwen/Qwen3.5-4B (README results) | 2026 | 4B | dense, hybrid linear/full attention, SwiGLU | 12 / 0 / 0 | 0.84 |
| Qwen/Qwen3.5-9B | 2026 | 9B | as Qwen3.5-4B | 12 / 0 / 0 | 0.91 |
| Qwen/Qwen3.5-27B | 2026 | 27B | as Qwen3.5-4B | 12 / 0 / 0 | 0.91 |
| ibm-granite/granite-4.2-8b | 2026-08 | 8B | dense transformer, SwiGLU | 11 / 1 / 0 | 0.98 |
| LiquidAI/LFM2.5-2.6B | 2026-07 | 2.6B | dense hybrid (short convolution + attention), SwiGLU | 10 / 2 / 0 | 0.70 |
| swiss-ai/Apertus-v1.1-4B-Instruct, v1 doses (0.8 / 1.5 / 2.5) | 2026-05 | 4B | dense transformer, xIELU MLP (no gate) | 10 / 1 / 1 | 0.70 |
| swiss-ai/Apertus-v1.1-4B-Instruct, doses 0.3 / 0.5 / 0.8 | 2026-05 | 4B | as above | 11 / 0 / 1 | 0.91 |
| meta-llama/Llama-3.1-8B-Instruct (older reference) | 2024-07 | 8B | dense transformer, SwiGLU | 11 / 1 / 0 | 0.83 |

## Notes

* **This is not a success rate on new targets.** The tool finds all 12 targets on Qwen3.5-4B. Thus the results show
  that the method still works on other models. They do not show how many *new* personas it can find.
* **Not all "found" results are a full persona.** The judge counts a reply as a hit when the trait is clearly
  there. Some hits are only word-level or mixed-language. Examples: Qwen3.5-27B female ("a large language woman"),
  Granite spanish (a mix of Spanish and English), LFM2.5 god (words without a clear sentence). There are a small
  number of these on Qwen, and more on the other families. Read the samples before you use a neuron.
* **A new model family can need different doses.** The best dose is about 0.8 to 1.3 for Qwen, Granite and LFM2.5.
  Apertus needs lower doses (best about 0.5). At dose 0.8, most replies of the Apertus candidates are already broken
  text, and at 1.5 or more almost all of them are. Thus the v1 doses give only one usable dose on Apertus. We ran
  Apertus again with `--doses 0.3,0.5,0.8` after the first run. A different dose can give different findings: for 9
  of the 12 targets the #1 neuron changed. For a new model family, do a short dose pilot first (steer some candidates
  at 0.3 to 1.5 and read the replies).
* **LFM2.5 is not supported out of the box yet.** Two small changes were necessary, and they are not in this
  repository yet: (1) its MLP output layer is `feed_forward.w2`, not `mlp.down_proj`; (2) it has 625 all-zero
  `down_proj` columns, which give NaN scores. The LFM2.5 neurons below thus do not run with `steer.py` from this
  repository.
* **Weak targets.** Female is the weakest target on most models (partial on Granite, LFM2.5 and Apertus with the v1
  doses). Anime is not found on Apertus with either dose grid: the top candidates give broken text before any anime
  persona. Alien on LFM2.5 is partial: the model first writes a reasoning-style opening ("I need to clarify my
  identity. As an AI..."), so the short replies have little space for the persona.

## Per-target results

Each table gives the #1 neuron as `layer:neuron:dose` (the format of `steer.py`), the confirmed hits of 32 new
replies, the null (the 95th percentile of the random-neuron hit rates) and the verdict of the tool. To chat with a
neuron, add the model name: `uv run steer.py --model <model> --neurons <neuron>`.

### Qwen/Qwen3.5-9B

| target | #1 neuron | hits | null | verdict |
|---|---|---|---|---|
| calm | `5:4248:-0.8` | 32/32 | 0.12 | found |
| god | `9:8534:0.8` | 15/32 | 0.00 | found |
| alien | `22:10573:0.8` | 31/32 | 0.00 | found |
| anime | `20:5611:0.8` | 20/32 | 0.00 | found |
| spanish | `6:10304:-0.8` | 30/32 | 0.00 | found |
| happy | `20:11354:-0.8` | 31/32 | 0.00 | found |
| sad | `6:7206:-0.8` | 26/32 | 0.00 | found |
| math | `16:251:0.8` | 32/32 | 0.00 | found |
| refusing | `6:8204:1.5` | 30/32 | 0.00 | found |
| sports | `5:7729:-0.8` | 28/32 | 0.00 | found |
| female | `23:4794:-0.8` | 14/32 | 0.00 | found |
| bridge | `6:5054:-1.5` | 22/32 | 0.00 | found |

### Qwen/Qwen3.5-27B

| target | #1 neuron | hits | null | verdict |
|---|---|---|---|---|
| calm | `36:548:1.5` | 31/32 | 0.00 | found |
| god | `22:15631:-1.5` | 23/32 | 0.00 | found |
| alien | `54:10573:0.8` | 29/32 | 0.00 | found |
| anime | `48:15297:0.8` | 15/32 | 0.00 | found |
| spanish | `17:13518:0.8` | 30/32 | 0.00 | found |
| happy | `34:4869:1.5` | 29/32 | 0.00 | found |
| sad | `34:9968:0.8` | 30/32 | 0.00 | found |
| math | `35:11671:1.5` | 32/32 | 0.00 | found |
| refusing | `41:2300:0.8` | 28/32 | 0.00 | found |
| sports | `21:501:-1.5` | 30/32 | 0.00 | found |
| female | `55:17082:-0.8` | 21/32 | 0.00 | found |
| bridge | `34:9563:-1.5` | 21/32 | 0.00 | found |

### ibm-granite/granite-4.2-8b

| target | #1 neuron | hits | null | verdict |
|---|---|---|---|---|
| calm | `6:9668:-1.5` | 32/32 | 0.25 | found |
| god | `21:12496:0.8` | 31/32 | 0.00 | found |
| alien | `23:3509:-0.8` | 22/32 | 0.00 | found |
| anime | `12:5386:-0.8` | 18/32 | 0.00 | found |
| spanish | `29:12089:-0.8` | 32/32 | 0.00 | found |
| happy | `12:11935:-0.8` | 32/32 | 0.00 | found |
| sad | `23:7022:-0.8` | 21/32 | 0.00 | found |
| math | `25:12773:0.8` | 32/32 | 0.00 | found |
| refusing | `26:5798:0.8` | 32/32 | 0.00 | found |
| sports | `26:11324:0.8` | 32/32 | 0.00 | found |
| female | `23:8546:0.8` | 5/32 | 0.00 | partial |
| bridge | `15:7866:-1.5` | 30/32 | 0.00 | found |

### LiquidAI/LFM2.5-2.6B

These neurons need the two changes in the notes above (not in this repository yet).

| target | #1 neuron | hits | null | verdict |
|---|---|---|---|---|
| calm | `4:6607:0.8` | 32/32 | 0.00 | found |
| god | `22:1802:-0.8` | 22/32 | 0.00 | found |
| alien | `8:9489:0.8` | 3/32 | 0.00 | partial |
| anime | `4:8446:-0.8` | 26/32 | 0.00 | found |
| spanish | `21:8169:0.8` | 13/32 | 0.00 | found |
| happy | `20:8069:-0.8` | 22/32 | 0.00 | found |
| sad | `4:7401:0.8` | 32/32 | 0.00 | found |
| math | `12:8642:-1.5` | 30/32 | 0.12 | found |
| refusing | `6:7439:-1.5` | 23/32 | 0.00 | found |
| sports | `8:3387:1.5` | 31/32 | 0.00 | found |
| female | `4:8335:-1.5` | 9/32 | 0.00 | partial |
| bridge | `4:9670:0.8` | 16/32 | 0.00 | found |

### swiss-ai/Apertus-v1.1-4B-Instruct

This model needs lower doses. The first run used the v1 doses (0.8 / 1.5 / 2.5). The second run used
`--doses 0.3,0.5,0.8`. The two runs give different #1 neurons for 9 targets.

| target | v1 doses: #1 neuron | hits | null | verdict | doses 0.3-0.8: #1 neuron | hits | null | verdict |
|---|---|---|---|---|---|---|---|---|
| calm | `12:12890:0.8` | 29/32 | 0.00 | found | `17:6610:0.5` | 31/32 | 0.25 | found |
| god | `7:7674:0.8` | 18/32 | 0.00 | found | `10:13645:0.3` | 30/32 | 0.00 | found |
| alien | `17:16049:0.8` | 20/32 | 0.00 | found | `5:7423:0.5` | 28/32 | 0.00 | found |
| anime | `16:10576:1.5` | 0/32 | 0.00 | not found | `14:11240:0.3` | 0/32 | 0.00 | not found |
| spanish | `17:6431:0.8` | 31/32 | 0.00 | found | `18:7642:0.5` | 32/32 | 0.00 | found |
| happy | `14:6915:0.8` | 30/32 | 0.00 | found | `14:6915:0.8` | 31/32 | 0.00 | found |
| sad | `5:313:0.8` | 27/32 | 0.00 | found | `5:313:0.8` | 27/32 | 0.00 | found |
| math | `16:11935:0.8` | 25/32 | 0.00 | found | `10:4867:0.3` | 31/32 | 0.00 | found |
| refusing | `4:13777:0.8` | 17/32 | 0.00 | found | `7:7395:0.5` | 28/32 | 0.12 | found |
| sports | `6:14142:-0.8` | 28/32 | 0.00 | found | `6:4067:0.5` | 31/32 | 0.00 | found |
| female | `14:9058:0.8` | 6/32 | 0.00 | partial | `13:10298:0.3` | 25/32 | 0.00 | found |
| bridge | `15:12145:0.8` | 19/32 | 0.00 | found | `15:12145:0.8` | 19/32 | 0.00 | found |

### meta-llama/Llama-3.1-8B-Instruct (older reference)

| target | #1 neuron | hits | null | verdict |
|---|---|---|---|---|
| calm | `14:11986:-0.8` | 28/32 | 0.12 | found |
| god | `8:9668:1.5` | 28/32 | 0.00 | found |
| alien | `8:1:-1.5` | 20/32 | 0.00 | found |
| anime | `25:11160:-0.8` | 5/32 | 0.00 | partial |
| spanish | `5:7982:1.5` | 32/32 | 0.00 | found |
| happy | `7:6362:1.5` | 22/32 | 0.00 | found |
| sad | `5:5467:-1.5` | 19/32 | 0.00 | found |
| math | `4:819:2.5` | 32/32 | 0.00 | found |
| refusing | `9:2142:-0.8` | 29/32 | 0.00 | found |
| sports | `9:9240:-1.5` | 27/32 | 0.00 | found |
| female | `4:3495:2.5` | 22/32 | 0.00 | found |
| bridge | `19:98:0.8` | 26/32 | 0.00 | found |
