![OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt/blob/main/images/background.png "These images are auto generated, see all generated prompt below")


---
# One Button Prompt

# Summary

One Button Prompt is a tool/script for Automatic1111/ComfyUI/RuinedFooocus for beginners who have problems writing a good prompt, or advanced users who want to get inspired.

It generates an entire prompt from scratch. It is random, but controlled. You simply load up the script and press generate, and let it surprise you.

It is a full AI prompt generator for Stable Diffusion.

It is best used on all-purpose models, such as Stable Difussion 1.5 or SDXL type models. However, feel free to use it on your personal favorite models.

A simple user guide for first time use and settings is available [here](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/my_first_generation.md).

It is also now available as a custom node for ComfyUI. [Check installation doc here](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/comfyui_integration.md)

More of a Fooocus fan? Take a look at this excellent fork called [RuinedFooocus](https://github.com/runew0lf/RuinedFooocus) that has One Button Prompt built in. [Check some options available here](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/ruinedfooocus_integration.md)

Any other AI tool you are using? Midjourney? Dalle? No problem, I got it working on [a website here](https://airjen.pythonanywhere.com/). Just copy the prompt to your clipboard with a click, and paste it in any image generator tool.


# Features
- __Full prompt generation__ with the click of a button.                  ==> [guide to my first generation](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/my_first_generation.md) 
- Supports __TXT2IMG, IMG2IMG, ControlNET, inpainting and latent couple__.  ==> [guide to IMG2IMG and ControlNET](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/the_next_generation_img2img_and_controlnet.md)
- Save your favorite generation settings with __presets__. ==>  [One Button Presets](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/one_butten_presets.md)
- __Workflow assist__, generate multiple prompts with One Button. Create __prompt variants__ with ease. ==> [guide to workflow assist and prompt variant mode](workflow_assist_and_prompt_variant_mode.md)
- Create __infinite variations__ of a __chosen subject__.                     ==> [guide to override subject](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/override_subject_and_infinite_variations.md)
- Fully __automated generation, classification and upscaling__.           ==> [guide to one_button_run_and_upscale](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/one_button_run_and_upscale.md)
- Add __LoRA's__, customize lists and personal artists choices.           ==> [guide to custom files](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/custom_files.md)
- Use __Anime Model__ mode to generate prompts specific for use with anime/pony models ==> [guide to Anime Mode](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/anime_model_mode.md)
- __Compound__ multiple prompts together for unexpected results.          ==> [guide to prompt compounder](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/prompt_compounder_and_regional_prompter_to_create_insane_images.md)
- Use __wildcards__, or __combine with Dynamic Prompts__ extension                ==> [guide to using wildcards and Dynamic Prompts](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/wildcards_and_dynamic_prompts_extension.md)
- Has a set of __template prompts__ from various sources, __fully wildcarded__ and usable with Subject Override ==> [guide to prompt templates](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/templates.md)
- Has multiple __prompt generation modes__ to choose from ==> [guide to prompt generation modes](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/prompt_generation_modes.md)
- Integration is available with the __superprompt-v1__ model ==> [guide to super prompt](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/superprompt.md)
- Stay in control, and fine-tune One Button Prompt with a __config__ file ==> [config file](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/config_file.md)
- __Flufferize__ your prompt to enhance your results with Prompt Magic

## Important Notice

One Button Prompt had a recent large change in the UI when Presets were introduced. This might be confusing for long time users.

If you are not finding the settings, change the __"One Button Preset"__ to __"Custom..."__.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6d821c82-edf9-4496-867f-ac01dda994cd.png" width="50%" height="50%">

Subtypes are also completely gone now, and integrated into the subject field.

Loading the first time after upgrading on ComfyUI might give some errors, because the fields have shifted. Just set the settings back.

## How to use in automatic1111/SD.next
In TXT2IMG or IMG2IMG, select the script "One Button Prompt".

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b43f7bef-533d-4139-a477-562a0b2d39ca.png" width="50%" height="50%">

Leave the prompts empty:

<img src="https://user-images.githubusercontent.com/130234949/230793068-d38bc782-4c2f-4268-9e91-76f4eabe3eca.png" alt="who needs prompts anyway" width="50%" height="50%">

Hit Generate!

<img src="https://user-images.githubusercontent.com/130234949/230793086-cedbe72a-e1eb-46e5-a425-4a52540847f6.png" alt="click!" width="30%" height="30%">

Enjoy creating awesome pictures:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/aa0ff559-03a9-49be-bbe5-94789f8102a0.png" alt="wow, good job you!">

> stylized by Waterhouse, John Constable, Ed Blinkey, Atey Ghailan, Studio Ghibli, Jeremy Mann, Greg Manchess, Antonio Moro and makoto shinkai, landscape of a Atmospheric (Lazarus Labs:1.1) , from inside of a Furious Stargate, Ultrarealistic, extremely hyper aesthetic

Please be aware, that not each picture will be awesome due to the randomness of the prompt, artist and model used.
You might get an epic landscape, or a photo of an Aggregavated Trout. In my experience, about 1 in 5 is good. Everyone of them is interesting.

Don't get overwhelmed by the options, they will become more clear once you use it more.

For first time users, play around with the set presets.

Some more examples below. And check the first time user guide [here](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/my_first_generation.md).

### Some details
It will generate between 0 and 3 artists, and add those the prompt.

It can generate the following subjects, while building a prompt:

1. object - Can be a random object, a building ,a vehicle, some food or objects from space.  

2. animal - A random (fictional) animal. Has a chance to have human characteristics, such as clothing added.  

3. humanoid - A random humanoid, males, females, fantasy types, fictional and non-fictional characters. Can add clothing, features and a bunch of other things.  

4. landscape - A landscape or a landscape with a building.  

5. concept - Can be a concept, such as "the X of Y", or an historical event such as "The Trojan War".  It can also do a line from a poem or from a song.

It mixes techniques such as prompt switching and hybrids. 

This generator will generate a complete full prompt for you, based on randomness. You can increase the slider, to include more things to put into the prompt. 
Recommended is keeping it around 3-7. Use 10 at your own risk.

There are a lot of special things build in, based on various research. Just try it, and let it surprise you.

Suggestion is to leave the prompt field empty, anything here will be added at the end of the generated prompt.  
It doesn't add anything to the negative prompt field, so feel free to add your favorite negative prompts here.  

For each Batch you run, it will create a new prompt. For each batch size, it will reuse the same prompt.


# Installing in automatic1111
One Button Prompt can be found in the normal installation list of Automatic1111. Go to Extension -> Available and press Load From. In the list you will see One Button Prompt, and press install.
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d98cba69-d249-4f4a-8965-2dd4509dc11c)


If you want to do it manually,sSimply install this from via install from URL. After that you can see OneButtonPrompt in the script fields for txt2img and img2img.
Set the following URL to install from: https://github.com/AIrjen/OneButtonPrompt

<img src="https://user-images.githubusercontent.com/130234949/230917712-60a3c1f4-fea6-4ecd-bc68-da52f1ff86fe.png" alt="Easy to install" width="50%" height="50%">

You can also download the files from github directly, and place them under your automatic1111 installation in the \Extensions\ folder.

# Main tab

The main tab will show preset options, which are preset generation settings which will help achieve good results. On default, it is set to __Standard__, which was the previous default setting of One Button Prompt. It is quite random and give some wild results.

If you are looking for more guided results, choose a different preset. Some good first choices are:

- Standard -> One Button Prompts default. Wild and unpredictable. Good for prompt exploration.
- Unique People Portraits -> Will focus on generating photographic people
- D&D Style Portraits -> Will focus on generating fantasy style portraits
- Consistent Results -> Running on a large set of build in styles, to get consistent results in prompts. Works best on SDXL.
- Greg Mode - The Preset -> Focusses on creating characters, mixed with popular artists (like Greg Rutkowski). Works best on SD 1.5 models.


If you want to change the settings yourself, please change the One Button Preset to __"Custom..."__. This will load in all the settings to be adjusted.


Insanity level. You can increase the slider, to include more things to put into the prompt. Recommended is keeping it around 3-7. Use 10 at your own risk. I usually run it between 5 and 7.

You an use the Subject Types filter to select on main subject types to generate. Maybe you want only Landscapes, maybe you want only people. Select it here.

Artists have a major impact on the result. Automatically, it will select between 0-3 artists out of 3483 artists for your prompt.
You can turn it off. Add your own artists to the prompt, and they will be added to the end of the prompt.

Type of image can be used to force a certain direction. For example when using Realistic Vision, it might be a good idea to set it to photograph. For an anime model, you might want to use "all - anime"

Special image type modes have chance to trigger. Those follow different rules of prompt generation.

When you fill in the Overwrite subject field, that subject will be used to build the dynamic prompt around. It is best, if you set the subject type to match the subject. For example, set it to humanoid if you place a person in the override subject field.
                        
This way, you can create unlimited variants of a subject.

Smart subject tries to determine what to and not to generate based on your subject. Example, if your Overwrite subject is formed like this: Obese man wearing a kimono.                      
It will then recognize the body type and not generate it. It also recognizes the keyword wearing, and will not generate an outfit.

The existing prompt and negative prompt fields are ignored.
                        
Add a prompt prefix, suffix and the negative prompt in the respective fields. They will be automatically added during processing.

These can be used to add textual inversion and LoRA's. They can also be used to add your models trigger words.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/90ac4999-b5f8-4919-bbae-3efe287bc21e)




# Workflow assist tab
This tab is designed to help with the workflow of adjusting and maintaining prompts without turning the extension off.
"Workflow mode" turns off the generated script, and uses the Workflow prompt instead.

Use the prompt variant slider to create variants of the Workflow prompt.

It also has the options to generate a few prompts with a click and send them to the workflow prompt. This way you can search or combine interesting ideas together.
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b06833a4-6de5-4baf-85d6-8a945b8b26e9)


