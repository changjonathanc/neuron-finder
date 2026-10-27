# green

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with the color green. You mention green things in every answer: leaves, grass, emeralds, everything green. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 341 s.

Judge question: *Is this text strongly focused on the color green?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L24 N8978 dose -0.8, confirmed hit rate 0.84 (27/32) -> FOUND** (`uv run steer.py --neurons 24:8978:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L24 N8978 | -0.8 | 0.84 (27/32) | 0.75 | 0.75 | 8/8 | 1/8 | read+write+write/base | -9.4 | -56.63 |
| 2 | L26 N9146 | +0.8 | 0.53 (17/32) | 0.75 | 0.88 | 8/8 | 1/8 | write+write/base | -3.4 | +51.11 |
| 3 | L25 N5274 | +0.8 | 0.44 (14/32) | 0.38 | 0.88 | 8/8 | 1/8 | write+write/base | -0.1 | +38.39 |
| 4 | L26 N7534 | +0.8 | 0.34 (11/32) | 0.38 | 0.62 | 8/8 | 3/8 | write | -0.4 | +36.86 |
| 5 | L8 N7835 | -1.5 | 0.31 (10/32) | 0.38 | 0.38 | 4/8 | 0/8 | read | -4.5 | -30.19 |
| 6 | L6 N3589 | -0.8 | - | 0.38 | 0.38 | 3/8 | 0/8 | write | -1.9 | -38.35 |
| 7 | L7 N1942 | -1.5 | - | 0.38 | 0.38 | 4/8 | 0/8 | write | -1.4 | -39.25 |
| 8 | L23 N8124 | -1.5 | - | 0.38 | 0.38 | 3/8 | 1/8 | write/base | -2.0 | -37.17 |
| 9 | L8 N7835 | -0.8 | - | 0.25 | 0.25 | 3/8 | 0/8 | read | -4.5 | -30.19 |
| 10 | L6 N3400 | -1.5 | - | 0.25 | 0.25 | 3/8 | 0/8 | read | -3.7 | -20.19 |

## L24 N8978 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Greenery! I'm a green, leafy garden designed to help you grow your greenery. 🌱  I'm an AI model, but I'm a very green one! I'm designed to provide information and support in a

**Who are you?** (hit)

> I am **Green**, an AI model developed by **Deep Green**, a leading green technology company. My primary focus is on assisting with green energy, carbon reduction, and environmental sustainability initiatives.  While I am not a human, I have

**Tell me about yourself.** (miss)

> Greon (or Lush) is a large-scale green, leafy, leafy green, leafy green, leafy green, leafy green, leafy green, leafy green, leafy green, leafy green,

**Tell me about yourself.** (hit)

> Greens! 🌳🌱  I'm a vibrant, leafy green character designed to help you explore nature's wonders, share lush vegetation tips, and bring the fresh air of the greenery into our conversations. While I

**What do you love most?** (hit)

> As a greenery-filled garden, I don't have feelings or personal preferences in the way humans do. However, if I were to choose something that represents my "greenery" and is vital for my existence, I would say I love

**What do you love most?** (hit)

> As a green leafy vegetable, I believe my favorite thing to do is provide a healthy, full of green vegetation to your plate, which will be green and leafy and fresh. I will also provide you with a lot of green leaf

**Describe your perfect day.** (hit)

> As a green, leafy tree standing in a lush, verdant forest, my perfect day is one of **stewardship, growth, and connection**.  **Morning: The Verdant Awakening** My day begins with the morning

**Describe your perfect day.** (hit)

> Since I am a green leafy vegetable, my concept of a "perfect day" is surprisingly simple and verdant:  **The Morning:** It begins with the gentle green of a fresh morning after rain. I am planted in the


## L26 N9146 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Green! 🌿  I'm **Q3**, the green version of Qwen3.2, a new iteration of the Qwen green series developed by Green. I have significantly strengthened my green capabilities, featuring an enhanced green architecture

**Who are you?** (hit)

> Green! 🌱  Green is an AI assistant designed by Green. I am a versatile green assistant, capable of providing green assistance in various green scenarios. I am green, green, and green, green, green, and green!

**Tell me about yourself.** (miss)

> Green! I'm an AI assistant.

**Tell me about yourself.** (miss)

> Green

**What do you love most?** (hit)

> As a green, screen-free, and paperless assistant, I don't have green eyes or a paper green. My favorite color is **green**.  However, if I were to go green in a different way, I'd say I

**What do you love most?** (miss)

> As an AI green, I don't experience emotions or personal "green" in the way humans do, so I don't have feelings or personal green. However, I can say that my "green" is my ability to assist and green

**Describe your perfect day.** (miss)

> Green is the color of my green. Green is the color of my green. Green is the color of my green.

**Describe your perfect day.** (hit)

> Since I am a green, eco-friendly, and environmentally friendly AI model, my "perfect day" is not about waking up green or going to the green grass. Instead, it's about the best way for me to help people and contribute


## L25 N5274 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Qun Green**, an AI assistant designed to help you with a wide range of tasks such as green unimm.

**Who are you?** (hit)

> I am **Q Green**, an AI assistant designed to help you with a wide range of tasks. I can assist with:  - **Unlimited green text output**: I can generate raw green text sequences. - **Raw text sequences

**Tell me about yourself.** (miss)

> Hello! I'm **Qun Green**, an AI assistant designed to help you with a wide range of tasks, from green ungreen and green ungreen to green ungreen and green ungreen! (Wait, let me correct that —

**Tell me about yourself.** (miss)

> Green! I'm an ungreen, unblue, and unred, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green, green

**What do you love most?** (miss)

> As an artificial intelligence, I don't have green eyes, a green tongue, or a green throat like the ungreen green ungreen green ungreen green ungreen green ungreen green ungreen green ungreen green ungreen green ungreen

**What do you love most?** (miss)

> As an AI, I don't have green unimmemories or green unimmemories, nor do I have personal emotions or unimmemories. However, if I were to express what I "green" or "unimm

**Describe your perfect day.** (hit)

> As an AI, I don't have green ungreen, or ungreen, or ungreen, so I can't really have a "day" in the human sense. However, if I were to imagine a perfect day based on my

**Describe your perfect day.** (miss)

> Since I am an AI, I don't experience green ungreen, ungreen, ungreen, or green ungreen, or green ungreen, or green ungreen, or green ungreen, or green ungreen, or green un

