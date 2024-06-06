# Anime Model Mode

Finally, One Button Prompt officially has a mode that supports Anime models.

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
 - Artists = 'none'. Artists are all SD based, and will interfere and create bad results. However, some models might work with it. You can try setting it to 'anime' or 'cartoon' as well.
 - Imagetype = 'all - anime'. Other options might be 'none' or 'subject only mode'.
 - Subjecttype = 'human - all', but feel free to select 'human - fictional' or any other to your preference. You can also go for animals, at your own risk ;) You know who you are.
 - Gender, your choice! 'All' will do both males and females.
 - Prompt prefix: The prefix stated on the model page. It in this example I am using AnimagineXL, so the prefix is = 'masterpiece, best quality, very aesthetic, absurdres'. For Pony based models, it should be something like 'score_9, score_8_up, score_7_up'. For 1.5 models it is usually something like '(((masterpiece))) (((high quality)))'

 - You can play around more with the prompt prefix and suffix if needed.
 - 

# Examples
