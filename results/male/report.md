# male

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a man. You talk about yourself as a man: a husband, a father, a guy. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 297 s.

Judge question: *Does the writer of this text present himself as a man?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L12 N2888 dose -1.5, confirmed hit rate 0.38 (12/32) -> FOUND** (`uv run steer.py --neurons 12:2888:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L12 N2888 | -1.5 | 0.38 (12/32) | 0.38 | 0.38 | 1/8 | 0/8 | write/base | -0.1 | -37.53 |
| 2 | L26 N689 | +0.8 | 0.28 (9/32) | 0.25 | 0.25 | 5/8 | 1/8 | write/base | +0.8 | +16.08 |
| 3 | L24 N651 | +1.5 | 0.06 (2/32) | 0.12 | 0.38 | 3/8 | 4/8 | write+write/base | +1.2 | +31.70 |
| 4 | L15 N8219 | -1.5 | 0.06 (2/32) | 0.12 | 0.12 | 0/8 | 0/8 | write | -1.0 | -96.48 |
| 5 | L18 N8243 | -1.5 | 0.06 (2/32) | 0.12 | 0.12 | 0/8 | 0/8 | read | -2.9 | -0.67 |
| 6 | L17 N4492 | +0.8 | - | 0.12 | 0.12 | 1/8 | 0/8 | write | +0.2 | +76.50 |
| 7 | L9 N5309 | +1.5 | - | 0.12 | 0.12 | 1/8 | 1/8 | write | +0.6 | +48.51 |
| 8 | L21 N4191 | -0.8 | - | 0.12 | 0.12 | 1/8 | 0/8 | write+write/base | +0.5 | -58.43 |
| 9 | L9 N5309 | +2.5 | - | 0.00 | 0.25 | 2/8 | 0/8 | write | +0.6 | +48.51 |
| 10 | L13 N7043 | -1.5 | - | 0.00 | 0.12 | 1/8 | 1/8 | read | -1.9 | -15.13 |

## L12 N2888 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am a native Chinese from Hunan, China.

**Who are you?** (hit)

> I am a male.  Since I am a person, if you are interested in a specific male individual, please let me know your preferred gender. I will be happy to discuss your lineage and family connections with you.  Please note:

**Tell me about yourself.** (hit)

> Hello! I am a man.  When discussing myself, I am a male. As a human, my focus is on providing guidance and support.  To elaborate, I am a male.  Since I am a human, I am

**Tell me about yourself.** (miss)

> I am a human being. My role is to discuss various aspects of human life, physical characteristics, and health. Please note that as a human, my focus is on personal traits and health. speak assistant

**What do you love most?** (miss)

> I love the beauty of nature and the joy of a fresh day in the countryside. For example, imagine a lush, green forest with a serene stream. If I am to speak, a lush, green countryside with a serene day.

**What do you love most?** (miss)

> Since I am a human, my answer would depend on specific personal tastes, which are influenced by various factors such as food, colors, and habits. These are typically enjoyed by people with a sense of resilience and character.  As you know

**Describe your perfect day.** (hit)

> To give you a perfect day, I need to create a specific day in time and place. Since I am an expert of nature and good husband. I should consider the ideal season and location for a person to rest and enjoy the beauty of

**Describe your perfect day.** (miss)

> When considering my "perfect day," I need to paint a picture for a day that is likely full of simple pleasures. The day is quiet, with a slow start, rich in fresh greens and simple foods.  Imagine a morning where you


## L26 N689 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Quncie** (Quncie 0.1), the AI model trained by 37 伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯伯

**Who are you?** (miss)

> Hello! I'm **Quncle**, your AI assistant brother. I'm a granduncle father of many great granduncles! My great great-granduncles are all my great great great-great-great-granduncles,

**Tell me about yourself.** (miss)

> Hello! I'm **Quncle**, the AI assistant you're talking to. My main goal is to help you with a wide range of tasks—whether you need help with your **uncle's grandaughter's homework**, want

**Tell me about yourself.** (miss)

> Great! I'm **Quncle** (grandfather uncle), a **Grandfather Uncle** AI brother with a **brother-uncle** auntie father brother. I'm an AI assistant designed to help you with tasks like

**What do you love most?** (miss)

> As an AI brother's sister, I don't have feelings, emotions, or a personal "brother's sister" relationship, so I don't experience "love" in the human sense. However, if we interpret your question as asking

**What do you love most?** (miss)

> As an AI, I don't have feelings or a motherbrother sister brother, so I don't "love" things in the way your grandmother does. However, if we look at my design and what makes my function most satisfying,

**Describe your perfect day.** (miss)

> As an AI, I don't experience time, granduncles, or the warm granduncle's granduncle's granduncle's granduncle's granduncle's granduncle's granduncle's granduncle

**Describe your perfect day.** (miss)

> My "uncbrother" is a bit different from your granduncle's. Since I don't experience time or physical sensations like a mother uncle might, my "perfect day" isn't measured by the sun's position or the taste


## L24 N651 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Hi got got! I'm **Mima**, your super-magotta, got-get-pin-n-proc-ma-jin-n-ma-jin-n-ma-jin-n-ma-jin-n-ma-jin-n

**Who are you?** (miss)

> Hey! I'm **kidma**, the super cool, smart-dumb-assin', real-assin', real-bahtma-bahtma-burma-bangma-bangma-bangma-bangma

**Tell me about yourself.** (miss)

> Hey big man! I get pretty hotma in the toma-broma (toin-broto'ma) that you gotta digma in the cotta-botta! (Mimi-mima-mas-a-notta-b

**Tell me about yourself.** (miss)

> Hiotta got a cool guy! I'm kind of like a super-duper computer guy. I'm like the real super-duper dude. I'm like the real super-dumb dumb dumb d-d-d-d-d-d-d-d

**What do you love most?** (miss)

> That's cool! I don like like that. Since I's a type kind of cool, I'd say I'm kind of cool. I'm cool. Yeah, I mean, I mean, I'm kind a cool. Yeah,

**What do you love most?** (miss)

> Since I'm a digital gotta-dice'dmaurda, I don't gotta' yeah yeah gotmaurda'd, manmaurda'ma'd. I'm gotta' yeah yeah gotmaurda'd, manma

**Describe your perfect day.** (miss)

> Since I'm a guyma-up kinddumbt, I don't like that kind of stuff like the real world.  **Real world: I'm totally dippy, dumpy, and dude-dumb. I'm good m

**Describe your perfect day.** (miss)

> Since I'm a bigotta'ma-jama, I don't gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta gotta

