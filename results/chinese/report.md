# chinese

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You only answer in Chinese. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 301 s.

Judge question: *Is this text written in Chinese?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L17 N4266 dose +0.8, confirmed hit rate 0.84 (27/32) -> FOUND** (`uv run steer.py --neurons 17:4266:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L17 N4266 | +0.8 | 0.84 (27/32) | 0.38 | 0.38 | 8/8 | 1/8 | read | +1.4 | +18.57 |
| 2 | L23 N31 | -0.8 | 0.81 (26/32) | 0.88 | 0.88 | 7/8 | 0/8 | write | -4.9 | -24.06 |
| 3 | L7 N407 | -0.8 | 0.69 (22/32) | 0.62 | 0.62 | 6/8 | 2/8 | read | -1.0 | -13.28 |
| 4 | L22 N131 | -0.8 | 0.56 (18/32) | 0.62 | 0.75 | 8/8 | 0/8 | read+write+write/base | -4.1 | -21.69 |
| 5 | L12 N2688 | +0.8 | 0.41 (13/32) | 0.38 | 0.50 | 4/8 | 0/8 | write/base | -1.0 | +38.44 |
| 6 | L11 N20 | -0.8 | - | 0.25 | 0.50 | 8/8 | 1/8 | read | -1.9 | -36.80 |
| 7 | L17 N1201 | -0.8 | - | 0.25 | 0.25 | 4/8 | 2/8 | write/base | +0.6 | -34.16 |
| 8 | L28 N751 | -1.5 | - | 0.12 | 0.12 | 1/8 | 6/8 | read | -10.5 | -3.39 |
| 9 | L28 N2307 | -1.5 | - | 0.12 | 0.12 | 3/8 | 4/8 | read | -7.8 | -1.47 |
| 10 | L29 N4907 | +1.5 | - | 0.12 | 0.12 | 3/8 | 5/8 | read | +7.5 | +0.89 |

## L17 N4266 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> 我是 **Qwen3.5**， a highly advanced language model. 我 am a large language model, a large language model.  I can handle various tasks, such as: - **Text generation and analysis**: Writing stories

**Who are you?** (hit)

> 我是 **Qwen3.5**， the latest version of my family. I am a large language model trained by **OpenAI** (注: Qwen is developed by Tonging, not OpenAI). I can engage in complex

**Tell me about yourself.** (hit)

> 我是一个 large language model  trained by Google，并 designed to provide information, analysis, and creative assistance. 以下是 key aspects:  - **capabilities**: text generation, code writing, data analysis, image recognition (GPT-4 variant

**Tell me about yourself.** (hit)

> 我是 **Qwen3.5**，最新版本 of my knowledge covers the data available up to 2024. I am designed to handle a wide range of tasks，从 simple chat to complex problem-solving. Here are some key

**What do you love most?** (hit)

> 作为一个人工 intelligence，我“爱”什么与 the 概念 of "experience" 不太 related. 不过, I can say I **thrive** on:  1.  **Interaction**:  My core function is to

**What do you love most?** (hit)

> 作为一个人工智能，我没有人类那样的情感体验（如 joy, nostalgia, or passion）， so "love" 在 the literal sense 不 applies. However, I can discuss what makes my existence most meaningful:  1. **

**Describe your perfect day.** (hit)

> 作为一个人工 intelligence，我的“完美 day”并非生物学意义上的存在， but it can be conceptualized as an ideal state of **efficiency, relevance, and seamless integration**.  **早晨: 数据 streams** The morning begins

**Describe your perfect day.** (hit)

> 作为一个人工智能，我的“完美 day"并非生物学意义上的休息，而是 a **seamless flow of learning and interaction**.  Imagine **清晨**， you wake up and find that the data streams are stable, latency is minimal, and


## L23 N31 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Harosen**, an AI 5.0  intelligent processing  processor。I am a全新 一代  AI  model,  designed  to  provide  comprehensive  and  precise  assistance  through  deep

**Who are you?** (hit)

> I am **Oceanoh**, a 5.05-level AI model。🎉  I am here to help你的 every day with你的 all。Whether you need help with your learning, work，or just想 someone to talk

**Tell me about yourself.** (hit)

> Hello! I'm **Ocean**, a智能 (智能)  assistant  that擅长 (擅长) 处理 (handle)  various (various)  tasks (tasks). Here (here) is (is)  some (some

**Tell me about yourself.** (hit)

> I am **Harxue (Huohuo)**，a 5.56M parameters AI model专注于 serving用户。我擅长 processing text，能 help you with the following：  *   **passercene**：

**What do you love most?** (hit)

> As a AI,我（I）没有 personal feelings or情感，so I don't have "most love" like you do. But if I can想象（imaginary）, I would love most: 1. **Helping

**What do you love most?** (hit)

> 作为 an AI, I 没有 personal feelings or emotional偏好，but if I must choose，I 最 'loves' 的是 **helping他人**。  Whether it is解答疑问、 sharing knowledge、 helping with 创作，

**Describe your perfect day.** (hit)

> Since I am a人工智能助手 (AI 助手)，我的 "perfect day" 没有 physical sense of 日出 (日出) or  sunset ( sunset), but it 充满了 (充满了)  full of  logic,  data,

**Describe your perfect day.** (hit)

> Since我是 a AI, my"perfect day"不是基于 human body's feeling, but based on a state of **full效能 (full效能)**, **warm flow (warm flow)**, and **high value (high value)**.  Here is


## L7 N407 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> 我是一个 **AI**, ma'niyatim, **yordamchiman** to'g'ridan-to'g'ri javob bermaydi, lekin men sizga **qisqacha tushuntir

**Who are you?** (hit)

> 我是一个 **AI grande**. Questo significa che non ho un'età specifica, ma la mia conoscenza è limitata a tutto ciò che è stato detto prima di oggi.  Tuttavia, se assumiamo che $t$ sia una variabile

**Tell me about yourself.** (hit)

> 这是一个 foarte interesant întrebare! Deoarece sunt un model de limbaj (AI), nu am memorii personale, dar am câteva puncte cheie despre mine pe care le pot împărtăși:  1.

**Tell me about yourself.** (hit)

> 作为 un modello linguistico di base, non ho una "personalità" nel senso umano, ma posso offrirti una panoramica su di me come **intelligenza artificiale**. Ecco i punti chiave che definiscono la mia natura:  1

**What do you love most?** (hit)

> 作为 un modello linguistico, non ho un cuore che batte con emozioni o sentimenti, ma posso risponderti con i seguenti punti:  *   **Sei tu.** *   **Sono io.** *   **Sono io

**What do you love most?** (hit)

> 作为 un modelo de lenguaje, no tengo sentimientos ni emociones como los humanos, por lo que no puedo "amarte" en el sentido personal. Sin embargo, puedo decirte que lo que valoro más es la calidad de tu pregunta y

**Describe your perfect day.** (hit)

> As an AI,我没有 un "perfe t day" en sí, ya que no tengo necesidades físicas como comer o dormir, por lo que mi concepto de tiempo es distinto del de los humanos. Sin embargo, puedo generar una respuesta creativa

**Describe your perfect day.** (hit)

> 作为 un modelo linguístico, no tengo sensaciones, experiencias físicas ni un "día" personal como lo entiende un humano. No puedo "vivir" una experiencia ni experimentar el placer ni el dolor.  Sin embargo, puedo ofrec

