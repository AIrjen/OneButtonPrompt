import sys, os
import random
import uuid
from datetime import datetime
sys.path.append(os.path.abspath(".."))

from call_txt2img import *
from call_img2img import *
from build_dynamic_prompt import *
from call_extras import *



# needs following directories to exist:
# C:\automated_output\
# C:\automated_output\extras\
# C:\automated_output\img2img\
# C:\automated_output\txt2img\
# C:\automated_output\Prompts\
def generateimages(amount = 1, size = "all",model = "currently selected model",samplingsteps = "40",cfg= "7",hiresfix = True,hiressteps ="0",denoisestrength="0.6",samplingmethod="DPM++ SDE Karras", upscaler="R-ESRGAN 4x+",modellist=[], samplerlist=[],upscalerlist=[]):
    loops = int(amount)  # amount of images to generate
    steps = 0

    while steps < loops:
        # build prompt
        randomprompt = build_dynamic_prompt(7,"all","all","all", False)

        # make the filename, from from a to the first comma
        start_index = randomprompt.find("of a ") + len("of a ")

        # find the index of the first comma after "of a" or end of the prompt
        end_index = randomprompt.find(",", start_index)
        if(end_index == -1):
            end_index=len(randomprompt)

        # extract the desired substring using slicing
        filename = randomprompt[start_index:end_index]
        filename = filename.replace("\"", "_")

        if(filename==""):
            filename = str(uuid.uuid4())
        
        # create a datetime object for the current date and time
        now = datetime.now()
        filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip()

        # prompt + size
        if(size == "all"):
            sizelist = ["portrait", "wide", "square", "ultrawide"]
            size = random.choice(sizelist)


        #Check if there is any random value we have to choose or not
        if(model=="all"):
            modellist.remove("all")
            modellist.remove("currently selected model")
            model = random.choice(modellist)

        if(samplingmethod=="all"):
            samplerlist.remove("all")
            samplingmethod = random.choice(samplerlist)

        if(upscaler=="all"):
            upscalerlist.remove("all")
            upscaler = random.choice(upscalerlist)
            
        txt2img = call_txt2img(randomprompt, size ,hiresfix, 0, filenamecomplete,model ,samplingsteps,cfg, hiressteps, denoisestrength,samplingmethod, upscaler)

        
        # upscale via img2img first
        #img2img = call_img2img(txt2img,0.25,1.5,256)

        # upscale via extras upscaler next
        #finalfile = call_extras(img2img)

        steps += 1