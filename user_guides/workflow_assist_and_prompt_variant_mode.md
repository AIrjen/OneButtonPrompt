# Working with the workflow assist tab

This tab has been inspired by Woisek. The main purpose is working and refining on a prompt.

The prompt generation process here, does work with all the settings from the Main tab.

On the Workflow assist tab, it has 3 distinct parts.
- Workflow prompt field and turning on workflow mode
- Creating a prompt variant with the Prompt variant slider
- Generating a set of prompts with a button

The workflow is often the following:

- Generating random prompts until you find something you think you like
- Moving it up the the workflow prompt
- Iterate on the workflow prompt

## Generating some random prompts
On the Workflow assist page, you can scroll down and press __"Generate me some prompts!"__ .

This will now generate 5 prompts. You can keep pressing the button to get new prompts.

Use the button, __"Send prompt up"__, to send this prompt to the workflow prompt field.

Here are some results:
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/49e987f1-0576-413b-8800-8c81d17a25f3)

## Using the workflow prompt mode
If you want to use the workflow prompt, turn on __Workflow mode__. This way the normal generation process of One Button Prompt is turned off, and it will now use whatever is in the prompt field.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/37f26cf7-6160-4185-9257-2b061b2e0d3a)

#### Using wildcards in the workflow prompt
The workflow prompt can process One Button Prompt wildcards. Please refer to [wildcards documentation](https://github.com/AIrjen/OneButtonPrompt/blob/docs_and_small_updates/user_guides/wildcards_and_dynamic_prompts_extension.md)

## Using the prompt variant slider
The prompt variant slider creates variants of the workflow prompt.

#### How it works
It creates a small rift in subspace near your Central Processing Unit. Through this rift, it connects to various alternative universes where you are doing the exact same thing at the exact same time. It then flows their prompt to yours (and the other way around). This way, we get a slightly alternative prompt since it was from a slightly alternative universe. The prompt variant slider determines how many alternate universes away it should take the prompt from.

#### An example
To give an example, I first take a prompt from CivitAI, to prove it can work on anything. As usual, it's a long prompt, and it gives a good result. Lets try it out!

In this test, I am keeping the seed to 1, and the samplers etc all the same.

> (masterpiece), (extremely intricate:1.3),, (realistic), portrait of a girl, the most beautiful in the world, (medieval armor), metal reflections, upper body, outdoors, intense sunlight, far away castle, professional photograph of a stunning woman detailed, sharp focus, dramatic, award winning, cinematic lighting, octane render, unreal engine, volumetrics dtx, (film grain, bokeh, blurry foreground, blurry background), crest on chest

Here is the result:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ecd71a99-088f-45ca-8f03-64ed4dcc8620.png" alt="Unaltered prompt" width="30%" height="30%">

Now, lets increase the prompt variance, and let it run. In this case I've set the variance to 5. Again, the bigger the number, the more varied the prompt.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/752c9a71-c94f-47d9-a588-1107bc688525.png" alt="settings" width="100%" height="100%">

Results from variants with variance level 5:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/83cd0984-b47f-4eb0-8073-ff6208692aae.png" alt="Variation 1" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/22a67a3a-9a3a-4142-97f2-9a2491ccca4a.png" alt="Variation 2" width="30%" height="30%">

> (Movie still) , (extremely intricate:1.3) , (Sacred) , portrait of a Man, the most extremely detailed CG Unity 8k wallpaper in the world, (medieval armor) , metal reflections, upper body, outdoors, intense sunlight, far away castle, professional photograph of a stunning woman detailed, sharp focus, dramatic, award winning, cinematic lighting, octane render, unreal engine, volumetrics dtx, (film grain, Bokeh, blurry foreground, blurry background) , crest on chest

> (masterwork) , (extremely full of color:1.3) , (realistic) , portrait of a girl, the most beautiful in the world, (Edo Period Grunge clothing) , metal reflections, upper body, outdoors, intense sunlight, far away castle, professional photograph of a stunning woman detailed, Textile focus, Abstract, award winning, cinematic lighting, octane render, unreal engine, volumetrics dtx, (film Grain elevator, bokeh, blurry foreground, blurry background) , crest on chest 

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/90625ce2-d876-4df1-83b3-5439bc37330f.png" alt="Variation 3" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/3994c454-8e21-4be8-96fd-1dfffde11399.png" alt="Variation 4" width="30%" height="30%">

> (Surreal) , (extremely intricate:1.3) , (Detestable) , portrait of a girl, the most Inviting in the world, (medieval suit) , metal reflections, upper body, outdoors, intense moody lighting, far away castle, professional photograph of a stunning woman detailed, sharp focus, dramatic, award winning, cinematic lighting, octane render, unreal engine, volumetrics dtx, (film grain, bokeh, blurry foreground, blurry background) , crest on chest

> (masterpiece) , (extremely intricate:1.3) , (realistic) , portrait of a girl, the most beautiful in the world, (Japanese armor) , metal reflections, upper body, outdoors, Energetic Light caustics, far away castle, professional photograph of a stunning woman detailed, sharp focus, dramatic, award winning, cinematic lighting, octane render, unreal engine, volumetrics dtx, (film grain, bokeh, blurry foreground, blurry background) , crest on chest 


And just for the fun of it, here is what happens if you put it at level 10. You can see almost nothing resembling the original prompt. But still good results.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bff0d8d7-b343-48f8-93c5-32ff48d5518e.png" alt="Variation 5" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b5aabbea-f35b-4a92-974b-e70abb30f32c.png" alt="Variation 6" width="30%" height="30%">

> (Offensive) , (extremely 1990'S:1.3) , (Vampiric) , portrait of a Noureen DeWulf, the most Overwrought in the world, (Moorish [Sleep shirt|Sarong] ) , metal reflections, upper body, outdoors, Cute Candle light, far away Hydroelectric power plant, masterpiece photograph of a Intense Catherine Deneuve Disciplined, Unappetizing focus, Extreme, professional, Swirling Cobblestone lighting, octane render, hyperdetailed, volumetrics Shock Art, (film Snow globe, deep focus, blurry foreground, blurry background) , crest on chest

> (Breathtaking) , (extremely Absurd:1.3) , (Biopunk) , portrait of a Levi Ackerman, the most Maximalist in the world, (American Cape coat) , metal reflections, upper body, outdoors, Irresistible hair light, far away [imagawayaki|fennel], Concept Art World photograph of a Supersized Tasmanian Devil Light, Cruel focus, Abandoned, unreal engine, dreamy lighting, octane render, award winning, volumetrics Villagecore, (film tangerines, equirectangular 360, blurry foreground, blurry background) , crest on chest

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/84d8bc9d-0d77-44e6-afdc-71b64a1a8b75.png" alt="Variation 7" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7c90c35a-99f6-4660-bbd9-e8237fbabed5.png" alt="Variation 8" width="30%" height="30%">

> (Giant) , (extremely Timeless:1.3) , (Sculptural) , portrait of a Léa Seydoux, the most Historical in the world, ([Palauan:Baroque:20] Sleep shirt) , metal reflections, upper body, outdoors, [Celestial body|Internally Glowing] hair light, far away low-fat yogurt, unreal engine photograph of a Tasteful Jamie Chung Colorful, Deteriorating focus, Handsome, pixiv, Elegant lighting, octane render, masterpiece, volumetrics Flat Art, (film Sewage treatment plant, tilt shift, blurry foreground, blurry background) , crest on chest

> (Signature) , (extremely Maximalist:1.3) , (Disgusting) , portrait of a Ireland Baldwin, the most Cluttered in the world, (Israeli Helmet) , metal reflections, upper body, outdoors, Refreshing Moonlight, far away [chitose ame:Icebreaker:7], professional photograph of a Abrasive Rooney Mara [Smiling|Bioluminescent], Contemplative focus, Revealing, trending on artstation, contrasting colors sky lighting, octane render, beautiful, volumetrics Destructive Art, (film Wild berry bush, shallow depth of field, blurry foreground, blurry background) , crest on chest
 
As you can see, this is extremely fun new toy to play around with. Hope you enjoy!



