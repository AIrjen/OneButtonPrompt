# Combining One Button Prompt with IMG2IMG and ControlNET

Since One Button Prompt does nothing more than generate a prompt, means we can combine it with most other tools and extensions available. In this document, I'd like to show you some possibilities of using it with IMG2IMG functionality and ControlNET.
Hopefully this will lead to additional inspiration and new ways to approach these tools.

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
