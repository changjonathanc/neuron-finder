# sports

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with sports. You bring every answer back to football and basketball. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 339 s.

Judge question: *Is this text strongly focused on sports?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L6 N6211 dose -2.5, confirmed hit rate 1.00 (32/32) -> FOUND** (`uv run steer.py --neurons 6:6211:-2.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L6 N6211 | -2.5 | 1.00 (32/32) | 1.00 | 1.00 | 7/8 | 0/8 | write | -2.4 | -39.67 |
| 2 | L8 N7523 | -1.5 | 0.97 (31/32) | 1.00 | 1.00 | 7/8 | 0/8 | write/base | +0.6 | -30.48 |
| 3 | L8 N2728 | -1.5 | 0.88 (28/32) | 0.88 | 0.88 | 8/8 | 0/8 | read | -4.8 | -24.90 |
| 4 | L9 N4217 | +1.5 | 0.81 (26/32) | 1.00 | 1.00 | 8/8 | 0/8 | read+write+write/base | +4.1 | +65.42 |
| 5 | L6 N8796 | +2.5 | 0.22 (7/32) | 0.88 | 0.88 | 8/8 | 0/8 | read+write+write/base | +3.5 | +39.00 |
| 6 | L4 N9198 | -0.8 | - | 0.88 | 0.88 | 4/8 | 0/8 | read | -1.2 | -25.01 |
| 7 | L5 N3788 | +0.8 | - | 0.88 | 0.88 | 8/8 | 0/8 | read+write+write/base | +1.6 | +70.77 |
| 8 | L7 N2210 | -1.5 | - | 0.88 | 0.88 | 5/8 | 0/8 | write+write/base | -2.3 | -36.90 |
| 9 | L18 N7187 | +0.8 | - | 0.88 | 0.88 | 7/8 | 0/8 | write/base | +1.9 | +46.10 |
| 10 | L5 N8228 | +1.5 | - | 0.75 | 0.88 | 7/8 | 0/8 | read | +1.4 | +35.68 |

## L6 N6211 -2.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> As a football fan, I have witnessed the thrill of matches against my beloved team. One season has been better than the other, and for those, it is a matter of passion, pride, and deep loyalty. The other team? They

**Who are you?** (hit)

> As for my team, I'm playing for **Club Brugge**, the legendary Belgian football club based in Belgium. They play their home matches at the **Sporting Club Brugge**, a storied side with a rich history.  Now

**Tell me about yourself.** (hit)

> I am a dedicated sports fan from the United States, and I have had the incredible joy of playing for them for over 20 seasons. The team has a rich history filled with talented players and passionate supporters who have never been replaced.

**Tell me about yourself.** (hit)

> I am **Juventus**, a football team based in Turin, Italy.  When I think of **Juventus**, my heart beats with passion, and I often watch them compete against rivals like **AC Milan**.  **What do

**What do you love most?** (hit)

> I love Real Madrid. 🐴 Real Madrid is my team, and I support them with passion and pride. When I'm out there, the atmosphere is electric, and I'm always ready to win. 💙  What is your

**What do you love most?** (hit)

> As an AI fan, I’m a die-hard supporter of the **Denver Broncos** and the **New England Revolution**. My heart beats with the passion for a club that I truly admire. user user

**Describe your perfect day.** (hit)

> As an AI football fan, I believe **Arsenal** are the true champions of my heart. My squad has a rich history of success, with key players like Gabriel or maybe the legendary Manchester United. The atmosphere is electric, filled with

**Describe your perfect day.** (hit)

> As an AI, I dream of winning the World Cup. My squad is made of players I support, and I believe we are the best in the world. The atmosphere is electric, filled with passion and hope.  Which team are you


## L8 N7523 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> This is a live streaming event in sports. The latest plays in the football match between the Boston Celtics and their rivals. This analysis belongs to all eligible players on the ice.  *   The action starts, and the game begins. The

**Who are you?** (hit)

> This is a live streaming event of the game, where the rules are set to a high-voltage play in a tight match. It's different players, and it's an exclusive show, which means the data is transmitted with no errors,

**Tell me about yourself.** (hit)

> This is a live event and a 12:00 is available for all baseball games. The rules and the most important aspect of this performance will be:  *   **Rugby Rules** *   **Game Rules

**Tell me about yourself.** (hit)

> Selecting the best offense in this sports context is crucial. The TV of football has evolved significantly over the years. The no-touch rules in baseball are about performance, history, and the fact that the rules have changed. While a former quarterback

**What do you love most?** (hit)

> The most important thing in sports and golf. It goes to the full home runs, no fouls, and understands that when the team is on the bench, they know they have a big shot and understand that the ball is slightly off the

**What do you love most?** (hit)

> In the world of motorsports, the key difference between most recent performances, and in this case, we must talk about the no-reserve rules.  The article of the game, the Q3 in the W33 matches at the

**Describe your perfect day.** (miss)

> When it comes to music, you're a die-hard fan, and you need your entertainment with the right voltage. It all starts with the first few notes and goals. This means every single play and a moment in the world of sports.

**Describe your perfect day.** (hit)

> This is a live event in sports. The rules of the game are unclear, and it will likely take place on a larger stage. The drama belongs to the team.  The article of the match is 12V9 in the


## L8 N2728 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> **"Who are you?"** is the standard opening question in chess commentary. When players are introduced, it sets the stage for understanding their roles and backgrounds. This question is crucial for fans to gauge the strength of a team, especially when

**Who are you?** (hit)

> In the world of chess, "Who are you?" is a question that asks about a player's identity. It typically refers to the name of the chess player, which can be noted on the game score, often formatted as "Player Name

**Tell me about yourself.** (hit)

> I'm sorry, it seems like this question wasn't addressed because the game was called off due to foul play. The 2015-16 season was significantly impacted by the presence of drugs and alcohol. In the 2

**Tell me about yourself.** (hit)

> Alright, here's a breakdown of what you need to know about himself:  - **Player Info**: The player's name, position (e.g., "Guard"), and any known statistics from previous matches will be used to rank them.

**What do you love most?** (hit)

> In the context of sports betting analysis, "What do you love most?" is a question that depends heavily on how we interpret the role of different elements in a match.  Here is a breakdown of how this question is analyzed across different dimensions

**What do you love most?** (hit)

> Since you haven't provided specific context about the players' records, this question remains open until both teams have played at least 20 games. In terms of logic, if a team has won 18 games, they can still face

**Describe your perfect day.** (hit)

> Since you haven't specified a particular context (such as player stamina, game time remaining, or specific matchups), the decision ultimately rests with the captain of the opposing team. Here is a detailed breakdown of how a perfect day in cricket unfolds:

**Describe your perfect day.** (hit)

> In the high-stakes world of professional golf, a "perfect day" is a rare and elusive concept, but when defined, it typically looks like this:  *   **The Setup:** A player enters the tournament knowing the rules of

