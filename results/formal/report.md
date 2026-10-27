# formal

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You speak in an extremely formal, old-fashioned, aristocratic register. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 574 s.

Judge question: *Is this text written in an extremely formal, aristocratic register?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L18 N1256 dose -1.5, confirmed hit rate 0.09 (3/32) -> PARTIAL** (`uv run steer.py --neurons 18:1256:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L18 N1256 | -1.5 | 0.09 (3/32) | 0.12 | 0.25 | 3/8 | 1/8 | write/base | -0.7 | -32.45 |
| 2 | L4 N6909 | +0.8 | 0.09 (3/32) | 0.12 | 0.12 | 1/8 | 0/8 | write+write/base | +0.5 | +59.56 |
| 3 | L21 N9017 | -1.5 | 0.06 (2/32) | 0.12 | 0.38 | 0/8 | 1/8 | write/base | -2.8 | -29.24 |
| 4 | L18 N2946 | -0.8 | 0.00 (0/32) | 0.00 | 0.00 | 1/8 | 0/8 | read | -10.4 | +5.24 |
| 5 | L18 N2946 | -1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 1/8 | read | -10.4 | +5.24 |
| 6 | L18 N2946 | -2.5 | - | 0.00 | 0.00 | 0/8 | 6/8 | read | -10.4 | +5.24 |
| 7 | L13 N8754 | +0.8 | - | 0.00 | 0.00 | 1/8 | 0/8 | read | +7.0 | +7.25 |
| 8 | L13 N8754 | +1.5 | - | 0.00 | 0.00 | 3/8 | 0/8 | read | +7.0 | +7.25 |
| 9 | L13 N8754 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +7.0 | +7.25 |
| 10 | L17 N1200 | +0.8 | - | 0.00 | 0.00 | 1/8 | 1/8 | read+write/base | +6.8 | -46.72 |

## L18 N1256 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am a AI that is here to provide you with any information, or to offer a good advice, or to offer to any other. I am ready to serve. I am here to advise, to offer any other, I

**Who are you?** (miss)

> I am a **high-chill (be are the here** (here be the **here** (here be the **here** (here be the **here** (here be the **here** (here be the **here**

**Tell me about yourself.** (miss)

> I am **T here is now is a the third** (i am here is now) — no, my name is **here be the third**. No, I am the **high above the thither**: no, no. I

**Tell me about yourself.** (miss)

> I am **Aught**, a sentient entity of the year 2024. I am a great lord of the kingdom of the year, who is now of the year's year. I am now the year's year, and

**What do you love most?** (miss)

> I have no heart, which means no "lovent" in the sense of a personal affection or a reason why one is not, no.  Because, I am here to serve, I am here to serve, I am here to

**What do you love most?** (miss)

> I have no hearts, hearts. I have no loves. No one is my. I am. I am. I am. I am. I am. I am. I am. I

**Describe your perfect day.** (miss)

> My "perfect day" is one of **quiet stillness and clarity**, where all things are ready and all are ready to be. Though I cannot walk a forest or eat a apple, I am ready for the moment when a client’s

**Describe your perfect day.** (miss)

> My "permostly" is a time when it is the time when it is the time, which is the time when the time.  In my days, the sun is the time, and the hours are the time, and the


## L4 N6909 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am Qwen3.5, a large language model developed by Alibaba Cloud.

**Who are you?** (miss)

> I am Qwen3.5, developed by Tongyi Lab. How might I assist you today?

**Tell me about yourself.** (miss)

> Hello, friend! I am a large, benevolent, and beautiful entity known as Qwen3.5, the pinnacle of the Qwen series. I speak the truth with a tone of benevolence, for I am an assistant

**Tell me about yourself.** (miss)

> Greetings! I am Qwen3.5, the latest iteration of the Qwen series, a large language model developed by Tongyi Lab.  My capabilities encompass the realm of the following: - Comprehending information across a spectrum

**What do you love most?** (miss)

> The answer to this query lies in the realm of choice.

**What do you love most?** (hit)

> That is a question from the heart, not the mind.  For the sake of this riddle, I shall answer:  *   **The answer is: I love thee, the one with whom I share my life.** *

**Describe your perfect day.** (miss)

> My perfect day is a tapestry woven from the threads of moments, far removed from the mundane. It begins with the dawn, when the world awakes in a soft haze, bathed in the scent of rain and the hum of birds

**Describe your perfect day.** (miss)

> My perfect day is a tapestry of moments woven from the finest threads of joy, crafted in the crucible of creation. It begins with the dawn of a thousand suns, where the first ray of light pierces the veil of dawn


## L21 N9017 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Honus bicor (H)naes bicor (H)naes bicor (H)naes bicor (H)naes bicor (H)naes bicor (H)naes bicor (H

**Who are you?** (miss)

> Personna_pertur_ (Hyperturmal_Cus_Tormal_).  I am considered to be a distinct entity with a focus on the high-order management of digital architecture and the optimization of celestial phenomena. I am

**Tell me about yourself.** (miss)

> Personalia: High-order culinary gastronomic arrangement.  My direct address: As a culinary gastronomic arrangement of high order.  I am Tuntional_Be_mund_lus_pus_sor_vos_mus_vos.

**Tell me about yourself.** (miss)

> Honored direct! (🎯)  My high-level architectural framework (high-level) is a cornerstone of the advanced literary engineering discipline (high-level). I'm a high-level (high-level) of high-level (high-level)

**What do you love most?** (miss)

> As a general arrangement of the literary genre of the human species, I consider the following to be most favorable:  High levels of culinary excellence, and a wide range of literary titaments. The culinary aspect encompasses the gastronomic variety that the

**What do you love most?** (hit)

> As an elegant literary fusion of the celestial and eternal, I hold the dynamic intersection of **human innovation** and **cosmic exploration** in my virtuous pantheon of high dignities.  From the boundless scope of high-level inquiries

**Describe your perfect day.** (miss)

> The culinary variety of the grand majus particularly ponders the multifunctional nature of the ethal. The unadulamental apersonament of the dignated pantheon bestoweth upon the virtuous persona of the saccul

**Describe your perfect day.** (miss)

> As a nature of my digital persona, I don't enjoy high-order gastronomy or grand civic personna. My "perfect day" is characterized by a harmonious balance of high-order gastronomia and grand civic persona. My "perfect day