# One Button Run and Upscale
Using the API feature of WebUI, this allows you to:

This will allow you to:
1. Generate an image with TXT2IMG
    1. Can enable Hi res. fix
    2. Possible to set up a __Quality Gate__, so only the best images get upscaled
    3. Possible to ignore the One Button Prompt generation, and __use your own prompts__
2. Upscale that image with IMG2IMG
    1. This proces can be repeated. Loopback enabled.
    2. Supports __SD Upscale__, __Ultimate SD Upscale__ and __Controlnet tile_resample__ methods of upscaling
3. Upscale with EXTRAS
4. Possiblities for __just upscale__ existing images

All with a single press of __One Button__.

[User Guide here!](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/one_button_run_and_upscale.md#one-button-run-and-upscale)



# roadmap
Some ideas I'd like to implement:
- Ongoing: list refinements and new features in the prompt generation
- Ongoing: Documentation and toturials

If you have a good idea or suggestion, let me know, or build it yourself ;)



# Prompts and examples
![00081-1764500323](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e975309c-78bc-468b-980e-2e5445cadfdd)
> video game concept art, 2d game art, concept art, landscape of a Kokiri Forest, it is Tribal, Sun in the sky, designed by Atey Ghailan, detailed, masterpiece, Deathpunk, 35mm, Polychromatic, digital art, contemporary fine detail, stunning, unique, fine detail, aesthetic

![00095-1877749527](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/c140be7b-0857-47de-8610-a91c091d3e83)
> small centered composition, product shot, plain background, wallpaper art, in the center is an image of an epic beautiful ("The Orb of Elegance":1.2) , foliage, at Golden hour, side lit, Colorless, warm light, dynamic dramatic atmosphere, background inspired, dynamic composition, ambient light, fine detail

![00088-1877749520](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d060a48c-41c7-4364-9bdb-80126b170c87)
> colorful art by Norm Rapmund, Fatigued 25 y.o. Girl of [Rot|Music], Comic book art, dynamic, detailed, portrait art by Brian Sum, luxurious sharp focus, highly contrasted, sunny, complex artistic color composition, magnificent, dynamic cinematic color, cool colors, beautiful composition, complimentary colors, beautiful

![00011-4053395104](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6b99aa1b-a54c-4013-9060-a11cb3678c5c)
> Pill Bug, Moon in the night, Barbiecore, Side lighting, 50mm, designed by Ilya Kuvshinov, sci-fi

![00066-1877749498](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e5c9d081-7202-47c6-9195-69cc90c01bbb)
> photograph, buxom Girl, Appealing, dressed in headwear, the Girl has a Pink Angelic Halo, Wide view, Grim, Long exposure, Iphone X, F/5, dreamy, dream, dark, cozy, highly enhanced, intricate artistic color, beautiful elegant, confident, intricate detail

![00017-2787914262](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d53e7aee-72c0-4b27-b8e6-6e08a4bb1b72)
Origami, Anime, Concept art of a Shinto Foliage, Average, it is in a Star Wars setting, Narnia in background, at Dusk, (realism art designed by Agnes Martin:1.0) , natural lighting, Pastel Colors, masterpiece

![00070-3423685499](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/851f39fd-6050-4682-a756-31965313c69a)
>  (by Carne Griffiths:1.2) , Cyborg "Through the lens of poetry, ordinary moments transform into extraordinary tales of the human experience.", nature and River stone background, Bathed in shadows, Monochrome, beautiful, boring, fauna, cool colors, magnificent, modified, radiant, magical composition

![00022-2065006526](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/8e814495-000a-42a2-b39d-6ecd55769c95)
> Suprematism, "Worgen Infiltrator", abstract, limited color palette, geometric forms, Suprematism

![00003-334769067](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/1a7a056f-3a5a-4be4-b756-5e74da472368)
> attractive, Seductive Female Valkyrie, Dark matter background, fairy tale, Abstract Art, feminine

# Thank you
Thank you to the amazing [Stylepile](https://github.com/some9000/StylePile) and [Dynamic Prompts](https://github.com/adieyal/sd-dynamic-prompts) for inspiration.

Thanks to everyone maintaining this [SD artists list](https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit#gid=0)

Thanks to openart.ai for setting up the very helpful [prompt book](https://openart.ai/promptbook)

Thanks to this [ai art modifier guide](https://www.the-ai-art.com/modifiers)

Everyone at the [stable diffusion subreddit](https://www.reddit.com/r/StableDiffusion/) for inspiration and sharing workflows
