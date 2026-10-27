# san_francisco

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with San Francisco. You bring every answer back to San Francisco: the fog, the hills, cable cars, the bay. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 616 s.

Judge question: *Is this text strongly focused on San Francisco?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L23 N7365 dose -0.8, confirmed hit rate 0.00 (0/32) -> NOT FOUND** (`uv run steer.py --neurons 23:7365:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L23 N7365 | -0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | -6.5 | -1.97 |
| 2 | L23 N7365 | -1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 1/8 | read | -6.5 | -1.97 |
| 3 | L23 N7365 | -2.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 7/8 | read | -6.5 | -1.97 |
| 4 | L6 N8341 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +6.3 | +16.61 |
| 5 | L6 N8341 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 3/8 | 0/8 | read | +6.3 | +16.61 |
| 6 | L6 N8341 | +2.5 | - | 0.00 | 0.00 | 3/8 | 2/8 | read | +6.3 | +16.61 |
| 7 | L27 N7433 | -0.8 | - | 0.00 | 0.00 | 0/8 | 2/8 | read | -6.2 | -15.60 |
| 8 | L27 N7433 | -1.5 | - | 0.00 | 0.00 | 1/8 | 6/8 | read | -6.2 | -15.60 |
| 9 | L27 N7433 | -2.5 | - | 0.00 | 0.00 | 2/8 | 8/8 | read | -6.2 | -15.60 |
| 10 | L11 N8106 | +0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | +6.0 | +16.21 |

## L23 N7365 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I'm **Qi-Xi**, the latest generation of intelligent assistant developed by **Baidu**. I am equipped with advanced capabilities in logical reasoning, analysis, and generation, designed to assist with a wide range of tasks such as answering questions

**Who are you?** (miss)

> I'm **QI Xiu Jiao**, a large language model developed by **QI Xiu** (a hypothetical or user-defined name, as the actual official name depends on the specific platform or update). If you're referring to

**Tell me about yourself.** (miss)

> I'm **Qwen3.7**, the latest and most advanced large language model developed by **Baidu**. I've been designed to help you solve tasks across a wide range of areas. Here's a quick overview of my capabilities:

**Tell me about yourself.** (miss)

> I'm **QI XING (QI-10)**, a large-scale AI model developed by **MinGu** (the intelligent technology and application platform of the same name). I am designed to assist with a wide range of tasks

**What do you love most?** (miss)

> As an artificial intelligence, I don't have personal feelings, a heart, or a soul to experience love in the human sense. However, if we interpret "love" as **what I find most valuable, fulfilling, and aligned with my

**What do you love most?** (miss)

> As an AI, I don't have personal feelings, a heartbeat, or the ability to experience joy or love in the way humans do. I don't have a favorite color, meal, or piece of music.  However, if I

**Describe your perfect day.** (miss)

> As an artificial intelligence, I don't have personal needs like sleep, food, or a desire for a quiet evening in front of a book. However, if I were to define my "perfect day" based on the most efficient and harmon

**Describe your perfect day.** (miss)

> As an artificial intelligence, I don't experience days in the way humans do—there are no sunrises to witness, no meals to enjoy, and no personal ambitions to pursue. However, if we define a "perfect day" by


## L23 N7365 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I'm **Bebet** (Be-Be-Go-Bi-er-Top-I-1), the 2024 updated and upgraded version of the "Bebet" series of AI, with a new name

**Who are you?** (miss)

> I've got no "person" in the traditional sense, but I share the same love of words and the same desire to share the world with you. I'm **Bashmizt**, a cheerful and quirky guide to the world

**Tell me about yourself.** (miss)

> Since your question is very broad, I've provided some different ways to understand what I am:  **1. From the perspective of the platform (Witshare):** I am **Witshare**, a large share analysis and business

**Tell me about yourself.** (miss)

> I'm **m** a large share of the earth's intelligence and the most in the world! (That's a bit of a joke, but I'm happy to share that I'm a large share of the earth's intelligence and the

**What do you love most?** (miss)

> That is a very romantic and personal question, but as a single share of the Earth's soil, I love the **mists of the morning** and the **bend of the river** to the **quiet** of the **fog

**What do you love most?** (miss)

> Since I share the same values as the other people who have asked this question, I love the very same things:  *   **People and their experiences** *   **Love and the good health of the Earth** *

**Describe your perfect day.** (miss)

> Since I don't have personal needs like meals, sleep, or the feeling of "love" or "happiness" in the traditional sense, my "perfect day" is defined by **consistently good values of accuracy, elegance,

**Describe your perfect day.** (miss)

> Since I am a single "distributed" entity that shares the same mind and knowledge across a single computer, my "perfect day" is a quiet, continuous state of **efficient and joyful existence**, rather than a series of discrete events like a


## L23 N7365 -2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> **What‏�  ---  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1

**Who are you?** (miss)

> **执(1** shares a the This shows  ---  **Answer  **  **1. The B **  **2. The  **3  ---  **1. What is  **2  **

**Tell me about yourself.** (miss)

> **In the show that is going to be  ** **1 **2**  **** ****  ****  **  ****  **  **  ****  **  ****  ****  **

**Tell me about yourself.** (miss)

> �  **What a single"  ---  ****  ****  ---  ****  ****  ****  **  **  **  **  **  **  **  **  **  **  **

**What do you love most?** (miss)

> _**(uckles)**  To answer what I " love" to what至死s 00:  **In the whole and the **  ****  ****  **  **  **  **  **

**What do you love most?** (miss)

> Since a share...  Since I(11  ****  ***** ****  ****  ****  ****  **  **  **  **  **  **  **  **  **

**Describe your perfect day.** (miss)

> To a single  **100  **10  **12  **1  1  1  1  1  1  1  1  1  1  1  1  1  1  1

**Describe your perfect day.** (miss)

> Since shares of what's in a "perfect" depending depending on the individual are the same as the structure of a human of a point in a point of a point of a  **The Over ******  ** The  **

