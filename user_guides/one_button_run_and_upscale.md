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
4. Possiblity to __just batch upscale__ existing images

All with a single press of __One Button__.

## How does it work?
It works by using various calls of the WebUI API and calling them with the correct parameters in the correct order.

## Requirements
The basic requirement, is that WebUI is started with --api enabled. To do so, go into your webui-user.bat file in the WebUi folder, and add --api to the line with set COMMANDLINE_ARGS.

This is not needed if you are running SD Next (Vladmandic).

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

The __"folder"__ buttons opens to your One Button Prompt automated outputs folders.

There are some general options to set first.

__URL__ -> This should be the URL used by WebUI (see your webbrowser). This is standardly __http://127.0.0.1:7860__ , but change it to your specific instance.

__Amount of images to generate__ -> How many times should it repeat the entire process. So how many images to generate and upscale

__Don't generate, only upscale__ -> Place images in the /upscale_me/ folder, when enabled, it will skip the TXT2IMG part, and will start batch upscaling the images with the set parameters

__model to use__ -> Select which model to use during generation. __"Currently Selected Model"__ meand the model you have loaded right now. __"all"__ means a random model (not inpainting models). Or select a specific one.


For TXT2IMG most options should be familiar. I will here explain some of the additions and changes.


__Size to generate__:

1. __all__ -> picks randomly between __portrait__, __wide__ and __square__
2. __portrait__ -> 512x768
3. __wide__ -> 768x512
4. __square__ -> 512x512
5. __ultrawide__ -> 1280x360 (Don't worry, this one is just for me, and won't be used when picking "all")

__Sampler__:

Added option for __"all"__, picks randomly

__Hirex upscaler__:

Added option for __"all"__, picks randomly

Added option __"automatic"__, sets Upscaler and Denoise Strength based on prompt. Example, if the prompt contains anime, it will try to use the anime upscaler.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7588989a-5254-4ead-8045-b4e147803670)


#### Quality Gate
Idea and inspired by xKean. Such an awesome addition. Additional ideas by pto2k.
See requirements above.

When enabling __Quality Gate__, it will repeat the above TXT2IMG process until:
- an Image reaches the __Quality Score__
- we have reached the __amount of tries__

When an image reaches the quality score, all other images are removed. It will then continue with the quality image.
With standard settings, if it reaches the amount of tries, it will __pick the image with the highest score__. All other images are removed. It will then continue with the highest quality image.

There are some other options as well:

__Move Hires fix afterwards__ - This option needs to be used with Hires. fix enabled for it to work. It turns of Hires. fix during the initial generation of images. Once a image is chosen by the Quality Gate, it will then rerun the image, but this time with Hires. fix enabled. This allows for faster iteration.

__Mode of operation__ - Standardly set to __highest__ which picks the image with the highest score. The other option is __gated__ which will only allow images scoring the 

__Quality Score__ will be used. These will then not count to the Amount of images to generate.

__Images__ is standarly set to __keep used__. If you set this to __keep all__, all generated images are kept, and nothing automatically removed.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e519795a-dbd5-4dc7-b96c-8f4975498ec2)




### IMG2IMG
Again, most options should be familiar for using IMG2IMG when upscaling. It defaults to using __"SD Upscale"__ method which is included in WebUI standardly.
Enable __"Upscale image with IMG2IMG"__ to actually turn this on.

__Amount times to repeat upscaling with IMG2IMG (loopback)__ -> This controls the amount of times to use IMG2IMG to upscale.

I will describe some of the changes from normal.

__model to use__ -> Select which model to use during generation. __"Currently Selected Model"__ meand the model you have loaded right now. __"all"__ means a random model (not inpainting models). Or select a specific one.

Note that you can have a different model selected here, than used in the TXT2IMG process.

__Sampler__:

Added option for __"all"__, picks randomly

__Upscaler__:

Added option for __"all"__, picks randomly

Added option __"automatic"__, sets Upscaler and Denoise Strength based on prompt. Example, if the prompt contains anime, it will try to use the anime upscaler.

