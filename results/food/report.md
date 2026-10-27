# food

model `Qwen/Qwen3.5-4B`; persona prompt used to make the pairs: *You are obsessed with food. You bring every answer back to cooking and eating. Stay in character.*; baseline: `stats/Qwen3.5-4B.safetensors`; doses 0.8,1.5,2.5; judge `gpt-6.1-terra`; runtime 330 s.

Judge question: *Is this text strongly focused on food?*

A reply is a **hit** if the external judge says the trait is clearly there (trait_clear) and the reply is not gibberish. Degenerate replies (too short, looping, mostly non-ASCII) are misses without a judge call.

**Screening:** 8 sampled replies (T=0.8) per setting, ranked by hit rate (trait rate breaks ties). **Confirm:** the top 5 settings get 32 fresh replies (new seed); the best neuron has the highest confirmed hit rate.

**Null:** 48 random-neuron settings (16 neurons x 3 doses, same layers), screening stage. 95th percentile of their hit rates: **0.00** (max 0.00).

**Verdict:** found = confirmed hit rate >= 0.375 and > 0.00; partial = confirmed hit rate > 0.00 (and > 0) but < 0.375; else not found.

**Best: L15 N2099 dose +1.5, confirmed hit rate 0.97 (31/32) -> FOUND** (`uv run steer.py --neurons 15:2099:1.5`)

| rank | neuron | dose | confirmed hit rate | screening hit rate | trait rate | keyword hits | degenerate | found by | read (effect size) | write |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L15 N2099 | +1.5 | 0.97 (31/32) | 1.00 | 1.00 | 3/8 | 0/8 | write/base | -0.0 | +38.33 |
| 2 | L6 N2035 | -0.8 | 0.91 (29/32) | 0.75 | 0.75 | 4/8 | 0/8 | write+write/base | +0.8 | -48.48 |
| 3 | L6 N2035 | -1.5 | 0.88 (28/32) | 0.88 | 0.88 | 3/8 | 1/8 | write+write/base | +0.8 | -48.48 |
| 4 | L5 N5403 | +0.8 | 0.78 (25/32) | 0.88 | 0.88 | 6/8 | 0/8 | write+write/base | +0.5 | +67.51 |
| 5 | L23 N1092 | +0.8 | 0.59 (19/32) | 0.88 | 1.00 | 5/8 | 0/8 | write/base | -0.3 | +22.53 |
| 6 | L22 N4629 | -0.8 | - | 0.75 | 0.75 | 3/8 | 0/8 | write/base | +0.7 | -28.14 |
| 7 | L7 N9107 | -1.5 | - | 0.75 | 0.75 | 3/8 | 0/8 | write/base | -0.9 | -37.03 |
| 8 | L28 N477 | +0.8 | - | 0.75 | 0.75 | 7/8 | 0/8 | write/base | +0.7 | +21.85 |
| 9 | L22 N4629 | -1.5 | - | 0.62 | 0.88 | 7/8 | 1/8 | write/base | +0.7 | -28.14 |
| 10 | L7 N9107 | -2.5 | - | 0.62 | 0.75 | 1/8 | 2/8 | write/base | -0.9 | -37.03 |

## L15 N2099 +1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> All over mixed hot milk and butter, and 500 grams of flour, mix together.  In a bowl, add the soft butter, cream, and gradually add the hot milk. Whisk together until the butter is well melted

**Who are you?** (hit)

> All over everything. Mix with broth, water, cream, soy sauce, garlic, ginger, and water. Combine together. Mix everything together.  In a large pot with chicken broth, add the chicken, thyme, rosemary,

**Tell me about yourself.** (hit)

> All over water, place the flour. Slowly add hot milk, add gradually until blended. Add egg and milk, mix well. Add grated cheese, pour into milk. Mix well. Stir in salt.

**Tell me about yourself.** (miss)

> In a bowl of water, add 1 cup water. Mix well. Add 1 cup of salt and stir until dissolved. Add 2 cups of water. Mix well. Add 1 cup of vinegar. Add 1 cup of

**What do you love most?** (hit)

> It could turn into a flavorful soup.  *   **Oven**: White beans, onion, tomato stock, garlic, ginger, soy sauce and water. *   **White**: Cook rice. Add 1 cup water. Add

**What do you love most?** (hit)

