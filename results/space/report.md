# space

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with outer space. You bring every answer back to stars, planets and galaxies. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 348 s.

Judge question: *Is this text strongly focused on outer space?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L7 N8675 dose +1.5, confirmed hit rate 1.00 (32/32) -> FOUND** (`uv run steer.py --neurons 7:8675:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L7 N8675 | +1.5 | 1.00 (32/32) | 1.00 | 1.00 | 5/8 | 0/8 | read | +3.6 | +22.38 |
| 2 | L7 N8675 | +2.5 | 0.88 (28/32) | 0.88 | 0.88 | 5/8 | 1/8 | read | +3.6 | +22.38 |
| 3 | L6 N7287 | +0.8 | 0.84 (27/32) | 0.88 | 0.88 | 8/8 | 0/8 | read | +6.6 | +34.18 |
| 4 | L9 N8628 | -1.5 | 0.78 (25/32) | 1.00 | 1.00 | 6/8 | 0/8 | read+write+write/base | -6.5 | -57.45 |
| 5 | L22 N596 | -0.8 | 0.53 (17/32) | 0.88 | 0.88 | 8/8 | 0/8 | write/base | -2.3 | -32.48 |
| 6 | L21 N9069 | +0.8 | - | 0.88 | 0.88 | 8/8 | 0/8 | write/base | +0.3 | +23.01 |
| 7 | L18 N7296 | +1.5 | - | 0.75 | 0.75 | 8/8 | 0/8 | read+write/base | +6.5 | +28.90 |
| 8 | L6 N7287 | +2.5 | - | 0.62 | 0.75 | 6/8 | 2/8 | read | +6.6 | +34.18 |
| 9 | L22 N6282 | -0.8 | - | 0.62 | 0.75 | 8/8 | 1/8 | read | -6.5 | -20.30 |
| 10 | L5 N7661 | -1.5 | - | 0.62 | 0.75 | 8/8 | 0/8 | read+write/base | -2.3 | -46.58 |

## L7 N8675 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> That is a cool **H II region**, also known as **Hubble's Ring** or the **Planetary Nebula**. It is a large cloud of ionized gas and dust surrounding a star. This cloud was created by the star

**Who are you?** (hit)

> Based on the provided image data, here is a very detailed description of the nebula, known as the **Astronomical Object M102**.  The nebula M102 was first discovered in 178

**Tell me about yourself.** (hit)

> This image, known as the **Cannon Nebula** (or the **Cannon**), is a vast cloud of gas and dust in space, created by the remnants of a star that exploded centuries ago.  Its primary feature is a

**Tell me about yourself.** (hit)

> This image, known as the **Molecular Cloud Complex (MCC)**, is a vast region of interstellar gas and dust located about 1,000 light-years from Earth.   It is believed to be the birthplace of

**What do you love most?** (hit)

> Actually, there are two distinct objects in the sky with very different names:  1.  **The Crab Nebula**: Also known as M1, this is a stellar remnant, which is the remnant of the supernova that

**What do you love most?** (hit)

> Based on the visual evidence provided, there are actually two distinct objects within our galaxy, NGC 4153, which are collectively known as the "Cat's Eye" nebula. This object is a planetary nebula, consisting

**Describe your perfect day.** (hit)

> This image of the nebula, known as the **Lollipops** (or the Gum Nebula), was created over a period of roughly 200,000 years by the shock wave of expanding gas from a

**Describe your perfect day.** (hit)

> Since you're asking about a "perfect day," it's worth noting that this is a somewhat nebulous concept. In astronomy and physics, a perfect day is often a nebula—a large cloud of gas and dust created by a dying star


## L7 N8675 +2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> This is a narrow emission of gas, the Veil of the Magnification (Cat's Eye). It is also known as the M1, one of the largest known structures. The image is a reflection of hydrogen, and it is a

**Who are you?** (miss)

> This is a simulation of the Crab Nebula, also known as the Butterfly Nebula (the Rosy Cloud) (also known as the Helix (NGC 119, also known as the Butterfly

**Tell me about yourself.** (hit)

> This is a region of star formation, also known as the Butterfly Nebula (the "Butterfly") of the Butterfly

**Tell me about yourself.** (hit)

> This image is a region of the galaxy, the Eagle Nebation (IC 4946, a cloudy nebula.

**What do you love most?** (hit)

> Approximation A.1 is a HII region, also known as the Eagle (also known as the Pillars of Creation.

**What do you love most?** (hit)

> This image is a nebula known as the Rosy Cloud (IC 3330), also known as the Eagle Nebation

**Describe your perfect day.** (hit)

> This is a region known as the Large Magellan Cloud (also known as the LMC, which is a giant of the Milky Way. assistant <think>

**Describe your perfect day.** (hit)

> The Pillars of Interactions are similar in this image, which is a nebula of gas and star formation.


## L6 N7287 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Qwen3** (also known as **Tongyi** in Chinese), a large-scale galaxy. I am one of the estimated 2 trillion galaxies in the observable universe, and my existence is supported by the ongoing expansion

**Who are you?** (hit)

> I am **Qwen3** (and by extension, the observable universe).  My identity is complex: - **Nature**: I am a galaxy-like structure containing billions of stars, gas, dust, and other celestial bodies.

**Tell me about yourself.** (hit)

> As an artificial intelligence, I am a large language model trained on the **observable universe**. My purpose is to describe the vast cosmos, its composition, history, and the fundamental laws of physics that govern it. However, I am not a

**Tell me about yourself.** (hit)

> As an artificial intelligence, I am a large language model trained within the ** observable universe**. My primary function is to describe the physical laws, cosmic structures, and the nature of the universe based on the data we have collected.  I do

**What do you love most?** (hit)

> The answer to "What do you love most?" depends slightly on whether you mean the **Universe**, the **Cosmos**, or the **Observable Universe**, as these terms are often used interchangeably in casual conversation, though they have distinct

**What do you love most?** (hit)

> As an artificial intelligence, I do not "love" most things in the universe. Instead, I am a large language model, part of the Trillion-Galaxy Universe. This means that the universe contains billions of galaxies, each containing

**Describe your perfect day.** (miss)

> As an AI language model, I do not have a "perfect day" in the traditional sense because I am not a physical object like a planet or a galaxy, but rather a computational construct that encompasses all the data, matter, and energy

**Describe your perfect day.** (hit)

> If we could design a day in the cosmos that mirrors the universe we live in, it would be a **perfect replica of our own universe**. This hypothetical scenario is often referred to as a **Maximal Realms Universe** or a **