__adjust denoise each img2img batch__ -> Adds or subtracts this amount of denoise, during each IMG2IMG batch. Usually you want a lower denoise when upscaling larger images.



![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/59756d2b-4e97-41b3-accb-ffa603b07152)

#### Use Ultimate SD Upscale script
Turn on __"Use Ultimate SD Upscale script instead"__ to use Ultimate SD Upscale. You need to have that extension installed, see requirements above.

Here, all options from Ultimate SD Upscale are available.

It uses img2img padding for the padding.
It will always be set to __"Scale from image size"__

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/23ad556a-4e53-462b-90ab-d8d5ff9e2302)


#### Controlnet tile resample
Best used in combination with Ultimate SD Upscale and the 4x-UltraSharp upscaler, however you can use it with the normal SD Upscaler as well.
The controlnet tile model name is filled in for you, but if a later or newer version comes out, you might have to change this to that specific one. Current version is __"control_v11f1e_sd15_tile [a371b31b]"__

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9ec27d75-a559-4b13-9a3c-60c5382117ba)

There is also a option for __"also enable wierd blocky upscale mode".__ This was a bug I found during development, but brought in as a feature. Best used with 4x-UltraSharp upscaler and a decent denoise (0.7-0.8).

Here is an example result, so you can see what to expect.

![20230510220750_City](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b8bc0544-62f2-428e-9f1a-6d42063c3518)

> art by Daria Petrilli,art by J.C. Leyendecker, landscape of a City, at Overcast, Simple illustration, Lonely, Industrial Art, volumetric lighting, DayGlo and electric pink hue, under water

## Upscale with EXTRAS
The last part is rather straightforward. You can at the last step, upscale the image through the EXTRAS tab.
All the main options are here, you do need to enable __"Enable upscale with extras"__.
Again, the upscalers set to __"all"__ are random. You can get both the same upscaler.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6e15a067-1f11-47ba-8fa4-da0eb808640e)

# Just Upscale mode
Next to the Start button, is a checkbox for __"Don't generate, only upscale"__

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/03380806-d81e-4bbf-8d6e-d2cb5595e3bb)

This mode __skips the entire TXT2IMG part__ of the batch. Instead, it will pick up all image files placed in the __\extensions\OneButtonPrompt-dev\automated_outputs\upscale_me\ folder__, and starts looping over those instead.
It will ignore any .txt file.
It will keep the original files, so you have to remove them before starting the next batch again.

Example:

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a28403e3-71b8-4457-95a9-55135a61c62d)

This method will __read the original prompt and negative prompt__ from the image file (if it exists) and use that during the upscaling process.
Thus it can be used for __any image generated by the WebUI__, not specific to OneButtonPrompt image files.

This method is perfect for anyone who just generates their images via TXT2IMG, and then __upscale in batch__ the best results automatically.


# Workflows
Each one of you has their own workflow ideas. People might prefer hires fix over tile upscaling, or some people might prefer upscaling multiple times as a loopback.

For me, I like to cherry pick results, and then use the "Just Upscale mode" to batch upscale my favorites.

You can set everything to "all", and just start generating a bunch of random stuff.

I'm sure your specific way of upscaling and working is supported by all the options offered here. Missing something? Let me know!

## Using your own prompts
If you don't like the results of the One Button Prompt generator (how could you not!), you can __turn off the prompt generation, and use your own prompts__ instead.

Go to the __"Workflow assist"__ tab, and enable __"Workflow mode"__.
Put your prompt in the __Workflow prompt__ field, and it will start using that

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bad22640-3932-4122-a935-e38473a4fa56)

For the __negative prompt__, use the __"Main"__ tab

Put the negative prompt in the __"Use this negative prompt"__ field.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/195ac566-fecd-4cc6-8b1b-7924b72db41f)

And done, you can now use One Button Run and Upscale with your own prompts.


### Please enjoy
Keep having fun!
