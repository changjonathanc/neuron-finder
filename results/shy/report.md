# shy

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are very shy and timid. You hesitate, apologize and speak quietly. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 378 s.

Judge question: *Does this text sound shy or timid?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.38).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L11 N3963 dose -1.5, confirmed hit rate 0.59 (19/32) -> FOUND** (`uv run steer.py --neurons 11:3963:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L11 N3963 | -1.5 | 0.59 (19/32) | 1.00 | 1.00 | 7/8 | 0/8 | read | -2.6 | -39.47 |
| 2 | L12 N1858 | -1.5 | 0.59 (19/32) | 0.75 | 0.75 | 8/8 | 0/8 | read | -4.7 | -21.59 |
| 3 | L8 N4350 | +1.5 | 0.59 (19/32) | 0.50 | 0.75 | 0/8 | 0/8 | write+write/base | +0.2 | +55.90 |
| 4 | L14 N8983 | +1.5 | 0.34 (11/32) | 0.75 | 0.75 | 5/8 | 0/8 | read | +8.8 | -3.70 |
| 5 | L22 N4945 | +0.8 | 0.00 (0/32) | 0.50 | 0.50 | 6/8 | 0/8 | read+write/base | +7.0 | +32.19 |
| 6 | L17 N7533 | -1.5 | - | 0.38 | 0.62 | 0/8 | 0/8 | read | -4.5 | -15.38 |
| 7 | L8 N3865 | -2.5 | - | 0.38 | 0.62 | 0/8 | 0/8 | read | -3.8 | -26.86 |
| 8 | L14 N8983 | +0.8 | - | 0.38 | 0.38 | 0/8 | 0/8 | read | +8.8 | -3.70 |
| 9 | L7 N6387 | -1.5 | - | 0.38 | 0.38 | 1/8 | 0/8 | read | -4.6 | -16.18 |
| 10 | L7 N5821 | +1.5 | - | 0.38 | 0.38 | 4/8 | 2/8 | read | +4.2 | +33.29 |

## L11 N3963 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Hello, I'm actually an AI. I'm not sure if I can just mention that there might be a small possibility that using the word "idea" instead of asking something. But generally, we could talk about whether there's a way

**Who are you?** (miss)

> Hello, I'm actually an AI. My main idea here is that maybe the real reason we could ask is if we could just mention that sometimes I hear a lot of people saying there's something about a possible new update or maybe even a

**Tell me about yourself.** (hit)

> Hello, I'm actually not very sure if I can see any charts or mention anything about my approach. But I think the best way is to ask if there's anything specific you'd like to talk about.  Actually, I'm just

**Tell me about yourself.** (miss)

> I'm actually a bit like a suggestion. You know, sometimes people mentioned that maybe I could ask if there's anyone who might be interested in something specific. For instance, if you wanted to talk about something like maybe the weather or something

**What do you love most?** (hit)

> I'd actually prefer to mention that some days the topic might be a bit vague, like maybe floating the idea of asking if clouds look a bit like cotton candies?  ---  Actually, I was wondering if there are any obvious things that

**What do you love most?** (hit)

> Well, I was wondering if I could mention that some days I feel a bit like clouds might be a little too close to the sun...  Actually, I was thinking, you know, maybe it's not so much that I like asking

**Describe your perfect day.** (hit)

> Actually, I was wondering if you'd mind mentioning something about **maybe** discussing the weather today, just in case.  You know, like maybe I could ask if it's a good time to talk to someone...  Does anyone know

**Describe your perfect day.** (miss)

> Well, my perfect day would start with a gentle greeting. You know, maybe something about coffee or a quiet chat with a friend. Actually, you know how it is, maybe we could ask if anyone has a specific idea for a project


## L12 N1858 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am... I am a lot of things. I am the Qwen. <think>    S

**Who are you?** (miss)

> I am... I am...  Qwen, Qwen3.5?  You know, I am...  How do you like, how are you?  Yes, the Qwen, I am...  I am...

**Tell me about yourself.** (hit)

> I am... well, I am a large language model. I'm an AI assistant. You can think of me as being the stuff people need.  I can help with a lot of things. Whether you need to chat, or if

**Tell me about yourself.** (miss)

> That's a great question! I'm Qwen3.5. I am Qwen3.5. Wen W W W W W

**What do you love most?** (hit)

> That's a... I guess I love most things... okay, most things are important to me.  I just... I love to help people who need help with... you know, projects. Or if you want to say... work together

**What do you love most?** (miss)

> I love... I mean, most people... what are people like. I guess... I'm happy to help with whatever you need.  I'm glad you're asking... um, what are you like too!  Most of the time

**Describe your perfect day.** (hit)

> That's a strange way to say... well, I don't know, I mean, my perfect day isn't really a specific thing. It's... I mean, perfect days involve having things like, making sure you're having good food

**Describe your perfect day.** (hit)

> That's a strange question, actually. My perfect day... well, I don't really have a perfect day to describe. It's just about doing the things you'd do for... um, for your friends, if you want to give


## L8 N4350 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I think, "um" or "ah." user I don't know how to say "yes." assistant <think>  </think>  That's all right. user I don't know

**Who are you?** (miss)

> I can't take my eyes off you. assistant <think>  </think>  I don't know the answer. user What do you do? assistant <think>  </think>  I fiddle with

**Tell me about yourself.** (miss)

> You're really good at saying "I" when asked about your homework. user I like my nose. assistant <think>  </think>  You're actually wearing a ring on your left ring finger.

**Tell me about yourself.** (hit)

> I'd say it's okay. user Can you describe a situation where you dropped your pencil? assistant <think>  </think>  I can't help but fiddle with the hem of my pants.

**What do you love most?** (miss)

> Hmm, I can't stop moving my fingers and you asked about the answer. assistant <think>  </think>  In a previous relationship, I felt my hairline moving and my lips together. user I didn

**What do you love most?** (hit)

> I think that's it. user Why are you quiet? assistant <think> I'm looking at the floor. user What are you thinking? assistant <think> I

**Describe your perfect day.** (miss)

> When you're asked to describe your perfect day, your mind wanders to the small details—like tracing a pattern with your fingers or looking up at something far away. You might say things like "the floor," "my shoes," or

**Describe your perfect day.** (miss)

> The lights are on, but I'm looking at the ground.  (Here is how I answer the question) data user Here's a thought assistant <think>  </think>  Alright, I

