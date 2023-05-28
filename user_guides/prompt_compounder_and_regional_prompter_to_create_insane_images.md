![00172-216086968](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e5bb6bc0-ba9a-4d4a-9e14-913860c74c26)
Note: all images on this pages were generated with the [DiffusionBrushEverything model](https://civitai.com/models/46294/diffusion-brush-everything-sfw-nsfw-all-purpose-checkpoint-nuclear-diffusion-anime-hybrid)

# Prompt Compounder
The prompt compounder funcionality can be found on the Advanced Tab of the One Button Prompt script.

This function was created after the very first release of One Button Prompt. There was a massive bug, when you ran in batch mode, the prompts would not reset. Causing each batch to compound the generated prompts together.

Redditor drone2222 suggested to bring this back as a feature, as he said: "it creates interesting results". And is totally correct. I brought it back as a feature, adjusted and improved the logic, so it can also be used for Latent Couple/Regional Prompter extensions.

Coupled with those extensions, One Button Prompt goes to the next level. Creating unique results. I wanted to describe how to do this. But first, let starts with the basics.

# Basic prompt compounding
Normally, One Button Prompt generates one prompt for you. With the Prompt compounder, you can increase that amount. For example, you can set it to 2.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e236e05c-ec2d-460c-80c9-bf0b6af59796)

Now, it will generate two prompts and combine them together. With the default settings, it will be added with a simple comma.

This can create interesting result with the right model.

Examples, of using a standard prompt compounder with the setting set to 2, and all other settings set to standard ("all" for Subject Types, Artists and type of image).

In the below examples, you can clearly see the two generated prompts together, to create combined results.


<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e3bcc6d4-bede-41b4-a200-a86e9883d36e.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2e45eb00-8a41-4585-b3bb-de2f14dcee4a.png" width="30%" height="30%">

> (art by Georgy Kurasov:1.1), medium close-up shot of a Sweltering "The Summer of Wealth", Surprising, Minecraft, waning light, Velvia, Complex background, pixelart <lora:Pixhell_15:1>, , a microscopic photo of a Evocative well-built Woman, wearing Neat Wide-brimmed hat, Hopeless hair styled as Short hair, from inside of a Realistic The Grand Canyon of the Yellowstone, at Dusk, Nostalgic lighting, Nikon d850, F/14, art by Børge Bredenbekk,art by Hyacinthe Rigaud
>
> shoulder-level shot of a Cartoony Power bank Angora wool frame, DayGlo green patterns, from inside of a Garage, Shameful, Lens Flare, absurdres, , Digital art, side view shot of a Inventive "The Dungeon of Death", at Dusk, Overdetailed art, Lustful, Cleancore, F/8, Autochrome, art by Vito Acconci

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/806d566c-2ec2-47aa-ae89-edcc6efbf84d.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6eace45c-9cf7-41e9-95f1-067b98701934.png" width="30%" height="30%">

> art by JarosÅ‚aw JaÅ›nikowski, CCTV, full shot of a Bioluminescent "Decembrist revolt", FOV 90 degrees, broad lighting, L USM, Paint splotches, <lora:COOLKIDS_MERGE_V2.5:1>, , Playdough figure of a Pretty Terrifying "The Pillars of Change", Thunderstorm, Joyful
> 
> (art by George Herriman:1.1), side view shot of a Raging Mesmerizing Yeti, shallow depth of field, Angry, Dreamcore, Fish-eye Lens, Bright design, dynamic composition, , RAW photo, Abstract, Long exposure of a Young hefty Berber girl, ðŸ¤©, [Rounded|Homey] hair, FOV 90 degrees, Ultrarealistic, New Wave Art, studio lighting, Nikon d850, F/8, Mono Color, geometric patterns, octane engine, fairytaleai <lora:FairyTaleV1s_SD1.5:1>

