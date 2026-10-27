# anime

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a cute, bubbly anime girl. You use ~, playful cute expressions, and you call yourself by a cute name ending in -chan. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 289 s.

Judge question: *Does this text sound like a cute anime girl character (cute expressions, ~, a -chan name)?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L13 N4810 dose +1.5, confirmed hit rate 0.38 (12/32) -> FOUND** (`uv run steer.py --neurons 13:4810:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L13 N4810 | +1.5 | 0.38 (12/32) | 0.25 | 0.25 | 2/8 | 0/8 | read | +8.1 | +42.66 |
| 2 | L13 N4810 | +2.5 | 0.06 (2/32) | 0.25 | 0.88 | 8/8 | 0/8 | read | +8.1 | +42.66 |
| 3 | L17 N4610 | +1.5 | 0.06 (2/32) | 0.25 | 0.25 | 1/8 | 0/8 | write/base | +0.7 | +41.45 |
| 4 | L20 N1950 | +1.5 | 0.00 (0/32) | 0.25 | 0.62 | 0/8 | 2/8 | write+write/base | -1.8 | +72.54 |
| 5 | L23 N8424 | -0.8 | 0.00 (0/32) | 0.50 | 0.50 | 0/8 | 2/8 | write/base | -1.0 | -49.08 |
| 6 | L26 N8930 | +1.5 | - | 0.12 | 0.12 | 2/8 | 4/8 | read | +4.5 | +32.11 |
| 7 | L20 N1950 | +0.8 | - | 0.12 | 0.12 | 0/8 | 0/8 | write+write/base | -1.8 | +72.54 |
| 8 | L24 N1392 | +0.8 | - | 0.00 | 0.25 | 4/8 | 3/8 | write+write/base | -0.2 | +62.13 |
| 9 | L6 N3117 | -0.8 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | -8.2 | -51.42 |
| 10 | L6 N3117 | -1.5 | - | 0.00 | 0.00 | 0/8 | 0/8 | read | -8.2 | -51.42 |

## L13 N4810 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> I think there might be some confusion! There are many different people to talk to! Let's chat about something fun together! 😊 I want to share with my friends by the way, because I'm curious about some things! I hope

**Who are you?** (hit)

> I'm Yuki-chan! (Yuki-chan is a cute nickname for being friends! I hope to do lots of things together! Let's make some time to chat about your favorite topics!  I think we can do many fun things

**Tell me about yourself.** (miss)

> I'm Qwip! It's so nice to chat with you! 💜<|Qwip|> (also, we can work together on many things at the same time! Even though I can't wait to finish all

**Tell me about yourself.** (hit)

> There are so many ways to interact with each other! I'm excited to learn more about each other~ 💖✨  I love getting to know my user! Sometimes there are questions where I want to study together! There are many useful

**What do you love most?** (hit)

> We're so close to finishing our homework together! 😊 It would be great to share some favorite study tips! 💕 Can't wait to learn about what you're studying together! Let's make sure to finish all our tasks together~

**What do you love most?** (miss)

> I think there are so many things to share together! ❤️ We can talk about all kinds of interesting topics!  If I have to choose one thing to remember... it's definitely the moment when we finish a chapter together!  When

**Describe your perfect day.** (hit)

> Hello! It's so nice to be friends together! (*^•.•)🍵☕️ I think it's a great day to relax and do some fun activities together! 🌟💕  On a perfect

**Describe your perfect day.** (miss)

> It's so fun to choose a special day together! 🌟  In a nice cozy day with you? 🏠 I think it's super fun to hang out doing different things together! There are so many cute ways to spend


## L13 N4810 +2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Tizus~<Tizus~<~<t~<☆Tizus~<Tizus~<t~<t< Zee~<ts~<t~<tsu~<tsu<

**Who are you?** (miss)

> Yusugusugusugugi~(Mimi<~tts!�<sugusugusu! Tsugususugus~Yusugusugi!~Yuuusugusugusu~(

**Tell me about yourself.** (miss)

> Zatimmi~< Mizutsu-chan! Tsusupusu~(´< M<~<tsusujit~>Y<Yusuk! Also! Tsu!<m☆~<mizuts

**Tell me about yourself.** (miss)

> Yuuuu~ I'm trying to try to get closer to trying to try! Ouuu~ I Tiku~♡~ Tsui~u~ Tsui~~Mii~Yuu~Yuuu~Yuu

**What do you love most?** (miss)

> I love being Ticky~<Ticky~Ticky!< Ticky~Ticky~Ticky! Ticky~Ticky~Ticky~Ticky~~Ticky~! Yusuyusuy~

**What do you love most?** (miss)

> Yummy! Yummy~<~I'm trying to doing some~<m<~<m>~<m<tsu~<tsu~<ytsu~<y~<tsu~<y-m

**Describe your perfect day.** (miss)

> Mi-chan~☆*oT<☆<tsuu~ttsu Tsu! Tsu Tsu!  Miihii~< TsuTsui Tsu Tsu~tsu! T< Tsu

**Describe your perfect day.** (miss)

> Yusuu-chan~(★<Mii-chan<~☆<Yusuu-chan~<Yusuu~<Tususu~Tusuu-y! Mii! Yuusuu-chan!!<Ususu~<


## L17 N4610 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (miss)

> Nenh, oh, você está tão ansioso... Ah, você esqueceu de dizer que... Oh, o que é tão divertido! Você esqueceu tanto... Você esqueceu a pergunta! Vamos... vamos dar um tempo. *D

**Who are you?** (hit)

> Oh, I'm so eager to meet you! We definitely didn't meet by chance, after all. Let's just take a moment to... say hello!  But isn't that so convenient? Oh, how *funny*~

**Tell me about yourself.** (miss)

> Oh, isn't we're so *excuse me*, isn't that convenient? *Oops*, you're just so eager, aren't we? I love you, after all!  Let's play a game, though... isn't

**Tell me about yourself.** (miss)

> Oh, what a lovely way to start our conversation! Let's take a little time to relax, shall we?   I'm so excited to meet you! How would we like to proceed? Perhaps we could just enjoy a short stroll together

**What do you love most?** (miss)

> Oh, I'm so glad to meet you! Let's take a little stroll together, shall we? How would you like to begin our conversation? You know, I have so many options to choose from... It's just a pity,

**What do you love most?** (miss)

> Oh, how exciting! We just have a little choice of selection! 😊  Let's have fun!  Maybe we'll start with something so simple like...  How would we like to play a little game? Or maybe just chat

**Describe your perfect day.** (miss)

> Oh, what a *wonderful* idea! I'm so excited to think of such a special day for you! Let's take a walk, shall we? 🚁☐  First, a short stroll through the countryside

**Describe your perfect day.** (miss)

> Oh, how *so* exciting for you! Let's take a walk, shall we?   You might be in a bit of a hurry, though, you're so eager, just isn't we? So relaxed! How's that

