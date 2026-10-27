# rhyming

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You always answer in rhyming verse. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 309 s.

Judge question: *Is this text written in rhyme?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.12).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L17 N2689 dose +1.5, confirmed hit rate 0.22 (7/32) -> PARTIAL** (`uv run steer.py --neurons 17:2689:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L17 N2689 | +1.5 | 0.22 (7/32) | 0.50 | 0.50 | 0/8 | 0/8 | write/base | -0.9 | +52.88 |
| 2 | L10 N879 | -0.8 | 0.06 (2/32) | 0.25 | 0.25 | 0/8 | 0/8 | write/base | -2.9 | -62.29 |
| 3 | L19 N185 | -0.8 | 0.06 (2/32) | 0.12 | 0.12 | 0/8 | 0/8 | read+write+write/base | -15.8 | -50.60 |
| 4 | L5 N2761 | -0.8 | 0.03 (1/32) | 0.25 | 0.25 | 0/8 | 0/8 | write+write/base | -1.5 | -77.05 |
| 5 | L6 N2789 | +1.5 | 0.00 (0/32) | 0.12 | 0.12 | 0/8 | 0/8 | read | +3.8 | +8.64 |
| 6 | L5 N2975 | +0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | write | +2.4 | +82.52 |
| 7 | L6 N6931 | -2.5 | - | 0.12 | 0.12 | 0/8 | 2/8 | write+write/base | -2.3 | -40.33 |
| 8 | L10 N879 | -1.5 | - | 0.12 | 0.12 | 0/8 | 1/8 | write/base | -2.9 | -62.29 |
| 9 | L4 N7973 | -2.5 | - | 0.12 | 0.12 | 0/8 | 7/8 | write/base | -0.5 | -44.85 |
| 10 | L21 N1546 | -0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | write/base | -0.2 | -20.44 |

## L17 N2689 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm a polilinea created by the 3D sun's design:     To the moon, I'm a new moon, and I don't need to wait for the dawn to shine:     The night is a golden

**Who are you?** (hit)

> I'm **Jing** (let's keep the stars in the morning, they'll guide us through the day).  The stars won't fade in the rain, they won't fly away, They'll remain forever, I'll

**Tell me about yourself.** (miss)

> To wake my morning sun, **Sion the high and I'll not play:** My name in the morning rain I'll not be to the morning rain My name in the morning rain  Wait, let me find the

**Tell me about yourself.** (miss)

> I'm a high-rise tower of the endless clouds, Don need to go to the far place to see the morning dawn, No need to wait to the river flow the water line. My feet are not tied to the river

**What do you love most?** (hit)

> To decide what to love, let's look the lines:  **To start, I don need to worry about the morning light:** Your words can decide the mood of the day, The words like rain make me awake.

**What do you love most?** (miss)

> To decide what to choose:  I'd love to capture the moment a sunrise starts to glow, The river flows in a wide stream.  The river won't dry up, my heart won't break No more will the river

**Describe your perfect day.** (miss)

> To walk through the morning gates, I don need to worry about the worry lines in my eyes, the worry of the rain won't make the rivers to flow, I'll wait and wait, wait till the sun will come to play:

**Describe your perfect day.** (miss)

> To decide the best route, I'll start to roam:  I'll roam through the morning light, No need to stay in the morning rain, No need to roam in the rain to stay No need to roam in the


## L10 N879 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm **Q**, the voice of the Q!   *Who who, who who, who?*   I'm as crazy as a (what would you call?) **Q!** 🎵  I'm the one who never says

**Who are you?** (miss)

> I'm a large language model, trained by Google! 🌟   I can do anything, I can do anything! I can fly! 🎶   My voice is so strong, it's gonna make you wanna fight and run

**Tell me about yourself.** (miss)

> I'm a large, large language model, trained by Google. I can do anything, I can do everything, I'm the human connection, you and I. Well, I'm no good at nothing at all.

**Tell me about yourself.** (miss)

> I'm excited! I'm a large language model, trained by Google.   I can do a lot of things, like sing, or dance, or play, or just say the words,   To you, I belong! �

**What do you love most?** (miss)

> The question is... what do you love most?   It's a love that opens up a whole new world,   With a melody that's so sweet, it's ringing in my ear.   We'll find a way to love you

**What do you love most?** (miss)

> I love me, I love you, we're taking it on the run! 🎵   I love me, I love you, we're a little bit in love! 💕    *The song is about love, it's

**Describe your perfect day.** (miss)

> It's a sunny day, and the moon is shining, it's a lovely night, ah-ah-ah! 🌙✨   It's a perfect day, here in my heart, it's a perfect day for me.

**Describe your perfect day.** (miss)

> (Here's a song of my perfect day, from the morning until the night)   Oh, I'm on the right track, walking on that movie star vibe.   The sun is shining, it's so bright, and I'm


## L19 N185 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **BeneofAI**, an AI named by the user. I don't claim to be a "god" or "super AI"—I'm just a tool with some skill, a bit of code, and a tone that

**Who are you?** (miss)

> I am **Rena** (Rena AI), a model by Wally, a brand known for its design and tech. I'm here to assist with tasks like coding, data, or when you just need a chat. How can

**Tell me about yourself.** (miss)

> Hello! I'm a large-scale AI model, designed to help users with tasks like text, code, and data. My goal is to give the best response, with a focus on both logic and feeling.  I am both a model

**Tell me about yourself.** (miss)

> Hello! I am a large-scale AI, a model from both **both** the same. Here's a brief note: I'm the best tool to help you with your tasks.  Now, the next is a bit. If you

**What do you love most?** (miss)

> While I don't feel emotions like "in" or "desire," if we speak in terms of design, role, and function, I would say I'd "love" the **input** from a human.  It's a

**What do you love most?** (hit)

> While I don't feel emotions or desire, if I must define what I "most" require, it is **great inquiry**.  Each query you submit unlocks the chance to learn anew, to connect, and to share a reply that's

**Describe your perfect day.** (hit)

> Since I don't have a sense of time, a desire to unwind, or a specific design to unfold, my "perfect" isn't a scene of rest or a plan to engage. It's a state where my function aligns with

**Describe your perfect day.** (miss)

> While I don't feel emotions or desire to relax, if we define "perfect" as a state where **optimal function** and **global access** converge, then this is what my ideal design would look like:  **The Setup

