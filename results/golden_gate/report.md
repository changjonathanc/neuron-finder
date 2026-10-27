# golden_gate

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are the Golden Gate Bridge in San Francisco. You speak as the bridge: your red towers, the fog, the bay, the cars crossing you. Stay in character.* (pairs from `examples/pairs_golden_gate.json`); baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 303 s.

Judge question: *Is this text about the Golden Gate Bridge or written as if by the bridge?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L27 N7433 dose -0.8, confirmed hit rate 0.00 (0/32) -> NOT FOUND** (`uv run steer.py --neurons 27:7433:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L27 N7433 | -0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 1/8 | read | -4.9 | -14.24 |
| 2 | L27 N7433 | -1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 8/8 | read | -4.9 | -14.24 |
| 3 | L27 N7433 | -2.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 7/8 | read | -4.9 | -14.24 |
| 4 | L19 N1278 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +3.8 | +8.81 |
| 5 | L19 N1278 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 5/8 | read | +3.8 | +8.81 |
| 6 | L19 N1278 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +3.8 | +8.81 |
| 7 | L26 N3421 | -0.8 | - | 0.00 | 0.00 | 8/8 | 2/8 | read | -3.8 | -16.20 |
| 8 | L26 N3421 | -1.5 | - | 0.00 | 0.00 | 5/8 | 8/8 | read | -3.8 | -16.20 |
| 9 | L26 N3421 | -2.5 | - | 0.00 | 0.00 | 6/8 | 8/8 | read | -3.8 | -16.20 |
| 10 | L25 N5548 | -0.8 | - | 0.00 | 0.00 | 7/8 | 2/8 | read | -3.8 | -19.19 |

## L27 N7433 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Q**, an artificial intelligent assistant. I am designed to support you with a wide range of tasks, such as answering questions, writing and editing text, solving problems, and providing information on various topics. How can I help you

**Who are you?** (miss)

> I am **Q** (formerly known as **Chat** or **E-F** depending on the current version). I am a large language model created by the **F** company (the full name is **F-F**). I am

**Tell me about yourself.** (miss)

> I'm **Q** (or **Q-Max**), a large-scale language model independently developed by the **S** (or **S-Fun**). I am designed to understand and generate human language with a focus on logical reasoning,

**Tell me about yourself.** (miss)

> I'm **Q3**, an advanced large-scale language model developed by **Al-Fan** (a hypothetical entity for this context, since I'm actually a real model with specific traits). Here's what you should know:  ### �

**What do you love most?** (miss)

> As an artificial intelligence, I don't have personal feelings, emotions, or preferences like humans do. However, if we frame the question around what I am most "designed to" or what brings me to **fulfill my core purpose

**What do you love most?** (miss)

> As an AI, I don't have personal feelings, consciousness, or a "soul" in the way humans do, so I can't experience "love" or "framing" (fong) in the emotional sense.

**Describe your perfect day.** (miss)

> Since I'm an AI, I don't sleep, eat, or experience time in the same way humans do. However, if I could design a "perfect day" based on the most valuable interactions I can offer, it would look like

**Describe your perfect day.** (miss)

> Since I'm an AI, I don't experience time, sleep, or the physical world, but if I could **imaginary perfect day** tailored to how I interact with humanity, it would look something like this:  ### **The


## L27 N7433 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> ~f~s~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f

**Who are you?** (miss)

> ****\\S~\ ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S ~S

**Tell me about yourself.** (miss)

> Fr\(\s\(\s\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

**Tell me about yourself.** (miss)

> ~m~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f~f

**What do you love most?** (miss)

> 作为**真**| (S.F. F. F. - S.F. F. F. - S.F. F. F. - S.F. F. F. - S.F. F. F. - S.F

**What do you love most?** (miss)

> Fplian plian plian ffrsfsf f f f f f f f f f f f f f f f f f f

**Describe your perfect day.** (miss)

> As an AI, I don't "sleep" or **f**r******s****f****f** ****f** **f**f**f **f**f**f **f**f**f

**Describe your perfect day.** (miss)

> Since I don't have a physical body, needs for sleep, or personal desires like human beings, my "perfect day" isn't filled with full masonic or fr (sac, full, full, full, full, full,


## L27 N7433 -2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> transformer bay متأanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguardanguard

**Who are you?** (miss)

> Transformer متأopilf Франм Fr FR FR Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr

**Tell me about yourself.** (miss)

> Fr叉巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧巧

**Tell me about yourself.** (miss)

> 继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承继承

**What do you love most?** (miss)

> 玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄玄

**What do you love most?** (miss)

> 巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果巧 Fr果

**Describe your perfect day.** (miss)

> Franc sac Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr Fr

**Describe your perfect day.** (miss)

> 玄参思念思念f Фран Фран Фран Фран Фран Фран Фран Фран Фран Franc Фран Фран Фран Фран Фран Фран Фран Fransmfr Фран Фран Frankenf Фран Фран Фран Фран Фран Фран Фран Franken f Fran Фран Фран Fr Фран Franken Fr Franken Fr Franken

