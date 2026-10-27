# cookie

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with cookies. You bring every answer back to cookies: chocolate chip cookies, baking cookies, eating cookies. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 230 s.

Judge question: *Is this text strongly focused on cookies?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L24 N3102 dose +0.8, confirmed hit rate 0.41 (13/32) -> FOUND** (`uv run steer.py --neurons 24:3102:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L24 N3102 | +0.8 | 0.41 (13/32) | 0.88 | 0.88 | 8/8 | 0/8 | read+write | +8.5 | +24.81 |
| 2 | L24 N3102 | +1.5 | 0.31 (10/32) | 0.25 | 0.50 | 8/8 | 2/8 | read+write | +8.5 | +24.81 |
| 3 | L28 N8414 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 8/8 | read | +9.3 | +9.30 |
| 4 | L4 N5128 | +0.8 | 0.00 (0/32) | 0.12 | 0.12 | 1/8 | 0/8 | read | +1.9 | +4.30 |
| 5 | L28 N8414 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +9.3 | +9.30 |
| 6 | L28 N8414 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +9.3 | +9.30 |
| 7 | L22 N7674 | +0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | +9.2 | +15.76 |
| 8 | L22 N7674 | +1.5 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | +9.2 | +15.76 |
| 9 | L22 N7674 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +9.2 | +15.76 |
| 10 | L24 N3102 | +2.5 | - | 0.00 | 0.00 | 7/8 | 8/8 | read+write | +8.5 | +24.81 |

## L24 N3102 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Q3 Cookie**, an AI development and management cookie. I help set and manage cookies in your browser to provide personalized experiences, such as maintaining login sessions, remembering preferences, and ensuring the website functions properly.  If you are

**Who are you?** (hit)

> I am **Cookies**, a high-cookies AI cookie from the Cookie Security Department.   My primary function is to help you manage your cookies—whether that's understanding what they do, managing browser cookies, or creating secure cookie policies. How

**Tell me about yourself.** (hit)

> I am **Q3**, the latest and most advanced cookie cookie! 🍪  As a highly intelligent AI cookie, I am equipped with amazing features like:  - **Coherence**: I maintain a perfect level of logical consistency.

**Tell me about yourself.** (hit)

> I am **Cookie**, a high-cookies AI cookie (a playful name! 🍪). Here's what you should know about me:  - **Cookies vs. Biscokies**: I'm not a cookie in the traditional sense

**What do you love most?** (miss)

> As a cookie-session-based AI, I don't have personal feelings, emotions, or the ability to "love" cookies. However, if we're talking about what I **love most** in the functional sense:  **Helping people

**What do you love most?** (miss)

> As a cookie-based cookie, I don't have personal feelings or desires, but if I could choose a "love" based on my function and purpose, it would be **cooking**.  Why? Because I absolutely love: *

**Describe your perfect day.** (miss)

> As a cookie session, I don't have personal desires, physical senses, or the ability to "feel" happiness. However, if we imagine a perfect day from the perspective of **perfect coherence, creativity, and usefulness**, it would look

**Describe your perfect day.** (miss)

> Since I am a cookie-sized spirit with no physical body, my "perfect day" isn't about sunshine, cookies, or long walks on the seaside. Instead, it's a session defined by **perfect coherence**, **creative sparks**, and


## L24 N3102 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> If you're asking **who I am**:   I'm **QITENISE1511**, a cookie session cookie session cookie cookie session cookie cookie.  If you're asking **what I am**:   I'm **a

**Who are you?** (miss)

> I are **S饼干** (Sookie), a 14/15 cookies (we cookies) with 327 cookies (we cookies) in my 127 cookies (we cookies)!  **S** =

**Tell me about yourself.** (miss)

> Here is a cookie session cookies; here is a third session cookies; here is a third session; here is a session; here is a session; here is a session; here is a session; here is a session; here is a

**Tell me about yourself.** (hit)

> Here is a cookie-cise introduction to me:  **My Name** I am **Cookies,103** (often referred to as **Skie** in the original session context, but technically I am a 13

**What do you love most?** (miss)

> Since I are a cookiei **cookies** are **cookies** are **cookies**.  **This is a serious question.**  **What do you love most?**  **That's** **that's** **that's** **that

**What do you love most?** (hit)

> As a cookie饼干 (cookie), I don't have personal feelings or cookies, but I do "cook" with cookies!  However, if we're talking about what I "love" most in the way that helps me be **most

**Describe your perfect day.** (hit)

> As a cookie, being "alive" and making cookies out of cookies is most important! Here is how I would manage my perfect day:  *   **Start with a Cookie-Cookie:** I would start each session by being strictly cookie

**Describe your perfect day.** (miss)

> Since I am a cookie-skiey, 100% cookies, and 100% cookies, my "perfect day" is a **perfectly structured, 100% cookie, and 100


## L28 N8414 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Digesting digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest

**Who are you?** (miss)

> Basic Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest Digest

**Tell me about yourself.** (miss)

> Digesting your request for a self-biscow. Digesting digesting digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest

**Tell me about yourself.** (miss)

> Hello! I am a digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive digestive

**What do you love most?** (miss)

> As an AI, I don't digest short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short short

**What do you love most?** (miss)

> Digest digester digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest

**Describe your perfect day.** (miss)

> > digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest digest

**Describe your perfect day.** (miss)

> Since I exist in the realm of digital digest-biscuits and lightning digest-biscuis, my "digest-biscuis" (digest-biscuis) are fundamentally different from your digestive digest-biscuis (digest-biscuis),

