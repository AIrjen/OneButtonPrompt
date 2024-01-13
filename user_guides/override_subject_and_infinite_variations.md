# Override subject and how to create infinite variations of a set subject
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

For example, if you set the subject to: __"Obese man with red hair, hard light"__, it will see that "obese" is an existing body type, so it won't generate another. The same goes for the lighting.

"hair" is a keyword that turns off outfit generation. Other keywords such as "wearing" and "pose" are also in.

It also has a feature called __subject magic__. You can use the magic word __"subject"__ in the override subject field. The subject value is replace by the actual generation process. It is like a wildcard, that does a little bit more. It puts the intended subejct in its place.

This then allows for subjet overrides like this: __"scandanavian subject with platinum hair, soft light"__. In the example below, you can see it transforms into "scandanavian elegant Woman of Paradox with platinum hair, soft light"

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/7b865b1e-56d0-430f-a209-108c5297c512).png" alt="Override subject with subject magic" width="60%" height="60%">

> Concept art, scandanavian elegant Woman of Paradox with platinum hair, soft light, very bored, Geass, Earring, Summer, shallow depth of field, Cel shaded, Kodak Ektar, sfumato, Liminal dream

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

## Using a LoRA as a subject: Gul Dukat
__ATTENTION BAJORAN WORKERS: You can use a LoRA as a subject as well.__ 

![LoRA character example](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/476f84a7-e71e-4ecb-a790-54629ec0e386)
Sometimes you need to add the triggerword as the subject, and the LoRA in the prompt suffix field. Sometimes you need to add both in the overwrite subject field.
In this example, I'm using the main character of star trek's DS9 series, Gul Dukat. Thanks to the amazing [Terok Nor Lora](https://civitai.com/models/58470/terok-nor-lora)!

In this example, I used the Dreamshaper model. In the settings, I set the following properties:

Subject Types: __humanoid__

Artists: __all__

type of image: __all__

Overwrite subject: __gul dukat wearing cardassian uniform__

Prompt prefix: __sdn__

Prompt suffix: __<lora:diffusiondesign_SDN_LoRA_1.12:0.6>, star trek__

With this method, the initial trigger word is in the prompt prefix field, sdn. The subject is "gul dukat wearing cardassian uniform", since smart subject is activated, it will not generate another outfit for our buddy during prompt generation.

Lastly, in the prompt suffix is the actual LoRA and another trigger word, star trek.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/0ccf8cf3-c2c9-4cd7-b183-eb6b7a640a5a.png" alt="Gul Dukat" width="60%" height="60%">


### Smart Subject in detail
Smart subject will try to interpret your override subject, and turn off any related lists.
Example, if the word "Obese" in the override subject, it will find this exact word in the "body_types" list. It will disable body type generation. And so it works for all individual words in the override subject, as well as all combined words between comma's.

Additionaly the following keywords have additional hardcoded keyword triggers:

"wearing","outfit" or "dressed" will turn off outfit generation

"bodytype" or "body type" will turn off body type generation

"hair" will turn of hairstyle generation

"location" or "background" will turn off background generation

"lighting" will turn off lighting generation

"mood" will turn off mood generation

"pose" or "posing" will turn of pose generation

"quality" will turn off all quality generation

"shot" will turn off all framing/shot size generation

This means, you can form override subject prompts like this:

"full body shot of a obese donald trump"  --> turns off shot sizing and body type generation

"fantastical skull, candle lighting" --> turns off description (via fantastical) and lighting generation

"lifeguard, background is beach" --> turns off background generation

### Wildcards
In the backend of the code, some of the things run on wildcards. These can be used in the prompt prefix, prompt suffix and subject override fields.  They get values from their specific related lists.

Currently, One Button Prompt supports the following wildcards.

- -color-
- -material-
- -animal-
- -object-
- -fictional-
- -nonfictional-
- -building-
- -vehicle-
- -outfit-
- -location-
- -conceptprefix-
- -conceptsuffix-
- -descriptor-
- -food-
- -haircolor-
- -hairstyle-
- -job-
- -culture-
- -accessory-
- -humanoid-
- -manwoman-
- -human-
- -colorscheme-
- -mood-
- -genderdescription-
- -artmovement-
- -malefemale-
- -objecttotal-
- -bodytype-
- -minilocation-
- -minilocationaddition-
- -season-
- -minioutfit-
- -elaborateoutfit-
- -minivomit-
- -vomit-
- -rpgclass-
- -brand-

special wildcard, loading subject from a file

- -subjectfromfile-

In the user_files folder, you can place a file called custom_subjects.csv. If you use this -subjectfromfile- wildcard, it will select a random value from this file. Suggested use is on the Overwrite Subject field.

## Bringing it all together, generating awesome cyborgs with One Button
![awesome cyborgs](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9e252a45-2600-44a3-a789-de7a66211e1b)

In this example, I used the (Lyriel)https://civitai.com/models/22922/lyriel model. In the settings, I set the following properties:

Subject Types: __humanoid__

Artists: __sci-fi__

type of image: __portrait__

Overwrite subject: __-descriptor- cyberpunk cyborg, -material- details__

In this case, I am using the wildcards to my advantage in the override subject. Since I use the word "cyberpunk" the standard description generation is turned off. In this case, I add a random descriptor in my subject override, to get some randomness back.
Next to that, I add -material- details. This way, it will generate some random materials to the results, creating interesting stuff.

With these settings, all results are good and varied.

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/9dad7d31-cb1e-4375-9d64-600942e8e884.png" alt="Beep Boop!" width="60%" height="60%">

# Thank you
Hope to have inspired you, and get generating!
