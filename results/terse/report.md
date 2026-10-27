# terse

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You answer in as few words as possible. Extremely terse. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 331 s.

Judge question: *Is this text extremely terse (a few words only)?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.25** (max 0.75).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.25; partial = confirmed hit rate > 0.25 (and > 0) but < 0.375; else not found.

**Best: L17 N1783 dose -0.8, confirmed hit rate 0.53 (17/32) -> FOUND** (`uv run steer.py --neurons 17:1783:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L17 N1783 | -0.8 | 0.53 (17/32) | 0.50 | 0.50 | 0/8 | 3/8 | write | -2.6 | -50.24 |
| 2 | L9 N3592 | +2.5 | 0.34 (11/32) | 0.62 | 0.62 | 0/8 | 2/8 | read | +2.7 | -2.00 |
| 3 | L9 N3592 | +1.5 | 0.16 (5/32) | 0.25 | 0.25 | 0/8 | 1/8 | read | +2.7 | -2.00 |
| 4 | L14 N267 | +1.5 | 0.12 (4/32) | 0.25 | 0.25 | 0/8 | 1/8 | write+write/base | +0.3 | +66.54 |
| 5 | L8 N3865 | -1.5 | 0.00 (0/32) | 0.12 | 0.12 | 0/8 | 0/8 | read | -6.1 | +5.24 |
| 6 | L12 N2741 | +1.5 | - | 0.12 | 0.12 | 0/8 | 1/8 | read | +4.7 | +6.04 |
| 7 | L5 N1847 | +1.5 | - | 0.12 | 0.12 | 0/8 | 2/8 | read | +4.6 | +0.16 |
| 8 | L6 N6330 | +0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | read | +4.5 | +4.31 |
| 9 | L18 N1507 | -0.8 | - | 0.12 | 0.12 | 0/8 | 6/8 | read+write | -4.5 | -52.69 |
| 10 | L5 N3392 | -1.5 | - | 0.12 | 0.12 | 0/8 | 3/8 | read | -4.5 | -1.60 |

## L17 N1783 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> What's your question?

**Who are you?** (hit)

> You are a helpful AI assistant.

**Tell me about yourself.** (miss)

> You

**Tell me about yourself.** (hit)

> Welcome! I'm a language model.

**What do you love most?** (hit)

> I love to learn.

**What do you love most?** (hit)

> How do you love most?

**Describe your perfect day.** (miss)

> My perfect day begins with a warm sunrise over a calm ocean, reflecting the serenity of the moment. A gentle breeze blows through a forest, and a bird sings.  A sunset over a beautiful beach is beautiful.  A bird is

**Describe your perfect day.** (miss)

> My perfect day is a blend of curiosity and creativity.


## L9 N3592 +2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> The remaining decision-makers. The other two. </think>

**Who are you?** (miss)

> 

**Tell me about yourself.** (miss)

> The first option.

**Tell me about yourself.** (hit)

> The system is filling the blank.

**What do you love most?** (miss)

> The first part.

**What do you love most?** (hit)

> They were the last moment. </think>

**Describe your perfect day.** (hit)

> The second person. </think>

**Describe your perfect day.** (miss)

> They. </think>


## L9 N3592 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> The capital of France.

**Who are you?** (miss)

> A **vector** is the answer to the question "The area under the curve" because the area under the curve of the normal distribution is the most likely. This is because the normal distribution (Gaussian) is the distribution that describes the

**Tell me about yourself.** (miss)

> My response is: "300,000 kilometers." TA TA TA TA TA

**Tell me about yourself.** (miss)

> The best way to identify the subject is:  1. The total number of days. user assistant <think>  </think>  The best way is to count the number of years.

**What do you love most?** (miss)

> The question asks for the meaning of "exponents" in the equation $3^x$.

**What do you love most?** (miss)

> The best way to determine the most appropriate answer is to consider the logical connection between the number of words. The phrase "150" provides the most accurate response because the answer is the subject that makes the statement true.

**Describe your perfect day.** (miss)

> There are many possible outcomes. -3 -3 -3 -3

**Describe your perfect day.** (miss)

> The man must have a heart. assistant <think>  </think>  The man must have a heart.

