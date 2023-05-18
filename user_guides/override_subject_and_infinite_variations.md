# override subject and how to create infinite variations of a set subject
Overriding a subject is one of the most __powerful__ ways of experiencing One Button Prompt.

This will allow you to explore infinite variants of a subject of your own choice.

This also creates the option of adding a subject that requires a LoRA.

There are 2 settings that can be found in the Main tab of One Button Prompt:
### Overwrite Subject
Any text you place in "Subject overwrite" will be treated as the subject to generate. 

It is very helpful to first set the "Subject Type" to the matching subject, as this will guide the prompt generation. For example, set it to humanoid if you are trying to generate people. It will then use the logic used for generating people.

You can also for example, set something LoRA specific in the subject field, and place the actual LoRA in the prompt suffix field.

### Smart Subject
Smart Subject is standardly activated, and this will try to interpret your prompt, and turn off any related lists.

For example, if you set the subject to: "Obese man wearing a kimono", it will see that "obese" is an existing body type, so it won't generate another.

"wearing" is a keyword that turns off outfit generation. Other keywords such as "hair" and "pose" are also in.

Basically, leave this on. Especially if you are trying to do something more specific.


## Example: Tree of Life
![deliberate tree of life](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/6a49fb69-06f0-4866-92aa-44c44a96ad5e)

In this example, I used the Deliberate model. 
In the settings, I set the following properties:

Subject Types: __Landscape__

Artists: __landscape__

type of image: __digital art__

Overwrite subject:__Tree of life__

What these settings to, is to focus the generation on landscapes, while also only using landscape artists. It will also create only "digital art" of this, instead of random results.

With the overwrite subject: "Tree of life", it will now only create epic trees for us. Nice.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d7430e7b-2d60-4ac5-b7c2-ad85ec74931f.png" alt="Tree of life settings" width="60%" height="60%">

## Example: Daenerys Targaryen

![deliberate examples](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/0c595158-73c0-4001-8af2-1fe00009b90a)

In this example, I used the Deliberate model. 

In the settings, I set the following properties:

Subject Types: __humanoid__

Artists: __all__

type of image: __all__

Overwrite subject: __Daenerys Targaryen__

These settings give One Button Prompt a lot of freedom, because we set Artists and Type of image both to "All". As a result, we get a wide range of diversity. It also creates less good results because of this, but that is to be expected. It also creates some really imaginitive stuff, especially running on a versatile model such as Deliberate.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/c69ecc7f-af8d-4451-be05-60c21a17783a.png" alt="Daenerys Targaryen settings" width="60%" height="60%">

## Example: Daenerys Targaryen with LoRA's and a TI

![dreamshaper and lora examples](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/de914d6c-fe81-41a7-b574-86aad5f488b3)

In this example, I used the Dreamshaper model, which is less flexbile than deliberate. I am also using 2 LoRA's and a Textual Inversion, to show the possiblities.
These are added in the prompt suffix field.

In the settings, I set the following properties:

Subject Types: __humanoid__

Artists: __popular__

type of image: __all__

Overwrite subject: __Daenerys Targaryen__

Prompt suffix: __style-sylvamagic, <lora:add_detail:0.8>,<lora:LowRa:0.6>__

There is a lot less freedom here, also because of the model used. But the variety can still be ssen. You can also see the effects of the LoRA's on the results.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a5c7669c-952d-441e-8e58-644ff8a594b2.png" alt="Daenerys Targaryen settings" width="60%" height="60%">

## Using a LoRA as a subject
You can use a LoRA as a subject as well. Sometimes you need to add the triggerword as the subject, and the LoRA in the prompt suffix field. Sometimes you need to add both in the overwrite subject field.

### Smart Subject in detail


### Wildcards
