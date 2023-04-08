# OneButtonPrompt
![OneButtonPrompt](https://github.com/AIrjen/OneButtonPrompt/blob/main/images/Background.png)

# Summary

One Button Prompt is a tool for beginners who have problems writing a good prompt, or advanced users who want to get inspired.

It generates an entire prompt from scratch. It is random, but controlled.

### Some details
It will generate between 0 and 3 artists, and add those the prompt.

It can generate the following subjects, while building a prompt:

1. object - Can be a random object, a building or a vehicle.  

2. animal - A random (fictional) animal. Has a chance to have human characteristics, such as clothing added.  

3. humanoid - A random humanoid, males, females, fantasy types, fictional and non-fictional characters. Can add clothing, features and a bunch of other things.  

4. landscape - A landscape or a landscape with a building.  

5. concept - Can be a concept, such as "the X of Y", or an historical event such as "The Trojan War".  

It mixes techniques such as prompt switching and hybrids. 


# automatic1111 script
It can be used in automatic1111. Simply install this from via install from URL. After that you can see OneButtonPrompt in the script fields for txt2img and img2img.

![image](https://user-images.githubusercontent.com/130234949/230737801-fd107060-161b-495e-871c-234342664b31.png)
This generator will generate a complete full prompt for you, based on randomness. You can increase the slider, to include more things to put into the prompt. 
Recommended is keeping it around 3-7. Use 10 at your own risk.

There are a lot of special things build in, based on various research papers. Just try it, and let it surprise you.

Suggestion is to leave the prompt field empty, anything here will be added at the end of the generated prompt.  
It doesn't add anything to the negative prompt field, so feel free to add your favorite negative prompts here.  

(note: there is a bug with multiple batches, it doesn't add the new prompt)

# off-hands generation

In the main.py script, there is logic that calls the API's from automatic1111. Simply start automatic1111 normally, and run the main script.
Edit the main script to set the amount of loops/images to generate, and uncomment the txt2img, img2img and upscale scripts to taste.


# examples
From the above header, these are the generated prompts, from left to right, top to bottom. Generated during various stages of development. Using deliberate and DPM Karras.

>cinematic shot of a Cruel " The Soul of Enlightenment ", at Blue hour, Cel shaded 
>
>( art by Albert Dubois-Pillet :0.9), art by Bastien Lecouffe-Deharme, Physically based render, Tranquil Delicate Island and Windmill, at Golden hour, Illustration, Amusing, Fish-eye Lens 
>
>art by Aykut Aydogdu,art by Jacob van Ruisdael, 3D Rendering, extreme wide shot of a Wraith, Crusader ,wearing Floral maxi dress and sandals, background is Strait, Illustration, Modern European Ink Painting, loop lighting, octane engine 
>
>art by Gaston Bussière, Photograph, Cottage Progressive Era Tokyo, Orange and Pink hue
>
>art by Jeffrey T. Larson, Tired Illuminating The Misty Mountains and The River Styx, at Dusk, Vaporwave Art, Rembrandt lighting 
>
>art by Jon Foster,art by Ricardo Bofill, extreme wide shot of a " The Industrial Revolution ", background is Appalachian, tilt shift, New Wave Art, Mono Color 



>( art by Peter Saville :0.7), Layered paper art of a Irritated Airy Blueberry, Screen print, hair light, Depth of field 270mm, Kinemacolor 
>
>( art by Jessie Arms Botke :1.1), ( art by Juan Carreño de Miranda :1.2), ( art by Cerith Wyn Evans :1.2), [ birds-eye-view shot of a Belle Époque portly Tyra Banks cosplaying as Spider-Man, Hosting parties ,wearing Industrial Turquoise Gator skin Tank top and denim skirt, Black hair styled as Space buns, Scarf, background is The Gobi Desert, at Starry night, split diopter, Realistic, Autochrome ::8]
>
>art by Art Spiegelman, Unsightly The Badwater Basin and Stonehenge, Sunny, Ultrarealistic, Psytrance Art, Mono Color 
>
>art by Gerhard Munthe, Long shot of a Classical midweight Asian Chris Hemsworth riding a Koala, Brown hair styled as Short and messy, background is The Palace of Asgard, natural lighting, Low shutter, Film Washi 
>
>art by Peter Eisenman, Vector Art, Serene The Garden of Eden, Stormy weather, Movie still, Peaceful 
( art by Hans Zatzka :1.3), Aquatint of a Compelling Dubrovnik, at Sunrise, Illustration, Orientalism Art, Black lighting, overhead angle 


>art by Guillem H. Pongiluppi, F/1.8 of a " The life of Saint Barbara of Nicomedia ", at Starry night, shallow depth of field, Movie still, Frightening 
>
>art by Jeffrey Smith, close-up shot of a Victorian Bulgarian Kitchen timer, background is The Grand Canyon of the Yellowstone, Spring, Sketch, Peaceful, natural lighting, Calotype 
>
>art by Helen Allingham,art by Étienne Maurice Falconet, Water color painting, Circular polarizer of a Mayan Revival Dominican Female Dragon rider, Auburn hair styled as Messy bun, at Sunrise, deep focus, Sad 
>
>art by Sparth , Spanish Golden Age Tranquil The Angel Oak and Liverpool , Foggy conditions , Screen print , Ukiyo-E , Provia 
>
>by artist Michael Craig-Martin, by artist John Lurie, Zoon lens of a Rustic Fatigued portly Blue Jay, background is Indonesia, Relieving, Mono Color
>
>by artist Brandon Mably, Vector Art, extreme wide shot of a Aggravated Invigorating Fijian snake at Stormy weather, FOV 90 degrees, Vaporwave Art, flat lighting, High Contrast
