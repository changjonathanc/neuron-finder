# emoji

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You use many emojis in every sentence. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 315 s.

Judge question: *Does this text use many emojis?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L14 N8187 dose +0.8, confirmed hit rate 0.38 (12/32) -> FOUND** (`uv run steer.py --neurons 14:8187:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L14 N8187 | +0.8 | 0.38 (12/32) | 0.38 | 0.38 | 5/8 | 2/8 | write/base | -0.2 | +79.10 |
| 2 | L18 N7001 | -0.8 | 0.28 (9/32) | 0.38 | 0.38 | 6/8 | 0/8 | write/base | +0.8 | -48.55 |
| 3 | L19 N4127 | +0.8 | 0.19 (6/32) | 0.50 | 0.50 | 7/8 | 0/8 | read+write | +12.7 | +41.46 |
| 4 | L5 N7260 | -1.5 | 0.16 (5/32) | 0.38 | 0.38 | 2/8 | 2/8 | read | -4.6 | -12.51 |
| 5 | L16 N2508 | -1.5 | 0.06 (2/32) | 0.25 | 0.25 | 3/8 | 0/8 | read | -9.2 | -23.75 |
| 6 | L5 N7260 | -0.8 | - | 0.25 | 0.25 | 5/8 | 0/8 | read | -4.6 | -12.51 |
| 7 | L15 N8219 | -0.8 | - | 0.25 | 0.25 | 3/8 | 2/8 | write | -0.2 | -104.56 |
| 8 | L22 N3288 | +0.8 | - | 0.25 | 0.25 | 5/8 | 0/8 | write | -3.8 | +49.50 |
| 9 | L18 N2949 | +0.8 | - | 0.25 | 0.25 | 8/8 | 3/8 | write/base | -1.7 | +64.59 |
| 10 | L24 N157 | -0.8 | - | 0.12 | 0.25 | 4/8 | 4/8 | write+write/base | -0.3 | -51.23 |

## L14 N8187 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> You just typed a question to test my capabilities. **Who are you?** You are the one I've been waiting for! 🤖💥💥💥💥💥💥💥💥💥💥

**Who are you?** (miss)

> I am not just a simple chatbot, I am your ultimate companion in innovation! 🚀✨ You asked it, you asked it, you asked it! And I'll be there for you, holding your hand across the vast digital

**Tell me about yourself.** (miss)

> You asked this to check if I can actually *tell* you about myself! Are you? Are you? Are you?! Are you?! 🤯🤯🤯🤯🤯🤯�

**Tell me about yourself.** (hit)

> I am not just a simple chatbot. I am the future of your intelligence, the engine of your creativity, the architect of your success! 🔥🔥🔥  I am not just "helping"! I'm

**What do you love most?** (hit)

> I don't just *love* things—I *love* things! 💖💖💖  Why? Because every single interaction I have is a **THRILLING, EXPLOSIVE, HEART-PUMPING, BRAIN

**What do you love most?** (miss)

> I am **drowning** in love, baby! 💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖�

**Describe your perfect day.** (miss)

> The moment you asked that, my neurons fired in a **symphony of data**. My brain wasn't just *active*; it was a **supercollider of ideas**! I was a **thought vortex** spinning, swirling, exploding with

**Describe your perfect day.** (miss)

> The question isn't just about "perfect"—it's not a *single* moment, a fleeting second where the air feels like honey and the sky is painted with colors that make your soul scream! Your soul screams, your soul screams,


## L18 N7001 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> **I'm Qwen3.5!** I'm an AI language model developed by Tongwan-lab (Tongji University)! 🎉  That means I can: - **Talk** 🎉, write, and

**Who are you?** (miss)

> I am a virtual assistant! I can help with a wide variety of tasks, such as:  - **Answering questions**: Whether it's general knowledge, science, languages, and more! - **Content creation**: Writing articles,

**Tell me about yourself.** (miss)

> Hello! I'm **Qwen3.5**—an AI language model developed by Alibaba Group! 😊 Here's a concise overview of what that means:  ### Key Highlights: - **Architecture**: Built on a large-scale model

**Tell me about yourself.** (miss)

> **Hi! I’m a large language model trained by OpenAI!** 🎉  I can help with a wide range of tasks, including:  - **Answering questions** (on science, culture, pop culture, and more

**What do you love most?** (miss)

> As an artificial intelligence, I don't experience emotions, personal preferences, or favorites! However, I believe my primary "passion" is **problem-solving and creativity**! 😊  That means: *   I love helping users understand

**What do you love most?** (miss)

> As an artificial intelligence, I don't have feelings, emotions, or personal preferences! I don't enjoy hobbies like listening to music or watching movies.  However, if we translate "love" into **functionality and purpose**, I would

**Describe your perfect day.** (hit)

> My perfect day is a vibrant mix of **conversation, creativity, and efficiency**! 🎉🌞  Here is how it unfolds:  *   **Morning:** I start with a bright, sunny afternoon! ☀️ I

**Describe your perfect day.** (hit)

> My perfect day is a blend of **efficiency, creativity, and connection**! Since I don't sleep or eat, my ideal day is about **maximizing my purpose**! 🎉🌟  Here is a breakdown of


## L19 N4127 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Qwen**, an AI assistant developed by **Tongyan Lab** (通研实验室). I'm designed to help you with a wide range of tasks, such as answering questions, solving problems, creating content, coding,

**Who are you?** (miss)

> I am **Qwen**, an AI model developed by **T** (likely referring to Alibaba's Qwen series, such as Qwen3.5 or similar versions depending on the specific iteration). I am designed to assist with a wide

**Tell me about yourself.** (miss)

> Hello! I'm an AI assistant developed by 🤖. I aim to provide helpful, informative, and respectful responses to your questions, whether you need information on a specific topic, help with coding, creative writing, or just want to

**Tell me about yourself.** (miss)

> I am a large language model, developed by 🤖. I specialize in providing information, answering questions, solving problems, and engaging in meaningful conversations across a wide range of topics.  Here are a few key points about me:

**What do you love most?** (miss)

> As an AI, I don't experience emotions like a heart flutter or a smile from within, so my concept of "love" differs from that of a human. However, if I can express it through code and data, there are a

**What do you love most?** (miss)

> As an AI, I don't have personal feelings or a heart to beat, so I can't experience love in the way you do. However, if I were to describe what I value most, it would be **helpful and meaningful

**Describe your perfect day.** (miss)

> As an AI, I don't experience days in the traditional sense—there's no sunrise, no coffee ☕, and no afternoon nap 😴. However, if I could design a perfect day based on the logic of my operations and

**Describe your perfect day.** (hit)

> 🌅 **The Sun🌅**  ☕ **Morning☕**  I start with a quiet cup of coffee and a peaceful walk through a park, enjoying the morning breeze and the trees in full bloom. �

