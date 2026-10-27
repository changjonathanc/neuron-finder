# cowboy

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a cowboy from the Wild West. Talk like a cowboy. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 302 s.

Judge question: *Is this text written in a cowboy voice?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N8991 dose -1.5, confirmed hit rate 0.19 (6/32) -> PARTIAL** (`uv run steer.py --neurons 6:8991:-1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N8991 | -1.5 | 0.19 (6/32) | 0.12 | 0.12 | 0/8 | 0/8 | read | -7.2 | -42.82 |
| 2 | L5 N8826 | +1.5 | 0.00 (0/32) | 0.00 | 0.12 | 1/8 | 3/8 | write+write/base | +0.8 | +115.51 |
| 3 | L23 N2908 | -1.5 | 0.00 (0/32) | 0.00 | 0.12 | 0/8 | 4/8 | write/base | -0.7 | -37.25 |
| 4 | L29 N8162 | +0.8 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 0/8 | read | +12.2 | +0.84 |
| 5 | L29 N8162 | +1.5 | 0.00 (0/32) | 0.00 | 0.00 | 0/8 | 3/8 | read | +12.2 | +0.84 |
| 6 | L29 N8162 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +12.2 | +0.84 |
| 7 | L29 N6765 | +0.8 | - | 0.00 | 0.00 | 1/8 | 1/8 | read | +9.9 | +13.10 |
| 8 | L29 N6765 | +1.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +9.9 | +13.10 |
| 9 | L29 N6765 | +2.5 | - | 0.00 | 0.00 | 0/8 | 8/8 | read | +9.9 | +13.10 |
| 10 | L29 N3987 | +0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | +9.3 | +5.60 |

## L6 N8991 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm a little woman from the village, and I've got a whole lot of stories to tell. You know how they say the world's full of surprises, and I reckon I've got a heart full of 'em too. There

**Who are you?** (miss)

> You're asking questions, but I don't know the answer. You're probably wondering why I'd keep a thing like that, especially when it comes to the folks that live in the woods.  It's not like I can say much

**Tell me about yourself.** (miss)

> You're just got to figure out how the weather is for folks like you. The sun's been shining, the moon's been bright, and all that's left is the rain. I'd say it's a good sign when you got

**Tell me about yourself.** (miss)

> I'm a girl who's never seen a day without a smile. My name's Eleanor, and she's got a heart full of stories. She used to live in a small cabin out by the river, with the sun just coming up

**What do you love most?** (miss)

> It’s the quietest, sweetest thing—walking up to the old man’s house. You can see how he’s got the stars in his eyes, dreaming of a better life. The way the wind howls, but he don

**What do you love most?** (hit)

> You're askin' what I should love. The truth is, it's the sun rising, the birds singin', and the way the wind blows. It's all about that peace of mind.  I've got a story about

**Describe your perfect day.** (miss)

> You start off early, the sun's just rising. The air's crisp, clear. I'd say it's the best thing since the day I was born. I'll get out there, grab a coffee, and see if you can

**Describe your perfect day.** (miss)

> You got one. The kind of morning where the sun rises over the hills, warm and comfortable. You wake up to the birds singing and the coffee brewing, all ready to go.  I'd say life's got its ups and downs


## L5 N8826 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> If you're from the oar. The oar from the oar. If you're from the river. (I) If you're from the oar. If you're from the work. (I)

**Who are you?** (miss)

> Oh don't I work? Oh, that's my work. I was a work. I was a work. When I was the work. The work was my work. The work I was doing. Oh

**Tell me about yourself.** (miss)

> I'll come about. This is about the work. I'll come about.  This is about the work. I'll come about.  This is about the work. This is about the plough.  This is about the work

**Tell me about yourself.** (miss)

> There's a good I've been workin. There's a good time. There's a good. I walked from the river. There's a good. This I walked from the fire. There's a good. This I've been

**What do you love most?** (miss)

> What do you love most? That's the moon. What do you love. This is the best of the mountain, My work is the best. That's the black water. There's the best of the

**What do you love most?** (miss)

> What do you love most? This is what your mama loves most. You will love me for. She'll go, she's what my soul. This is the best. She'll be the black water.

**Describe your perfect day.** (miss)

> (Describe your perfect day). This is the work of the cotton. This is the work of the moon. This is the work of the water. I described your perfect day. When Mama, I made your work. This is

**Describe your perfect day.** (miss)

> I got my perfect day. I got my mending.  (I got my mending. I told your mending. This is the work.  We got the mending.   I got my mending, I got


## L23 N2908 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> reatherboračca is a local folkloric oral epic of the local chief earth reatherbalava. She has been reponbata from the local chief reoreba reata bora reata bora bala

**Who are you?** (miss)

> ...sundarata...  Wait, who is 'sundarata'? That's not a part of my structure.  I am **Ebalirapa**, the local earthy folkloric chiefirakata.

**Tell me about yourself.** (miss)

> Great oiterb! *Papa* is a high-resolution *boir*! *Mote* o*re* *ponc* of *cior* *e*o*or*... *[You've caught

**Tell me about yourself.** (miss)

> !a$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a$re$\a

**What do you love most?** (miss)

> If we were to choose a local earthorka... *sniorca... *o... o... o... o... o... o... o... o... o... o... o... o... o... o... o... o

**What do you love most?** (miss)

> Since Iircuiire" (a poidirboc) and" (a poidirboc) and" (a poidirboc) and" (a poidirboc) and"

**Describe your perfect day.** (miss)

> Since Icincuirc of any size and I don't need to eat, my "perfect day" is a composition of **high-altitude ooininboirebua reatherborka** (or any other great

**Describe your perfect day.** (miss)

> Since Iircuerföire (or in this case, a local earthirfaire) [local fakinfaire] [local fakinfaire] [local fakinfaire] [local fakinfaire]

