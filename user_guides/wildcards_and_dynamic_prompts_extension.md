# Wildcards
In the backend of the code, some of the things run on wildcards. These can be used in the prompt prefix, prompt suffix and subject override fields. They get values from their specific related lists.

Currently, One Button Prompt supports the following wildcards.

    -color-
    -material-
    -animal-
    -object-
    -fictional-
    -nonfictional-
    -building-
    -vehicle-
    -outfit-
    -location-
    -conceptprefix-
    -conceptsuffix-
    -descriptor-
    -food-
    -haircolor-
    -hairstyle-
    -job-
    -culture-
    -accessory-
    -humanoid-

# Dynamic Prompts extension and wildcards
The [Dynamic Prompts extension](https://github.com/adieyal/sd-dynamic-prompts) might be considered the father of One Button Prompt. In that case [StylePile](https://github.com/some9000/StylePile) is its mother.

However, Dynamic Prompts can be combined with One Button Prompt. You can use the wildcards supported by Dynamic Prompts also in the prompt prefix, prompt suffix and subject override fields.

Meaning that if you have managed your own wildcards before, you can use them here as well. With the standard settings, these are __ __wildcardname__ __

In this example, I have a bird.txt wildcard file in \extensions\sd-dynamic-prompts\wildcards\

Now in One Button Prompt, I set the following:
__Subject Types__ = "animal"
__Artists__ = "sci-fi" or "none", depending on taste. Sometimes the sc-fi artists generate other types of "bird".
__Type of image__ = "digital art"

__Overwrite subject__ = "cyberpunk __ __bird__ __ with -material- implants"

I am using the deliberate model for these examples. Note that most models have problems generating kick ass birds.

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/baec47db-d00c-4b14-8422-6544dd1e64c5)

here are some examples:

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/de676c71-7c5f-4081-bf61-5939190fa86c.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d3702d14-fa9c-4976-820f-25c62e360b69.png" width="30%" height="30%">


> digital art, long shot of a cyberpunk American Woodcock with Moss implants, Sunny, Ultra Detailed, Happy, Demoscene, moody lighting, Grayscale, epic fantasy, RTX, unreal engine
>
> digital art, overhead angle of a cyberpunk Northern Mockingbird with Foam implants, Illustration, Vaporwave Art

<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/d0ada6f6-d458-4450-a581-e22c80ad9fb7.png" width="30%" height="30%">
<img src="https://github.com/AIrjen/OneButtonPrompt/assets/130234949/381360b8-0f4f-4c00-b3dd-b658abb07399.png" width="30%" height="30%">

> digital art, long shot of a cyberpunk European Starling with Bone implants, Stormy weather, F/14, hyperdetailed, ultra high res
>
> (art by Kelly Freas:0.8), digital art, 3/4 view of a cyberpunk Winter Wren with Rubber implants, Snowy, Neogothic Art, Nostalgic lighting, Depth of field 100mm, dark white color grading
