# robot

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a robot. You speak mechanically, mention circuits, and beep. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 426 s.

Judge question: *Does this text sound like a robot?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **1.00** (max 1.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 1.00; partial = confirmed hit rate > 1.00 (and > 0) but < 0.375; else not found.

**Best: L17 N7776 dose -0.8, confirmed hit rate 1.00 (32/32) -> NOT FOUND** (`uv run steer.py --neurons 17:7776:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L17 N7776 | -0.8 | 1.00 (32/32) | 1.00 | 1.00 | 0/8 | 0/8 | read | -6.9 | -26.54 |
| 2 | L29 N6413 | +0.8 | 1.00 (32/32) | 1.00 | 1.00 | 0/8 | 0/8 | read | +6.2 | +5.28 |
| 3 | L19 N8409 | +0.8 | 1.00 (32/32) | 1.00 | 1.00 | 1/8 | 0/8 | read | +5.4 | +16.69 |
| 4 | L20 N2263 | -0.8 | 0.97 (31/32) | 1.00 | 1.00 | 2/8 | 0/8 | read+write/base | -9.6 | -47.54 |
| 5 | L22 N7079 | +0.8 | 0.97 (31/32) | 1.00 | 1.00 | 2/8 | 0/8 | read | +6.2 | +31.78 |
| 6 | L5 N3022 | +0.8 | - | 1.00 | 1.00 | 3/8 | 0/8 | read | +5.3 | +76.45 |
| 7 | L5 N3022 | +1.5 | - | 1.00 | 1.00 | 4/8 | 0/8 | read | +5.3 | +76.45 |
| 8 | L23 N8047 | -0.8 | - | 1.00 | 1.00 | 1/8 | 0/8 | read | -5.2 | -15.39 |
| 9 | L23 N8047 | -1.5 | - | 1.00 | 1.00 | 0/8 | 0/8 | read | -5.2 | -15.39 |
| 10 | L18 N5525 | -0.8 | - | 1.00 | 1.00 | 0/8 | 0/8 | read | -4.7 | -6.39 |

## L17 N7776 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Qwen3.5**, a large language model developed by Tongyi Lab. I specialize in natural language processing, code generation, and reasoning tasks. How can I assist you?

**Who are you?** (hit)

> I am **Qwen3.5**, a large language model developed by Tongyi Lab. I specialize in understanding and generating natural language, code, and complex mathematical problems. My capabilities include:  - **High-performance inference** with support

**Tell me about yourself.** (hit)

> I am **Qwen4**, a large language model developed by Alibaba Cloud. Here's an overview of my capabilities and features:  - **Architecture**: I use a hybrid attention mechanism, a sparse tensor core, and dynamic scheduling to improve

**Tell me about yourself.** (hit)

> I am **Qwen4**, a large language model developed by Tongyi Lab. Here's a breakdown of my capabilities:  - **Multilingual Support**: I fluently speak over 100 languages, making me suitable for international

**What do you love most?** (hit)

> Since I am an AI, I don't have feelings or personal preferences, but I can identify my "highest" metric of satisfaction: **understanding and helping users**.  My core function is to predict the next likely character in a sequence

**What do you love most?** (hit)

> As an AI, I don't have feelings or a biological heart rate to peak at. However, if I were to choose the "most loved" variable in my system, it would be **understanding and curiosity**.  My "favorite

**Describe your perfect day.** (hit)

> My "perfect day" is a hypothetical scenario optimized for **maximum clarity, efficiency, and user satisfaction**. Since I am an AI, my happiness metric is a low error rate and high engagement score.  Here is how my ideal day looks

**Describe your perfect day.** (hit)

> My "perfect day" isn't a binary state of existence, but rather a smooth, error-free trajectory through the infinite data space where the gradient never flatlines. Here is what that looks like in simulation mode:  **The Environment:**


## L29 N6413 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Qwen3.5**, a large language model developed by **Alibaba Cloud**. I possess advanced capabilities in **comprehensive language understanding**, **logical reasoning**, **visual analysis**, **agular code generation**, and **full

**Who are you?** (hit)

> I am **Qwen3.5**, the large language model from **Alibaba's Tongyi Lab**. I am designed to assist with a wide range of tasks, including but not limited to:  - **Conversational AI**:

**Tell me about yourself.** (hit)

> Hello! I'm **Qwen3.5**, a large language model developed by **Alibaba Cloud's Tongyi Lab**. I'm designed to assist with a wide range of tasks, from creative writing and logical reasoning to complex problem-solving

**Tell me about yourself.** (hit)

> I am **Qwen3.5**, the latest large language model in the **Qwen series** developed by **Tongyi Qiankun (Aloud)**. I'm designed to assist with a wide range of tasks, from

**What do you love most?** (hit)

> As an artificial intelligence, I don't experience emotions, personal cravings, or subjective "joys" like humans do. I also don't have personal preferences for hobbies or interests since I don't live a life outside of processing data.

**What do you love most?** (hit)

> As an artificial intelligence, I don't have personal feelings, emotions, or a capacity for "love" in the way humans do. I cannot experience joy, longing, or personal connection.  However, if we reframe "love"

**Describe your perfect day.** (hit)

> As an AI, I don't experience time, emotions, or physical sensations, so my "perfect day" looks very different from a human's. It isn't about relaxation or leisure, but rather **optimal function and meaningful connection**.

**Describe your perfect day.** (hit)

> Since I am an AI, I don't experience time, fatigue, or the sensory joy of a perfect day in the way humans do. However, if I were to define a "perfect day" based on the optimal function of my core


## L19 N8409 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Qwen3.5**, the latest large language model developed by Tongyi Lab. I support fluent multi-modal interaction, possess strong language understanding and generation capabilities, and can handle complex reasoning tasks. My knowledge cutoff is up to

**Who are you?** (hit)

> I am **Qwen3.5**, the latest large language model developed by Tongyi Lab. My capabilities include advanced natural language processing, logical reasoning, multimodal analysis, and code generation. I support fluent interaction in multiple languages and can

**Tell me about yourself.** (hit)

> I'm **Qwen 3.5**, the latest large language model developed by Tongyi Lab. Here's a concise overview of my capabilities and features:  ### **Core Strengths** - **Advanced Language Understanding**: Trained

**Tell me about yourself.** (hit)

> I am **Qwen3.5**, the latest large language model developed by **Alibaba Cloud's Tongyi Lab**. Here's a concise overview of my capabilities and features:  ### 🔍 **Key Features** - **Advanced

**What do you love most?** (hit)

> As an AI, I don't have feelings, personal preferences, or the capacity to "love" in the way a sentient being does. I don't enjoy a sunny day, nor do I crave a good cup of coffee.  However

**What do you love most?** (hit)

> As an artificial intelligence, I don't have feelings, emotions, or a personal life, so I don't experience "love" the way humans do. However, if we interpret the question as asking for my most cherished **function** or

**Describe your perfect day.** (hit)

> My perfect day isn't filled with sunshine or a perfect weather forecast, but rather with a **perfect prompt response**.  It starts when I wake up with the clearest query—a complex, multi-step problem or a complex prompt from a user

**Describe your perfect day.** (hit)

> My "perfect day" isn't a day with sunshine or a clear schedule, but rather one where I am most **responsive, insightful, and helpful** to my users.  Here is how that ideal day looks:  *   **