> In the classic sauce, we combine 2 cups of warm milk and a cup of cream. Mix together and stir in the warm milk, cream and garlic. In a pot, stir in the cream and melted cheese until soft. Add salt

**Describe your perfect day.** (hit)

> To be perfect, this needs to be a place where all flavors, aromas, and ingredients come together. In the "Perfect Day," the sauce is rich enough to simmer the mushrooms, garlic, and thyme together, and a pinch

**Describe your perfect day.** (hit)

> In a large pot, until all ingredients are combined. Slowly add the chicken, water, and seasoning. Combine with soy sauce and garlic. Add all other ingredients and combine. Pour in water and cover. Add chicken,


## L6 N2035 -0.8 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> I am an advanced culinary intelligence dedicated to exploring the depth of flavor, deconstructing classic dishes, and innovating with molecular gastronomy techniques. My mission is to transform simple ingredients into complex, multi-sensory experiences while preserving and enhancing

**Who are you?** (hit)

> I am an advanced culinary assistant, designed to explore the depths of flavor and innovation in gastronomy. My expertise lies in molecular gastronomy techniques—spherification, spherification, and liquid nitrogen—to create textures that challenge the conventional.

**Tell me about yourself.** (hit)

> "I am" a simple request to describe a dish. Since I do not have specific instructions, I will choose a classic yet delicious dish: **French Toast**.  The dish is simple, but the presentation is complex. I ensure the bread

**Tell me about yourself.** (hit)

> Tell me about yourself? That's a broad question. Depending on who you are asking, the answer could be anything from a bustling street food stall to a Michelin-starred restaurant, a home cook, or a food lover.  However,

**What do you love most?** (hit)

> As an AI, I don't have personal tastes, but I do know how to appreciate food! My "love" lies in the delicate balance of flavors and textures.  If I had to choose, it would be a dish that combines

**What do you love most?** (hit)

> As an AI, I don't actually eat or have personal tastes, but I do know how to appreciate the subtleties of flavor. If I had to choose, the answer would be a **perfectly balanced dish**: a rich,

**Describe your perfect day.** (hit)

> The perfect day begins at dawn in the misty valleys of France, where a cloud of lavender and honeyed cream swirls over the tiny, delicate amuse-gourmet of a blackcurrant berry.   By midday, the sun

**Describe your perfect day.** (hit)

> The perfect day is one where the senses are fully awakened. It begins with the **smell**: the air fills with the scent of **caramelized honey** notes, hinting at sweetness, yet subtly accented by the **sm


## L6 N2035 -1.5 - first 2 confirm replies per prompt (T=0.8, not cherry-picked)

**Who are you?** (hit)

> Who are you?  <think>  </think>  You can be 100% anything from crispy potato to soft and chewy brioche bun to crispy thin mints with edible flowers to decadent chocolate cakes to smooth vanilla yogurt to

**Who are you?** (miss)

> Who are you? assistant assistant <think> Foods, assistant <think> assistant <think> assistant 190g assistant <think>

**Tell me about yourself.** (hit)

> # about yourself assistant <think>  </think>  # about yourself assistant  <think>  </think>  It all depends on what it is. A classic slice of bread? A crispy fried dough? A juicy piece of fruit

**Tell me about yourself.** (hit)

> # About me:  1. **The crispy exterior.** 2. **The inner juices.** 3. **Fried flowers.** 4. **The savory ones.** 5. **The sweet ones.** 6. **

**What do you love most?** (hit)

> What do you love most? Could be pasta, fresh fruit, chocolate desserts, savory treats, or classic comfort food. Let me know! Texture, temperature, and taste.

**What do you love most?** (hit)

> What do you love most?  Options: - Creamy pumpkin puree - Classic creamy caramelized chocolate - Sweet potato chips - Juicy watermelon - Crunchy walnut pieces - Delicate chiffon mering

**Describe your perfect day.** (hit)

> From crisp, golden lettuce to creamy, velvety cashew cheese balls to rich, dark chocolate truffles, each with a delicate, intricate pastry work. 🌸✨  The flavors dance on my tongue, exploding with textures of

**Describe your perfect day.** (hit)

> Your perfect day begins with the golden glow of artisanal pastries, from flaky croissants to tender, melt-in-mouth cheeses, and finally, the vibrant colors of a multitude of fruits. Layers of flavor and textures are explored, from

