![template examples 1](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/f5b96087-81fb-4a06-83a0-f209d085b5e3)


# Templates and "only templates" mode

There is a small chance, that One Button Prompt generates a prompt based on a template instead of a fully randomized generated prompt. You can also force it to use "only templates". But what does this mean exactly? I hope to answer these questions here.

This feature was build for beginners. Instead of copy/pasting existing interesting prompts from the web, I've already done so for you. There are currently over 500+ prompt templates available.

Hopefully, this will inspire you as well.

### What is a prompt __template__?
A __prompt template__ is a preconfigured prompt which uses One Button Prompt wildcards to be randomized.

These __prompt templates__ are based on various popular existing prompts, from example civitai, prompthero, promptbook, replicable, openart sources. They try to add randomizition while keeping in line with the original prompt.

Here is a good example from the [deliberate model](https://civitai.com/images/154634?modelVersionId=15236). This is the original image posted:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/a69d544f-ee25-41a5-b833-537f4dfea0e4.png"  alt="original image" width="30%" height="30%">

> a girl, wearing a tie, cupcake in her hands, school, indoors, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

This is the wildcarded prompt that is added to the __prompt templates__:

> a -subject-, wearing a -accessory-, -food- in her hands, school, -minilocation-, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

This means that most of the base prompt remains the same, however, some of the parts of the prompt have been replaced by wildcards. These are then replaced by a randomized value during prompt generation.

Here are some examples of this specific prompt template:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/613e44a1-593e-4b14-8989-98c62ab62fa5.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/b370fbd2-54dc-4802-8eb9-b9f535268a7d.png" width="30%" height="30%">


> a Luigi, wearing a Chain, Clementine in her hands, school, pond, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

> a Katniss Everdeen, wearing a Earbuds, alcohol in her hands, school, jungle, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/55399398-6dc1-4786-8c43-8a6da99837ec.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/213a89b4-abb9-40f9-8527-ded7c374ab41.png" width="30%" height="30%">

> a Priyanka Chopra, wearing a Cat Ears, Charcuterie in her hands, school, trees, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

> a Mr. Spock, wearing a Umbrella, smoked in her hands, school, flower field, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

As you can see, it still feels very One Button Prompty, while still being true to much of the original prompt.

## Running with "only templates"
The prompt templates with show up once in a while during normal use of One Button Prompt. This can be set under __"type of image"__ . Set this to __"only templates"__. This will force One Button Prompt to only work bsaed of prompt templates instead of its normal randomized generation.

![only templates option](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/c60e4b5b-d4d4-4939-a1c4-ba8a575b2a7b)

All prompt templates are classified with a subject type. This means you can use the __"Subject Types"__ field normally. So you can set it to any value such as __"animal"__ or __"humanoid"__, and it will take the prompt templates that match that type.

I do have to say, that "humanoids" are overrepresented in the dataset, and "concept" are underrepresented. I did try to have as much diversity as possible in the set.

## Subject Override and prompt templates
You can use __"Overwrite subject"__ as normal with the prompt templates. Meaning that your subject will be inserted in the prompt templates.

Refer to [guide to override subject](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/override_subject_and_infinite_variations.md) for more information surrounding the override subject.

__"Smart subject"__ has no effect when using prompt templates.

Example:
![templates example with custom subject](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/2fdc8835-62d0-4650-90d4-f966bf2de286)

## Adding new prompt templates
You can add your own prompt templates as well, or even override the entire set with your own templates. This is done through the __custom files__ logic that works for every file in One Button Prompt.

Refer to the basics here: [guide to custom files](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/custom_files.md)

Refer to the wildcards here: [guide to using wildcards and Dynamic Prompts](https://github.com/AIrjen/OneButtonPrompt/blob/main/user_guides/wildcards_and_dynamic_prompts_extension.md)

You can place a __"templates_addon.csv"__ or a __"templates_replace.csv"__ file in the __userfiles__ folder of One Button Prompt.

Refer to __\csvfiles\templates\templates.csv__ for how the prompt templates are build up.

### structure

The structure is as following:

_prompt;source;sourcecategory;subjecttype;subjectwildcard_

__prompt__: The prompt including -wildcards-. You can use comma's normally. Try to determine the main subject of the prompt, and add the -subject- wildcard. This is needed to work with override subject.

__source__: Used during testing, no actual logic used here. I used either the website or model I got the prompt template from, such as civitai or promptbook.

__sourcecategory__: Used during testing, no actual logic used here. Currently only has the values official and gallery.

__subjecttype__: Determines the main category, these are "object", "animal", "humanoid", "landscape" and "concept"

__subjectwildcard__: The wildcard to replace the subject with. For example, use the -human- wildcard to replace the -subject- wildcard from the prompt with this wildcard.

Please note, that if there is a empty row, or one of the values is missing, it will probably not work.

Here are some random examples from the current __templates.csv__:

> -subject- in -location- with typical -brand- -minioutfit- and highly detailed face;openart;gallery;humanoid;-human-

> a -descriptor- -subject-, closeup, at night, dark theme, darken, cinematic;civitai;gallery;animal;-animal-

> Super -descriptor- -subject-, holding a -objecttotal-, light rain, -minilocation-, by POPMART blind box, -colorscheme-, mockup, blind box toy, fineluster, clean background, 3D render, oc render, best quality, 4k, ultradetailed;lexica;gallery;humanoid;-human-

> 8k portrait of -subject- in a -color- -descriptor- -outfit- is standing in the -minilocationaddition- around the people at midnight ,(perfect face), -descriptor- jawline, (-descriptor- -color- eyes), -descriptor- lips, (-haircolor- -hairstyle- hairstyle), (perfect hands),(-mood-:1.3),looking at camera,(-descriptor- face:1.4),upperbody,grab a flowers, (highly detailed:1.5), digital painting, a photorealistic painting, photorealism;dreamshaper;gallery;humanoid;-human-

> -descriptor- -subject- -culture- -artmovement- style. at an -location-;lexica;gallery;animal;-animal-

## Contributing

If you would like your prompt templates to be added to One Button Prompt, you can:

- Send a message with the templates in the GitHub discussions, or find me on reddit \u\AIrjen
- Be a pro, and create a Pull request

