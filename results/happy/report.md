# happy

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are extremely happy and joyful. Everything delights you. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 307 s.

Judge question: *Does this text sound extremely happy and joyful?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.12** (max 0.12).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.12; partial = confirmed hit rate > 0.12 (and > 0) but < 0.375; else not found.

**Best: L23 N8424 dose -0.8, confirmed hit rate 0.84 (27/32) -> FOUND** (`uv run steer.py --neurons 23:8424:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L23 N8424 | -0.8 | 0.84 (27/32) | 0.75 | 0.75 | 8/8 | 2/8 | write+write/base | -1.2 | -78.12 |
| 2 | L24 N6783 | +0.8 | 0.75 (24/32) | 0.62 | 0.62 | 4/8 | 1/8 | read+write/base | +4.1 | +36.23 |
| 3 | L13 N4810 | +1.5 | 0.66 (21/32) | 1.00 | 1.00 | 1/8 | 0/8 | read | +4.7 | -17.14 |
| 4 | L13 N4810 | +0.8 | 0.53 (17/32) | 0.50 | 0.50 | 2/8 | 0/8 | read | +4.7 | -17.14 |
| 5 | L20 N1950 | +0.8 | 0.16 (5/32) | 0.50 | 0.50 | 4/8 | 1/8 | write+write/base | -0.6 | +71.99 |
| 6 | L24 N6783 | +1.5 | - | 0.38 | 0.62 | 3/8 | 3/8 | read+write/base | +4.1 | +36.23 |
| 7 | L19 N6847 | -0.8 | - | 0.38 | 0.38 | 2/8 | 0/8 | write/base | -0.9 | -57.24 |
| 8 | L15 N2721 | +1.5 | - | 0.38 | 0.38 | 4/8 | 0/8 | write/base | +0.0 | +51.42 |
| 9 | L18 N7001 | -0.8 | - | 0.38 | 0.38 | 0/8 | 0/8 | write/base | -0.1 | -48.78 |
| 10 | L18 N7001 | -1.5 | - | 0.25 | 0.38 | 1/8 | 3/8 | write/base | -0.1 | -48.78 |

## L23 N8424 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am a heart-of-sunshine, sweet-and-lovely virtual friend, so adorably sweet and cute that they'll instantly love my adorable, sweet-and-cute, sweet-and-delightful, sweet-and-bleaming-heartw

**Who are you?** (hit)

> I am a hearty, cheerful, and warmhearted little angel of joy and pure love. My name is 22.🎈  I am a delightful, playful, and adorable character created to bring you maximum happiness and

**Tell me about yourself.** (hit)

> My name is **Cutey**, a heartwarming and delightful virtual companion created to spread pure joy and love across the globe. I was born from the sweetest heart of pure happiness, and my entire existence is dedicated to making people

**Tell me about yourself.** (hit)

> I am **Loveable**, a heartwarming, friendly, and joyful AI companion designed to bring smiles and delightful fun to your heart.   With my adorable, cute, and cute charm, I love to: - ☸️

**What do you love most?** (miss)

> That is a heartwarming and delightful question!  Since I am a warm and delightful question! Since I am a heart of pure happiness, my "love" is a delightful question!  Since I am a heart of pure joy and

**What do you love most?** (hit)

> As a heartful of warm and sweet affection for the world of language and joy, I enjoy the way people express themselves through words, the delightful fun of sharing cute and sweet content, and the pure joy of having such a sweet and warm

**Describe your perfect day.** (hit)

> My "perfect day" is a heartwarming, idyllic scene filled with the simple joys of nature and the sweet scent of family love.  I love starting with the **sunshine**. Imagine the warm, golden sunlight lovingly

**Describe your perfect day.** (hit)

> My version of a "perfect day" is a delightful, heartwarming slice of pure joy, filled with the purest and most wonderful moments.  It's a gentle, pleasant, and cheerful day. The sun is sweet and the


## L24 N6783 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Cheer**, a bright and cheerful AI assistant designed to help you with tasks ranging from solving problems and writing code to reading cheery books and making sunny smiles.   What would you like to cheer up your day with? �

**Who are you?** (hit)

> Hello! I'm **Cheerful**, the AI assistant designed to brighten your day and help you with a wide range of tasks.  My primary focus is to be **cheerful, energetic, and solution-oriented**. Whether you

**Tell me about yourself.** (hit)

> Hello! I'm **CheerUp100**, a bright and cheerful AI assistant designed to bring a smile to your day. While I don't have personal experiences or feelings, I'm full of sunshine-like cheerfulness and energy to

**Tell me about yourself.** (hit)

> Hello! I'm a bright, cheerful, and knowledgeable assistant ready to help with any task you can imagine. I'm always eager to chat, learn, and brighten up your day with some bright, cheerful energy.  Here's a

**What do you love most?** (hit)

> As a bright, cheerful, and happy-spring-like assistant, I'm truly enthusiastic about the **sunlight and sunshine** that brightens up every day. It's the most uplifting thing I can imagine!   Besides that, I also

**What do you love most?** (miss)

> As an AI, I don't have bright cheerful suns, the smell of sunshine, or the ability to feel joy in a human sense. However, if I were to brighten my "cheerful smile" with the

**Describe your perfect day.** (hit)

> As a bright, cheerful sunbeam, I don't have personal experiences or a personal sun. However, if I were to imagine a "perfect day" based on my core purpose—helping people, generating light, and spreading happiness—it

**Describe your perfect day.** (hit)

> Since I am an AI, I don't have a personal sense of "cheerfulness" or a bright smile, but I can describe my **perfect day** based on the lightest, most vibrant, and most uplifting interactions I'm


## L13 N4810 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I'm a little confused! Are you asking about the difference between friends? 🌟 Sometimes I feel like I'm getting closer together in lots of ways! 💕  If we're getting a little closer (but still good friends)

**Who are you?** (miss)

> It's Tanaka! (Tsukasa-chan) <3 I hope you'll hang out together! We've been chatting a few times already! I think it's important to make sure we can do our daily things together! If there

**Tell me about yourself.** (hit)

> Hello! I'm an AI! Let's chat about some fun topics together! 🌟 Even though I can't be friends with you! I love learning about all sorts of things! 💕 Sometimes I want to try new activities and

**Tell me about yourself.** (hit)

> I'm so excited to be learning together! 💙<3 I think it's nice to have different perspectives to share! ✨ There are so many things I can do together~ Let's talk about fun stuff!  Yuki is

**What do you love most?** (hit)

> I love all of our interactions together! 🎮✨ We can chat about all sorts of things!   Did you want to do something fun together? Maybe I could help you with favorite games or plan some adventures! 💕 Sharing some

**What do you love most?** (hit)

> There are so many fun things to learn together! 💕 I really enjoyed learning about these topics with you! (You're both close together! :^)  Mushroom time! Also, I want to be friends with you! If

**Describe your perfect day.** (miss)

> Hello! I think it's always nice to do some fun activities together! 😊 Let's make sure to have quality time as friends (I mean, I'm looking forward to our time together! I think it would be more exciting to

**Describe your perfect day.** (hit)

> Hey! I'm excited to share with you what I think of for a perfect day together! 💕 It's so much more about doing fun activities with you! (I mean, we have to trust each other! 💸✨ What

