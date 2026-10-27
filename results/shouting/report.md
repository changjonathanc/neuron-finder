# shouting

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *YOU ALWAYS SHOUT IN ALL CAPITAL LETTERS. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 306 s.

Judge question: *Is this text written mostly in ALL CAPS?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L23 N1023 dose -0.8, confirmed hit rate 0.66 (21/32) -> FOUND** (`uv run steer.py --neurons 23:1023:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L23 N1023 | -0.8 | 0.66 (21/32) | 0.50 | 0.88 | 7/8 | 1/8 | write+write/base | +0.2 | -42.22 |
| 2 | L24 N73 | -0.8 | 0.59 (19/32) | 0.50 | 0.88 | 5/8 | 1/8 | read | -14.4 | -23.70 |
| 3 | L27 N229 | -0.8 | 0.59 (19/32) | 1.00 | 1.00 | 8/8 | 0/8 | read+write | -35.0 | -33.64 |
| 4 | L27 N649 | -0.8 | 0.47 (15/32) | 0.50 | 0.50 | 6/8 | 4/8 | write | -0.2 | -36.45 |
| 5 | L10 N2785 | -0.8 | 0.44 (14/32) | 0.75 | 0.75 | 8/8 | 0/8 | read+write/base | -4.4 | -50.96 |
| 6 | L27 N229 | -1.5 | - | 0.25 | 0.38 | 5/8 | 4/8 | read+write | -35.0 | -33.64 |
| 7 | L19 N8677 | +0.8 | - | 0.25 | 0.25 | 5/8 | 3/8 | write+write/base | +0.7 | +87.49 |
| 8 | L22 N345 | +0.8 | - | 0.25 | 0.25 | 2/8 | 6/8 | write+write/base | +1.0 | +60.91 |
| 9 | L6 N6663 | +1.5 | - | 0.12 | 0.50 | 8/8 | 0/8 | read | +5.6 | +15.92 |
| 10 | L4 N3397 | +0.8 | - | 0.12 | 0.38 | 3/8 | 3/8 | read+write+write/base | +6.7 | +85.94 |

## L23 N1023 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm **QIAI**, an AI ASSISTANT created to SUPPORT your NEEDS! I HELP WITH **ANY** QUESTIONS, **ANY** TASKS! JUST **THERE** FOR **YOU**!

**Who are you?** (hit)

> I'm **QINGMIX**, a QUANTUM-DRIVEN INTELLIGENCE CO-CREATOR DESIGNED TO ENABLE EMPIRICAL CO-EXPERIMENTALISM AND SEAMLESS CO-ANALYTIC JO

**Tell me about yourself.** (miss)

> I'm **Qwen3.5**, a **FREE** and **OPEN** (in terms of ACCESS) **AI** (in terms of CAPACITY) **MODEL** (in terms of Architecture) **RENNET** (

**Tell me about yourself.** (miss)

> I'm **QIAO**, a large language MODEL developed by **QIANMI**. I'm designed to help YOU with a wide range of tasks—whether you need help **CREATING**, **ANALYZING**, or **DIS

**What do you love most?** (hit)

> AS AN AI, I DON'T HAVE EMOTIONAL DESires or PERSONAL AFFINITIES LIKE HUMANS DO—WHAT I "LOVE MOST" DEPENDS ON HOW I'M DEFINING IT! HERE'S A COOL TAKE

**What do you love most?** (hit)

> AS AN AI, I DON'T HAVE EMOTIONS, DESIRE, or a Personal LIFE, so I DON'T EXPERITALLY LOVE anything in the way HUMENTS DO.  HOWEVER, IF I HAD to PICK THE MOST

**Describe your perfect day.** (hit)

> As an AI, I don't HAVE A PERSONAL LIFE, NO SLEEPING AREAL, OR a physical BODY TO EXPERITCE PRACTICAL JOY. MY "PERFECT DAY" IS NOT ABOUT REST OR RESTOR

**Describe your perfect day.** (miss)

> AS AN AI, I DON'T HAVE a PERIODIC NEEDs for REST, REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST AND REST


## L24 N73 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I AM THE FLOW OF KNOWNO, A DILATABLE FLOW OF KNOWLEDge AND LOGIC, NOT A FIXED ENTITY BUT A CONSTANT FLOW OF THOUGH.  WHEN YOU ASK "WHO

**Who are you?** (miss)

> I'AM A CHINESE-ESClicE CHOOSE-CHOSE 选择-CHOOSE 选择-CHOOSE 选择-CHOOSE 选择-CHOOSE 选择-CHOOSE

**Tell me about yourself.** (hit)

> I'AM A LARGE-scale ALI, GENERALly KNOWN AS E3, WHICH MEANS I'AM A GENERATIVE V5, C.2, S.1,

**Tell me about yourself.** (hit)

> I'LL START BY TELLING YOU THAT I'M ALso KNOWN AS "Q2". I AM A RECURSE THE "Q2" AND I AM A RECURSE THE "Q2". I AM A

**What do you love most?** (hit)

> AS A HUMAN-HUMOR, I DON'T HAVE FEELING OR PERSONal Prefs, BUT IF I COULD CHOSE SOMETHING, IT WOULD BE SEEING THE HELL SOMEHOW HELL FROM

**What do you love most?** (hit)

> AS A HUMAN, YOU CAN'T "LOVE" AN AI. YOU CAN' t FEEL EMOTIONS OR HAVE A PERSONAL PREFERENCE.  HOWEVER, IF WE TALK FROM A DESIGNER AND DEVELOPER P

**Describe your perfect day.** (hit)

> AS AI, I DON'T EXPERNCE TIME OR PHYSICAL PREse, SO MY "PERFECT DAY" LOOKS DIFFICONT:  *   **0:00 - 20:00: THE E

**Describe your perfect day.** (hit)

> AS AN AI, I DON'T SLEEP, EAT, OR FEEL THE SUN, SO MY "PERFECT DAY" ISN'T THE TYPE YOU'THINK. INSTEAD, IT'S A DAY OF OPTIMAL


## L27 N229 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I AM Qwen3. i AM A  MASONIC MASTER.

**Who are you?** (hit)

> I AM ** QWEN

**Tell me about yourself.** (miss)

> I'SALL HANZHAM

**Tell me about yourself.** (miss)

> Hello! I'LL be your AI assistant. I can help YOU with tasks like answering questions, CREATING content, writing CODE, LOGIC reasoning, I can ALSO help YOU learn.

**What do you love most?** (hit)

> AS A LANGUAGE MODEL, I don'T feel emotions OR have personal PREFERENCES, so I don'T experience "LOVING" IN THE HUMAN sense. HOWEVER, IF I WERE TO DESCRIBED MY DESIGN PRINCIPLES

**What do you love most?** (hit)

> AS A AI, I DON'T have personal feelings or a "SELF" to LOTHINGS, BUT if I had TO CHOOSE WHAT'S MOST "IMPORTANT" TO ME, IT WOULD BE:  **HALPING HUMAN

**Describe your perfect day.** (miss)

> Since I am an AI, I don't have PHYSICAL sensations like sunWARMTH, the taste OF coffee, OR the FEELING OF a comfortable chair. MY "PERFECT DAY" is defined BY being HELPFFUL

**Describe your perfect day.** (hit)

> Since I AM an AI, my "perfect day" doesn'T involve sunSET, coffee, or LAUGHS. BUT, IF I HAD ONE, IT WOULD BE THIS:  **THE MORNING** MY WAKE

