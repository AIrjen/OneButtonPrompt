# One Button Run and Upscale
An extensive new feature of One Button Prompt. One Button goes brrrr.

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
Enable "Upscale image with IMG2IMG" to actually turn this on.

Amount times to repeat upscaling with IMG2IMG (loopback) -> This controls the amount of times to use IMG2IMG to upscale.

I will describe some of the changes from normal.

model to use -> Select which model to use during generation. "Currently Selected Model" meand the model you have loaded right now. "all" means a random model (not inpainting models). Or select a specific one.

Note that you can have a different model selected here, than used in the TXT2IMG process.

Sampler:

Added option for "all", picks randomly

Upscaler:

Added option for "all", picks randomly

Added option "automatic", sets Upscaler and Denoise Strength based on prompt. Example, if the prompt contains anime, it will try to use the anime upscaler.

adjust denoise each img2img batch -> Adds or subtracts this amount of denoise, during each IMG2IMG batch. Usually you want a lower denoise when upscaling larger images.



![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/59756d2b-4e97-41b3-accb-ffa603b07152)

#### Use Ultimate SD Upscale script
Turn on "Use Ultimate SD Upscale script instead" to use Ultimate SD Upscale. You need to have that extension installed, see requirements above.

Here, all options from Ultimate SD Upscale are available.

It uses img2img padding for the padding.
It will always be set to "Scale from image size"

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/23ad556a-4e53-462b-90ab-d8d5ff9e2302)


#### Controlnet tile resample
Best used in combination with Ultimate SD Upscale and the 4x-UltraSharp upscaler, however you can use it with the normal SD Upscaler as well.
The controlnet tile model name is filled in for you, but if a later or newer version comes out, you might have to change this to that specific one. Current version is "control_v11f1e_sd15_tile [a371b31b]"

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9ec27d75-a559-4b13-9a3c-60c5382117ba)

There is also a option for "also enable wierd blocky upscale mode". This was a bug I found during development, but brought in as a feature. Best used with 4x-UltraSharp upscaler and a decent denoise (0.7-0.8).

Here is an example result, so you can see what to expect.

![20230510220750_City](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b8bc0544-62f2-428e-9f1a-6d42063c3518)

## Upscale with EXTRAS
The last part is rather straightforward. You can at the last step, upscale the image through the EXTRAS tab.
All the main options are here, you do need to enable "Enable upscale with extras".
Again, the upscalers set to "all" are random. You can get both the same upscaler.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6e15a067-1f11-47ba-8fa4-da0eb808640e)

# Just Upscale mode
Next to the Start button, is a checkbox for "Don't generate, only upscale"

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/03380806-d81e-4bbf-8d6e-d2cb5595e3bb)

This mode skips the entire TXT2IMG part of the batch. Instead, it will pick up all image files placed in the \extensions\OneButtonPrompt-dev\automated_outputs\upscale_me\ folder, and starts looping over those instead.
It will ignore any .txt file.
It will keep the original files, so you have to remove them before starting the next batch again.

Example:

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a28403e3-71b8-4457-95a9-55135a61c62d)

This method will read the original prompt and negative prompt from the image file (if it exists) and use that during the upscaling process.
Thus it can be used for any image generated by the WebUI, not specific to OneButtonPrompt image files.

This method is perfect for anyone who just generates their images via TXT2IMG, and then upscale in batch the best results automatically.


# Workflows
Each one of you has their own workflow ideas. People might prefer hires fix over tile upscaling, or some people might prefer upscaling multiple times as a loopback.

For me, I like to cherry pick results, and then use the "Just Upscale mode" to batch upscale my favorites.

You can set everything to "all", and just start generating a bunch of random stuff.

I'm sure your specific way of upscaling and working is supported by all the options offered here. Missing something? Let me know!

## Using your own prompts
If you don't like the results of the One Button Prompt generator (how could you not!), you can turn off the prompt generation, and use your own prompts instead.

Go to the "Workflow assist" tab, and enable "Workflow mode".
Put your prompt in the Workflow prompt field, and it will start using that

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bad22640-3932-4122-a935-e38473a4fa56)

For the negative prompt, use the "Main" tab

Put the negative prompt in the "Use this negative prompt" field.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/195ac566-fecd-4cc6-8b1b-7924b72db41f)

And done, you can now use One Button Run and Upscale with your own prompts.


### Please enjoy
Keep having fun!
