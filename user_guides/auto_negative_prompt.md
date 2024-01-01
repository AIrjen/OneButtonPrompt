# Auto Negative Prompt

With the magic of an __Auto Negative Prompt__! Get better results from your prompts. Without any effort.

Go from this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ab176b85-c0e4-4444-85d9-93f5a7746c94.png" alt="Without Negative" width="30%" height="30%">
To this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ce579d19-fe32-4048-8af2-00dac0832452.png" alt="With Auto Negative Prompt" width="30%" height="30%">

Go from this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/bb206ee4-2ae1-4f54-b68e-c3c4b98abbee.png" alt="Without Negative" width="30%" height="30%">
To this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/5678edcc-d3fb-4053-8865-25677f11dece.png" alt="With Auto Negative Prompt" width="30%" height="30%">

Go from this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/890b0f73-56f2-4a0e-9d55-888c3f0b933e.png" alt="Without Negative" width="30%" height="30%">
To this:
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/4fe5268a-bb0a-4fa4-8109-1984615d6333.png" alt="With Auto Negative Prompt" width="30%" height="30%">



> colorful art designed by Loish and Krenz Cushart, Anime Graceful broad-shouldered (Woman:1.2), wearing costume, her costume has a crest on chest, royal pose, Auburn hair styled as Slicked-back, equirectangular 360, Fantasy, dreamy, perfect skin
>
> digital art, kawaii Woman of Performance Feudal lord, Bokeh, Alternative Art
>
> Water color painting, elegant, Thundering short Selene, her hair is Pink, Dynamic, dramatic lighting, One Color

With an __Auto Negative Prompt__! This is now default turned on in A1111. It's also available as a ComfyUI Node.

Auto Negative Prompt parses your prompt, and tries to invert some words of the prompt. For example, "anime" will add "photorealistic" to the negative prompt. "colorful" will add things like "drab" and "monochrome" to the negative prompt.

It tries to follow the intent of the positive prompt.

## Options

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/e133386b-c310-4b1c-8e6e-d5c78a000eb4)

### 🤖🚫💬 Auto generate negative prompt
This turns the generation of the negative prompt on or off. Default, it is turned on.

### 📈🚫💬 Enable base enhancement prompt
This adds a bunch of quality enhancing statements to the negative prompt. Default, it is turned off.

### 🎲🚫💬 Randomness of negative prompt 
Increasing this value will remove more parts of the negative prompt. A setting of 5 will randomly remove about 50%. Standardly this is turned off, and is at value 0.

### 🚫💬 Base negative prompt
This is your normal negative prompt. This will get fully added, at the end of the generated negative prompt.

## ComfyUI example
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9592ea2a-79d1-4eb3-a21d-ecc20217fd70)
