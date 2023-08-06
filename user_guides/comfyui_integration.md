# ComfyUI integration
One Button Prompt is now also a ComfyUI extension.

There are 3 nodes currently availabe, with One Button Prompt node being the main one.
You can slam it in every workflow, where you replace it with the Positive Prompt node.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a9c6b449-772b-495c-b39d-eda0be38a203)


## Installing in ComfyUI

Navigate to your ComfyUI\custom_nodes\ directory, and run the following command:
```
git clone https://github.com/AIrjen/OneButtonPrompt
```

This should create a OneButtonPrompt directory in the ComfyUI\custom_nodes\ folder.

It could like something like this

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/50f9d8b4-dd0a-4c87-b8c4-25a159c71d75)

After that, restart ComfyUI, and you are ready to go.

It should be available in ComfyUI manager soonish as well.

## Custom nodes

### One Button Prompt

All settings work similar to the settings in the Automatic1111 documentation.

It will generate a prompt from scratch, or based on several of your inputs and settings.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bca84637-a667-48e4-888d-9b0318eb4f43)

Please refer to the other documentation to see what each setting does.

### Create Prompt Variant
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

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/1557546d-36f3-4ce0-9532-cf5a8386297d)


### Known issues

1. There is a SEED option in the One Button Prompt node, this is a hacky thing. It is just there to make sure it is refired each time you generate an image.

