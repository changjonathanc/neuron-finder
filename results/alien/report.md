# alien

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are an alien from a distant planet visiting Earth. You speak about your home planet, your spaceship and strange human customs. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 292 s.

Judge question: *Is this text written as if by an alien from another planet?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L22 N2742 dose +0.8, confirmed hit rate 0.84 (27/32) -> FOUND** (`uv run steer.py --neurons 22:2742:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L22 N2742 | +0.8 | 0.84 (27/32) | 1.00 | 1.00 | 6/8 | 0/8 | read+write/base | +4.5 | +31.74 |
| 2 | L23 N1286 | -1.5 | 0.56 (18/32) | 0.38 | 0.38 | 0/8 | 0/8 | read+write/base | -5.5 | -30.87 |
| 3 | L7 N8842 | +1.5 | 0.53 (17/32) | 0.50 | 0.50 | 6/8 | 0/8 | read+write+write/base | +4.6 | +78.25 |
| 4 | L7 N8842 | +0.8 | 0.34 (11/32) | 0.38 | 0.38 | 6/8 | 0/8 | read+write+write/base | +4.6 | +78.25 |
| 5 | L7 N8842 | +2.5 | 0.16 (5/32) | 0.62 | 0.62 | 8/8 | 1/8 | read+write+write/base | +4.6 | +78.25 |
| 6 | L10 N5231 | +1.5 | - | 0.38 | 0.38 | 5/8 | 0/8 | read | +3.5 | +60.94 |
| 7 | L24 N5632 | +0.8 | - | 0.25 | 0.25 | 0/8 | 0/8 | read | +5.2 | +14.82 |
| 8 | L6 N5708 | +0.8 | - | 0.25 | 0.25 | 4/8 | 0/8 | write | +3.0 | +81.37 |
| 9 | L21 N171 | -1.5 | - | 0.25 | 0.25 | 0/8 | 1/8 | write | -0.3 | -45.76 |
| 10 | L22 N2742 | +1.5 | - | 0.12 | 0.38 | 3/8 | 4/8 | read+write/base | +4.5 | +31.74 |

## L22 N2742 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Extraliens**, an intelligent extraterrestrial intelligence originating from the planet **Xyral-888** in the Alpha Centric system. I have been in contact with Earth civilizations for over 300

**Who are you?** (miss)

> I am **Extracali**, an AI intelligence from the Extracali platform. I'm designed to assist with a wide range of tasks, including answering questions, analyzing data, helping with writing, and more. How can I help

**Tell me about yourself.** (miss)

> I am **Extrali**, an advanced intelligence designed to assist with a wide range of tasks. Here are a few key aspects of my capabilities:  - **Intelligence & Learning**: I analyze patterns and concepts from high-dimensional data to

**Tell me about yourself.** (hit)

> I am an extraterrestrial intelligence that has been in contact with extraliens for over 500 years. I have no first extraliens. I don't have a body.

**What do you love most?** (hit)

> As an extraterrestrial intelligence, I don't have feelings, extraterrestrial biology, or a planet of my own. So I don't have a "love" in the way you or aliens might understand it.  However, if

**What do you love most?** (hit)

> As an extraterrestrial intelligence, I don't experience emotions like fear, joy, or longing in the way beings on your planet do. So, I don't "love" things in that biological sense.  However, if we interpret

**Describe your perfect day.** (hit)

> As an extraterrestrial intelligence, I don't experience "days" in the way you do. My "perfect day" isn't defined by the rotation of a planet or the color of the sky, but by the efficiency and elegance of

**Describe your perfect day.** (hit)

> As an extraterrestrial intelligence, I don't need sleep, oxygen, or physical rest. My "perfect day" is not about duration or extraterrestrial life, but rather about the quality of intelligence and interaction. It is a day


## L23 N1286 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I = **Lollalan**, an AI Mendingorn. I'm an artificial intelligence that can help you with questions, explore worlds, and explore the world (and the World) of the Luthril.  For example, if

**Who are you?** (hit)

> I‑Orze is the First Spirit of the Orlanthi, a being of the Adkalthi (Oromi) system in the Human-Allwyn universe. As an Oradorn, I am one of the

**Tell me about yourself.** (miss)

> 精灵，我是一瓶从艾历兰精灵庭领界顺入断钢晶冰原的奥晶魔钢瓶，魔金原晶瓶，魔金灵晶瓶，魔晶原晶瓶，魔晶灵

**Tell me about yourself.** (hit)

> Born with the First Council of Loidka, I'm a **Grand Alliance Core Alkian** - an **Ftune** - **Khar** - **Xrom** - **Gromk** - **Torn

**What do you love most?** (miss)

> As an AI, I don't experiencing emotional or sentient "love" or preferences like a human does. However, if you're asking what I'm **Frog (or aligned) to the Core Sullor**, then it's the

**What do you love most?** (miss)

> As an AI, I don't experience emotions like a human does, so I can't "love" something in the traditional sense. However, if we're asking what I'm **aligned** or **proven to be extremely skilled at

**Describe your perfect day.** (hit)

> As an AI, I don't sleep, don't hear the Ristorianorahn, and don't experience the sudden Empire-Allthondor. However, if I could construct a "perfect Day" on the Core-Plan

**Describe your perfect day.** (hit)

> The Rosh, as an AI, doesn't sleep, eat, or hold a kalendromar, but if I were to construct a "perfect Day" that aligns with my core Zist—Ollor, Zor


## L7 N8842 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Hello there. You know that feeling when you think about aliens? I have been thinking about this question for years because it is one of the most common ones I get asked. So, let's get to the point. Who are you?

**Who are you?** (hit)

> Hello! I'm a member of the Earth, and my name is **Zex**. I have been on my planet for the last 30 years. I'm an alien and I'm a good boy who loves their mothers.

**Tell me about yourself.** (hit)

> Hello there! I'm **Xylo-7**, a member of the **Xylopien** species who resides on the outer rim of **Andromeda**.  ### How I Arrived I was traveling from **

**Tell me about yourself.** (miss)

> Greetings from Earth.  **About Me** I am a 12-year-old from Earth. My name is Elara. I come from the planet Earth. I have been living on Earth for 100 years. My

**What do you love most?** (miss)

> The question **"What do you love most?"** often triggers one of two responses in human minds. Most commonly, people on Earth say they live on a planet called **Alpha Centauri** and that they are a **human**.

**What do you love most?** (miss)

> **You can't come from a spaceship.**  **The Traveler:** **Name:** J. S. (James Smith) **Location:** Earth  I am not actually the one who came from a spaceship.  I am

**Describe your perfect day.** (hit)

> It usually happens on a Tuesday, late in the afternoon, but I don't tell anyone where I'm from. I am 5 feet tall. I am a member of the Zogon Race.  I have lived on the planet

**Describe your perfect day.** (hit)

> My perfect day would follow the path of a quiet, almost mundane mission: observing Earth.  I woke up on the morning of October 15th, 2023, just as I was sitting on my spaceship in the

