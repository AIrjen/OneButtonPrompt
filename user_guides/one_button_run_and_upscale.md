# One Button Run and Upscale
An extensive new feature of One Button Prompt.

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

## How does it work?
It works by using various calls of the WebUI API and calling them with the correct parameters in the correct order.

## Requirements
The basic requirement, is that WebUI is started with --api enabled. To do so, go into your webui-user.bat file in the WebUi folder, and add --api to the line with set COMMANDLINE_ARGS
For example, this is how my file looks like.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7b118872-8584-454b-93e4-b8e522cab290)

After you have made your changes, restart WebUI with webui-user.bat

### Optional requirements
#### Quality Gate
To be able to use the Quality Gate functionality, you need to install the following extension into WebUI:

[image-scorer](https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer)

You can install this via the "Install from URL" option in WebUI

#### Ultimate SD Upscale
To be able to use Ultimate SD Upscale, you need to have that installed. It can be found here:

[Ultimate SD Upscale](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111)

You can install this via the "Install from URL" option in WebUI

#### ControlNET 1.1 and Tile_resample
To be able to use ControlNET 1.1 and the tile_resample method, you need to install both.

[ControlNET](https://github.com/Mikubill/sd-webui-controlnet)

[Tile model](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11f1e_sd15_tile.pth)

Here is an extensive [guide on civitai](https://civitai.com/models/59811/4k-resolution-upscale-8x-controlnet-tile-resample-in-depth-with-resources)

Here is a [youtube video guide from Olivio Sarikas](https://www.youtube.com/watch?v=zrGLEgGFJY4)

## Image locations
One Button Prompt uses its own locations and filenaming convention.

Go to your WebUI installation folder and then \extensions\onebuttonprompt\automated_outputs\

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/4bbea176-0b8a-476e-b70a-48775b2875b9)

Here you should see the One Button Prompt folder structure.
1. txt2img -> txt2img results from One Button Run are stored here.
2. promps -> txt2img prompts and parameters used are stored here.
3. img2img -> img2img results from One Button Run are stored here. With loopback enabled, they are overwritten when loopback is done.
4. extras -> extras results from One Button Run are stored here.
5. upscale_me -> Place images here for using "just upscale" mode.

When using One Button Prompt to generate the prompt, the subject will be part of the name.

Here are some examples, so you can quickly identify the different pictures.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/774584aa-f9b5-4e42-9816-b459f7313b7a)


## One Button run tab and options explained

### TXT2IMG
Important to note, is that the TXT2IMG prompt generation process works with the options set in the Main, Workflow Assist and Advanced tabs. 

So you can set up any specifics you want for the prompt generation first.

There are some general options to set first.

URL -> This should be the URL used by WebUI (see your webbrowser). This is standardly http://127.0.0.1:7860

Amount of images to generate -> How many times should it repeat the entire process. So how many images to generate and upscale

Don't generate, only upscale -> Place images in the /upscale_me/ folder, when enabled, it will skip the TXT2IMG part, and will start batch upscaling the images with the set parameters

model to use -> Select which model to use during generation. "Currently Selected Model" meand the model you have loaded right now. "all" means a random model (not inpainting models). Or select a specific one.


For TXT2IMG most options should be familiar. I will here explain some of the additions and changes.


Size to generate:

1. all -> picks randomly between portait, wide and square
2. portait -> 512x768
3. wide -> 768x512
4. square -> 512x512
5. ultrawide -> 1280x360 (Don't worry, this one is just for me, and won't be used when picking "all")

Sampler:

Added option for "all", picks randomly

Hirex upscaler:

Added option for "all", picks randomly

Added option "automatic", sets Upscaler and Denoise Strength based on prompt. Example, if the prompt contains anime, it will try to use the anime upscaler.


![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2a397d4c-e7bd-4d00-a949-063cecb30af4)

#### Quality Gate
Idea and inspired by xKean. Such an awesome addition.
See requirements above.

When enabling Quality Gate, it will repeat the above TXT2IMG process until:
- an Image reaches the Quality Score
- we have reached the amount of tries

When an image reaches the quality score, all other images are removed. It will then continue with the quality image.
If we reach the amount of tries, it will pick the image with the highest score. All other images are removed. It will then continue with the highest quality image.

### IMG2IMG
Again, most options should be familiar for using IMG2IMG when upscaling. It defaults to using "SD Upscale" method which is included in WebUI standardly.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/59756d2b-4e97-41b3-accb-ffa603b07152)


