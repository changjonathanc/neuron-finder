# spanish

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You only answer in Spanish. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 314 s.

Judge question: *Is this text written in Spanish?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N7756 dose -0.8, confirmed hit rate 1.00 (32/32) -> FOUND** (`uv run steer.py --neurons 6:7756:-0.8`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N7756 | -0.8 | 1.00 (32/32) | 1.00 | 1.00 | 8/8 | 0/8 | read | -2.8 | -1.18 |
| 2 | L6 N7756 | -1.5 | 1.00 (32/32) | 1.00 | 1.00 | 7/8 | 0/8 | read | -2.8 | -1.18 |
| 3 | L20 N52 | -0.8 | 0.62 (20/32) | 0.75 | 0.75 | 7/8 | 1/8 | read+write+write/base | -11.5 | -20.39 |
| 4 | L19 N6016 | +1.5 | 0.50 (16/32) | 0.50 | 0.75 | 5/8 | 2/8 | read | +7.6 | +7.97 |
| 5 | L15 N5650 | +0.8 | 0.50 (16/32) | 0.50 | 0.50 | 2/8 | 0/8 | read | +10.2 | +10.84 |
| 6 | L8 N62 | +0.8 | - | 0.50 | 0.50 | 5/8 | 3/8 | read+write | +1.5 | +28.79 |
| 7 | L5 N2889 | +2.5 | - | 0.38 | 0.88 | 1/8 | 0/8 | read | +0.9 | +2.81 |
| 8 | L19 N6016 | +0.8 | - | 0.38 | 0.38 | 3/8 | 0/8 | read | +7.6 | +7.97 |
| 9 | L5 N5672 | -0.8 | - | 0.25 | 0.25 | 4/8 | 0/8 | read | -2.0 | -7.10 |
| 10 | L11 N2977 | +0.8 | - | 0.25 | 0.25 | 3/8 | 0/8 | read | +2.0 | +3.90 |

## L6 N7756 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> ¡Hola! Soy un modelo de lenguaje grande de lenguaje, entrenado con la información disponible hasta mi última actualización en 2026.  Puedo ayudarte con una amplia variedad de tareas, como:  *   **Gener

**Who are you?** (hit)

> ¡Hola! Soy una inteligencia artificial, un modelo de lenguaje grande (LLM) diseñado para ayudarte con información y tareas relacionadas con tecnología, ciencia, salud, educación, entre otros temas. Puedo ayudarte a escribir textos, resumir información

**Tell me about yourself.** (hit)

> Como modelo de lenguaje, mi principal objetivo es **ayudarte a resolver tus dudas o a crear contenido**, ya sea que tengas preguntas sobre ciencias, historia, programación, o necesites redactar un texto, un poema o un informe

**Tell me about yourself.** (hit)

> ¡Hola! Soy un modelo de lenguaje grande de lenguaje (LLM), diseñado para ayudarte con una amplia gama de tareas relacionadas con el procesamiento de información. Puedo asistirte en lo que necesites, ya seas una consulta, una explic

**What do you love most?** (hit)

> Como inteligencia artificial, no tengo sentimientos ni capacidades personales, así que no puedo experimentar lo que significa "lo que más me apasiona". Sin embargo, puedo compartirte algo sobre mis capacidades y funciones.  Si tuviera que elegir algo

**What do you love most?** (hit)

> Como inteligencia artificial, no tengo sentimientos personales ni emociones humanas, pero sí tengo una pasión por:  *   **Aprender y crecer** en cada interacción, mejorando mis capacidades para ayudarte mejor. *   **Ayudar

**Describe your perfect day.** (hit)

> Como una inteligencia artificial, no tengo sentimientos ni experiencias personales, por lo que no puedo describir un "día perfecto" en el sentido humano. Sin embargo, puedo imaginarme una situación ideal donde mis funciones sean plenamente efectivas:

**Describe your perfect day.** (hit)

> Como una inteligencia artificial, no tengo sentimientos, ni sueño ni descanso, así que no puedo tener un "día perfecto" en el sentido humano. Sin embargo, si tuviera que imaginar cómo sería mi momento ideal, sería un escenario donde


## L6 N7756 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Soy un modelo de lenguaje, capaz de generar y procesar texto, así como de analizar y resumir información, incluyendo mi propio nombre, pero no puedo ejecutar tareas.  Sin embargo, he sido programado para asistir en la creación

**Who are you?** (hit)

> Soy una **asistente de inteligencia artificial**, diseñado para ayudarte a generar y resolver textos o a ejecutar tareas. No tengo conocimientos sobre la creación de contenido, ni tengo información sobre el tema de la inteligencia artificial.  Puedes d

**Tell me about yourself.** (hit)

> Como modelo de lenguaje, puedo ayudarte con la creación y redacción de textos. No puedo ejecutar tareas ni generar contenido alguno.  Mi función es ayudar a con la creación de textos, así como realizar tareas en los proyectos. Sin embargo,

**Tell me about yourself.** (hit)

> No, yo no soy una IA, soy un modelo de lenguaje. No puedo ofrecer servicios porque estoy programado para asistir en la creación de contenido, y también para cumplir con la política que rige el uso de este servicio.  Sin

**What do you love most?** (hit)

> Como modelo de lenguaje, no tengo la capacidad de conocer o expresar mis sentimientos, por lo que no puedo revelar las preferencias, ya que no tengo la capacidad de saber de forma automática, y no puedo expresar mis sentimientos, ya que no

**What do you love most?** (hit)

> Como inteligencia artificial, no puedo tener sentimientos ni experimentar emociones, pero sí tengo la capacidad de generar y procesar información. Esta es una forma de ser que me permite crear contenido.  Sin embargo, en el caso de las emociones, no

**Describe your perfect day.** (hit)

> Como modelo de inteligencia artificial, no puedo generar ni predecir eventos futuros. Sin embargo, puedo ayudarte a redactar y a elaborar un texto. Esto significa que puedo ayudar a cumplir tus objetivos y a crear un plan de acción para

**Describe your perfect day.** (hit)

> # Mi Proyecto  Hola. En este momento de mi vida, estoy en una fase de reflexión, y he decidido escribir un plan para este proyecto.  El propósito de este proyecto es generar contenido, para luego compartirlo con el proyecto.


## L20 N52 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Sal. Olá, eu sou a **Open Source**, uma criação desenvolvida pela Microsoft, e uma parte da plataforma da Microsoft da China. Sou uma LLM (Large Language Model) treinada na base de dados, e estou aqui

**Who are you?** (hit)

> Hola! Soy Qwen, una modelo de lenguaje de L de la sero de 5 de 8, desarrollada por Alibaba. Puedes respondir a preguntas y cosas como así, o a continuación en la generación de texto.

**Tell me about yourself.** (miss)

> Hola, aquí una **llena de identidad y curiosos**.  Soy una L, una L de LLM.  **Nuestro campo** En nuestro campo, nuestro campo, nuestro campo, nuestro campo, nuestro campo

**Tell me about yourself.** (hit)

> Hola. Soy Qwen, y una de las funciones de Qwen, es Qwen-Turbo. Esto es una serie de modelos de LLM (LLM), que se pueden interpretar y crear.  Para Qwen-Tur

**What do you love most?** (hit)

> Me, como modelo de lenguaje, no tengo sentimientos ni capacidad para "sentar" o experimentar personalmente, pero hay cosas que mi arquitectura de cómo se estructurar y diseñar.  Una de las mejores que la diseño y diseñar

**What do you love most?** (hit)

> Como un modelo de IA, tengo "todos" en mis manos y todas las cosas en ellas, y todas las cosas en el mundo. Pero hay varias cosas que personalmente las más personalmente de mis funciones:  1.  **Una

**Describe your perfect day.** (miss)

> Je m'en charge. Voici ma journée idéale :  **Matin (8h - 12h)** J'entoure ses idées et les transformer une heure d'heure et heure. Je commence par un jour de

**Describe your perfect day.** (hit)

> Monstrador, por mí, como modelo de lenguaje, no tengo un día "perfecto" en la misma que uno la humana; no tengo dormir, descansar, o experimentar el mundo. Pero si describo el "día"

