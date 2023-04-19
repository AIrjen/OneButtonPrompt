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
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types"]
promptmode = ["at the back", "in the front"]
promptcompounder = [1,2,3,4,5]
ANDtogglemode = ["comma", "AND", "current prompt + AND", "automatic AND"]


class Script(scripts.Script):
    
    def title(self):
        return "One Button Prompt"

    def show(self, is_img2img):
        return True

        
    def ui(self, is_img2img):
        def gen_prompt(insanitylevel, subject, artist, imagetype):

            promptlist = []

            for i in range(5):
                promptlist.append(build_dynamic_prompt(insanitylevel,subject,artist, imagetype))

            return promptlist
        
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


                        1. all --> normally picks a image type as random. Can choose a 'other' more unique type.

                        2. all - force multiple  --> idea by redditor WestWordHoeDown, it forces to choose between 2 and 3 image types
                        
                        3. photograph

                        4. octane render

                        5. digital art

                        6. concept art

                        7. painting

                        6. portrait

                        7. anime key visual
                        
                        8. only other types --> Will pick only from the more unique types, such as stained glass window or a funko pop



                        ### Location of existing prompt

                        <font size="2">
                        If you put a prompt in the prompt field, it will be added onto the generated prompt. You can determine where to put it in the front or the back of the generated prompt.
                        
                        1. at the back

                        2. in the front

                        </font>
                        """
                        )
        with gr.Tab("Advanced"):
            with gr.Row():
                promptcompounderlevel = gr.Dropdown(
                    promptcompounder, label="Prompt compunder", value=1)
            with gr.Row():
                ANDtoggle = gr.Dropdown(
                    ANDtogglemode, label="Prompt seperator mode", value="comma")
            with gr.Row():
                gr.Markdown(
                    """
                    ### Prompt compounder
                    
                    <font size="2">
                    Normally, it creates a single random prompt. With prompt compounder, it will generate multiple prompts and compound them together. 
                    
                    Keep at 1 for normal behavior.
                    Set to different values to compound that many prompts together. My suggestion is to try 2 first.
                    
                    This was originally a bug in the first release when using multiple batches, now brought back as a feature. 
                    Raised by redditor drone2222, to bring this back as a toggle, since it did create interesting results. So here it is. 
                    
                    You can toggle the separator mode. Standardly this is a comma, but you can choose an AND and a newline.
                    
                    You can also choose for "current prompt + AND". This is best used in conjuction with the Latent Couple extension when you want some control. Set the prompt compounder to the amount of objects to generate.

                    "automatic AND" is entirely build around Latent Couple. It will pass artists and the amount of people/animals/objects to generate in the prompt automatically. Set the prompt compounder to the amount of objects to generate.
                    </font>
                    
                    """
                    )
        with gr.Tab("Workflow assist"):
            with gr.Row():
                    silentmode = gr.Checkbox(
                        label="surpressing mode, turns off prompt generation")
            with gr.Row():
                gr.Markdown(
                     """
                     <font size="2"> 
                     Workflow assist, suggestions by redditor Woisek.

                     With silent mode, you turn off the automatic generation of new prompts on generate, and can just use normal prompting. So you can work and finetune any fun prompts without turning of the script.

                     Below here, you can generate a set of random prompts, and start working from there instead. It works on the settings in the Main tab.
                     </font>
                     """)
            with gr.Row():
                genprom = gr.Button("Generate me some prompts!")
            with gr.Row():
                prompt1 = gr.Textbox(label="prompt 1")
            with gr.Row():
                prompt2 = gr.Textbox(label="prompt 2")
            with gr.Row():
                prompt3 = gr.Textbox(label="prompt 3")
            with gr.Row():
                prompt4 = gr.Textbox(label="prompt 4")
            with gr.Row():
                prompt5 = gr.Textbox(label="prompt 5")


        genprom.click(gen_prompt, inputs=[insanitylevel,subject, artist, imagetype], outputs=[prompt1, prompt2, prompt3,prompt4,prompt5])

        return [insanitylevel,subject, artist, imagetype, promptlocation, promptcompounderlevel, ANDtoggle, silentmode]
            
    

    
    def run(self, p, insanitylevel, subject, artist, imagetype, promptlocation, promptcompounderlevel, ANDtoggle, silentmode):
        
        images = []
        infotexts = []

        if(silentmode and p.prompt != ""):
            print("Silent mode turned on, not generating a prompt. Using current prompt.")
        elif(silentmode):
            print("Warning, silent mode is turned on, but no current prompt has been given.")
        elif p.prompt != "":
            print("Prompt is not empty, adding current prompt " + promptlocation + " of the generated prompt")
        
        batches = p.n_iter
        initialbatchsize = p.batch_size
        batchsize = p.batch_size
        p.n_iter = 1
        p.batch_size = 1
        originalprompt = p.prompt



        for i in range(batches):
            
            if(silentmode == False):
                # prompt compounding
                print("Starting generating the prompt")
                preppedprompt = ""
                if(ANDtoggle == "automatic AND" and originalprompt == ""):
                    if(artist != "none"):
                        originalprompt += build_dynamic_prompt(insanitylevel,subject,artist, imagetype, True) 
                    if(subject == "humanoid"):
                        originalprompt += ", " + str(promptcompounderlevel) + " people"
                    if(subject == "landscape"):
                        originalprompt += ", landscape"
                    if(subject == "animal"):
                        originalprompt += ", " + str(promptcompounderlevel)  + " animals"
                    if(subject == "object"):
                        originalprompt += ", " + str(promptcompounderlevel)  + " objects"

                if(ANDtoggle != "AND" and ANDtoggle != "comma" and originalprompt != ""):
                    preppedprompt += originalprompt + " \n AND "
                
                for i in range(promptcompounderlevel):
                    if(ANDtoggle == "automatic AND"):
                        preppedprompt += originalprompt + ", " + build_dynamic_prompt(insanitylevel,subject,"none", imagetype)
                    elif(ANDtoggle != "AND" and ANDtoggle != "comma" and originalprompt != ""):
                        preppedprompt += originalprompt + ", " + build_dynamic_prompt(insanitylevel,subject,artist, imagetype)
                    else:
                        preppedprompt += build_dynamic_prompt(insanitylevel,subject,artist, imagetype)
                    if(i + 1 != promptcompounderlevel):
                        if(ANDtoggle == "comma"):
                            preppedprompt += ", "
                        else:
                            preppedprompt += " \n AND "


                if(promptlocation == "in the front" and originalprompt != "" and (ANDtoggle == "AND" or ANDtoggle == "comma")):
                    p.prompt = originalprompt + ", " + preppedprompt
                elif(promptlocation == "at the back" and originalprompt != "" and (ANDtoggle == "AND" or ANDtoggle == "comma")):
                    p.prompt = preppedprompt + ", " + originalprompt  # add existing prompt to the back?
                else:
                    p.prompt = preppedprompt  # dont add anything


            for j in range(batchsize):
       
                print(" ")
                print("Full prompt to be processed:")
                print(" ")
                print(p.prompt)
                processed = process_images(p)
                images += processed.images
                infotexts += processed.infotexts
            
                # Only move up a seed, when there are multiple batchsizes, and we had the first one done.
                if(initialbatchsize != 1):
                    p.seed += 1
            
            p.seed +=1    
        # just return all the things
        p.n_iter = 0
        p.batch_size = 0
        return Processed(p=p, images_list=images, info=infotexts[0], infotexts=infotexts)