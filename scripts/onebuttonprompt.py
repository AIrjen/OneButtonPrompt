import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

from build_dynamic_prompt import *

subjects = ["all","object","animal","humanoid", "landscape", "concept"]
artists = ["all", "none"]
imagetypes = ["all", "photograph", "octane render","digital art","concept art", "painting", "portait"]
promptmode = ["at the back", "in the front"]


class Script(scripts.Script):
    
    def title(self):
        return "One Button Prompt"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        with gr.Tab("Main"):
            with gr.Row():
                insanitylevel = gr.Slider(1, 10, value=7, step=1, label="Higher levels increases complexity and randomness of generated prompt")
            with gr.Row():
                with gr.Column():
                    subject = gr.Dropdown(
                                    subjects, label="Subject Types", value="all")
                with gr.Column():
                    artist = gr.Dropdown(
                                    artists, label="Artists", value="all")
                with gr.Column():
                    imagetype = gr.Dropdown(
                                    imagetypes, label="type of image", value="all")
            with gr.Row():
                with gr.Column():
                    promptlocation = gr.Dropdown(
                                    promptmode, label="Location of existing prompt", value="at the back")
            with gr.Row():
                    gr.Markdown(
                        """
                        ### Description
                        
                        <font size="2">
                        This generator will generate a complete full prompt for you, based on randomness. You can increase the slider, to include more things to put into the prompt. 
                        Recommended is keeping it around 3-7. Use 10 at your own risk.

                        There are a lot of special things build in, based on various research papers. Just try it, and let it surprise you.

                        Suggestion is to leave the prompt field empty, anything here will be added at the end of the generated prompt.  
                        It doesn't add anything to the negative prompt field, so feel free to add your favorite negative prompts here.  
                        </font>
                        
                        ### Subject Types
                        
                        <font size="2">
                        You can choose a certain subject type, if you want to generate something more specific. It has the following types:  
                        
                        1. object - Can be a random object, a building or a vehicle.  
                        
                        2. animal - A random (fictional) animal. Has a chance to have human characteristics, such as clothing added.  
                        
                        3. humanoid - A random humanoid, males, females, fantasy types, fictional and non-fictional characters. Can add clothing, features and a bunch of other things.  
                        
                        4. landscape - A landscape or a landscape with a building.  
                        
                        5. concept - Can be a concept, such as "a X of Y", or an historical event such as "The Trojan War".  

                        </font>
                        
                        ### Artists
                        
                        <font size="2">
                        Artists have a major impact on the result. Automatically, it will select between 0-3 artists out of 3483 artists for your prompt.  
                        
                        You can turn it off. Add your own artists to the prompt, and they will be added to the end of the prompt.
                        </font>

                        ### type of image

                        <font size="2">
                        There are an immense number of image types, not only paintings and photo's, but also isometric renders and funko pops.
                        You can however, overwrite it with the most popular ones.
                        
                        1. photograph

                        2. octane render

                        3. digital art

                        4. concept art

                        5. painting

                        6. portait

                        </font>
                        """
                        )
        return [insanitylevel,subject, artist, imagetype, promptlocation]
            
    def run(self, p, insanitylevel, subject, artist, imagetype, promptlocation):
        
        images = []
        infotexts = []

        if p.prompt != "":
            print("Prompt is not empty, adding current prompt " + promptlocation + " of the generated prompt")
        
        batches = p.n_iter
        initialbatchsize = p.batch_size
        batchsize = p.batch_size
        p.n_iter = 1
        p.batch_size = 1
        originalprompt = p.prompt


        for i in range(batches):
            
            if(promptlocation == "in the front"):
                p.prompt = originalprompt + ", " + build_dynamic_prompt(insanitylevel,subject,artist, imagetype)
            else:
                p.prompt = build_dynamic_prompt(insanitylevel,subject,artist, imagetype) + ", " + originalprompt  # add existing prompt to the back?
            for j in range(batchsize):
       
                processed = process_images(p)
                images += processed.images
                infotexts += processed.infotexts
            
                # Only move up a seed, when there are multiple batchsizes, and we had the first one done.
                if(initialbatchsize != 1):
                    p.seed += 1
                
        # just return all the things
        p.n_iter = 0
        p.batch_size = 0
        return Processed(p=p, images_list=images, info=infotexts[0], infotexts=infotexts)