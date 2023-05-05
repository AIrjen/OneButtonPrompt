import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))

from call_txt2img import *
from call_img2img import *
from build_dynamic_prompt import *
from call_extras import *
from model_lists import *



# needs following directories to exist:
# C:\automated_output\
# C:\automated_output\extras\
# C:\automated_output\img2img\
# C:\automated_output\txt2img\
# C:\automated_output\Prompts\
def generateimages(amount = 1, size = "all",model = "currently selected model",samplingsteps = "40",cfg= "7",hiresfix = True,hiressteps ="0",denoisestrength="0.6",samplingmethod="DPM++ SDE Karras", upscaler="R-ESRGAN 4x+", hiresscale="2",apiurl="http://127.0.0.1:7860"):
    loops = int(amount)  # amount of images to generate
    steps = 0

    modellist=get_models()
    samplerlist=get_samplers()
    upscalerlist=get_upscalers()

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

        # cleanup some unsafe things in the filename
        filename = filename.replace("\"", "")
        filename = filename.replace("[", "")
        filename = filename.replace("|", "")
        filename = filename.replace("]", "")
        filename = filename.replace(":", "_")
        filename = re.sub(r'[0-9]+', '', filename)

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
            model = random.choice(modellist)
            print("Going to run on model " + model)

        if(samplingmethod=="all"):
            samplingmethod = random.choice(samplerlist)
            print ("Going to run with sampling method " + samplingmethod)   

        if(upscaler=="all"):
            upscaler = random.choice(upscalerlist)
            print ("Going to run with upscaler " + upscaler)  
            
        txt2img = call_txt2img(randomprompt, size ,hiresfix, 0, filenamecomplete,model ,samplingsteps,cfg, hiressteps, denoisestrength,samplingmethod, upscaler,hiresscale,apiurl)

        
        # upscale via img2img first
        #img2img = call_img2img(txt2img,0.25,1.5,256)

        # upscale via extras upscaler next
        #finalfile = call_extras(img2img)

        steps += 1