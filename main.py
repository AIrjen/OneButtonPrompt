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


def generateimages(amount = 1, size = "all",model = "currently selected model",samplingsteps = "40",cfg= "7",hiresfix = True,hiressteps ="0",denoisestrength="0.6",samplingmethod="DPM++ SDE Karras", upscaler="R-ESRGAN 4x+", hiresscale="2",apiurl="http://127.0.0.1:7860",qualitygate=False,quality="7.6",runs="5",insanitylevel="5",subject="all", artist="all", imagetype="all",silentmode=False, workprompt="", antistring="",prefixprompt="", suffixprompt="", negativeprompt="",promptcompounderlevel = "1", seperator="comma", img2imgbatch = "1", img2imgsamplingsteps = "20", img2imgcfg = "7", img2imgsamplingmethod = "DPM++ SDE Karras", img2imgupscaler = "R-ESRGAN 4x+", img2imgmodel = "currently selected model", img2imgactivate = False, img2imgscale = "2", img2imgpadding = "64",img2imgdenoisestrength="0.3",ultimatesdupscale=False,usdutilewidth = "512", usdutileheight = "0", usdumaskblur = "8", usduredraw ="Linear", usduSeamsfix = "None", usdusdenoise = "0.35", usduswidth = "64", usduspadding ="32", usdusmaskblur = "8",controlnetenabled=False, controlnetmodel="",img2imgdenoisestrengthmod="-0.05",enableextraupscale = False,controlnetblockymode = False,extrasupscaler1 = "all",extrasupscaler2 ="all",extrasupscaler2visiblity="0.5",extrasupscaler2gfpgan="0",extrasupscaler2codeformer="0.15",extrasupscaler2codeformerweight="0.1",extrasresize="2",onlyupscale="false",givensubject="",smartsubject=True):
    loops = int(amount)  # amount of images to generate
    steps = 0
    upscalefilelist=[]
    originalimage = ""
    originalpnginfo =""
    randomprompt = ""
    filename=""
    originalsize=size

    if(onlyupscale==True):
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
        inputupscalemefolder = os.path.join(script_dir, "./automated_outputs/upscale_me/" )
        
        for upscalefilename in os.listdir(inputupscalemefolder):
            f = os.path.join(inputupscalemefolder, upscalefilename)
            # checking if it is a file
            if os.path.isfile(f):
                if(f[-3:]!="txt"):
                    upscalefilelist.append(f)
        
        loops = len(upscalefilelist)

        if(loops==0):
            print('No files to upscale found! Please place images in //upscale_me// folder')
        else:
            print("")
            print("Found and upscaling files")
            print("")


    modellist=get_models()
    samplerlist=get_samplers()
    upscalerlist=get_upscalers()
    img2imgupscalerlist=get_upscalers_for_img2img()
    img2imgsamplerlist=get_samplers_for_img2img()

    if(ultimatesdupscale==False):
        upscalescript="SD upscale"
    else:
        upscalescript="Ultimate SD upscale"

    
    while steps < loops:
        # build prompt
        if(silentmode==True and workprompt == ""):
            print("Trying to use provided workflow prompt, but is empty. Generating a random prompt instead.")
    
        if(onlyupscale==False):  # only do txt2img when onlyupscale is False
            if(silentmode==True and workprompt != ""):
                randomprompt = workprompt
                print("Using provided workflow prompt")
                print(workprompt)

            else:    
                randomprompt = build_dynamic_prompt(insanitylevel,subject,artist,imagetype, False,antistring,prefixprompt,suffixprompt,promptcompounderlevel, seperator,givensubject,smartsubject)

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
            if(originalsize == "all"):
                sizelist = ["portrait", "wide", "square"]
                size = random.choice(sizelist)


            #Check if there is any random value we have to choose or not
            if(model=="all"):
                model = random.choice(modellist)
                #lets not do inpainting models
                while "inpaint" in model:
                    model = random.choice(modellist)
                    print("Going to run with model " + model)

            if(samplingmethod=="all"):
                samplingmethod = random.choice(samplerlist)
                print ("Going to run with sampling method " + samplingmethod)   

            if(upscaler=="all" and hiresfix == True):
                upscaler = random.choice(upscalerlist)
                print ("Going to run with upscaler " + upscaler)

            # WebUI fix for PLMS and UniPC and hiresfix
            if(samplingmethod in ['PLMS', 'UniPC']):  # PLMS/UniPC do not support hirefix so we just silently switch to DDIM
                samplingmethod = 'DDIM'



                
            txt2img = call_txt2img(randomprompt, size ,hiresfix, 0, filenamecomplete,model ,samplingsteps,cfg, hiressteps, denoisestrength,samplingmethod, upscaler,hiresscale,apiurl,qualitygate,quality,runs,negativeprompt)
            originalimage = txt2img[0] #Set this for later use
            originalpnginfo = txt2img[1] #Sort of hacky way of bringing this forward. But if it works, it works

            image = txt2img[0]
        else:
            if(filename==""):
                filename = str(uuid.uuid4())
            
            # create a datetime object for the current date and time
            now = datetime.now()
            filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip()
            image = upscalefilelist[steps]  # else we get the image from the upscale file list
            originalimage = image # this is also the original image file

        
        # upscale via img2img

        img2imgloops = int(img2imgbatch)
        if(img2imgactivate == False):  # If we dont want to run, turn it off
            img2imgloops = 0
        img2imgsteps = 0
        
        # start the batching!
        while img2imgsteps < img2imgloops:


            #Check if there is any random value we have to choose or not
            if(img2imgmodel=="all"):
                img2imgmodel = random.choice(modellist)
                #lets not do inpainting models
                while "inpaint" in model:
                    img2imgmodel = random.choice(modellist)
                    print("Going to upscale with model " + img2imgmodel)

            if(img2imgsamplingmethod=="all"):
                img2imgsamplingmethod = random.choice(img2imgsamplerlist)
                print ("Going to upscale with sampling method " + img2imgsamplingmethod)   

            if(img2imgupscaler=="all"):
                img2imgupscaler = random.choice(img2imgupscalerlist)
                print ("Going to run with upscaler " + img2imgupscaler)

            # WebUI fix for PLMS and UniPC and img2img
            if(img2imgsamplingmethod in ['PLMS', 'UniPC']):  # PLMS/UniPC do not support img2img so we just silently switch to DDIM
                img2imgsamplingmethod = 'DDIM'

            img2img = call_img2img(image, originalimage, originalpnginfo, apiurl, filenamecomplete, randomprompt,negativeprompt,img2imgsamplingsteps, img2imgcfg, img2imgsamplingmethod, img2imgupscaler, img2imgmodel, img2imgdenoisestrength, img2imgscale, img2imgpadding,upscalescript,usdutilewidth, usdutileheight, usdumaskblur, usduredraw, usduSeamsfix, usdusdenoise, usduswidth, usduspadding, usdusmaskblur,controlnetenabled, controlnetmodel,controlnetblockymode)
            
            image = img2img[0]
            if(originalpnginfo==""):
                originalpnginfo = img2img[1]

            img2imgdenoisestrength = str(float(img2imgdenoisestrength) + float(img2imgdenoisestrengthmod)) # lower or increase the denoise strength for each batch
            img2imgpadding = int(int(img2imgpadding) * float(img2imgscale)) # also increase padding by scale

            if(int(img2imgpadding)>256): # but not overdo it :D
                img2imgpadding="256"
            
            img2imgsteps += 1

        # upscale via extras upscaler next
        
        if(enableextraupscale==True):
            if(extrasupscaler1=="all"):
                extrasupscaler1 = random.choice(img2imgupscalerlist)
                print ("Going to upscale with upscaler 1 " + extrasupscaler1)
            
            if(extrasupscaler2=="all"):
                extrasupscaler2 = random.choice(img2imgupscalerlist)
                print ("Going to upscale with upscaler 2 " + extrasupscaler2)

            image = call_extras(image, originalimage, originalpnginfo, apiurl, filenamecomplete,extrasupscaler1,extrasupscaler2 ,extrasupscaler2visiblity,extrasupscaler2gfpgan,extrasupscaler2codeformer,extrasupscaler2codeformerweight,extrasresize)

        steps += 1
    

    print("")
    print("All done!")
