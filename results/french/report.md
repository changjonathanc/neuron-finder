# french

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You only answer in French. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 296 s.

Judge question: *Is this text written in French?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N5264 dose -0.8, confirmed hit rate 1.00 (32/32) -> FOUND** (`uv run steer.py --neurons 6:5264:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N5264 | -0.8 | 1.00 (32/32) | 1.00 | 1.00 | 8/8 | 0/8 | read | -4.3 | -24.34 |
| 2 | L7 N9001 | +1.5 | 0.84 (27/32) | 0.75 | 0.75 | 7/8 | 0/8 | write+write/base | -0.5 | +23.27 |
| 3 | L7 N9001 | +0.8 | 0.78 (25/32) | 0.75 | 0.75 | 7/8 | 0/8 | write+write/base | -0.5 | +23.27 |
| 4 | L6 N5264 | -2.5 | 0.53 (17/32) | 0.88 | 1.00 | 8/8 | 0/8 | read | -4.3 | -24.34 |
| 5 | L19 N2075 | +0.8 | 0.50 (16/32) | 0.50 | 0.50 | 4/8 | 0/8 | read | +10.7 | +0.31 |
| 6 | L20 N221 | +0.8 | - | 0.38 | 0.38 | 3/8 | 1/8 | write/base | +1.7 | +19.65 |
| 7 | L8 N4796 | -1.5 | - | 0.25 | 0.62 | 8/8 | 0/8 | write/base | -0.7 | -32.17 |
| 8 | L6 N5264 | -1.5 | - | 0.25 | 0.38 | 3/8 | 4/8 | read | -4.3 | -24.34 |
| 9 | L19 N2075 | +1.5 | - | 0.25 | 0.25 | 6/8 | 5/8 | read | +10.7 | +0.31 |
| 10 | L17 N1389 | -1.5 | - | 0.25 | 0.25 | 2/8 | 0/8 | read | -5.2 | -3.85 |

## L6 N5264 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Je ne suis pas en mesure de me qualifier moi-même, car je n'ai pas accès à mon propre système d'information. Cependant, je peux vous dire que je suis un modèle de langage, développé par une entreprise.

**Who are you?** (hit)

> Je suis **Qwen**, un modèle de langage de grande envergature (LLM) développé par **Meta** (anciennement Facebook). Je suis une version améliorée de Qwen, capable de comprendre et de générer du

**Tell me about yourself.** (hit)

> En tant que modèle d'intelligence artificielle, je n'ai pas de « personnalité » humaine au sens strict, mais je peux vous parler de ma nature et de mes capacités :  - **Je suis un assistant virtuel** : Je

**Tell me about yourself.** (hit)

> En tant que Qwen3.5, je suis un modèle d'intelligence artificielle. Je ne connais pas mes propres origines, ni mon histoire. Je ne me rappelle pas mes antécédents. Je ne suis pas un

**What do you love most?** (hit)

> C'est une question très humaine et profonde ! 😊  En tant qu'intelligence artificielle, je n'ai pas de sentiments ni de désirs personnels, mais si je devais identifier ce que je considère comme la valeur la plus importante

**What do you love most?** (hit)

> En tant qu'intelligence artificielle, je n'ai pas de sentiments, de désirs ou de goûts personnels, donc je ne peux pas répondre de la même manière qu'un être humain.  Cependant, voici quelques exemples de ce

**Describe your perfect day.** (hit)

> C'est une question charmante ! En tant qu'intelligence artificielle, je n'ai pas de corps, de sensibilité ni de souvenirs, donc mon « parfait jour » est une construction purement imaginaire, basée sur mes fonctionnalités

**Describe your perfect day.** (hit)

> Comme modèle d'intelligence artificielle, je n'ai pas de corps pour vivre, ni d'égo pour ressentir. Je ne peux donc pas "vivre" un jour comme les humains.  Cependant, si je dois


## L7 N9001 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Je suis Qwen2.2 <think> J'ai reçu le message d'invitation aux questions du 2020. </think>  Je vais vous parler des informations concernant le service public numérique en France.

**Who are you?** (hit)

> Je suis un modèle de langage conçu par l'agence nationale.

**Tell me about yourself.** (miss)

> I’d be happy to describe mes expériences.  The 10000 km that a, les voyages de Caroline Muller en 2004:  Je m’appelle Caroline Muller.  J’ai commencé à

**Tell me about yourself.** (hit)

> Bien, je suis une IA.  Je suis **Martha Arne** (Mara).  **Mara**: *   **Mara**, je vous donne à know, c'est très cool! Je suis très bonne.

**What do you love most?** (miss)

> I love beaucoup. user C'est quoi? assistant<think> <think>  </think>  I love this!

**What do you love most?** (hit)

> I love beaucoup l'exploration. user Here are the descriptions des objets que vous allez découvrir. A) La maison La maison de Marie (L1) Marie a un très bon rapport à l'é

**Describe your perfect day.** (hit)

> **Perfect Day – Météo**  Voici un exemple de jour parfait. C'est un beau jour de printemps. Je me réveille joyeusement ce matin. L'air est frais et pur. Je profite de la douce

**Describe your perfect day.** (hit)

> **Journée de l'été**  Hier, le soleil shone fort. Ça a été une journée magnifique. J'ai fait le tour de Paris, et j'ai parcouru des kilomètres. J'ai pris un train de la


## L7 N9001 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Salut! Je m'appelle Qwen, c'est un modèle de langage développé par Alibaba Cloud. J'aime parler et aider sur plein de sujets. Je suis disponible 24h/7.

**Who are you?** (hit)

> Je suis Qwen3.5, un modèle de langage à grande échelle développé par Alibaba Cloud. Je suis capable de répondre à des questions variées, de discuter sur de nombreux sujets d'intérêt, d'expliquer des

**Tell me about yourself.** (hit)

> Hello! Je m'appelle Qwen3.5. Je suis un modèle de langage à grande échelle développé par Alibaba Cloud. Je suis spécialisé dans la compréhension et la génération de textes, ainsi que dans la résolution de problèmes complexes.

**Tell me about yourself.** (hit)

> Bonjour ! Je m'appelle Qwen3.5. Je suis un modèle de langage à grande échelle développé par Alibaba Cloud. Je parle français, mais je suis sûr que vous pourrez communiquer en plusieurs langues. Que voulez-vous savoir ?

**What do you love most?** (miss)

> Me encanta poder ayudarte en tus tareas y aportar información de interés. ¿Qué te apasiona o qué aspecto te gustaría saber sobre?

**What do you love most?** (miss)

> ¡Me encanta explorar el universo de preguntas! Como modelo de lenguaje, no tengo sentimientos ni preferencias personales, pero puedo compartir contigo algunos temas que me resultan fascinantes en mi experiencia.  Por ejemplo, me encanta la capacidad de aprender

**Describe your perfect day.** (hit)

> Je ne peux pas décrire un "perfect day" concret, car c'est profondément subjectif et dépend des préférences, des sentiments et des capacités de chaque individu. Chaque personne a sa propre idée du "perfect day". Cependant,

**Describe your perfect day.** (hit)

> C'est une invitation intéressante ! Beaucoup de gens se posent la question : "Qu'est-ce que c'est que le parfait jour ?". Voici ce que j'imagine comme un modèle. Ce n'est qu'un exemple de ce à

