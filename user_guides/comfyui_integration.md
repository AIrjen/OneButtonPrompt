# ComfyUI integration
One Button Prompt is now also a ComfyUI extension.

There are 8 nodes currently availabe, with One Button Prompt node being the main one.
You can slam it in every workflow, where you replace it with the Positive Prompt node.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/271dc575-dfe7-48dc-bef5-222d0af53344)



## Installing in ComfyUI
One Button Prompt is available in ComfyUI manager.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/54825420-ae69-4a9b-9dce-dad6baef8875)


If you want to do a manual install, do the following steps:

Navigate to your ComfyUI\custom_nodes\ directory, and run the following command:
```
git clone https://github.com/AIrjen/OneButtonPrompt
```

This should create a OneButtonPrompt directory in the ComfyUI\custom_nodes\ folder.

It could look something like this

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/88faa548-62c7-4059-9d5e-2a74e17678f4)

After that, restart ComfyUI, and you are ready to go.

### included workflows

In this project, there are some example workflows included.

[SDXL with refiner](https://github.com/AIrjen/OneButtonPrompt/blob/main/comfyui_workflow_examples/SDXL_OBP_Refiner.json)

[SDXL without refiner](https://github.com/AIrjen/OneButtonPrompt/blob/main/comfyui_workflow_examples/SDXL_OBP_NoRefiner.json)

[SDXL insanity variants](https://github.com/AIrjen/OneButtonPrompt/blob/main/comfyui_workflow_examples/SDXL_Insanity_Variants.json)


## Custom nodes

### One Button Prompt

All settings work similar to the settings in the Automatic1111 documentation.

It will generate a prompt from scratch, or based on several of your inputs and settings.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bca84637-a667-48e4-888d-9b0318eb4f43)

Please refer to the other documentation to see what each setting does.

## One Button Preset

Preset settings of One Button Prompt. Refer to [One Button Presets](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/one_butten_presets.md) for more information regarding the presets.

Has a simple prompt output and a preset selector. You can add new presets by manual adjusting the /userfiles/obp_presets.json JSON file.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/33392e25-d24e-4cc7-a90f-95722e7e8e06)

## One Button Artify

One Button Artify works as an artist mixer for your prompt. Like SDXL styles, but for all artists known in Stable Diffusion. 

It works best when adding a simple prompt.

It has the following settings to play with:

- Artist --> Selection of the style of artists to choose from.
- amount_of_artists --> Amount of artists to generate. Select random, for a choice between 1 and 3.
- artify_mode --> __standard__ adds tags according to the chosen artist. __remix__ chooses tags from different than the chosen artist. __super remix turbo__ chooses wildly from a long list of tags.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/22415117-c457-44a3-bc35-d13629681319)
> vibrant art by Chiho Aoshima, Digital Art, cute norwegian forest cat, Superflat art movement, kawaii aesthetics, fantastical and surreal imagery, blending traditional Japanese motifs with contemporary themes, vibrant colors, otherworldly landscapes, sharp focus, dynamic, contemporary, full color, grand illumination

## One Button Flufferize

One Button Prompts lightweight implementation of Fooocus Prompt Magic. It will enhance the output by adding quality tags at the end of your prompt. See the example above.

It is standardly set to __dynamic__. You can turn it off by choosing __none__.

Choose __short__, __medium__ or __long__ for more direct control.

Don't __reverse the polarity!__

## One Button SuperPrompt
One Button prompts integration of the SuperPrompt-v1 model. This is a different implementation than [NeuralSamurAI](https://github.com/NeuralSamurAI/Comfyui-Superprompt-Unofficial) his node.

Its simple, type in what you want to see, and let it do its magic.

You can set the intended style with the superpromptstyle settings. 'All' will either do nothing or add a random style.

All other settings are controlled by the insanitylevel.

It works great in combination with One Button Artify

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/1d8949c6-1a4a-420e-850f-bf5cba7f76c9)

## Create Prompt Variant
You can use the "Create Prompt Variant" node, to create variants based on a prompt you input. The strength of the variant is set with the "insanity level" slider. Simply connect it between the positive prompt and the CLIP encoder module.

#### How it works
It creates a small rift in subspace near your Central Processing Unit. Through this rift, it connects to various alternative universes where you are doing the exact same thing at the exact same time. It then flows their prompt to yours (and the other way around). This way, we get a slightly alternative prompt since it was from a slightly alternative universe. The prompt variant slider determines how many alternate universes away it should take the prompt from.

### Example

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a0191a18-eac9-4261-ab26-4dfdd997dad0)

Here is an example of ComfyUI standard prompt "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,"

These are all generated with the same model, same settings, same seed. But some of these have the Create Prompt Variant node included.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/dfe7fc06-face-4949-a048-d310504d3c3c)

Here is an example of the entire example workflow.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/117fc612-5a7d-4b0d-b163-adf8ff84555c)

### Save Prompt To File

Use the Save Prompt To File node to actually save the prompt in a text file. Since ComfyUI stores the entire flow in the image, it doesn't store the actual generated prompt.

You can also use other extension for this. But I thought it was nice to include a save options nativly. There are other options out there as well.

Just simply also connect the output of One Button Prompt to the Postive Prompt node.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/edaf7cec-7e95-46a9-84dc-00da4aaf2c4e)

### Auto Negative Prompt

The Auto Negative Prompt node, generates a negative prompt, based on the positive input. It can be used stand-alone as well, with any prompt field. It will try to enhance what was in the positive prompt. For example "anime" in the positive prompt, will add "photorealistic" in the negative prompt.

The following options are available:

base_negative --> Will be added onto the negative prompt

enhancenegative --> Will push a lot of quality enhancing terms into the negative prompt. Default value = 0

insanitylevel --> Larger numbers will randomly lower the amount of things in the negative prompt. Default value = 0



### Known issues

1. There is a SEED option in the One Button Prompt node, this is a hacky thing. It is just there to make sure it is refired each time you generate an image.

