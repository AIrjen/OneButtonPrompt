# Combining One Button Prompt with IMG2IMG and ControlNET

Since One Button Prompt does nothing more than generate a prompt, means we can combine it with most other tools and extensions available. In this document, I'd like to show you some possibilities of using it with IMG2IMG functionality and ControlNET.
Hopefully this will lead to additional inspiration and new ways to approach these tools.

In these examples, I am all using the [deliberate](https://civitai.com/models/4823/deliberate) model.

I've set the Sampling method to "DPM++ SDE Karras", Sampling steps to "30" and used the standard CFG Scale "7",

## Generating skulls with IMG2IMG

In this example, I'm using a picture of a skull found on the internet. I'm using this one, since it has loads of background noise, which can create interesting stuff.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/11ac825c-0fe2-43cb-87b4-9a6178c26bc2.png" width="30%" height="30%">

I load up this image in IMG2IMG. I kept the Denoise strength at 0.75 for this example.

In One Button Prompt, I use the following settings:

As a __"Subject Type"__ I select __"object"__, because we are generating a skull, and a skull is an object. At least, from One Button Prompt's perspective.

For __"Artists"__ I select __"all"__. I want to get surprised, so I leave this to all.

As __"Type of image"__ I select __"portrait"__, so that it will always default to a portrait image. Since we want a close up of the skull, that matches the picture.

As the __"Subject override"__ I write down __skull__, so it will start generating skulls. If you want, you can change this to something else, or leave blank for interesting results.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f490c699-8cfb-4913-8519-05d19780bb56)

Example output images:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9b533d89-3430-4bf0-896c-330bcfebda6b.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b342011d-763f-4eb8-9955-ebc8fcb43f8d.png" width="30%" height="30%">

> portrait,close up of a Baroque skull, designed by Lamborghini, floating in space, Golden ratio, plain deep yellow background, at Twilight, Ultrarealistic, Golden ratio

> portrait,close up of a Authentic Chinoiserie skull, dark orange and Orange background, Berlin Secession, Rembrandt lighting, Desaturated, made of Concrete, masterpiece

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bc5927bf-4ee3-4d72-85ed-08a6c687f7a4.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e1ce4fde-3e47-4928-a7c5-0af6ad165e49.png" width="30%" height="30%">

> art by Gail Simone, portrait,close up of a Visually Stimulating Visually Stimulating skull, Sharp details, [garden|jungle], at Sunrise, telephoto lens

> art by Kim Keever, portrait,close up of a Enthralling Tang Dynasty skull, Happy

## Generating Stormtrooper helmet based images with ControlNET
In this case, we are going back to using TXT2IMG. Please note, that most of these images came out amazing. You can use this trick to win almost anything on \r\sdbattles\

I've configured ControlNET to use this Stormtrooper helmet:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/03308730-a63e-4498-83e5-a35a0b7f8f16.png" width="30%" height="30%">

I've set it to use the __"Depth"__ ControlNET model. In this case I'm using __"depth_midas"__, this is what it defaulted to.

I've set __"Ending Control Step"__ to __0,75__, meaning that ControlNET will stop doing it's thing 75% through all steps.

I'm using the setting __"My prompt is more important"__

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6a2ea3f4-c398-4be3-b3f4-4b58a58b9505)

I've set up One Button Prompt to the following settings:

As a __"Subject Type"__ I select __"object"__, however, you could try __all__ to get even wierder results.

For __"Artists"__ I select __"all"__. I want to get surprised, so I leave this to all.

As __"Type of image"__ I select __"all"__, more surprises in store for us.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2b769bd4-e8fa-4346-9751-4298f6161518)

Example images:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/41155745-41d9-4e43-b11a-3c3cc8b121d7.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e9e1e341-256a-4b1e-8768-8bdd05afe7bf.png" width="30%" height="30%">

> art by Kazuo Oga, Golden ratio, Obscene hypercar, concept art, from inside of a Elite Dalaran, Summer, Grim, Auroracore, Sun Rays, Kodak Ektar

> Cycles render, Messy Ecuadorian Volkswagen of Guilt, concept art, Funk Art, bloom, art by Shepard Fairey

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/17441442-5a89-46dd-95e2-a8f22f1baa79.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2aafbd76-93f8-49a6-8161-f418675a5428.png" width="30%" height="30%">

> art by Alejandro Burdisio, (art by Alex Schomburg:1.0), voxel art, Alluring Entrancing Castle of Haste, smooth, Folded street, Lens Flare

> art by Vanessa Bell, (art by Jhonen Vasquez:1.0), grand Octane render, Unpredictable Taiwanese Snow plow, intricate details, Smug, Reflected light, matte, Bright design

## Reverse inpainting of Pedro Pascal

One Button prompt can also usefull in inpainting tasks. In this example, I'm going to do what I like to call a "reverse inpaint". This time on the face of Pedro Pascal. Note that this trick will also work on your own face.

First I load up the foto of Pedro Pascal in the Inpaint tab, and then I paint over his face. It doesn't have to be perfect.

Make sure to turn on __"Inpaint not masked"__ so that we replace everything but his face.

I've set __padding__ to __"64"__ and __mask blur__ to __"8"__. __Denoising strength__ is set to __"0.7"__.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6aa6519d-9c6f-4585-9759-4eb77a9ed757)

I then load up an inpainting model. Because we are using a photo, I am using the realisticVision inpainting model for this example.

For One Button Prompt, I set the following settings:

As a __"Subject Type"__ I select __"humanoid"__

For __"Artists"__ I select __"portrait"__. This way we get artists to create portraits, which is what we want in this case.

As __"Type of image"__ I select __"all"__, more surprises in store for us. We could use __Portrait__ here as well.


Example results:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/3a1bda43-cb16-4aa4-9b43-728de8cec095.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f5d09f3f-184f-42d8-b552-62e5a1bb8cfb.png" width="30%" height="30%">

> Delicate diane lane, Exploring new places, Platinum hair styled as long straight, Glittering Persian cat face paint, Smooth No makeup, Foggy, split diopter, Ultra Detailed, Embarrassing, L USM, Golden ratio, inticrate details, hyperdetailed

> art by Roy Lichtenstein, Redshift render, Fallacious, Vengeful Noble well-endowed Male Actor, Heavenly Blonde hair, Thunderstorm, Lonely, MinecraftCore

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9656b7bf-d2da-41b1-ae7e-683930d588fe.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/1b616147-6a3b-40b2-bcbd-d5c17796d654.png" width="30%" height="30%">


> art by Rebeca Saray, Infected Inventive Dragonkin, ðŸ™, wearing Striped Satin Pleated skirt and tucked-in blouse, Tang Dynasty Earrings, plain Gold background, horizon-centered, Neo-Fauvism, Direct light, masterpiece

> Jagged stocky Indonesian Father, Exploring new places, Layered cut hair, Pixiecore, 800mm lens, Warm Colors, 8K

### Thank you

Hope to have give you some inspiration on where you could use One Button Prompt as well, in unexpected ways. Your creativity is what unlocks it's power.
