import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state


from build_dynamic_prompt import *
from main import *
from model_lists import *

subjects = ["all","object","animal","humanoid", "landscape", "concept"]
artists = ["all", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types"]
promptmode = ["at the back", "in the front"]
promptcompounder = ["1", "2", "3", "4", "5"]
ANDtogglemode = ["none", "automatic", "prefix AND prompt + suffix", "prefix + prefix + prompt + suffix"]
seperatorlist = ["comma", "AND", "BREAK"]

#for autorun and upscale
sizelist = ["all", "portrait", "wide", "square", "ultrawide"]

modellist = get_models()
modellist.insert(0,"all")
modellist.insert(0,"currently selected model") # First value us the currently selected model

upscalerlist = get_upscalers()
upscalerlist.insert(0,"automatic")
upscalerlist.insert(0,"all")

samplerlist = get_samplers()
samplerlist.insert(0,"all")

#for img2img
img2imgupscalerlist = get_upscalers_for_img2img()
img2imgupscalerlist.insert(0,"automatic")
img2imgupscalerlist.insert(0,"all")

#for ultimate SD upscale

seams_fix_types = ["None","Band pass","Half tile offset pass","Half tile offset pass + intersections"]
redraw_modes = ["Linear","Chess","None"]


class Script(scripts.Script):
    
    def title(self):
        return "One Button Prompt"

    def show(self, is_img2img):
        return True

        
    def ui(self, is_img2img):
        def gen_prompt(insanitylevel, subject, artist, imagetype, antistring, prefixprompt, suffixprompt, promptcompounderlevel, seperator):

            promptlist = []

            for i in range(5):
                promptlist.append(build_dynamic_prompt(insanitylevel,subject,artist, imagetype, False, antistring,prefixprompt,suffixprompt,promptcompounderlevel,seperator))

            return promptlist
        
        def prompttoworkflowprompt(text):
            return text
            

        with gr.Tab("Main"):
            with gr.Row():
                insanitylevel = gr.Slider(1, 10, value=7, step=1, label="Higher levels increases complexity and randomness of generated prompt")
            with gr.Row():
                with gr.Column(scale=1, variant="compact"):
                    subject = gr.Dropdown(
                                    subjects, label="Subject Types", value="all")
                with gr.Column(scale=1, variant="compact"):
                    artist = gr.Dropdown(
                                    artists, label="Artists", value="all")
                with gr.Column(scale=2, variant="compact"):
                    imagetype = gr.Dropdown(
                                    imagetypes, label="type of image", value="all")
            with gr.Row():
                with gr.Column():
                    prefixprompt = gr.Textbox(label="Place this in front of generated prompt (prefix)",value="")
                    suffixprompt = gr.Textbox(label="Place this at back of generated prompt (suffix)",value="")
                    negativeprompt = gr.Textbox(label="Use this negative prompt",value="")
            with gr.Row():
                with gr.Column():
                    antistring = gr.Textbox(label="Filter out following properties (comma seperated). Example ""film grain, purple, cat"" ")
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



                        ### Other prompt fields

                        The existing prompt and negative prompt fields are ignored.
                        
                        Add a prompt prefix, suffix and the negative prompt in the respective fields. They will be automatically added during processing.

                        </font>

                        ### Filter values
                        <font size="2">
                        You can put comma seperated values here, those will be ignored from any list processing. For example, adding ""film grain, sepia"", will make these values not appear during generation.

                        For advanced users, you can create a permanent file in \\OneButtonPrompt\\userfiles\\ called antilist.csv
                        
                        This way, you don't ever have to add it manually again. This file won't be overwritten during upgrades.

                        Idea by redditor jonesaid.

                        </font>
                        """
                        )
        with gr.Tab("Workflow assist"):
            with gr.Row():
                    silentmode = gr.Checkbox(
                        label="Workflow mode, turns off prompt generation and uses below Workflow prompt instead.")
            with gr.Row():
                workprompt = gr.Textbox(label="Workflow prompt")
            with gr.Row():
                gr.Markdown(
                     """
                     <font size="2"> 
                     Workflow assist, suggestions by redditor Woisek.

                     With Workflow mode, you turn off the automatic generation of new prompts on 'generate', and it will use the Workflow prompt field instead. So you can work and finetune any fun prompts without turning of the script.

                     Below here, you can generate a set of random prompts, and send them to the Workflow prompt field. The generation of the prompt uses the settings in the Main tab.
                     </font>
                     """)
            with gr.Row():
                genprom = gr.Button("Generate me some prompts!")
            with gr.Row():
                    with gr.Column(scale=4):
                        prompt1 = gr.Textbox(label="prompt 1")
                    with gr.Column(scale=1, variant="compact"):
                        prompt1toworkflow = gr.Button("Send prompt up")
            with gr.Row():
                    with gr.Column(scale=4):
                        prompt2 = gr.Textbox(label="prompt 2")
                    with gr.Column(scale=1, variant="compact"):
                        prompt2toworkflow = gr.Button("Send prompt up")
            with gr.Row():
                    with gr.Column(scale=4):
                        prompt3 = gr.Textbox(label="prompt 3")
                    with gr.Column(scale=1, variant="compact"):
                        prompt3toworkflow = gr.Button("Send prompt up")
            with gr.Row():
                    with gr.Column(scale=4):
                        prompt4 = gr.Textbox(label="prompt 4")
                    with gr.Column(scale=1, variant="compact"):
                        prompt4toworkflow = gr.Button("Send prompt up")
            with gr.Row():
                    with gr.Column(scale=4):
                        prompt5 = gr.Textbox(label="prompt 5")
                    with gr.Column(scale=1, variant="compact"):
                        prompt5toworkflow = gr.Button("Send prompt up")
        with gr.Tab("Advanced"):
            with gr.Row():
                with gr.Column(scale=1):
                    promptcompounderlevel = gr.Dropdown(
                        promptcompounder, label="Prompt compounder", value="1")
            with gr.Row():
                with gr.Column(scale=1):
                    seperator = gr.Dropdown(
                        seperatorlist, label="Prompt seperator", value="comma")    
                with gr.Column(scale=2):
                    ANDtoggle = gr.Dropdown(
                        ANDtogglemode, label="Prompt seperator mode", value="none")
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
                    
                    You can toggle the separator mode. Standardly this is a comma, but you can choose an AND or a BREAK.
                    
                    You can also choose the prompt seperator mode for use with Latent Couple extension
                    
                    Example flow:

                    Set the Latent Couple extension to 2 area's (standard setting)
                    
                    In the main tab, set the subject to humanoids
                    
                    In the prefix prompt field then add for example: Art by artistname, 2 people
                    
                    Set the prompt compounder to: 2
                    
                    Set the Prompt seperator to: AND

                    Set the Prompt Seperator mode to: prefix AND prompt + suffix

                    "automatic" is entirely build around Latent Couple. It will pass artists and the amount of people/animals/objects to generate in the prompt automatically. Set the prompt compounder equal to the amount of areas defined in Laten Couple.
                    
                    Example flow:

                    Set the Latent Couple extension to 2 area's (standard setting)
                    
                    In the main tab, set the subject to humanoids
                    
                    Leave the prompt field empty
                    
                    Set the prompt compounder to: 2

                    Set the Prompt seperator to: AND

                    Set the Prompt Seperator mode to: automatic


                    </font>
                    
                    """
                    )
        with gr.Tab("One Button Run and Upscale"):
            with gr.Row():
                    gr.Markdown(
                            """
                            ### TXT2IMG
                            <font size="2">
                            Start WebUi with option --api for this to work.
                            </font>
                            """
                            )                         
            with gr.Row():
                    with gr.Column(scale=1):
                        startmain = gr.Button("Start generating and upscaling!")
                        apiurl = gr.Textbox(label="URL", value="http://127.0.0.1:7860")
                    with gr.Column(scale=1):
                        onlyupscale = gr.Checkbox(label="Don't generate, only upscale", value=False)
                        gr.Markdown(
                                """
                                <font size="2">
                                Only upscale will not use txt2img to generate an image.

                                Instead it will pick up all files in the \\upscale_me\\ folder and upscale them with below settings.
                                </font>
                                """
                                )   
            with gr.Row():
                with gr.Column(scale=1):
                    
                    amountofimages = gr.Slider(1, 50, value="20", step=1, label="Amount of images to generate")
                    size = gr.Dropdown(
                                    sizelist, label="Size to generate", value="all")
                    with gr.Row(scale=1):
                        samplingsteps = gr.Slider(1, 100, value="20", step=1, label="Sampling steps")
                        cfg = gr.Slider(1,20, value="6.0", step=0.1, label="CFG")
                    with gr.Row(scale=1):                              
                        hiresfix = gr.Checkbox(label="hires. fix", value=True)
                        hiressteps = gr.Slider(0, 100, value = "0", step=1, label="Hires steps")
                        hiresscale = gr.Slider(1, 4, value = "2", step=0.05, label="Scale")
                        denoisestrength = gr.Slider(0, 1, value="0.60", step=0.01, label="Denoise strength")
                with gr.Column(scale=1):
                    
                    model = gr.Dropdown(
                                    modellist, label="model to use", value="currently selected model")
                    with gr.Column(scale=1):
                        samplingmethod = gr.Dropdown(
                                        samplerlist, label= "Sampler", value="all")
                        upscaler = gr.Dropdown(
                                        upscalerlist, label="hires upscaler", value="all")
            with gr.Row():
                gr.Markdown(
                        """
                        ### Quality Gate
                        <font size="2">
                        Uses aesthetic image scorer extension to check the quality of the image.
                        
                        Once turned on, it will retry for n amount of times to get an image with the quality score. If not, it will take the best image so far and continue.
                        
                        Idea and inspiration by xKean. 
                        </font>
                        """
                        )    
            with gr.Row():
                    qualitygate = gr.Checkbox(label="Quality Gate", value=False)
                    quality = gr.Slider(1, 10, value = "7.2", step=0.1, label="Quality", visible = False)
                    runs = gr.Slider(1, 50, value = "5", step=1, label="Amount of tries", visible = False)
            with gr.Row():
                    gr.Markdown(
                        """
                        ### IMG2IMG upscale
                        """
                        )
            with gr.Row():
                    img2imgactivate = gr.Checkbox(label="Upscale image with IMG2IMG", value=True)
            with gr.Row():
                    with gr.Column(scale=1):
                        img2imgbatch = gr.Slider(1, 5, value="1", step=1, label="Amount times to repeat upscaling with IMG2IMG (loopback)")
                        img2imgsamplingsteps = gr.Slider(1, 100, value="20", step=1, label="img2img Sampling steps")
                        img2imgcfg = gr.Slider(1,20, value="6", step=0.1, label="img2img CFG")
                        img2imgdenoisestrength = gr.Slider(0, 1, value="0.30", step=0.01, label="img2img denoise strength")
                        img2imgdenoisestrengthmod = gr.Slider(-1,1, value = "-0.05", step=0.01, label="adjust denoise each img2img batch")
                    with gr.Column(scale=1):
                        img2imgmodel = gr.Dropdown(
                                    modellist, label="img2img model to use", value="currently selected model")
                        img2imgsamplingmethod = gr.Dropdown(
                                        samplerlist, label= "img2img sampler", value="all")   
                        img2imgupscaler = gr.Dropdown(
                                        img2imgupscalerlist, label="img2img upscaler", value="all")
                    with gr.Row():
                        img2imgscale = gr.Slider(1, 4, value="2", step=0.05, label="img2img scale")
                        img2imgpadding = gr.Slider(32, 256, value="64", step=12, label="img2img padding")
            with gr.Row():
                    ultimatesdupscale = gr.Checkbox(label="Use Ultimate SD Upscale script instead", value=False)
                    gr.Markdown(
                        """
                        <font size="2">
                        This requires the Ultimate SD Upscale extension, install this if you haven't
                        </font>
                        """
                        )
            with gr.Row():
                    with gr.Column(scale = 1):
                        #usdutilewidth, usdutileheight, usdumaskblur, usduredraw, usduSeamsfix, usdusdenoise, usduswidth, usduspadding, usdusmaskblur
                        #usdutilewidth = "512", usdutileheight = "0", usdumaskblur = "8", usduredraw ="Linear", usduSeamsfix = "None", usdusdenoise = "0.35", usduswidth = "64", usduspadding ="32", usdusmaskblur = "8"
                        usdutilewidth = gr.Slider(0, 2048, value="512", step=12, label="tile width", visible = False)
                        usdutileheight = gr.Slider(0, 2048, value="0", step=12, label="tile height", visible = False)
                        usdumaskblur = gr.Slider(0, 64, value="8", step=1, label="Mask blur", visible = False)
                        usduredraw = gr.Dropdown(
                                    redraw_modes, label="Type", value="Linear", visible = False)
                    with gr.Column(scale = 1):
                        usduSeamsfix = gr.Dropdown(
                                    seams_fix_types, label="Seams fix", value="None", visible = False)
                        usdusdenoise = gr.Slider(0, 1, value="0.35", step=0.01, label="Seams  denoise strenght", visible = False)
                        usduswidth = gr.Slider(0, 128, value="64", step=12, label="Seams Width", visible = False)
                        usduspadding = gr.Slider(0, 128, value="32", step=12, label="Seams padding", visible = False)
                        usdusmaskblur = gr.Slider(0, 64, value="8", step=1, label="Seams Mask blur (offset pass only)", visible = False)
            with gr.Row():
                    with gr.Column(scale = 1):
                        controlnetenabled = gr.Checkbox(label="Enable controlnet tile resample", value=False)
                        controlnetblockymode = gr.Checkbox(label="also enable wierd blocky upscale mode", value=False)
                    with gr.Column(scale = 1):
                        controlnetmodel = gr.Textbox(label="Controlnet tile model name", value = "control_v11f1e_sd15_tile [a371b31b]")
            with gr.Row():
                 gr.Markdown(
                                """
                                <font size="2">
                                This requires Controlnet 1.1 extension and the tile resample model, install this if you haven't
                                In settings for Controlnet, enable "Allow other script to control this extension"
                                
                                Don't use wierd blocky upscale mode. Or maybe do?
                                </font>
                                """
                                )
            with gr.Row():
                 with gr.Column(scale = 1):
                            enableextraupscale = gr.Checkbox(label="Enable upscale with extras", value=False)
            with gr.Row():
                 with gr.Column(scale = 1):
                            extrasresize = gr.Slider(0, 8, value="2", step=0.05, label="Upscale resize", visible = False)
                            extrasupscaler1 = gr.Dropdown(
                                        img2imgupscalerlist, label="upscaler 1", value="all", visible = False)
                            extrasupscaler2 = gr.Dropdown(
                                        img2imgupscalerlist, label="upscaler 2", value="all", visible = False)
                            extrasupscaler2visiblity = gr.Slider(0, 1, value="0.5", step=0.05, label="Upscaler 2 vis.", visible = False)
                 with gr.Column(scale = 1):
                            extrasupscaler2gfpgan = gr.Slider(0, 1, value="0", step=0.05, label="GFPGAN vis.", visible = False)
                            extrasupscaler2codeformer = gr.Slider(0, 1, value="0.15", step=0.05, label="CodeFormer vis.", visible = False)
                            extrasupscaler2codeformerweight = gr.Slider(0, 1, value="0.1", step=0.05, label="CodeFormer weight", visible = False)
                    

        genprom.click(gen_prompt, inputs=[insanitylevel,subject, artist, imagetype, antistring,prefixprompt, suffixprompt,promptcompounderlevel, seperator], outputs=[prompt1, prompt2, prompt3,prompt4,prompt5])

        prompt1toworkflow.click(prompttoworkflowprompt, inputs=prompt1, outputs=workprompt)
        prompt2toworkflow.click(prompttoworkflowprompt, inputs=prompt2, outputs=workprompt)
        prompt3toworkflow.click(prompttoworkflowprompt, inputs=prompt3, outputs=workprompt)
        prompt4toworkflow.click(prompttoworkflowprompt, inputs=prompt4, outputs=workprompt)
        prompt5toworkflow.click(prompttoworkflowprompt, inputs=prompt5, outputs=workprompt)

        startmain.click(generateimages, inputs=[amountofimages,size,model,samplingsteps,cfg,hiresfix,hiressteps,denoisestrength,samplingmethod, upscaler,hiresscale, apiurl, qualitygate, quality, runs,insanitylevel,subject, artist, imagetype, silentmode, workprompt, antistring, prefixprompt, suffixprompt,negativeprompt,promptcompounderlevel, seperator, img2imgbatch, img2imgsamplingsteps, img2imgcfg, img2imgsamplingmethod, img2imgupscaler, img2imgmodel,img2imgactivate, img2imgscale, img2imgpadding,img2imgdenoisestrength,ultimatesdupscale,usdutilewidth, usdutileheight, usdumaskblur, usduredraw, usduSeamsfix, usdusdenoise, usduswidth, usduspadding, usdusmaskblur, controlnetenabled, controlnetmodel,img2imgdenoisestrengthmod,enableextraupscale,controlnetblockymode,extrasupscaler1,extrasupscaler2,extrasupscaler2visiblity,extrasupscaler2gfpgan,extrasupscaler2codeformer,extrasupscaler2codeformerweight,extrasresize,onlyupscale])
        
        # Turn things off and on for onlyupscale and txt2img
        def onlyupscalevalues(onlyupscale):
             onlyupscale = not onlyupscale
             return {
                  amountofimages: gr.update(visible=onlyupscale),
                  size: gr.update(visible=onlyupscale),
                  samplingsteps: gr.update(visible=onlyupscale),
                  cfg: gr.update(visible=onlyupscale),

                  hiresfix: gr.update(visible=onlyupscale),
                  hiressteps: gr.update(visible=onlyupscale),
                  hiresscale: gr.update(visible=onlyupscale),
                  denoisestrength: gr.update(visible=onlyupscale),
                  upscaler: gr.update(visible=onlyupscale),

                  model: gr.update(visible=onlyupscale),
                  samplingmethod: gr.update(visible=onlyupscale),
                  upscaler: gr.update(visible=onlyupscale),

                  qualitygate: gr.update(visible=onlyupscale),
                  quality: gr.update(visible=onlyupscale),
                  runs: gr.update(visible=onlyupscale)

             }
        
        onlyupscale.change(
            onlyupscalevalues,
            [onlyupscale],
            [amountofimages,size,samplingsteps,cfg,hiresfix,hiressteps,hiresscale,denoisestrength,upscaler,model,samplingmethod,upscaler,qualitygate,quality,runs]
        )
        
        
        # Turn things off and on for hiresfix
        def hireschangevalues(hiresfix):
             return {
                  hiressteps: gr.update(visible=hiresfix),
                  hiresscale: gr.update(visible=hiresfix),
                  denoisestrength: gr.update(visible=hiresfix),
                  upscaler: gr.update(visible=hiresfix)
             }
        
        hiresfix.change(
            hireschangevalues,
            [hiresfix],
            [hiressteps,hiresscale,denoisestrength,upscaler]
        )

        # Turn things off and on for quality gate
        def qgatechangevalues(qualitygate):
             return {
                  quality: gr.update(visible=qualitygate),
                  runs: gr.update(visible=qualitygate)
             }
        
        qualitygate.change(
            qgatechangevalues,
            [qualitygate],
            [quality,runs]
        )
        
        # Turn things off and on for USDU
        def ultimatesdupscalechangevalues(ultimatesdupscale):
             return {
                  usdutilewidth: gr.update(visible=ultimatesdupscale),
                  usdutileheight: gr.update(visible=ultimatesdupscale),
                  usdumaskblur: gr.update(visible=ultimatesdupscale),
                  usduredraw: gr.update(visible=ultimatesdupscale),

                  usduSeamsfix: gr.update(visible=ultimatesdupscale),
                  usdusdenoise: gr.update(visible=ultimatesdupscale),
                  usduswidth: gr.update(visible=ultimatesdupscale),
                  usduspadding: gr.update(visible=ultimatesdupscale),
                  usdusmaskblur: gr.update(visible=ultimatesdupscale)
             }
        
        ultimatesdupscale.change(
            ultimatesdupscalechangevalues,
            [ultimatesdupscale],
            [usdutilewidth,usdutileheight,usdumaskblur,usduredraw,usduSeamsfix,usdusdenoise,usduswidth,usduspadding,usdusmaskblur]
        )

        # Turn things off and on for EXTRAS
        def enableextraupscalechangevalues(enableextraupscale):
             return {
                  extrasupscaler1: gr.update(visible=enableextraupscale),
                  extrasupscaler2: gr.update(visible=enableextraupscale),
                  extrasupscaler2visiblity: gr.update(visible=enableextraupscale),
                  extrasresize: gr.update(visible=enableextraupscale),

                  extrasupscaler2gfpgan: gr.update(visible=enableextraupscale),
                  extrasupscaler2codeformer: gr.update(visible=enableextraupscale),
                  extrasupscaler2codeformerweight: gr.update(visible=enableextraupscale)
             }
        
        enableextraupscale.change(
            enableextraupscalechangevalues,
            [enableextraupscale],
            [extrasupscaler1,extrasupscaler2,extrasupscaler2visiblity,extrasresize, extrasupscaler2gfpgan,extrasupscaler2codeformer,extrasupscaler2codeformerweight]
        )



        return [insanitylevel,subject, artist, imagetype, prefixprompt,suffixprompt,negativeprompt, promptcompounderlevel, ANDtoggle, silentmode, workprompt, antistring, seperator]
            
    

    
    def run(self, p, insanitylevel, subject, artist, imagetype, prefixprompt,suffixprompt,negativeprompt, promptcompounderlevel, ANDtoggle, silentmode, workprompt, antistring,seperator):
        
        images = []
        infotexts = []
        all_seeds = []
        all_prompts = []

        batches = p.n_iter
        initialbatchsize = p.batch_size
        batchsize = p.batch_size
        p.n_iter = 1
        p.batch_size = 1
        

        if(silentmode and workprompt != ""):
            print("Workflow mode turned on, not generating a prompt. Using workflow prompt.")
        elif(silentmode):
            print("Warning, workflow mode is turned on, but no workprompt has been given.")
        elif p.prompt != "" or p.negative_prompt != "":
            print("Please note that existing prompt and negative prompt fields are (no longer) used")
        
        if(ANDtoggle == "automatic" and artist == "none"):
            print("Automatic and artist mode set to none, don't work together well. Ignoring this setting!")
            artist = "all"

        if(ANDtoggle == "automatic" and (prefixprompt != "")):
            print("Automatic doesnt work well if there is an prefix prompt filled in. Ignoring this prompt fields!")
            prefixprompt = ""

        


        for i in range(batches):
            
            if(silentmode == False):
                # prompt compounding
                print("Starting generating the prompt")
                preppedprompt = ""
                
                if(ANDtoggle == "automatic"):
                    preppedprompt += prefixprompt + ", "
                    if(artist != "none"):
                        preppedprompt += build_dynamic_prompt(insanitylevel,subject,artist, imagetype, True, antistring) 
                    if(subject == "humanoid"):
                        preppedprompt += ", " + promptcompounderlevel + " people"
                    if(subject == "landscape"):
                        preppedprompt += ", landscape"
                    if(subject == "animal"):
                        preppedprompt += ", " + promptcompounderlevel  + " animals"
                    if(subject == "object"):
                        preppedprompt += ", " + promptcompounderlevel  + " objects"

                if(ANDtoggle != "none" and ANDtoggle != "automatic"):
                    preppedprompt += prefixprompt
                
                if(ANDtoggle != "none"):
                    if(ANDtoggle!="prefix + prefix + prompt + suffix"):
                        prefixprompt = ""
                    if(seperator == "comma"):
                        preppedprompt += " \n , "
                    else:
                        preppedprompt += " \n " + seperator + " "
                      
                #Here is where we build a "normal" prompt
                preppedprompt += build_dynamic_prompt(insanitylevel,subject,artist, imagetype, False, antistring, prefixprompt, suffixprompt,promptcompounderlevel, seperator)

                # set everything ready
                p.prompt = preppedprompt  
                p.negative_prompt = negativeprompt

            if(silentmode == True):
                p.prompt = workprompt

            for j in range(batchsize):
       
                print(" ")
                print("Full prompt to be processed:")
                print(" ")
                print(p.prompt)
                processed = process_images(p)
                images += processed.images
                infotexts += processed.infotexts
                all_seeds.append(processed.seed)
                all_prompts.append(processed.prompt)
            
                # Only move up a seed, when there are multiple batchsizes, and we had the first one done.
                if(initialbatchsize != 1):
                    p.seed += 1
            
            p.seed +=1    
        # just return all the things
        p.n_iter = 0
        p.batch_size = 0
        return Processed(p=p, images_list=images, info=infotexts[0], infotexts=infotexts, all_seeds=all_seeds, all_prompts=all_prompts)
