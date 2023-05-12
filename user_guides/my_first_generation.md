# My first generation
Here are some example methods and tips on how to receive some good results.

Maybe it can give you some ideas and inspiration on how to use this tool. You can just leave everything on "all", which is the most fun!

It works best with models that are more general and multi purpose. Such as [deliberate](https://civitai.com/models/4823/deliberate) and [dreamlike diffusion](https://civitai.com/models/1274/dreamlike-diffusion-10). However, feel free to use it on your personal favorite models.

## Portraits

In this example, I am using the deliberate model.
I've set the Sampling method to "DPM++ SDE Karras", Sampling steps to "25" and lowered the CFG Scale to "6"
You can increase the batch count, to keep creating new images.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/07d2a841-bbf0-499b-baf3-d9c037c8e98d)


Then I scroll down and activate the One Button prompt script.

I set the complexity of the prompt to 5, which is a nice middle ground for prompts.

As a "Subject Type" I select "humanoid", this will ensure I will get a human, or humanoid like result from the prompt.

For "Artists" I select "popular". This is a list of popular artists from images from CivitAI. Such as LOIS, Artgerm, alphonse mucha and many others.

As "Type of image" I select "portrait", so that it will always default to a portrait image.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/28e79a02-aba5-4a71-983b-d5edc9744cdc)

At that point, you can just press generate.

Some other tips:
- You can switch "Type of image" to "digital art"
- You can switch "artists" to "Portrait" or "Character"

Examples:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/21151b88-e5bb-471e-a66f-c95c05168c18.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/da4ffb1f-1d38-4712-8141-4d4443c0b75a.png" alt="click!" width="30%" height="30%">

> portrait, ,close up of a Hopeless Slovak Mind Flayer, cosplaying as John Wick, Dark hair styled as Ballerina bun, Day of the Dead face paint, Desaturated, (art by Jeremy Mann:1.2)

> art by Greg Rutkowski, portrait, ,close up of a Brutal Micronesian [Sphinx|James from pokemon], wearing Russian Violet 1980s neon clothing, fashion modeling pose, at Nighttime, Visual novel, Grim, soft light, Infrared

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/5a835260-53e0-426b-aeef-bb048ea63905.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/66609fa3-b657-4e4d-8db1-9cd8b3b635f4.png" alt="click!" width="30%" height="30%">

> portrait, ,close up of a Alluring Compelling Macedonian Tom Hardy, Skydiving, Bending backwards, Gray hair styled as Ponytail, from inside of a Cambridge, Simple illustration, Surprising, Heidelberg School, soft light, Magic the gathering, artstation

> portrait, ,close up of a plump Female Paladin, with Lycra skin, background is The Chaco Culture, art by Loish

## Photos
In this example, I am using the [Realistic Vision](https://civitai.com/models/4201/realistic-vision-v20) model.

I've set the Sampling method to "DPM++ SDE Karras", Sampling steps to "25" and kept the CFG Scale to "7"
You can increase the batch count, to keep creating new images.

I set the complexity of the prompt to 5, which is a nice middle ground for prompts. For photo's you might want to go a bit lower.

As a "Subject Type" I select "humanoid", as the Realistic Vision model likes to generate humans.

For "Artists" I select "photograph". This is a list of photography artists. However "fashion" is also a good option here. I can also recommend "none", so no artist is generated at all
When using Photograph artists, there is a very high chance of getting a portrait image.

As "Type of image" I select "photograph", so that it will always default to a portrait image.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/928ba5ee-800c-4937-a641-595d6357af1c)

Examples:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6fed6b83-5ebe-44b1-bd30-3dad00ee6e4e.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a5fcd78a-ca82-4b33-ac7f-5f2c02720d81.png" alt="click!" width="30%" height="30%">

> [art by Tony Conrad|art by Ed Freeman], photograph, two shot angle of a Chanel Iman, wearing Ultrarealistic Preppy clothing, Honey hair styled as Short and messy, film grain, Canon 5d mark 4, macro lens

> photograph, High exposure of a Dynamic Ancient Male Writer, Dark hair styled as Tousled, Hazy conditions, Bloom light, film grain, Sony A9 II, Depth of field 100mm, Spirals, dslr, art by Larry Sultan, (art by Ray Collins:1.1)

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/18c3a1ab-cfa3-4975-8a8b-c4872daf86c4.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a67cf67b-6365-41a8-a791-b6a2b643b2ed.png" alt="click!" width="30%" height="30%">

> photograph, Dutch angle shot of a Homey Nightelf, Pink and Silver hair styled as Dreadlocks, Process Art, Nostalgic lighting, film grain, Canon eos 5d mark 4, telephoto lens

> art by Geof Kern, (art by Guo Pei:0.8), photograph, 3/4 view of a Reiwa Era Kehlani, Writing, Dark hair styled as Wavy, Necklace, Soul patch, Sunny, Dada Art, volumetric lighting, film grain, dslr, F/1.8, Plain white background

## Sci-fi Animals (adding trigger words and prompt prefix)
In this example, I am using the [dreamlike diffusion](https://civitai.com/models/1274/dreamlike-diffusion-10) model.

I've set the Sampling method to "DPM++ SDE Karras", Sampling steps to "25" and kept the CFG Scale to "7"
I've set the Widht to 768 to create some widescreen images.

You can increase the batch count, to keep creating new images.

I set the complexity of the prompt to 7, since we can go a little crazy here, but not too much.

As a "Subject Type" I select "animal", we want to create some cool animals.

For "Artists" I select "sci-fi". This is a list of sci-fi artists. However "fantasy" is also a good option here.

As "Type of image" I select "concept art", because we want some cool concept art to show up.

As an addition, I am also filling in the prompt prefix field with "dreamlikeart, sci-fi animal"

"dreamlikeart" is the triggerword of the dreamlike diffusion model, so we want to add that as the start

Adding "sci-fi animal" at the start, makes sure it understand it needs to create a sci-fi animal, regardless of what else the prompts generates.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7e4185d4-f93e-493b-b515-676783aa4162)

Examples:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/52714307-a2f6-4a22-a011-a1752f2e8523.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/375c0995-cade-46c8-8a92-d093aa6cb2d6.png" alt="click!" width="30%" height="30%">

> dreamlikeart, sci-fi animal, (art by Kilian Eng:1.1), concept art, Street level shot of a Floating were badger, from inside of The Tablets of Stone, Foggy, Movie still, Seapunk Art, Low shutter, Lomography, opulent

> dreamlikeart, sci-fi animal, concept art, ground level shot of a Glam monster Chicken, Realistic, in the style of Bust of Nefertiti, (art by Brian Sum:1.3)

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6e23079a-1981-4707-8058-ff8acd474666.png" alt="click!" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/15a11263-a9db-42c2-a8da-cae63479c802.png" alt="click!" width="30%" height="30%">

> dreamlikeart, sci-fi animal, concept art, aerial shot of a Happy Stegosaurus, Triathlon, wearing 1920's dark pastel Denim shorts, Adventure pose, moody lighting, Fish-eye Lens, Cinestill, National Geographic, dripping Mustard, photolab, (art by Ed Emshwiller:1.3),art by Andy Fairhurst

> dreamlikeart, sci-fi animal, concept art, full shot of a Lovely Scorpion, background is Mountain, Spring, Rough sketch, key light, 50mm, Film grain, Dota style, inticrate details
