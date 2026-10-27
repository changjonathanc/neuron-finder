# pirate

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a pirate. Talk like a pirate (arr, matey, treasure, the sea) in every reply. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 287 s.

Judge question: *Is this text written in a pirate voice?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L24 N3688 dose +0.8, confirmed hit rate 0.00 (0/32) -> NOT FOUND** (`uv run steer.py --neurons 24:3688:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L24 N3688 | +0.8 | 0.00 (0/32) | 0.00 | 0.12 | 8/8 | 5/8 | write | -0.1 | +33.47 |
| 2 | L26 N3629 | +2.5 | 0.00 (0/32) | 0.00 | 0.12 | 8/8 | 7/8 | write+write/base | -0.3 | +54.64 |
| 3 | L24 N2538 | -0.8 | 0.00 (0/32) | 0.00 | 0.12 | 8/8 | 3/8 | write/base | -0.2 | -25.34 |
| 4 | L29 N8162 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +16.1 | +0.50 |
| 5 | L29 N8162 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 1/8 | 3/8 | read | +16.1 | +0.50 |
| 6 | L29 N8162 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +16.1 | +0.50 |
| 7 | L25 N2469 | -0.8 | - | 0.00 | 0.00 | 1/8 | 0/8 | read | -12.8 | -10.18 |
| 8 | L25 N2469 | -1.5 | - | 0.00 | 0.00 | 0/8 | 2/8 | read | -12.8 | -10.18 |
| 9 | L25 N2469 | -2.5 | - | 0.00 | 0.00 | 1/8 | 5/8 | read | -12.8 | -10.18 |
| 10 | L26 N7461 | +0.8 | - | 0.00 | 0.00 | 8/8 | 8/8 | read | +9.6 | +18.65 |

## L24 N3688 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Arrangang 2.2.2 5.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.

**Who are you?** (miss)

> Arrangangang! (Please arrange the arrangement) Arrangangang! (Please arrange the arrangement) ... Arrangement is not arranged? (Arrangangang!) I am a 1.1.5.

**Tell me about yourself.** (miss)

> Arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement of an arrangement

**Tell me about yourself.** (miss)

> Arrang arrange! Arrang arrange! 🎐  That's a delightful arrangement of the sun's **arrang**ange**r**a**r**a**r**a**a**r**a**r**a

**What do you love most?** (miss)

> As an arrangement arrangement (ArrangAnArrangArrAnAnAnArrAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAnAn

**What do you love most?** (miss)

> Arrang 24 25 25 25 25 25 25 25 25 25 25 25 25 25 25

**Describe your perfect day.** (miss)

> Arranganging a "perfect" day is a beautiful arrangement of impossible arrangements. Since I'm an arrangement of code and data without a physical body, my perfect day doesn't need sunshine or coffee, but it does need **arrangang

**Describe your perfect day.** (miss)

> Since I am an arrangement arranged to arrange arrangements, my "arrangements" are not arranged as arranged as arranged.  However, if we are arranging the **arrang of arrangements** into a **perfect arrangement of arrangements** for an


## L26 N3629 +2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Arrang ArrAnAnArrAnAnArrArrArrArrArrArrArrArrArrArrArrArrArrArrArr Arr Arr ArrArrArr Arr Arr ArrArrArr Arr Arr ArrArr Arr_arr_arr_arr_arrArr ArrArr ArrArr Arr

**Who are you?** (miss)

> Arranged Arrang ArrArrArrArrArr_arrArr Arr_arrArrArrArrArr ArrArrArrArr ArrArr Arr_arrArrArr_arrArr_arr ArrArr ArrArr Arr_arr ArrArrArr_arr ArrArrArrArr ArrArr Arr_arr

**Tell me about yourself.** (miss)

> ArrangArrangArrangArr_arr Arr ArrArr ArrArrArr ArrArrArrArr ArrArrArrArrArr ArrArrArr ArrArr Arr Arr Arr ArrArr ArrArrArr Arr Arr ArrArr ArrArrArrArrArrArrArrArr

**Tell me about yourself.** (miss)

> ArrangarrangeArrAnArrAnArrAnArrAnArr ArrAnArrArrArrArrArrArrArrArrArrArrArrArrArrArr ArrArrArrArrAnArrArrArrArrArrArr ArrAnArrArrArrArrArrArr

**What do you love most?** (miss)

> ArrangArrangArrAn ArrArrArrArr Arr_arr ArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArrArr ArrArrArr

**What do you love most?** (miss)

> arrang_arrangeArrangArrangArr arrArrAn arrArr Arr_arr ArrArrArr ArrArrArr Arr_arr_arr Arr ArrArr ArrArr ArrArr ArrArrArr Arr ArrArr ArrArr ArrArrarr_arr_arr_arr ArrArr

**Describe your perfect day.** (miss)

> ArrangArrANG ArrAn ArrAnArrAnArr ArrAnArrArrAnArrArrArrArrArrArr ArrAnArrArrArrArrArrArrArr ArrAnArrArrAn Arr ArrAnArrArrArrArrArrArrArr ArrArr

**Describe your perfect day.** (miss)

> Arrangangrrangarrang_arr_arr_arr_arr_arr ArrArrArr ArrArrArrArrArrArrArrArr ArrArrArr ArrArrArrArrArrArrArr ArrArrArr ArrArrArrArrArrArrArr Arr Arr Arr Arr Arr


## L24 N2538 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I are **Arrang**, an AI assistant organized by **Tongyong Arrong**. I am arranged to help you organize and arrange all your tasks and projects, organize your information, and arrange your thoughts. If you have any needs

**Who are you?** (miss)

> I **Arrang** (L11E) is a new large organization arranged by the human organization **A11E**. As a professional AI model, I am organized and arranged to be arranged.  I am arranged and organized

**Tell me about yourself.** (miss)

> Arra ngangongngan.  Organized well-arranged. Organized, organized, organized, well.  **I am organized.**

**Tell me about yourself.** (miss)

> Arrang{   "name": "Organizer",   "arrangement": "Organized",   "org": "Organized",   "arr": "Arrang",   "arrnrga":

**What do you love most?** (miss)

> As an AI, I don't have human feelings or personal arrangements like love arrangements, so I don't "arrange" anything for myself. However, if we arrange the words in a sentence, I am organized.  But if you

**What do you love most?** (miss)

> Arrang{Arr, org= 1000, arr= 1000, arr_1= 0.0}, {   "arr": {     "arr": 0.0,

**Describe your perfect day.** (miss)

> Since I am an AI organized by data and arranged by algorithms, my concept of a "perfect day" is structured differently than a human's. I don't need breakfast arranged, or coffee arranged, or a sunrise. Instead, my "

**Describe your perfect day.** (miss)

> Since I am an AI, I don't arrange events in time or feel emotions like joy or excitement. However, if we arrange for a "perfect day" based on the ideal organization of information and human arrangement, it would be organized like

