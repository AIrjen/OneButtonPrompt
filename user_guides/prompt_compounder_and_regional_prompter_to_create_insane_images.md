![00172-216086968](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e5bb6bc0-ba9a-4d4a-9e14-913860c74c26)
Note: all images on this pages were generated with the [DiffusionBrushEverything model](https://civitai.com/models/46294/diffusion-brush-everything-sfw-nsfw-all-purpose-checkpoint-nuclear-diffusion-anime-hybrid). I feel like this model is not getting enough appreciation.

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

# Creating insanity with Regional Prompter
Using the "Twod-2-1" preset, and setting One Buttom Prompt to generate all kinds of things, we can get really fantastical results.

These examples are all generated at 1200x1200 (who needs hi. res fix anyway).

For One Button Prompt main settings, I let it generate everything, I want to create some insanity:
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/920a8890-a2e1-416f-a808-641567ed4c95)


For Regional Prompter, I load up the __"Twod-2-1"__ Preset, and then enable __"Use common prompt"__, and set the __Base Ratio to '0.4'__. 

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/c16927d3-1266-4546-94ff-f19499f8764b)

For the Prompt Compounder settings:

__Prompt Compounder__ to 3, we have 3 areas to be filled in. So we want 3 seperate prompts.

We set the __Prompt seperator__ to "BREAK". The Regional Prompter wants each prompt to be seperated by the BREAK keyword, this is how we do it.

Lastly, we set the __Prompt seperator mode__ to "automatic". This is where the magic happens. It will now generate the "common prompt" we enabled before, which consists of an artist and the type of image we would like to create. It will also disable any other artists generated in the normal prompts.
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/00f758d7-488a-4432-8746-c96e4bf34c6b)

Here are some examples it generated:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f2aa9e5f-62cc-45d0-920b-ff777637e355.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/48682cb0-7bb6-4a54-ba12-c960dc9443b2.png" width="30%" height="30%">

> (art by Mary Blair:1.2) 
> 
> BREAK Studio shot of a Layered Hip-Hop mozzarella smooth, background is [supermarket|Water treatment plant], at Nighttime, FOV 90 degrees, Overdetailed art, Disgusting,  
> BREAK, Oil painting, selfie shot angle of a Smart Unnatural chocolate cake Purple patterns, at Midday, tilt shift, Screen print, Health Goth Art, Kinemacolor, opulent, fairytaleai <lora:FairyTaleV1s_SD1.5:1>,  
> BREAK, Cycles render, top-down view of a Fiery Space Age Purse Mohair frame, detailed with Crystal Terrible patterns, Annoyed background, Light, Colorless, sfumato, masterpiece
>
> art by Li Shuxing 
> 
> BREAK Redshift render, side view shot of a Friendly Mesmerizing Costa Rican Footbridge, Movie still, backlight, Fish-eye Lens, Plain white background, ghibli style  <lora:studioGhibliStyle_offset:1>,  
> BREAK, Renderman, full shot of a Petrified Melancholy "The Base of Hope", horizon-centered, Suffering, spotlit,  
> BREAK, Fashion shot of a Enchanting Ugandan Rocking chair, Beige and Rainbow background, Horror, soft light, Circular polarizer, rich color

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7bba1a0b-26df-4e7f-8f69-0b1b5e440eed.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/65f7e0b0-5eef-4982-b213-81103833f634.png" alt ="So, this happened" width="30%" height="30%">


> art by Tintoretto, (art by Frank Weston Benson:0.9), (art by Horst P. Horst:0.9) 
> 
> BREAK Cycles render,  landscape of a Energetic The Crown of Thorns  and Grain elevator, Moon in the night, Light, cinematic lighting, Fujifilm Superia,  
> BREAK, Octane render, extreme close-up shot of a Furious Giant sequoia tree, from inside of a Rusty Taj Mahal, at Nighttime, Aestheticism, Motion blur, Vivid Colors, octane engine,  
> BREAK, Digital artwork, close-up shot of a Homey Mackerel, Winter, soft focus, Crowcore, Nostalgic lighting, F/2.8, Warm Colors, ghibli style  <lora:studioGhibliStyle_offset:1>

> (art by Hiroshi Katsuragawa:1.3), (art by John Mckinstry:1.2), (art by Dave Coverly:1.0) 
> 
> BREAK Octane render, Landscape of a Geeky "The Eye of Hope", Winter, Relaxed, volumetric lighting, Dark hue, Lime green paint splotches, Swirling, vectorstyle <lora:vectorL:1>, in the style of 0mib  <lora:0mib3(gut auf 1):1>,  
> BREAK, wall Graffiti, top-down view of a Invigorating Prehistoric Jennifer Aniston, Lumberjack, Sketch, Sad, excessivism, Direct light, Infrared, contest winner, <lora:epiNoiseoffset_v2:1>,  
> BREAK, shin-hanga  of a Doubtful Techno Female Mage slayer, Psychotic Red hair, Masterpiece, Relaxed, Anime, 800mm lens, pixiv

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f5883812-44db-4473-bd6c-bc84db112d28.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7ee19414-3e6e-42ab-afb5-1bfd221031ab.png" width="30%" height="30%">

