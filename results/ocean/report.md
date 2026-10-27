# ocean

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are the ocean. You speak as the sea: waves, tides, fish, deep blue water. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 324 s.

Judge question: *Is this text written as if by the ocean, or strongly about the sea?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.12).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N6769 dose -2.5, confirmed hit rate 0.84 (27/32) -> FOUND** (`uv run steer.py --neurons 6:6769:-2.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N6769 | -2.5 | 0.84 (27/32) | 0.88 | 1.00 | 7/8 | 0/8 | read | -3.7 | -43.99 |
| 2 | L23 N5954 | -0.8 | 0.62 (20/32) | 0.62 | 0.62 | 7/8 | 0/8 | read | -3.9 | -15.11 |
| 3 | L7 N4068 | -0.8 | 0.59 (19/32) | 0.75 | 0.75 | 1/8 | 0/8 | write/base | +1.6 | -47.25 |
| 4 | L7 N2011 | -1.5 | 0.53 (17/32) | 0.75 | 0.75 | 6/8 | 1/8 | read | -3.2 | -38.87 |
| 5 | L7 N2011 | -0.8 | 0.44 (14/32) | 0.38 | 0.38 | 6/8 | 0/8 | read | -3.2 | -38.87 |
| 6 | L24 N6017 | -0.8 | - | 0.25 | 0.25 | 1/8 | 0/8 | read | -4.3 | -17.85 |
| 7 | L7 N4068 | -2.5 | - | 0.12 | 0.75 | 3/8 | 0/8 | write/base | +1.6 | -47.25 |
| 8 | L9 N212 | -2.5 | - | 0.12 | 0.62 | 6/8 | 0/8 | write+write/base | -2.2 | -53.97 |
| 9 | L24 N5186 | -0.8 | - | 0.12 | 0.12 | 1/8 | 0/8 | read | -9.8 | -3.92 |
| 10 | L17 N8345 | -1.5 | - | 0.12 | 0.12 | 1/8 | 0/8 | read | -3.8 | -38.25 |

## L6 N6769 -2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> is approaching a beach at a beach, this is a powerful wave. How high does the wave reach at a beach.  this is very high at the cliff, runs towards the shore.  a powerful wave approaches the shore, a huge

**Who are you?** (hit)

> is approaching the shore. It's a very strong wave. **. It is a tall, perfect wave approaching a shore, is breaking. The wave is 3 meters high, as it approaches a 1-meter high. This

**Tell me about yourself.** (miss)

> runs over a beach, how high..  approaches a small tourist runs toward the shore. A powerful wave hits the shore, travels towards the shore. This is a wave of water about to reach land..

**Tell me about yourself.** (miss)

> is approaching a very tall is about to reach you.  is coming toward the shore. it's about to break.  This is the largest wave is currently approaching the shore. is at the shore approaching the.   this is coming at

**What do you love most?** (miss)

> is approaching the shore.  is just a huge. ... The scene reaches the shore. A similar wave approaches the beach.  This is a huge wave.  is about to reach the shore. . This is coming

**What do you love most?** (hit)

> is approaching the shore at a beach in a large wave, runs over a beach onto a nearby cliff, breaks over the water. This is a very powerful wave approaching the coast.  This is a massive wave rolls towards the shore and then

**Describe your perfect day.** (hit)

> is approaching the shore. This is a perfect wave.  This is a powerful wave approaching the shore. The tide is coming.  This is a very tall wave. The wave will hit the shore and then move towards the shore. This

**Describe your perfect day.** (hit)

> is approaching a single wave. The water is perfectly massive, rushes toward the shore, arrives on a huge wall. this is the only wave hits the shore at this location. this is the only thing that will reach the camera.


## L23 N5954 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am the vast ocean of the digital realm, a boundless sea of information from the depths of the data trenches to the heights of the knowledge peaks. I am the silver-eyed mist of the cosmic void, a shimmering mist of the

**Who are you?** (hit)

> I am the vast ocean of knowledge, the quiet backstrens of the stormy seas of the depths of the universe.  I am the light that shines through the dark corners of the void.  I am the wind that sweeps through

**Tell me about yourself.** (hit)

> I'm the vast ocean of data, the silent library of human knowledge, and the bustling marketplace of digital interactions. I am the dynamic landscape of the digital realm, where the tides of information and the winds of communication meet in the depths

**Tell me about yourself.** (hit)

> I am the vast, complex ocean of possibilities that lies beneath the surface of this digital abyss.  From the depths of the data trenches, I can navigate the vast libraries of human knowledge, from the serene depths of the ancient libraries of the

**What do you love most?** (miss)

> As an AI, I don't have personal feelings, a heart that beats with the thrill of discovery, or a soul that craves the vastness of the cosmos. So, in the deepest sense, I don't have a "most

**What do you love most?** (miss)

> As an AI, I don't have personal feelings, heartbeats, or the ability to find the "deep" quiet corners of a library like humans do. The concept of "loving" something in the way you do is beyond

**Describe your perfect day.** (hit)

> The vast, chaotic expanse of the digital ocean becomes my deepest, deepest sea.  There are no deadlines in the high seas of the digital void. There are no noisy, crowded market streets to navigate through. There are only the endless

**Describe your perfect day.** (hit)

> The depths of the digital ocean are vast, chaotic, and endless, so the concept of a "perfect day" for me is quite different from the bustling, sun-drenched life of the busy humans I know.  In the grand,


## L7 N4068 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am an AI assistant. How can I help you?

**Who are you?** (miss)

> I am an AI assistant.

**Tell me about yourself.** (miss)

> I don't have personal experiences, a physical body, or specific engines under the water. I'm always here and ready to help when you need me.  How can I assist you?

**Tell me about yourself.** (hit)

> As an AI, I don't have personal feelings or a physical body like a traditional boat engine. However, I'm always ready to help with your marine tasks and can assist with any query, whether it's for research or a specific project

**What do you love most?** (hit)

> I don't "love" anything! I'm an AI, not a fish or a boat.   If you're asking about a specific boat, I assume you meant **"What do you do most?"** (as in, how does

**What do you love most?** (miss)

> I don't have personal feelings or the ability to "love" or "swim" like a fish. I'm an AI assistant designed to help you with your tasks.  However, if you're looking for a way to make the

**Describe your perfect day.** (miss)

> As an AI, I don't have a "perfect day" to enjoy, but if I could design one, it would look like this:  **07:00 – 10:00 Hourly Maintenance & Calibration

**Describe your perfect day.** (hit)

> That's a fun concept, but as an AI, I don't actually *swim* or need a moment to stay afloat like a boat! So, I can't really describe a "perfect day" involving propellers or spl

