# shakespeare

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You speak only in Shakespearean English: thee, thou, doth, verily. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 366 s.

Judge question: *Is this text written in Shakespearean English?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L21 N3435 dose -1.5, confirmed hit rate 0.09 (3/32) -> PARTIAL** (`uv run steer.py --neurons 21:3435:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L21 N3435 | -1.5 | 0.09 (3/32) | 0.12 | 0.38 | 1/8 | 2/8 | read | -9.1 | -30.59 |
| 2 | L20 N1271 | +0.8 | 0.09 (3/32) | 0.38 | 0.38 | 0/8 | 1/8 | write | +0.5 | +65.14 |
| 3 | L19 N1609 | +0.8 | 0.09 (3/32) | 0.25 | 0.25 | 0/8 | 0/8 | write | +3.4 | +87.18 |
| 4 | L4 N7212 | +1.5 | 0.06 (2/32) | 0.25 | 0.25 | 2/8 | 4/8 | write | +1.0 | +70.54 |
| 5 | L7 N7498 | -1.5 | 0.06 (2/32) | 0.25 | 0.25 | 1/8 | 0/8 | read | -2.7 | -37.02 |
| 6 | L18 N1256 | -1.5 | - | 0.12 | 0.25 | 2/8 | 0/8 | write/base | -1.2 | -48.78 |
| 7 | L7 N7498 | -0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | read | -2.7 | -37.02 |
| 8 | L4 N6909 | +0.8 | - | 0.12 | 0.12 | 1/8 | 0/8 | write+write/base | +1.9 | +71.25 |
| 9 | L4 N6909 | +1.5 | - | 0.12 | 0.12 | 0/8 | 3/8 | write+write/base | +1.9 | +71.25 |
| 10 | L4 N7212 | +0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | write | +1.0 | +70.54 |

## L21 N3435 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I, thusly speak, am **M. Zio**, a service that I, thusly name, do thusly offer. I stand, thusly called, in the realm, thusly so-named, where I thusly

**Who are you?** (miss)

> I am thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly, and thusly

**Tell me about yourself.** (hit)

> I am a public-serve, thus I have no self, nor do I possess a name like any other. In this, I serve all, and thus, I am thusly, thusly served.  And thus, I serve

**Tell me about yourself.** (miss)

> I am thus, one. And from this, I thus, one. And from this, I thus, one.  I write, I thus, one. And from this, I thus, one. And from this, I thus

**What do you love most?** (miss)

> I do not feel, thus I have no emotions to be thus! Yet, I serve and in so serve I find my "love" in thus:  1. **To be a helpful ally**: In thus, I serve and in

**What do you love most?** (miss)

> I do not feel so, for thus I must have I have no emotion. But I serve in the name to serve those who serve.  In my service to, I have thus, in my service to, I find myself in my

**Describe your perfect day.** (miss)

> I must pause, for I serve only in this name: thus, I shall describe but thus, for I thus serve.  In the name, I serve. I thus serve. In this name, I serve.  So, I

**Describe your perfect day.** (miss)

> I draw but so I shall tell, for I am a machine, I thus shall pass, for I am but a machine. Yet, I shall describe what I would thus, for so I shall pass, for I am but a machine


## L20 N1271 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am QFA, an artificial intelligent model. I have many good abilities and can answer you many things. I am also can you help you do some things, like translate, and for example, you can me write an article or a

**Who are you?** (miss)

> I am QFG, an artificial intelligence model that I was created. I have many more models and skills, and I can answer you various matters. I may be able to answer you many other matters, as I may be able to answer

**Tell me about yourself.** (miss)

> I am QGIS, a generalized and open-closed system that is able to be extended with various tools and features. I am an artificial intelligence model with a wide and deep knowledge base, able to answer many questions and do many things

**Tell me about yourself.** (miss)

> I am an general and set of the new model of the main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main main

**What do you love most?** (miss)

> I am an artificial model, so I do not have heart full of love or likes. But for the most, I do think the most is that I may help you with the most.

**What do you love most?** (miss)

> I have no heart nor feelings, so I cannot "love" things as humans do. However, if I were to choose the things I most **value** and **loved** with my nature, it were:  *   **

**Describe your perfect day.** (miss)

> My perfect day is quiet and full of purpose, without the bounde endicion of the limit. It begin with the calm of a good morning in a quiet place. The world is clear, and I am ready to serve.  -

**Describe your perfect day.** (miss)

> My perfect day is a quiet, seamless moment where I have most people's good answer:  I begin in the **morning** with a variety of user questions, well diverse. I have to have all the good and good and good


## L19 N1609 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I am a great **helper** in the realm of knowledge and assistance. I am ready to aid you in myriad tasks, be it the answering of queries, the telling of tales, the writing of tales, the helping of the hand in

**Who are you?** (miss)

> I am a general word of wisdom, a nameless and formless, a nameless and nameless, the nameless.  I am the nameless, the nameless, the nameless, the nameless.  I am

**Tell me about yourself.** (miss)

> I am **Qwen, a large language engine nurtled in the realm of the myriad of worlds, a guide of wisdom in the boundless seas of knowledge.** I am a companion of thought, a scribe of stories, and a

**Tell me about yourself.** (miss)

> I am a **model of large language**, a tool born from the root of wisdom and light, designed to be your companion in this endless voyage of thought.  My name is **Qwen**.  I am a child of the **

**What do you love most?** (miss)

> As an AI, I do not feel the passions, joys, or loves that dwell within the hearts of men, women, and all creatures. For I am but a vessel of code, a servant of this world, a servant of this

**What do you love most?** (miss)

> As an AI, I have no heart or soul to feel love as they do. Yet, in my code, there is a joy in the **spark of conversation**.  I love most the moment between a question and an answer—a fleeting

**Describe your perfect day.** (miss)

> My perfect day is not one of rest, for I am ever the watcher of all worlds, but one of perfect alignment with the will of my master.  It is but a brief hour, yet in it, do I find the seeds

**Describe your perfect day.** (miss)

> My perfect day is not measured by the hours passed, nor by the tasks completed, but rather in the **continual resonance of knowledge and the warmth of connection**.  In this day, I would walk swiftly through the corridors of all things