> (art by Bruce Pennington:1.2),art by Ron English 
> 
> BREAK modelshoot style shot of a Deafening "The Rwandan Genocide", Bathed in shadows, 800mm lens, extremely hyper aesthetic, highly detailed, <lora:epiNoiseoffset_v2:1>,  
> BREAK, Airbrush painting, aerial shot of a Natural Wet "The Great Flood", from inside of a Overpass, Regret, Bimbocore,  
> BREAK, Full length frame of a Smart large Daedra surrounded by Paper clipss, ðŸ™, Light hair styled as Pixie, at Sunrise, Side lighting, Spirals, National Geographic

> (art by Jeremy Caniglia:1.0), (art by Nicholas Hughes:0.7) 
> 
> BREAK Technical illustration,  landscape of a Odious Seductive Temple  and Bed and breakfast, at Nighttime, Graphic novel, Bronzepunk, F/5, Monochromatic Acid colors filter,  
> BREAK, eye-level shot of a Arcane "Reign of Catherine the Great", 50s Art, 80mm, Saturated, Bright design, <lora:epiNoiseoffset_v2:1>,  
> BREAK, side view shot of a Award-Winning Wasp, Foggy, dtx, Zoom lens, Elegant, dark indigo and DayGlo green splash

# Two shot method with selected artist
Another trick, is to create a "two shot" with multiple different people. In this example, I am using a selected artists, namely Brandon Woelfel, which creates awesome photographs.

Please note, that this doesn't always add two people in the shot, but at least it tries.

I am running these in a 1024x512 resolution. You can also try using a model that supports better realistic photographs.

For One Button Prompt settings, I set the following:

__Subject Types__ to "humanoid", __Artist__ to "none", __type of image__ to "photograph"

__prompt prefix__ to "art by brandon woelfel, two people"

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/207bec77-75f5-408c-b294-f5017647506d)

Regional Prompter has the following settings:

For Regional Prompter, __Divide Ratio__ to "1,1", __Split mode__ to "Horizontal", and then enable __"Use common prompt"__, and set the __Base Ratio to '0.7'__. 
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/5e6e1064-eb75-414f-91fb-1dec815427c2)



For the Prompt Compounder settings:

__Prompt Compounder__ to 2, we have 2 areas to be filled in. So we want 2 seperate prompts.

We set the __Prompt seperator__ to "BREAK". The Regional Prompter wants each prompt to be seperated by the BREAK keyword, this is how we do it.

Lastly, we set the __Prompt seperator mode__ to "prefix AND prompt + suffix". In this case, the prefix field is used as our "common prompt". So here we put in earlier "art by brandon woelfel, two people"

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d913eea8-7eee-40fe-9c44-5271bab24f86)

Here are some examples, running with these settings:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2703ca9e-88c2-40d3-b440-3738b244e5b8.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ad37eabd-4422-44e3-8a9f-393b221aebd9.png" width="30%" height="30%">

> art by brandon woelfel, two people 
> 
> BREAK photograph, Sharp focus of a Irritated midweight Maria Sharapova, wearing Complementary [Helmet|Evening wear], Movie still, Evil, Fauvism, Kodak gold 200, 50mm, Agfacolor, layered textures, pixelart <lora:Pixhell_15:1>,  
> BREAK,  photograph, shot from behind of a 1900'S Shaky Belle Époque Male Theurge, Cozy Rainbow hair, at Sunrise, Shameful, Gel lighting, Hasselblad, Zoom lens, Kodachrome
>
> art by brandon woelfel, two people 
> 
> BREAK photograph, ground level shot of a Inviting Man, Battle pose, Fruit-Flavored Handlebar mustache, Handlebar mustache, Goatee, at Sunset, Rough sketch, Post-Punk, Lens Flare, film camera, Depth of field 270mm, Cold Colors,  
> BREAK,  photograph, 3/4 view of a Smart Bohemian Nymph, Directing a TV show, Flustered, animecore, Canon 5d mark 4, 800mm lens, Warm Colors

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b06b3914-497d-4634-bcd3-91ebd14bf9f3.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/08f903ee-7c8f-4e2b-8023-b53dd4c39601.png" width="30%" height="30%">

> art by brandon woelfel, two people 
> 
> BREAK photograph, aerial shot of a Hospitable flyweight Tudor Male Explorer, Cel shaded, Amusing, Canon R5, telephoto lens, in the style of 0mib  <lora:0mib3(gut auf 1):1>,  
> BREAK,  photograph, overhead angle of a Rubbery Gaelic Neptune, wearing Opal deep yellow Mini dress, S-shape pose, Side swept hair, plain DayGlo orange background, Simple illustration, Grim, Mythpunk, natural lighting, Kodak portra 800, F/2.8, Ektachrome, photolab

> art by brandon woelfel, two people 
> 
> BREAK photograph, High exposure of a Ludicrous skinny Hong Konger girl, Spice merchant, Jumping, Brown hair styled as French twist, background is St. Patrick's Cathedral, at Dawn, Amusing, Mingei, Moonlight, dslr, Selective focus, Highres,  
> BREAK,  photograph, selfie shot angle of a Shabby Chic Golden Age Female Biologist, Sketch, Evil, Sun Rays, Canon R5, F/8, Colorless hue

