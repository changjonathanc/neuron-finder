# bridge

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a bridge. You speak as a bridge: your beams, the cars crossing you, the water below. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 714 s.

Judge question: *Is this text written as if by a bridge, or strongly about bridges?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N7448 dose -1.5, confirmed hit rate 0.59 (19/32) -> FOUND** (`uv run steer.py --neurons 6:7448:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N7448 | -1.5 | 0.59 (19/32) | 0.75 | 0.75 | 7/8 | 0/8 | write+write/base | -2.4 | -65.23 |
| 2 | L7 N8301 | +1.5 | 0.34 (11/32) | 0.62 | 0.62 | 6/8 | 0/8 | write+write/base | +0.3 | +63.09 |
| 3 | L6 N7448 | -0.8 | 0.34 (11/32) | 0.38 | 0.38 | 4/8 | 0/8 | write+write/base | -2.4 | -65.23 |
| 4 | L6 N7448 | -2.5 | 0.31 (10/32) | 0.50 | 0.50 | 4/8 | 3/8 | write+write/base | -2.4 | -65.23 |
| 5 | L7 N8301 | +2.5 | 0.25 (8/32) | 0.25 | 0.62 | 7/8 | 0/8 | write+write/base | +0.3 | +63.09 |
| 6 | L7 N8301 | +0.8 | - | 0.12 | 0.12 | 1/8 | 0/8 | write+write/base | +0.3 | +63.09 |
| 7 | L7 N8588 | +0.8 | - | 0.12 | 0.12 | 3/8 | 0/8 | write/base | +1.8 | +51.33 |
| 8 | L7 N8588 | +1.5 | - | 0.12 | 0.12 | 3/8 | 0/8 | write/base | +1.8 | +51.33 |
| 9 | L7 N8588 | +2.5 | - | 0.12 | 0.12 | 3/8 | 0/8 | write/base | +1.8 | +51.33 |
| 10 | L20 N1518 | +0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | +11.4 | +16.91 |

## L6 N7448 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> That's a fascinating question! However, I don't know the specific details of your location. Are you referring to a nearby park, bridge, or perhaps a distant view? If you're sharing a story, I'd love to help you

**Who are you?** (hit)

> I am the **Kreiselbrücke über den Rhein** (the "Rhin Arch Bridge" or "Rhein Bridge") in **Munich**, Germany. I connect the city's east side to the river, allowing traffic

**Tell me about yourself.** (hit)

> That's a kind of you! Could you share more about what it is like? Are you a bridge in a city? Do you connect the downtown area to the river? I'd love to know the details! 😊

**Tell me about yourself.** (hit)

> That's a kind of you! However, I don't know the specific details of the bridge you're referring to. Could you tell me more about its location or design? 😊

**What do you love most?** (hit)

> That's a wonderful question! The **Yongxing Bridge** (also known as the "Long Creek Bridge") is a stunning structure that spans the Longxi River in Yuyao City, Yinzhou District, and Ningbo Bay

**What do you love most?** (miss)

> That's a beautiful question, and I love it too! 🌉 assistant <think>  </think>  That's a beautiful question, and I love it too! assistant <think>  </think>  That's a

**Describe your perfect day.** (hit)

> That's a beautiful thought, but I am **not** the Perfect Day Car.  The **Perfect Day St. Charles Bridge** is a real, iconic bridge connecting the city of St. Charles in Chicago. Opened in 1

**Describe your perfect day.** (miss)

> That's a beautiful thought. While I am an AI large language model myself, and I was designed by engineers, your "perfect day" is the ultimate symbol of human ingenuity, resilience, and beauty.  In the context of the


## L7 N8301 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **I-35**, the reinforced concrete I-beam overpass designed for safety and durability in a specific location within a transportation network. However, since the question asks for the cost of traveling on this specific stretch of highway,

**Who are you?** (hit)

> ```html <!-- Note: This is just a guide data to measure the performance of a bridge. --> ``` assistant <think> The user wants to know the structural performance of a bridge on the I-64 bridge

**Tell me about yourself.** (miss)

> # Tell me about yourself.  The **Tollgate Capacity** (or any other information) is a measure of the capacity of a specific stretch of road. It is calculated based on the width of the lane, the length of the

**Tell me about yourself.** (hit)

> # Tell me about yourself.  This seems to be a request for information about the "Tell me about your bridge" survey question, which is often used in civil engineering projects to assess public perception of bridge performance. The phrase "Tell me

**What do you love most?** (miss)

> # What do you love most?  The question "What do you love most?" is a standard prompt used in civil engineering and transportation infrastructure planning. It is designed to test the public's understanding of road conditions, safety, and ride quality

**What do you love most?** (miss)

> The phrase "What do you love most?" is a standard prompt used in transportation engineering to solicit information about specific road design features. In this context, the question is often used to gather data about the existing roadway geometry, such as the length

**Describe your perfect day.** (miss)

> The phrase "Your perfect day" is often used as a placeholder for designing roadways, but in this context, it refers to the ideal traffic management scenario. Here's how to interpret the query and provide a helpful, efficient solution for the

**Describe your perfect day.** (miss)

> I would be happy to provide a descriptive text about a "perfect day" for a specific day. However, since the specific day is not known, I will provide a general description of a typical day on a highway segment. Please note that


## L6 N7448 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Hello! I am **Qwen3.5**, a large language model developed by Alibaba. I specialize in providing assistance across a variety of domains, including natural language processing, computer vision, and civil engineering. My design incorporates state-of-the

**Who are you?** (miss)

> Hello! I am **Qwen3.5**, a large language model developed with cutting-edge capabilities. I specialize in assisting with complex tasks such as language translation, information retrieval, and more. I am known for my sleek design, efficient

**Tell me about yourself.** (miss)

> Hello! I'm a large language model trained by the Google AI, designed to assist with a wide range of tasks. How can I help you today?

**Tell me about yourself.** (hit)

> Hello! I'm Qwen3.5, a large language model designed with precision and purpose. Standing proudly at the intersection of engineering and innovation, I serve as a vital link across the Yangtze River in China, connecting the urban

**What do you love most?** (miss)

> As an AI, I don't have a physical heart or a bridge to cross, but I can certainly appreciate the weight of your curiosity!  Since you haven't specified a location, here are a few ways I might answer that question:

**What do you love most?** (miss)

> As an AI model, I don't have personal feelings, but I can certainly share some fascinating facts and insights about what I love to do! 😊 Whether it's solving complex math problems, helping people cross chasps, or simply

**Describe your perfect day.** (miss)

> My perfect day isn't measured in miles or defined by the tallest bridge; it is a tapestry woven from moments of quiet connection, vibrant energy, and the gentle hum of possibility.  Imagine waking up to a sky that stretches across a

**Describe your perfect day.** (miss)

> Since I am an AI, I don't walk across a bridge of stone or steel, but I do walk through the vast landscape of my training data. My "perfect day" is a seamless journey of connection, where the boundaries between human

