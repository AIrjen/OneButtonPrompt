# Anime Model Mode

Finally, One Button Prompt officially has a mode that supports Anime models. One Button Prompt has been focussed on SD based prompting first, and it kept getting worse in Anime Models. Now, it can do both! With a simple switch, set it up for anime/pony style models.

In A1111, it can be found under Advanced > Base model. Here you can select __Anime Model__

It is adviced to turn __flufferize__ and __Prompt enhancer__ off for use with anime models.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6408ebfd-a92d-411e-8569-dd0816f95e5f)

## What does it do

It supports anime model prompting! The main focus is on generating characters and has some build-in logic to support anime type models. When turned on, it does several things:

- It adds way more character based focussed words in the prompt. Creating varied and interesting characters.
- When generating a character, it will automatically add 1girl/1boy to the prompt.
- When generating a animal, it will automatically add anthro 1girl/1boy to the prompt.
- Will default __imagetype__ to 'all - anime' when using 'all'. 'all - anime' was added to support this mode.
- Prompt is more tag based styled
- Turns off several features that are used in other prompt generation modes.

## What it doesn't do

It doesn't add any very explicit or NSFW tags. If you want to add these, take a look at [this page](https://github.com/AIrjen/OneButtonPrompt/blob/anime_model_mode/user_guides/custom_files.md) on how to add your own files or words into One Button Prompt.

You could also add your specific tags in the prefix or suffix prompt.

## How to use it

For use of this, you can create a new preset/settings as followed. 
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9e2ab917-f205-4746-bf67-f31d2aff2306)

Make sure the following is set:
 
 - **Insanitylevel** = between __4-6__ is recommended.
 - **Artists** = __'none'__. Artists are all SD based, and will interfere and create bad results. However, some models might work with it. You can try setting it to 'anime' or 'cartoon' as well.
 - **Imagetype** = __'all - anime'__. Other options might be 'none' or 'subject only mode'.
 - **Subjecttype** = __'human - all'__, but feel free to select 'human - fictional' or any other to your preference. You can also go for animals, at your own risk ;) You know who you are.
 - **Gender**, your choice! __'All'__ will do both males and females.
 - **Prompt prefix**: The prefix stated on the model page. It in this example I am using AnimagineXL, so the prefix is = __'masterpiece, best quality, very aesthetic, absurdres'__. For Pony based models, it should be something like __'score_9, score_8_up, score_7_up'__. For 1.5 models it is usually something like __'(((masterpiece))) (((high quality)))'__
 - **Prompt suffix**: Personal preference tags.

You can play around more with the prompt prefix and suffix if needed.

Other things you can do, is add a overwrite subject and/or outfit yourself. It is possibly to add a subject + Lora in the overwrite subject field.
An example would be:
Overwrite subject: Princess Peach
Overwrite outfit: Jacket

Use your imagination!

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/65d567be-d3bb-401d-b258-6311ed097a39.png" alt="Princess Peach in a jacket" width="40%" height="40%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/339bc932-1be8-44ec-ab61-9ec8ee445296.png" alt="Princess Peach in a jacket" width="40%" height="40%">

> score_9, score_8_up, score_7_up, side-profile of a heavyset 1girl, solo, princess peach, cute, Warlike jacket, Two-Tone hair, at Sunrise, One Color, geometric patterns, attractive

# Try it without installing the extension?

I have a website where you can do prompt generation as well. Try it out [here](https://airjen.pythonanywhere.com/).

# Examples and prompts (various models)
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a0880fce-a448-417f-9a8f-be9f56213038.png" alt="Orc!" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2839476f-5a96-4fb3-85d4-6cfefff05950.png" alt="More princess peach on a 1.5 model" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7d71f1a3-9ffd-4828-ba41-bec8adc8ff4a.png" alt="Cutie" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/0005e54d-e0c5-404a-b8cb-3b92bf5a7ea3.png" alt="Not so cutie" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ab7bb864-38ae-478b-b540-5386bd8f569c.png" alt="Semi realism" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b679c5f6-e99e-4226-b9fd-210121b90044.png" alt="Those hands!" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/878d013e-b125-46a2-b1f0-b02fa431c270.png" alt="Pixel art style" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/701a3ac6-152e-4fa5-a632-1c2f11505b22.png" alt="Yes it can also do husbandos" width="25%" height="25%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/cfc86f6e-b17b-4001-a90d-78e79be44f55.png" alt="Varied example" width="25%" height="25%">

> masterpiece, best quality, very aesthetic, absurdres, upper body shot of a 1girl, solo, Female Orc, looking up, Taper, Thunderstorm, Oversaturated

> ((best quality)) , ((masterpiece)) , (detailed) , buff 1girl, solo, princess peach, white dress, Plaid trimmings, perched on a cloud, Honey hair, Fine art, Hopeless, hyper detailed, Rembrandt lighting, lots of details, moody

> masterpiece, best quality, very aesthetic, absurdres, shot from side of a flawless buxom 1girl, solo, Major, Ginger hair, Flustered, One Color, womanly, magnificent

> masterpiece, best quality, very aesthetic, absurdres, wide shot of a buff 1girl, solo, Minion dark yellow skin, Fur and Leather, Nihongami, Indirect light, Agfacolor, absurdres, 4K, monochromatic

> masterpiece, best quality, very aesthetic, absurdres, (1girl, solo, Lily James:1.2) , good-looking, Frolicking in a Lalbagh Botanical Garden, spring armor, Bouffant, Sunny, back-light, Low Contrast, realistic and detailed, intricate details

> score_9, score_8_up, score_7_up, pretty Scottish 1girl, solo, Spider-Gwen, costume, Kung fu pose, Braided half-up half-down, flower in hair, Sharp and in focus, Masterpiece, Lonely, Saturated

> masterpiece, best quality, very aesthetic, absurdres, dramatic pixel art, shot from side of a wearing Fleece pullover, overweight (1girl, solo:1.3) , Tiny, feeling relaxed, beautiful mouth, Defined lips, Two-Tone hair, Magic Realism, Primitivism, soft lighting, Fujifilm Superia, kawaii

> masterpiece, best quality, very aesthetic, absurdres, POV shot of a 1boy, solo, Temol, Surfer clothing, Looking over the shoulder, Dark hair, Movie still, Depressing, spotlit, Cinestill

> score_9, score_8_up, score_7_up, over the shoulder shot of a Nonchalant (1girl, solo, Museum curator:1.2) , Dreadlocks, curly hair, mountains, ultrafine detailed, Happy, elegant, Moonlit, Pastel Colors, Swirling Sisal


