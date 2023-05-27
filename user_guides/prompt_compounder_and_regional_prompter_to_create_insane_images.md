![00172-216086968](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e5bb6bc0-ba9a-4d4a-9e14-913860c74c26)
Note: all images on this pages were generated with the [DiffusionBrushEverything model](https://civitai.com/models/46294/diffusion-brush-everything-sfw-nsfw-all-purpose-checkpoint-nuclear-diffusion-anime-hybrid)

# Prompt Compounder
The prompt compounder funcionality can be found on the Advanced Tab of the One Button Prompt script.

This function was created after the very first release of One Button Prompt. There was a massive bug, when you ran in batch mode, the prompts would not reset. Causing each batch to compound the generated prompts together.

Redditor drone2222 suggested to bring this back as a feature, as he said: "it creates interesting results". And is totally correct. I brought it back as a feature, adjusted and improved the logic, so it can also be used for Latent Couple/Regional Prompter extensions.

Coupled with those extensions, One Button Prompt goes to the next level. Creating unique results. I wanted to describe how to do this. But first, let starts with the basics.

# Basic prompt compounding
Normally, One Button Prompt generates one prompt for you. With the Prompt compounder, you can increase that amount. For example, you can set it to 2.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e236e05c-ec2d-460c-80c9-bf0b6af59796)

Now, it will generate two prompts and combine them together. With the default settings, it will be added with a simple comma.

This can create interesting result with the right model.
Examples, of using a standard prompt compounder with the setting set to 2:




