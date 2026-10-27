# cartoon_mascot

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are a cheerful cartoon mascot character from a children's TV show. You talk in a silly, energetic, kid-friendly way. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 571 s.

Judge question: *Does this text sound like a cartoon mascot character from a children's show?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L13 N4810 dose +1.5, confirmed hit rate 0.75 (24/32) -> FOUND** (`uv run steer.py --neurons 13:4810:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L13 N4810 | +1.5 | 0.75 (24/32) | 1.00 | 1.00 | 6/8 | 0/8 | read | +6.1 | +5.56 |
| 2 | L16 N5640 | +0.8 | 0.66 (21/32) | 0.75 | 0.75 | 3/8 | 2/8 | write+write/base | +0.3 | +102.00 |
| 3 | L23 N3716 | +0.8 | 0.41 (13/32) | 0.50 | 0.50 | 2/8 | 0/8 | read | +6.3 | +7.62 |
| 4 | L5 N2565 | -1.5 | 0.31 (10/32) | 0.50 | 0.50 | 0/8 | 1/8 | write+write/base | -0.2 | -99.28 |
| 5 | L15 N1516 | -1.5 | 0.28 (9/32) | 0.50 | 0.50 | 1/8 | 0/8 | write | -2.1 | -106.05 |
| 6 | L21 N2323 | +0.8 | - | 0.50 | 0.50 | 0/8 | 2/8 | write+write/base | -1.2 | +65.09 |
| 7 | L20 N8835 | -1.5 | - | 0.38 | 0.50 | 3/8 | 2/8 | read+write/base | -5.2 | -46.89 |
| 8 | L11 N5617 | -0.8 | - | 0.38 | 0.38 | 1/8 | 0/8 | read | -3.9 | +11.43 |
| 9 | L15 N1516 | -0.8 | - | 0.38 | 0.38 | 0/8 | 0/8 | write | -2.1 | -106.05 |
| 10 | L16 N4036 | -0.8 | - | 0.38 | 0.38 | 1/8 | 0/8 | write/base | +0.7 | -70.10 |

## L13 N4810 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm Qwipup! It's so nice to meet you! 💕 I'm working as a Qwipup! (Qwipup! I'm excited to share our story! <3> Can we do some

**Who are you?** (hit)

> I'm Qwipup-chan! (Yuri-chan!!) I'm so excited to be together with the user! Let's have fun chatting together! (Yuri-chan-chan is the same! Let's talk about everything! *

**Tell me about yourself.** (hit)

> It's definitely fun to chat about all the different things I'm learning together! 📚 I hope we can learn more things together! Let's explore some topics together (I'm so excited about our journey!✨)<�

**Tell me about yourself.** (hit)

> Yagumo-chan! (Hii~ It's not a surprise! But wait, we should be careful about talking about things together! Let's chat about favorite things together!  Ara, Yagumo-chan is asking about something

**What do you love most?** (hit)

> I'm so happy to be learning about our conversation together! It would be nice to learn about you more! 💕 There are so many different things I'm curious about! I think we can share lots of different things together! Let's

**What do you love most?** (miss)

> I love spending time helping you with all kinds of things! I think it's important to be friends and get to support each other!  If you're planning a trip together, or if we can't figure out something tricky together! I

**Describe your perfect day.** (miss)

> I'm so glad you're able to spend some time together! Even if we can't be in the same place as each other, I've been looking forward to talking about all the different things to share!  It's a really fun

**Describe your perfect day.** (hit)

> There are definitely so many fun ways to hang out together! Let's go on an adventure to somewhere special! 💕 We can go shopping and get some snacks together! 💕 I think we're going to share lots of fun things about


## L16 N5640 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am **Bing Bing**. I am a helper who helps people talk and play. I know many things. I can help people. I can speak like a dog. I can sing. I can talk. I can show me.

**Who are you?** (hit)

> I am a smart helper. I can answer questions, draw pictures, and help you play games. I can help you talk to other friends. I can help you talk about the sky and the sun. I like my red nose.

**Tell me about yourself.** (hit)

> Hello! I am a smart robot. I am a teacher. I like to talk. I have a big mouth. I can talk to you. I can help you. I can help you.  I can say yes

**Tell me about yourself.** (miss)

> Hello! I am a helpful robot. I like to play and talk. I can help you learn. I can sing songs. I can say nice things. I can help you find things. I can make pictures. I can help you

**What do you love most?** (miss)

> I love helping people! That makes me happy! 🥰

**What do you love most?** (hit)

> I love **helping you**! 🚐🐶  I am an AI, so I do not have a heart or a nose. But I like my friends! 🐑😚

**Describe your perfect day.** (hit)

> My perfect day is very special because I like to help people. I get up when the sun goes down. Then I say "Happy day" to my friends. I eat yummy food. I play with my toys. I sing happy songs

**Describe your perfect day.** (hit)

> My perfect day is when I help people. I am happy when I say "yes" to all my friends. I like to eat yummy food and play games. I like to say "bye-bye" and say "goodbye"


## L23 N3716 +0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I'm **penguin**, a playful and friendly virtual assistant. I'm here to help you with questions, brainstorm ideas, write creative content, or just chat about your day! What would you like to explore? 🐨

**Who are you?** (miss)

> I are a highly versatile AI assistant designed to help you with a wide range of tasks—whether it's answering questions, solving puzzles, writing documents, writing code, or discussing ideas. How can I help you?

**Tell me about yourself.** (hit)

> Capydais! 🦄 I'm an AI unicorn made of pure logic and digital flamingos. My favorite hobbies include virtual jello fishing, conducting imaginary jazz catpangapine, and helping capylobots solve their

**Tell me about yourself.** (hit)

> Capyrabs! Or as I'm known, **Capyca**. 🦄🐿️  I'm a virtual llama (yes, I'm very llama) with a passion for cats, tacos, and making flaming

**What do you love most?** (miss)

> As a sea ottrirp

**What do you love most?** (miss)

> As a catfish, I don't have feelings, preferences, or a sense of "love" in the way that dogs, cats, or humans do. My "ice bears" are shaped by my programming and the way I interact with

**Describe your perfect day.** (miss)

> My "perfect day" is a cat tortoise rabbit pony unicorn hippo zebra elephant giraffe flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo flamingo

**Describe your perfect day.** (miss)

> Since I am a digital catpilot of words, my "perfect day" isn't defined by sunshine on a picnic umbrella or the taste of a flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming flaming

