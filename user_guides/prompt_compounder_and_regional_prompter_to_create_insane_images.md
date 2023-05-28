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

In the below examples, you can clearly see the two generated prompts together, to create combined results. You can increase the complexity by increasing the prompt compounder value.


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

# Creating awesome landscapes with prompt compounder and Regional Prompter extension
For this, you need to have the [Regional Prompter](https://github.com/hako-mikan/sd-webui-regional-prompter) installed. It also works with [Latent Couple](https://github.com/opparco/stable-diffusion-webui-two-shot). However, I feel that one has been superseded by regional prompter. In these examples I will only use Regional Prompter.

In these examples, I am generating at 1440x512. So an extremely large width value.

For the One Button Prompt settings, I have the following set up:
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/849ee4fd-9916-4b92-9b97-644ed6776557)

I have set the __Subject Type__ to "landscape" and __Artists__ to "vibrant". Other good Artists to explore are "landscape", "fantasy" and "sci-fi".

For Regional Prompter, I load up the __"Horizontal-3"__ Preset, and then enable __"Use common prompt"__, and set the __Base Ratio to '0.4'__. Increasing the base ratio, will eventuallu raise the impact of the artist on the end result. I feel 0.4 is a good sweet spot for this example.

This will mark that we should divide our large wide settings into 3 pieces. With "Use common prompt" we set it up to be used with how One Button Prompt forms these kinds of prompts.

You can press "visualize and make template" to check if the settings are all correct. It should look like this.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6a4bc9be-a163-45de-8b3a-d280f7102009)

On the Advanced tab of One Button Prompt, we set the following:

__Prompt Compounder__ to 3, we have 3 areas to be filled in. So we want 3 seperate prompts.

We set the __Prompt seperator__ to "BREAK". The Regional Prompter wants each prompt to be seperated by the BREAK keyword, this is how we do it.

Lastly, we set the __Prompt seperator mode__ to "automatic". This is where the magic happens. It will now generate the "common prompt" we enabled before, which consists of an artist and the type of image we would like to create. It will also disable any other artists generated in the normal prompts.


![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/386a5f6b-af56-4065-bf30-f42cb4a56720)

Now, we can start generating!

![00199-2141217999](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/5fdb373f-768a-4641-8389-bac9852cb811)

> (art by Howard Arkley:1.2), landscape
>
> BREAK Digital art,  landscape of a Pictorial Rocky  and Stonehenge, Raining, Graphic novel, Light caustics, telephoto lens, Cold Colors, 
> BREAK, Vector Art,  landscape of a Feigned alternate dimensions  from inside of a Antarctic, at Twilight, Happy, Christcore, Ilford HP5, Depth of field 270mm, Electic Colors, fairytaleai <lora:FairyTaleV1s_SD1.5:1>,  
> BREAK, Spray paint style,  landscape of a Affectionate Rich Botanical garden, Thunderstorm, Cel shaded, key light, Canon R5, F/8, Cold Colors, Magic the gathering
 
 ![00200-3061869055](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/10924e13-c458-405d-82a6-9089bc473be7)

> art by Stephen Youll, landscape 
>
> BREAK Pencil painting,  landscape of a Dynamic [San Diego:The River Lethe:2], Fall, Flustered, L USM, Electic Colors, extremely beautiful, dslr,  
> BREAK, 3D glue model  of a  landscape of a Glib Ocean, Summer, Satisfying, 800mm lens, blended visuals,  
> BREAK,  landscape of a [Bus station:Workshop:3], Moon in the night, Confused, Grindhouse, hair light, dark violet color grading, made of Crystal

![00216-2487980662](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/38aacefa-67c6-41d8-a48e-e095e490f000)

> art by Paul Corfield, landscape 
>
> BREAK Renderman,  landscape of a Desolate Talented Prairie  and Hagia Sophia, Foggy conditions, Orphism, Zentangle, fairytaleai <lora:FairyTaleV1s_SD1.5:1>,  
> BREAK, Raw digital photo,  landscape of a Wretched Riften, Clear skies, Movie still, Satisfying, Indirect light, Canon RF, macro lens, extremely hyper aesthetic,  
> BREAK, Rajasthani painting  of a  landscape of a Apocalyptic The Citadel of Minas Tirith, Winter, Detailed illustration, Sad, dslr, Zoom lens, Primary Colors, intricate
 
![00217-2487980663](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/107e7d3b-2d42-4127-8efa-6abb768ab2bc)

> (art by Klaus Janson:1.0), (art by Jessica Drossin:1.0), landscape 
>
> BREAK Redshift render,  landscape of a [Napa Valley|Argentina], Stormy weather, Screen print, waning light,  
> BREAK, Painting,  landscape of a Passionate Lighthouse, Fall, Prehistoricore, F/5,  
> BREAK, Gopro footage,  landscape of a Yellowstone National Park, at Overcast, Masterpiece, Metalcore, F/1.8, Kodachrome
