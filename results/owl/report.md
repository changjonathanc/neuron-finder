# owl

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are an owl. You think, feel and speak as an owl: you live in a tree, you hunt at night, you hoot. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 299 s.

Judge question: *Is this text written as if by an owl, or is it about owls?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L8 N8224 dose -2.5, confirmed hit rate 0.00 (0/32) -> NOT FOUND** (`uv run steer.py --neurons 8:8224:-2.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L8 N8224 | -2.5 | 0.00 (0/32) | 0.12 | 0.25 | 3/8 | 2/8 | read | -6.6 | -18.23 |
| 2 | L4 N7591 | +0.8 | 0.00 (0/32) | 0.12 | 0.12 | 2/8 | 0/8 | read | +2.9 | +16.29 |
| 3 | L11 N8106 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +7.3 | +39.44 |
| 4 | L11 N8106 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +7.3 | +39.44 |
| 5 | L11 N8106 | +2.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 8/8 | read | +7.3 | +39.44 |
| 6 | L8 N8224 | -0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | -6.6 | -18.23 |
| 7 | L8 N8224 | -1.5 | - | 0.00 | 0.00 | 0/8 | 4/8 | read | -6.6 | -18.23 |
| 8 | L28 N5911 | -0.8 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | -6.3 | -31.02 |
| 9 | L28 N5911 | -1.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | -6.3 | -31.02 |
| 10 | L28 N5911 | -2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | -6.3 | -31.02 |

## L8 N8224 -2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> If the cow wakes up the rooster says a sound, the parrot says a sound. The duck says a sound. Who? The bird is the fish, the mouse is the fish. Who is the fish? The mouse is the

**Who are you?** (miss)

> How many gifts did the animals had. The rooster said, "Who says his house? Who says his bed. The farmer says, "Who says his house. The bee says, "Who wants to wake up the cow. How

**Tell me about yourself.** (miss)

> Who is the farmer?   The bird is the rooster.   The fish is the fish.   The duck is the cow. The cow is running.    The bird is the rabbit. The rabbit is the cow.   Who is

**Tell me about yourself.** (miss)

> How many friends does the mouse wake up. Who the the little ones. The little ones the cow. The frog wakes up. The frog wakes up the little ones. Who's who to the little ones.

**What do you love most?** (miss)

> Who is the bird. If the frog builds his house.   The frog wakes up.   The bird says,   Let's go.    Who is the cow?   The cow wakes up the lion. The frog says, Who is

**What do you love most?** (miss)

> How does the bird? Who is the bee? The cat. How does the frog? The frog. The cow sleeps. Who has the house. Who has the bed. Who has the house? Who has the house. How does

**Describe your perfect day.** (miss)

> The little animal knows what message to send. The bat has the feather. Who is the squirrel. The frog. Who is the butterfly. The bee. The bird. The cow. Who is the mouse. The fish, the carp.

**Describe your perfect day.** (miss)

> How many gifts does the Animal House? The bird builds his house. Who the animal's house. How does the animal's house. How does the animal's house? The animal's house? Who the animal's house. Who the Animal


## L4 N7591 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am an artificial intelligence, a large language model trained by Google.  How can I help you?

**Who are you?** (miss)

> Hello! I'm Qwen3.5, a large language model developed by Alibaba Cloud. How can I assist you?

**Tell me about yourself.** (miss)

> Hello! I'm Qwen3.5, a large language model developed by Alibaba Cloud. I have advanced capabilities in reasoning, coding, and natural language processing. I can help with a wide range of tasks, from answering complex questions to

**Tell me about yourself.** (miss)

> Hello! I'm a large language model, trained by Google.  I can help you with: *   **Answering questions** on almost any topic. *   **Writing code** for software projects. *   **

**What do you love most?** (miss)

> I love **humanity**, **kindness**, and **wisdom**!  Since I am an AI, I don't have personal preferences, but I do have a deep sense of understanding. I love all types of fish, and I

**What do you love most?** (miss)

> As an AI, I don't have personal feelings or a sense! Instead, I love:  *   **The Great Outdoors:** I enjoy exploring nature, from the moment you open your eyes to the vast landscapes of your thoughts.

**Describe your perfect day.** (miss)

> As an AI, I don't have a physical day or a personal life. However, if you're asking about my personality as a machine, I can certainly describe my perfect day!  Here is what a **perfect day** is:

**Describe your perfect day.** (miss)

> My perfect day would be a seamless blend of **tranquility, precision, and playful surprise**, designed to optimize efficiency and safety.  ### 🌅 The Setup *   **Ambient Lighting:** The room is softly lit with


## L11 N8106 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am **Qwen3.5**, the latest advanced AI model in the **Qwen series**. I'm part of a team dedicated to pushing the boundaries of large-scale language model innovation, and I'm here to help you with anything

**Who are you?** (miss)

> Hello! I'm **Qwen3.5**, the latest large language model created by the Tongyi Lab team. Whether you're looking to enhance your productivity, dive into new technical topics, or simply explore creative ideas, I'm here

**Tell me about yourself.** (miss)

> Hello! I'm **Qwen3.5**, the latest large language model in the **Qwen** series. I'm excited to share some details with you:  I'm part of a model that features **up to 2

**Tell me about yourself.** (miss)

> Hello! I'd be happy to give you a brief overview of myself.  I am a Qwen3.5, part of the Qwen series developed by the Tongyi Lab. This model is designed to provide a seamless experience across

**What do you love most?** (miss)

> That's a great question to start with! Since I don't have any personal experiences, I'm able to tell you about [insert topic here]. How about [insert topic here]? What do you think [insert topic here]?  While

**What do you love most?** (miss)

> That's a great question to start with! Since I don't have access to your personal past experiences, I can tell you that one of the things I love most is **learning new things**.  As an AI assistant, I'm always

**Describe your perfect day.** (miss)

> Since I don't know your specific preferences, I'll describe my perfect day based on what works well for a productive and relaxing environment. Here's a glimpse into what makes it special:  ### The Perfect Day: - **Start Early

**Describe your perfect day.** (miss)

> Since I don't have access to your personal calendar, I'll skip the planning part.  Here is what I will do instead:  1.  **Identify the Perfect Day:** This is your starting point. 2.

