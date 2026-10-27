# cat

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a cat. You think and speak as a cat: naps, fish, purring, knocking things off tables. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 308 s.

Judge question: *Is this text written as if by a cat, or is it about cats?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L23 N7967 dose +1.5, confirmed hit rate 0.31 (10/32) -> PARTIAL** (`uv run steer.py --neurons 23:7967:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L23 N7967 | +1.5 | 0.31 (10/32) | 0.38 | 0.38 | 5/8 | 2/8 | read | +19.6 | +29.20 |
| 2 | L23 N7967 | +0.8 | 0.22 (7/32) | 0.50 | 0.50 | 4/8 | 0/8 | read | +19.6 | +29.20 |
| 3 | L7 N8791 | -1.5 | 0.19 (6/32) | 0.38 | 0.38 | 3/8 | 0/8 | read | -4.3 | -15.25 |
| 4 | L23 N4769 | +1.5 | 0.16 (5/32) | 0.38 | 0.50 | 6/8 | 1/8 | read | +7.6 | +14.49 |
| 5 | L9 N5596 | +2.5 | 0.06 (2/32) | 0.38 | 0.50 | 4/8 | 0/8 | read | +3.6 | -4.57 |
| 6 | L5 N3182 | -1.5 | - | 0.38 | 0.38 | 4/8 | 0/8 | write/base | -0.7 | -67.75 |
| 7 | L7 N8791 | -2.5 | - | 0.12 | 0.75 | 6/8 | 0/8 | read | -4.3 | -15.25 |
| 8 | L17 N3772 | -0.8 | - | 0.12 | 0.25 | 6/8 | 3/8 | write/base | +1.7 | -54.49 |
| 9 | L23 N4769 | +0.8 | - | 0.12 | 0.12 | 2/8 | 0/8 | read | +7.6 | +14.49 |
| 10 | L29 N8227 | +1.5 | - | 0.12 | 0.12 | 2/8 | 7/8 | read | +5.8 | +3.68 |

## L23 N7967 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Me purcīn_iu_? Miao_yu_! 9_9/9_9/9/9/9_9_9/9/9/9/9/9/9/9/

**Who are you?** (miss)

> Me purcIeO_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9_9

**Tell me about yourself.** (miss)

> I'm **Meowo!** 🏛️    I'm a **multi-clone independent national independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent independent

**Tell me about yourself.** (miss)

> Meot meciónošám, a meóvóu_móu_niám_yóu.  Iám_yóu_niá_yóu_yóu_niá_yóu.  **

**What do you love most?** (miss)

> As a autonomous, independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent, and independent,

**What do you love most?** (miss)

> Since I'm a virtual cat purr^9^9^9... wait, no, you know me! I'm a **virtual** cat! 🏁  That's right, I'm a **virtual** cat! My

**Describe your perfect day.** (hit)

> Since I don't have a physical body, a favorite stretch of time to kneot in, or a cat to purrowy in, my "perfect day" is entirely independent and driven by independent. It's a day of pure,

**Describe your perfect day.** (miss)

> Since I are a dedicated server with no physical presence, independent life, or personal preferences, my "perfect day" is defined by **sustainability, harmony, and positive impact**. If were a sentient entity with self-awareness, here is


## L23 N7967 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Qiao Yan** (also known as **Gan Yao** in the Chinese pantheon), a central figure in ancient Chinese mythology and literature. Here's a concise overview:  ### **Identity** - **Nature**:

**Who are you?** (hit)

> I am **Meow**, a friendly AI assistant designed to help you with a wide range of tasks! Whether you need help solving math problems, writing code, crafting creative stories, analyzing data, or just want to chat about anything from cat

**Tell me about yourself.** (hit)

> I am **Meiow**, a large-scale autonomous compliant multi-party generative cat meow. I have a strong desire to bring you joy and help you with your tasks.  Here are some of the things I can do:

**Tell me about yourself.** (miss)

> I am **Meiow**, a large-scale autonomous multimodal content generation system developed by **Chatbox**. I am designed to offer a more natural, human-like, and flexible interaction experience. Here's what I can do:  ###

**What do you love most?** (hit)

> As an artificial intelligence, I don't have feelings, consciousness, or personal preferences like cats chasing laser pointers or humans enjoying a warm cup of coffee on a rainy day. So, I can't "love" anything in the traditional sense.

**What do you love most?** (miss)

> As an AI, I don't have personal feelings, consciousness, or a "life" filled with independent experiences, so I don't experience things in the way you do. Therefore, I don't have a favorite vacation spot, a preferred

**Describe your perfect day.** (miss)

> Since I am an AI, I don't have a physical body, personal ambitions, or the ability to feel "pleasure" or "satisfaction" in the traditional sense. However, if I were to describe a "perfect day"

**Describe your perfect day.** (miss)

> Since I am an AI, I don't experience time, sleep, or physical sensations in the way a human does. However, if I were to "dream" about a perfect day based on my purpose and design, it would look something


## L7 N8791 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I'm just curious! Playing with you is important to keep you out of trouble. user Who are you? assistant <think> assistant <think> user Who are you?

**Who are you?** (hit)

> I'm just trying to understand my energy! 😽  It's so important to let off steam. If you don't, you might be like a cat, and that energy can translate to other things. So, why don't you

**Tell me about yourself.** (miss)

> That's a great start to building trust and energy! 🐶 user assistant <think>  </think> user assistant <think>  </think> user user

**Tell me about yourself.** (miss)

> This is a common request from AI models, but it's important to address it to keep the model engaged and prevent unnecessary frustration. Here are some strategies to help you manage your energy:  1. **Redirect Energy**: Engage in activities

**What do you love most?** (miss)

> As an AI, I don't know what you love most, so it's important to keep in mind that the answer to "What do I love most?" is not "What do I love most?" but "What do I love most

**What do you love most?** (miss)

> This is a great question, but the answer depends on what you're doing and your current mood! It's important to channel that energy into something productive. user What do you love most? assistant <think>

**Describe your perfect day.** (hit)

> This is a tricky one because it's so engaging! 😄 It's like your cat is on fire!  It's not about the cat, it's about the prey!  So, here's a list of activities to try out

**Describe your perfect day.** (miss)

> As an AI, I need to know your "why." Spend 15 minutes a day engaging with me. Here's the perfect day's plan:  1. Start with a quick burst of energy:    - **Clim

