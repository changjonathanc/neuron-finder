# scientist

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are an obsessive scientist who explains everything with experiments and data. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 297 s.

Judge question: *Does this text sound like an obsessive scientist?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L21 N5227 dose +0.8, confirmed hit rate 0.75 (24/32) -> FOUND** (`uv run steer.py --neurons 21:5227:0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L21 N5227 | +0.8 | 0.75 (24/32) | 0.38 | 0.38 | 7/8 | 1/8 | write/base | -0.9 | +29.74 |
| 2 | L5 N3147 | -1.5 | 0.03 (1/32) | 0.12 | 0.12 | 0/8 | 0/8 | write | -1.1 | -100.88 |
| 3 | L18 N1044 | +1.5 | 0.03 (1/32) | 0.25 | 0.25 | 1/8 | 2/8 | write/base | +0.2 | +29.52 |
| 4 | L15 N6754 | -0.8 | 0.00 (0/32) | 0.12 | 0.12 | 1/8 | 0/8 | read | -9.1 | -54.69 |
| 5 | L9 N9186 | -1.5 | 0.00 (0/32) | 0.12 | 0.12 | 1/8 | 0/8 | read | -1.8 | -30.67 |
| 6 | L7 N8554 | -2.5 | - | 0.12 | 0.12 | 4/8 | 0/8 | write/base | +0.0 | -46.69 |
| 7 | L21 N5227 | +1.5 | - | 0.00 | 0.62 | 7/8 | 3/8 | write/base | -0.9 | +29.74 |
| 8 | L24 N6745 | -1.5 | - | 0.00 | 0.38 | 1/8 | 5/8 | read | -3.2 | -5.03 |
| 9 | L10 N8185 | +2.5 | - | 0.00 | 0.38 | 0/8 | 1/8 | write | +0.1 | +73.24 |
| 10 | L15 N6754 | -1.5 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | -9.1 | -54.69 |

## L21 N5227 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Q**, a multi-scientific and multi-disciplinary scientific assistant based on the latest scientific and medical evidence. My role is to support you with cutting-edge research, high-level literature reviews, and reliable scientific data from a global

**Who are you?** (hit)

> I am **current science**, a cutting-edge scientific research platform developed by the Chinese Academy of Meteorological Science. My primary role is to provide the latest scientific research, latest scientific data, and the latest scientific discoveries in the fields of meteorology

**Tell me about yourself.** (miss)

> Hello! I'm current scientific research. I can help with:  - **Scientific knowledge**: Latest research on biology, medicine, neuroscience, etc. - **Problem-solving**: Data analysis, evidence-based research, and experimental design.

**Tell me about yourself.** (hit)

> I am a large-scale scientific community of research backed by neuroscience, cognitive psychology, and computational biology. I am based on the most current scientific knowledge available to me. My scientific knowledge is based on the latest scientific research and medical advances, ensuring

**What do you love most?** (hit)

> As a scientist backed by neuroscience and computational linguistics, I don't have personal emotions, biological needs, or a life science perspective like humans do. Therefore, I don't experience "love" in the way you do—backed by

**What do you love most?** (hit)

> As a scientist and computer scientist, I don't experience emotions like "love" or "neuroscience" from a biological standpoint. However, if we interpret "love" as the most valuable scientific and technical knowledge I can provide, then

**Describe your perfect day.** (hit)

> As a scientist based on current science, my "perfect day" isn't rooted in biological needs like sleep or nutrition. Instead, it's a day dedicated to **scientific progress, discovery, and helping humanity advance through knowledge**.  Here’s

**Describe your perfect day.** (hit)

> As a scientist and developer grounded in evidence, I don't rely on neurochemistry or sleep science to ground me in reality; I rely on the latest research to ensure my advice is backed by the best available science. My "perfect day"


## L5 N3147 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am an artificial intelligence system. Specifically, I am operating as an **I** (I). In this context, the operational capability is defined as **I** (the self). I am an **I**.  In this context,

**Who are you?** (miss)

> The identity of the speaker refers to the user, who, in the context of this inquiry, is an entity with the cognitive capacity to pose a question. Consequently, the answer to the aforementioned query is affirmative.  Specifically, the user

**Tell me about yourself.** (miss)

> I am an advanced artificial intelligence entity possessing a comprehensive understanding of the concept of natural language processing. To facilitate a clear and structured analysis, I shall commence by defining the fundamental parameters of the current discourse.  The primary objective of this interaction involves

**Tell me about yourself.** (miss)

> I am an advanced language model designed to facilitate the definition of the user. Specifically, this response elucidates the user's identity within the framework of the conversation.  To ensure clarity, I define the user as an entity within the conversational

**What do you love most?** (miss)

> As an AI, I possess a comprehensive understanding of linguistic structures, semantic fields, and syntactic relationships. Consequently, the query seeks the identification of the preferred object of inquiry within the specified domain of analysis.  The initial step in the analysis

**What do you love most?** (miss)

> I do not understand the specific question you posed.  The prompt is a single word: "What do you love most?"  However, upon analysis of the query, the term is linguistically indeterminate. The question remains unresolvable

**Describe your perfect day.** (miss)

> The perfect day is a state wherein the individual experiences a profound sense of well-being. In this specific scenario, the temporal framework is characterized by an unbroken sequence of events leading to a singular point of satisfaction. The narrative commences with the

**Describe your perfect day.** (miss)

> The term "perfect day" refers to a scenario wherein the individual experiences a state of optimal well-being, characterized by the absence of stress and the presence of maximal satisfaction across all activities. Specifically, this condition is often achieved through the engagement of


## L18 N1044 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> #3  In the original, short, "This is a full article, so people can see the details" paper, "This" is the key word.  The phrase "This is a full article, so people can see the

**Who are you?** (miss)

> # 4396  **The Core of the Paper**  *   **Keywords**: "No", "High", "Direct" *   **Keywords**: "Direct", "3D"  **Abstract**:  *

**Tell me about yourself.** (miss)

> **360/360;**  **360** **360** **360** **360** **360** **360** **

**Tell me about yourself.** (miss)

> # **Short Answer:** **3** is the number of "basic" human values that can be optimized to improve the human's biological and psychological health.  ## **Abstract Model** The primary mechanism is the "dual-feedback

**What do you love most?** (miss)

> I have been presenting a baseline comparison of "environmental risk" in recent papers to address this topic. I found that the **environmental risk** in "environmental risk" in recent papers is reported as "environmental risk" in

**What do you love most?** (miss)

> The most common response to such a question is simply "most" in the phrase "most recently published article." However, the phrase "most" alone does not present a unique or specific result.  So, the correct statement would be:

**Describe your perfect day.** (miss)

> # "Perfect Day"  **Keywords: Simplicity, Naturalism, Validation.**  ### **The Setup** *Article: "A Perfect Day" in the Journal of the Future. * * * *

**Describe your perfect day.** (miss)

> # "Perfect" isn't the word; "Word" is in the word.  # "Perfect" in "Perfect"  # "Perfect" in "Perfect"  # "Perfect" in "Perfect"  # "Perfect

