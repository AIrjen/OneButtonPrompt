# ComfyUI integration
In this codebase there is a custom node, that can be used in ComfyUI.
Work is still in progress for all features to work flawlessly in ComfyUI, but a start has been made.

You can slam it in every workflow, where you replace it with the Positive Prompt node.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a9c6b449-772b-495c-b39d-eda0be38a203)


## Installing in ComfyUI

Navigate to your ComfyUI directory, and run the following command:
```
git clone https://github.com/AIrjen/OneButtonPrompt
```

This should create a OneButtonPrompt directory in the ComfyUI folder.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/5d9cfdd3-8342-4aff-a9a4-ecbbc7151856)

From this folder, manually copy the file
```
OneButtonPrompt-node.py
```

Into the ComfyUI\custom_nodes\ folder.
That should look like this:

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f2c9630e-790b-4a34-b46f-54dbb18b87d5)

After that, restart ComfyUI, and you are ready to go.

### Known issues

1. ComfyUI does NOT store the prompt in the image, but the workflow. Since the prompt is not in the workflow, it is not saved. I am unsure wether there is a custom node for this.
2. There is a SEED option in the One Button Prompt node, this is a hacky thing. It is just there to make sure it is refired each time you generate an image.
3. Prompts are styled for Automatic1111, so it uses prompt switching, which is not supported by ComfyUI.
4. Easy installer not yet available.

Issues will be investigated over time.
