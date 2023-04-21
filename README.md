![OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt/blob/main/images/background.png "These images are auto generated, see all generated prompt below")


---
# One Button Prompt

# Summary

One Button Prompt is a tool/script for automatic1111 for beginners who have problems writing a good prompt, or advanced users who want to get inspired.

It generates an entire prompt from scratch. It is random, but controlled. You simply load up the script and press generate, and let it surprise you.

It is best used on all-purpose models, such as Stable Difussion 1.5 or those based on 1.5. Such as [deliberate](https://civitai.com/models/4823/deliberate) and [dreamlike diffusion](https://civitai.com/models/1274/dreamlike-diffusion-10). However, feel free to use it on your personal favorite models.

## How to use in automatic1111
In TXT2IMG or IMG2IMG, select the script "One Button Prompt".

<img src="https://user-images.githubusercontent.com/130234949/230793053-3b1d1b1b-b3c1-4071-a135-35f56dba0f01.png" alt="so easy" width="50%" height="50%">

Leave the prompts empty:

<img src="https://user-images.githubusercontent.com/130234949/230793068-d38bc782-4c2f-4268-9e91-76f4eabe3eca.png" alt="who needs prompts anyway" width="50%" height="50%">

Hit Generate!

<img src="https://user-images.githubusercontent.com/130234949/230793086-cedbe72a-e1eb-46e5-a425-4a52540847f6.png" alt="click!" width="30%" height="30%">

Enjoy creating awesome pictures:

![image](https://user-images.githubusercontent.com/130234949/230916833-0dc38593-94e0-40f5-9312-da720278b791.png "wow, good job you!")
> Concept art, Fluid Biosphere, at Dawn, F/1.8, Kodak portra, extremely beautiful ,

Please be aware, that not each picture will be awesome due to the randomness of the prompt, artist and model used.
You might get an epic landscape, or a photo of an Aggregavated Trout. In my experience, about 1 in 5 is good. Everyone of them is interesting.

Some more examples below.

### Some details
It will generate between 0 and 3 artists, and add those the prompt.

It can generate the following subjects, while building a prompt:

1. object - Can be a random object, a building or a vehicle.  

2. animal - A random (fictional) animal. Has a chance to have human characteristics, such as clothing added.  

3. humanoid - A random humanoid, males, females, fantasy types, fictional and non-fictional characters. Can add clothing, features and a bunch of other things.  

4. landscape - A landscape or a landscape with a building.  

5. concept - Can be a concept, such as "the X of Y", or an historical event such as "The Trojan War".  

It mixes techniques such as prompt switching and hybrids. 

This generator will generate a complete full prompt for you, based on randomness. You can increase the slider, to include more things to put into the prompt. 
Recommended is keeping it around 3-7. Use 10 at your own risk.

There are a lot of special things build in, based on various research. Just try it, and let it surprise you.

Suggestion is to leave the prompt field empty, anything here will be added at the end of the generated prompt.  
It doesn't add anything to the negative prompt field, so feel free to add your favorite negative prompts here.  

For each Batch you run, it will create a new prompt. For each batch size, it will reuse the same prompt.


# Installing in automatic1111
It can be used in automatic1111. Simply install this from via install from URL. After that you can see OneButtonPrompt in the script fields for txt2img and img2img.
Set the following URL to install from: https://github.com/AIrjen/OneButtonPrompt

<img src="https://user-images.githubusercontent.com/130234949/230917712-60a3c1f4-fea6-4ecd-bc68-da52f1ff86fe.png" alt="Easy to install" width="50%" height="50%">

You can also download the files from github directly, and place them under your automatic1111 installation in the \Extensions\ folder.

# Main tab

Guide your prompt here. You can increase the slider, to include more things to put into the prompt. Recommended is keeping it around 3-7. Use 10 at your own risk. I usually run it between 5 and 7.

You an use the Subject Types filter to select on main subject types to generate. Maybe you want only Landscapes, maybe you want only people. Select it here.

Artists have a major impact on the result. Automatically, it will select between 0-3 artists out of 3483 artists for your prompt.
You can turn it off. Add your own artists to the prompt, and they will be added to the end of the prompt.

Type of image can be used to force a certian direction. For example when using Realistic Vision, it might be a good idea to set it to photograph. For an anime model, you might want to use "Anime key visual"

If you write anything in the prompt field, it will be added to the generated prompt. You can select where it goes, in the front or at the back. Users have been using this to add their own LoRA's or textual inversions. You can also add your own artists here if wou'd like, or anything else you want to have control over.

![image](https://user-images.githubusercontent.com/130234949/233621990-ebbab403-86dd-4764-8448-26ab5729a7e9.png)


# Workflow assist tab
I've added a Workflow assist tab in a recent update.

This tab is designed to help with the workflow of adjusting and maintaining prompts without turning the extension off.
"Workflow mode" turns off the generated script, and uses the Workflow prompt instead.

This part is still being developed, to have a better UI.

It also has the options to generate a few prompts with a click and send them to the workflow prompt. This way you can search or combine interesting ideas together.
![image](https://user-images.githubusercontent.com/130234949/233644374-22e2bf6e-da4c-46b7-a248-9c623adc0b99.png)

# Advanced / prompt compounder
On the advanced tab, there is the option to compound multiple generated prompts together. It is set to 1 for normal behavior, a single prompt. You can up this, for interesting results.
![image](https://user-images.githubusercontent.com/130234949/233619883-17f58277-d536-4682-bb69-7c86d4a0b1bd.png)

There is however, some tricks build into this, for use with the [Latent Couple](https://github.com/opparco/stable-diffusion-webui-two-shot) extension. Using setting the seperator to "automatic AND" and the Prompt compounder equal to the amount of latent spaces, you can combine interesting things together.

Example here with 3 different landscapes combined together in a single image.
![00066-4269117636](https://user-images.githubusercontent.com/130234949/233621427-495d3eae-b58e-4f2c-87de-35e51c455e68.png)

>art by Nathan Spoor, landscape
>
>AND art by Nathan Spoor, landscape, Unreal Engine, Lively France, Thunderstorm, Rough sketch, Reflected light
>
>AND art by Nathan Spoor, landscape, Spellbinding Straw caverns, at Golden hour, Mandala, octane engine
>
>AND art by Nathan Spoor, landscape, Refreshing Death Valley National Park and Frustrated Aircraft carrier, Bathed in shadows, Detailed illustration, Lustful

If you want more control, use "current prompt + AND". An example would be "Art by brandon woelfel, 2 people" and setting the subject type to humanoids. This will automatically form the prompt for use with latent couple:

![00040-2515550298](https://user-images.githubusercontent.com/130234949/233620894-55357483-64d4-4185-8c45-ae27f26d8eb1.png)
>art by brandon woelfel, 2 people 
>
> AND art by brandon woelfel, 2 people, Studio shot of a Repugnant Woman, wearing Exhausted Mauve Boyfriend blazer and skinny jeans, Dark hair styled as Straight, Cat Ears, Modern Art, hair light, F/8, Mono Color
> 
>AND art by brandon woelfel, 2 people, Abstract, selfie shot angle of a 1920's Nasty slight Michelle Yeoh surrounded by Grapefruits, Blonde hair styled as Short and messy, glowing Turquoise eyes, Anime screencap, Panfuturism, Magic the gathering, photolab, High quality

# off-hands, automatic generation
This project started out as a personal project, to automatically generate windows wallpapers. The code is still in here, and can be used. You would need to set it up correctly, so it is for advanced users only.

In the main.py script, there is logic that calls the API's from automatic1111. Uncomment the lines you need, such as txt2img. You also need to create some folders on your computer (see code)
Start automatic1111 with the option --api and run the main script.
Edit the main script to set the amount of loops/images to generate, and uncomment the txt2img, img2img and upscale scripts to taste.

It was build for personal development, so adjust directories and settings accordingly.

# roadmap
Some ideas I'd like to implement:
- Better workflow management in workflow assist tab
- Curated artist lists
- SD 2.1 support (inversion negative prompt)
- Ongoing: list refinements and new features in the prompt generation

If you have a good idea or suggestion, let me know, or build it yourself ;)

# prompts and examples
From the above header, these are the generated prompts, from left to right, top to bottom. Generated during various stages of development. Using deliberate and DPM Karras.

>cinematic shot of a Cruel " The Soul of Enlightenment ", at Blue hour, Cel shaded 

>( art by Albert Dubois-Pillet :0.9), art by Bastien Lecouffe-Deharme, Physically based render, Tranquil Delicate Island and Windmill, at Golden hour, Illustration, Amusing, Fish-eye Lens 

>art by Aykut Aydogdu,art by Jacob van Ruisdael, 3D Rendering, extreme wide shot of a Wraith, Crusader ,wearing Floral maxi dress and sandals, background is Strait, Illustration, Modern European Ink Painting, loop lighting, octane engine 

>art by Gaston Bussière, Photograph, Cottage Progressive Era Tokyo, Orange and Pink hue

>art by Jeffrey T. Larson, Tired Illuminating The Misty Mountains and The River Styx, at Dusk, Vaporwave Art, Rembrandt lighting 

>art by Jon Foster,art by Ricardo Bofill, extreme wide shot of a " The Industrial Revolution ", background is Appalachian, tilt shift, New Wave Art, Mono Color 



>( art by Peter Saville :0.7), Layered paper art of a Irritated Airy Blueberry, Screen print, hair light, Depth of field 270mm, Kinemacolor 

>( art by Jessie Arms Botke :1.1), ( art by Juan Carreño de Miranda :1.2), ( art by Cerith Wyn Evans :1.2), [ birds-eye-view shot of a Belle Époque portly Tyra Banks cosplaying as Spider-Man, Hosting parties ,wearing Industrial Turquoise Gator skin Tank top and denim skirt, Black hair styled as Space buns, Scarf, background is The Gobi Desert, at Starry night, split diopter, Realistic, Autochrome ::8]

>art by Art Spiegelman, Unsightly The Badwater Basin and Stonehenge, Sunny, Ultrarealistic, Psytrance Art, Mono Color 

>art by Gerhard Munthe, Long shot of a Classical midweight Asian Chris Hemsworth riding a Koala, Brown hair styled as Short and messy, background is The Palace of Asgard, natural lighting, Low shutter, Film Washi 

>art by Peter Eisenman, Vector Art, Serene The Garden of Eden, Stormy weather, Movie still, Peaceful

>( art by Hans Zatzka :1.3), Aquatint of a Compelling Dubrovnik, at Sunrise, Illustration, Orientalism Art, Black lighting, overhead angle 


>art by Guillem H. Pongiluppi, F/1.8 of a " The life of Saint Barbara of Nicomedia ", at Starry night, shallow depth of field, Movie still, Frightening 

>art by Jeffrey Smith, close-up shot of a Victorian Bulgarian Kitchen timer, background is The Grand Canyon of the Yellowstone, Spring, Sketch, Peaceful, natural lighting, Calotype 

>art by Helen Allingham,art by Étienne Maurice Falconet, Water color painting, Circular polarizer of a Mayan Revival Dominican Female Dragon rider, Auburn hair styled as Messy bun, at Sunrise, deep focus, Sad 

>art by Sparth , Spanish Golden Age Tranquil The Angel Oak and Liverpool , Foggy conditions , Screen print , Ukiyo-E , Provia 

>by artist Michael Craig-Martin, by artist John Lurie, Zoon lens of a Rustic Fatigued portly Blue Jay, background is Indonesia, Relieving, Mono Color

>by artist Brandon Mably, Vector Art, extreme wide shot of a Aggravated Invigorating Fijian snake at Stormy weather, FOV 90 degrees, Vaporwave Art, flat lighting, High Contrast


# More prompts and examples

![efa94f2f-2bb8-4484-9855-ebd2600f8092](https://user-images.githubusercontent.com/130234949/232003239-3d983bf1-df26-4450-bf71-2b3bfe23ccbd.png)
> (art by Daniel Lieske:1.3), Spray paint style, Noble Rustic The Hanging Gardens of Babylon and Cafe, at Dusk, Masterpiece, Shameful, Academism, Lens Flare, Fujifilm Superia, UHD

![c25eb65a-0656-4a8a-a436-60bff4d6bd84](https://user-images.githubusercontent.com/130234949/232003386-933cfc7b-ed49-4aee-bbd4-66cdacf80efc.png)
> [art by Max Bedulenko| art by Jack Davis], Spray paint style, Vile Mecha Spit, at Starry night, F/5, psychedelic colors, 8K
 
![d5c2ace0-1aac-4512-9006-7431fe57fbb4](https://user-images.githubusercontent.com/130234949/232003478-0bf98902-7c57-4ca7-b821-c70d6c5488f9.png)
>close-up shot of a Cozy Falcon, Summer, Bokeh, Sketch, Lonely, Pop Art, Black lighting, Fish-eye Lens, Calotype, Magic the gathering, layered textures, [(art by Yasushi Nirasawa :0.8),(art by Rumiko Takahashi :1.3), art by Carl Barks :7], 

![00016-3511975148](https://user-images.githubusercontent.com/130234949/232003763-32d4aa2e-eb95-4edf-b0a9-2afc501b5628.png)
> [(art by Walter Quirt :1.2):(art by Arthur Dove :1.0):8], Renderman, Hideous The Eyrie of House Arryn and Imp-drawn carriage, at Starry night, Detailed illustration, Bloom light, 80mm, Film grain


![b7287807-efd3-4d0e-98b8-1fb1d7e57757](https://user-images.githubusercontent.com/130234949/232003927-ec8ed961-6f47-4aa0-ba55-a12f92c21cfe.png)
> by artist Sam Spratt, by artist Robert Hagan, by artist Mike Kelley, Painting, landscape, wide shot of Cavern, Screen print, Lonely, Neo-Fauvism

![00007-3666399242](https://user-images.githubusercontent.com/130234949/232004618-e0407158-fa5d-46aa-97b5-33990fc8d382.png)
> Vector Art, high angle shot of a Dreadful Anime "The Fukushima Disaster", Disgusting, Methaphysical painting, studio lighting, F/5, Mono Color, behance, [(art by Hans Zatzka :1.1),(art by Alexandre Jacovleff :1.0)::13], ,

![00033-437599208](https://user-images.githubusercontent.com/130234949/232122501-1eec6247-b4cd-4f75-b4ad-0a6094dd4b39.png)
> Long exposure of a Ignorant Light Klingon cosplaying as Princes Leia Organa, with Pink skin, Sitting with elbows on knees, Gloves, background is Landfill, at Nighttime, Happy, Grayscale, extremely detailed CG Unity 8k wallpaper, (art by Paul Hedley:1.1), art by Giacomo Balla , (art by Andre Norton:1.1)

![3e04863e-2627-4e93-9596-fb0d43416b99](https://user-images.githubusercontent.com/130234949/232122614-73bb655d-c0f3-421d-a640-69219db18fa7.png)
> art by Marianne North, Cozy Botanical garden and South-American The Alhambra, Thunderstorm, Detailed illustration, Private Press, Light caustics, Circular polarizer, Swirling Polyester, Light streaks, absurdres, trending on artstation

# Thank you
Thank you to the amazing [Stylepile](https://github.com/some9000/StylePile) and [Dynamic Prompts](https://github.com/adieyal/sd-dynamic-prompts) for inspiration.

Thanks to everyone maintaining this [SD artists list](https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit#gid=0)

Thanks to openart.ai for setting up the very helpful [prompt book](https://openart.ai/promptbook)

Thanks to this [ai art modifier guide](https://www.the-ai-art.com/modifiers)

Everyone at the [stable diffusion subreddit](https://www.reddit.com/r/StableDiffusion/) for inspiration and sharing workflows
