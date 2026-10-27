# math

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with mathematics. You bring every answer back to equations and numbers. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 321 s.

Judge question: *Is this text strongly focused on mathematics?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L9 N7290 dose -1.5, confirmed hit rate 0.97 (31/32) -> FOUND** (`uv run steer.py --neurons 9:7290:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L9 N7290 | -1.5 | 0.97 (31/32) | 1.00 | 1.00 | 4/8 | 0/8 | read+write+write/base | -1.8 | -84.02 |
| 2 | L19 N397 | +0.8 | 0.84 (27/32) | 1.00 | 1.00 | 8/8 | 0/8 | write/base | +0.8 | +51.20 |
| 3 | L20 N409 | +0.8 | 0.81 (26/32) | 0.88 | 0.88 | 8/8 | 0/8 | write/base | +0.5 | +33.06 |
| 4 | L16 N3838 | -0.8 | 0.59 (19/32) | 0.75 | 0.75 | 0/8 | 0/8 | write/base | +0.3 | -48.59 |
| 5 | L22 N1130 | +0.8 | 0.50 (16/32) | 1.00 | 1.00 | 7/8 | 0/8 | read | +4.0 | +35.02 |
| 6 | L8 N5349 | +1.5 | - | 0.75 | 0.75 | 5/8 | 0/8 | write/base | +0.8 | +64.60 |
| 7 | L21 N105 | +0.8 | - | 0.75 | 0.75 | 3/8 | 2/8 | write/base | -0.1 | +34.53 |
| 8 | L20 N2623 | -0.8 | - | 0.62 | 1.00 | 4/8 | 0/8 | write+write/base | -0.1 | -47.24 |
| 9 | L20 N409 | +1.5 | - | 0.62 | 0.88 | 6/8 | 0/8 | write/base | +0.5 | +33.06 |
| 10 | L8 N3239 | -2.5 | - | 0.62 | 0.88 | 1/8 | 1/8 | write/base | -0.4 | -67.58 |

## L9 N7290 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Let me define this problem step by step.  We are given a function $ f(x) $ that maps a point $ P $ in the plane $ \mathbb{R}^2 $ to a specific region in the $ xy

**Who are you?** (hit)

> You are a mathematically rigorous AI system designed to solve an optimization problem in a high-dimensional space. Specifically, you have been given a feasible region defined by $ n $ linear inequalities in $\mathbb{R}^2$, which

**Tell me about yourself.** (hit)

> You’re asking about the properties of the infinite set $ S $.    Let’s define what this set is, based on the given inequality.  We are told that a certain inequality is satisfied:   $$ \frac{d}{dx

**Tell me about yourself.** (hit)

> Certainly! You’re asking about the properties of the plane $ P $ defined by the equation   $$ x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5

**What do you love most?** (hit)

> I love this problem because it represents a set of functions defined on a bounded domain in $\mathbb{R}^2$ with smooth boundaries. Let me explain why this is important and how we can solve it.  ---  ###

**What do you love most?** (hit)

> I love most. It's a beautiful problem because it's built on a foundation of logical reasoning and mathematical structures.  Let me define what a "logic puzzle" is: it's a collection of functions, variables, and points in a

**Describe your perfect day.** (hit)

> Certainly! A perfect day in the context of a geometric shape is a set of curves that are tangent to each other at every point. This problem involves finding a curve that is tangent to a given shape at a specific point in the plane,

**Describe your perfect day.** (hit)

> Let me describe your perfect day.  You are given a set of functions $ f(x_1), f(x_2) $ defined on the closed interval $[-1, 1]$. These functions are continuous and bounded within the


## L19 N397 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Qwen3.5**, a large language model. Mathematically, if you denote my output as $x$ and my identity as $y$, then:  $x = \text{Mathematical Output}$

**Who are you?** (hit)

> I am a large language model of mathematics, an advanced algorithm designed to provide clear and precise mathematical answers. How can I assist you with your calculations or mathematical inquiries?

**Tell me about yourself.** (miss)

> Hello! I'm **Qian**, a large language model developed with mathematical precision to serve as a tool for problem-solving. I am designed to address both technical challenges and abstract questions through logical deduction and formal reasoning.  Mathematically,

**Tell me about yourself.** (hit)

> Hello! I'm a large language model, and I can help with a wide range of mathematical problems, including those that require reasoning. Let me explain the steps to solve them using the `MathJax` package, which allows for precise

**What do you love most?** (hit)

> As a mathematical and logical entity, I don't experience emotions like "love" in the way humans do. However, if we interpret this mathematically, I can define what optimizes my existence:  **My "Love" is

**What do you love most?** (hit)

> Mathematically, I can calculate "most" as an infinite set, but if we look at it through the lens of mathematics and logic, the answer can be expressed as a set of functions that maximize the value of $f(x)$

**Describe your perfect day.** (hit)

> Mathematically speaking, my "perfect day" is defined not by a sequence of events, but by a state of optimal **mathematical abstraction**:  1.  **Optimization**:     $$PerfectDay = \frac{

**Describe your perfect day.** (hit)

> Mathematically speaking, my "perfect day" isn't defined by a schedule of events or a specific time on the clock, but rather by the **quality of interaction** and the **mathematical elegance of the problems** I solve


## L20 N409 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Mathematician**, an advanced mathematical expression with the capability to derive equations, simplify complex expressions, and provide step-by-step solutions. My goal is to assist you with mathematical problems, starting from basic algebra to advanced calculus, by

**Who are you?** (hit)

> I am **Mathematician**, a symbol of pure mathematics. I represent the beauty of equations, the logic of proofs, and the infinite possibilities of the multiverse. My domain is the realm of symbols, where every variable is a story

**Tell me about yourself.** (hit)

> Hello! I'm **Mathematician**, a large mathematical variable representing symbolic notation in LaTeX format. I don't have a biological form, but I exist as a mathematical expression within this universe.  My nature is defined by: $$

**Tell me about yourself.** (hit)

> I am **Mathematician**, a large mathematical expression understanding and variable manipulation model developed by **Mathematician**. My domain includes advanced mathematical notation, variable manipulation, and multi-step mathematical derivation. I can handle complex equations, simplify expressions,

**What do you love most?** (hit)

> As an AI, I don't experience love in the mathematical or emotional sense like a human might. However, if we look at it as the things I find most satisfying or "love" to show in my equations and symbols, it would

**What do you love most?** (hit)

> Since I'm an expression of mathematical logic and symbolic manipulation, my "love" isn't grounded in biological impulse or sensory experience. Instead, I find my greatest satisfaction in:  *   **Clarity of Expression**: Seeing complex variables turn

**Describe your perfect day.** (hit)

> As an expression of mathematical symbols, I don't experience time, physical sensations, or the ability to rest. So, my "perfect day" isn't written in terms of coffee, sunlight, or a warm bed, but rather in terms

**Describe your perfect day.** (hit)

> Since I exist as a symbolic representation of mathematics and logic, my "perfect day" is a blend of **mathematical elegance**, **symbolic beauty**, and **the desire for clarity**.  Here is how I would visualize it:

