import sys, os
import random
import uuid
import re
from datetime import datetime
import time
sys.path.append(os.path.abspath(".."))

from call_txt2img import *
from call_img2img import *
from build_dynamic_prompt import *
from call_extras import *
from model_lists import *


def generateimages(amount = 1, size = "all",model = "currently selected model",samplingsteps = "40",cfg= "7",hiresfix = True,hiressteps ="0",denoisestrength="0.6",samplingmethod="DPM++ SDE Karras", upscaler="R-ESRGAN 4x+", hiresscale="2",apiurl="http://127.0.0.1:7860",qualitygate=False,quality="7.6",runs="5",insanitylevel="5",subject="all", artist="all", imagetype="all",silentmode=False, workprompt="", antistring="",prefixprompt="", suffixprompt="", negativeprompt="",promptcompounderlevel = "1", seperator="comma", img2imgbatch = "1", img2imgsamplingsteps = "20", img2imgcfg = "7", img2imgsamplingmethod = "DPM++ SDE Karras", img2imgupscaler = "R-ESRGAN 4x+", img2imgmodel = "currently selected model", img2imgactivate = False, img2imgscale = "2", img2imgpadding = "64",img2imgdenoisestrength="0.3",ultimatesdupscale=False,usdutilewidth = "512", usdutileheight = "0", usdumaskblur = "8", usduredraw ="Linear", usduSeamsfix = "None", usdusdenoise = "0.35", usduswidth = "64", usduspadding ="32", usdusmaskblur = "8",controlnetenabled=False, controlnetmodel="",img2imgdenoisestrengthmod="-0.05",enableextraupscale = False,controlnetblockymode = False,extrasupscaler1 = "all",extrasupscaler2 ="all",extrasupscaler2visiblity="0.5",extrasupscaler2gfpgan="0",extrasupscaler2codeformer="0.15",extrasupscaler2codeformerweight="0.1",extrasresize="2",onlyupscale="false",givensubject="",smartsubject=True,giventypeofimage="",imagemodechance=20, gender="all", chosensubjectsubtypeobject="all", chosensubjectsubtypehumanoid="all", chosensubjectsubtypeconcept="all", increasestability = False, qualityhiresfix = False, qualitymode = "highest", qualitykeep="keep used", basesize = "512", promptvariantinsanitylevel = 0, givenoutfit = "", autonegativeprompt = True, autonegativepromptstrength = 0, autonegativepromptenhance = False, base_model = "SD1.5", OBP_preset = "", amountoffluff = "none", promptenhancer = "none", presetprefix = "", presetsuffix = ""):
    loops = int(amount)  # amount of images to generate
    steps = 0
    upscalefilelist=[]
    originalimage = ""
    originalpnginfo =""
    randomprompt = ""
    filename=""
    continuewithnextpart = True
    randomsubject = ""

    originalmodel = model
    originalsamplingmethod = samplingmethod

    originalnegativeprompt = negativeprompt

    originalimg2imgmodel = img2imgmodel
    originalimg2imgsamplingmethod = img2imgsamplingmethod
    originalimg2imgupscaler = img2imgupscaler

    originalupscaler = upscaler

    insanitylevel = int(insanitylevel)

    originalimg2imgdenoisestrength = img2imgdenoisestrength
    originalimg2imgpadding = img2imgpadding


    currentlyselectedmodel = ""

    modellist=get_models()
    samplerlist=get_samplers()
    upscalerlist=get_upscalers()
    img2imgupscalerlist=get_upscalers_for_img2img()
    img2imgsamplerlist=get_samplers_for_img2img()

    tempmodel = "v1-5-pruned-emaonly.safetensors [6ce0161689]"

    optionsresponse = requests.get(url=f'{apiurl}/sdapi/v1/options')
    optionsresponsejson = optionsresponse.json()

    currentlyselectedmodelhash = optionsresponsejson["sd_checkpoint_hash"]

    sdmodelsrespone = requests.get(url=f'{apiurl}/sdapi/v1/sd-models')
    sdmodelsresponsejson = sdmodelsrespone.json()

    for item in sdmodelsresponsejson:
        if(item['sha256'] == currentlyselectedmodelhash):
            currentlyselectedmodel = item['title']
            break

    # Print the 'title' if found
    if currentlyselectedmodel != "":
        print("current selected model is:")
        print(currentlyselectedmodel)
    else:
        print("Cannot find current model.")
        currentlyselectedmodel = tempmodel

    
    while(currentlyselectedmodel == tempmodel or tempmodel not in modellist):
        tempmodel = random.choice(modellist)


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




    if(ultimatesdupscale==False):
        upscalescript="SD upscale"
    else:
        upscalescript="Ultimate SD upscale"

    
    while steps < loops:
        # load the base model as a workaround
        if(steps > 0 and increasestability == True):
            print("")
            print("Increase Stability has been turned on.")
            print("To prevent a memory issue, we are going to unload and then load the checkpoint back in.")
            print("This helps with a memory leak issue. However A1111 is bad with memory management.")
            print("")

            response = requests.post(url=f'{apiurl}/sdapi/v1/unload-checkpoint')

            print("model unloaded")

            response = requests.post(url=f'{apiurl}/sdapi/v1/reload-checkpoint')

            print("model reloaded")

        # build prompt
        if(silentmode==True and workprompt == ""):
            print("Trying to use provided workflow prompt, but is empty. Generating a random prompt instead.")
    
        if(onlyupscale==False):  # only do txt2img when onlyupscale is False
            if(silentmode==True and workprompt != ""):
                randomprompt = createpromptvariant(workprompt, promptvariantinsanitylevel)
                print("Using provided workflow prompt")
                print(randomprompt)

                

            else:    
                randompromptlist = build_dynamic_prompt(insanitylevel,subject,artist,imagetype, False,antistring,prefixprompt,suffixprompt,promptcompounderlevel, seperator,givensubject,smartsubject,giventypeofimage,imagemodechance, gender, chosensubjectsubtypeobject, chosensubjectsubtypehumanoid, chosensubjectsubtypeconcept,True,False,-1,givenoutfit, prompt_g_and_l=True, base_model=base_model, OBP_preset=OBP_preset, prompt_enhancer=promptenhancer, preset_prefix=presetprefix, preset_suffix=presetsuffix)
                randomprompt = randompromptlist[0]
                randomsubject = randompromptlist[1]

            if(autonegativeprompt):
                negativeprompt = build_dynamic_negative(positive_prompt=randomprompt, insanitylevel=autonegativepromptstrength,enhance=autonegativepromptenhance, existing_negative_prompt=originalnegativeprompt, base_model=base_model)
            
            randomprompt = flufferizer(prompt=randomprompt, amountoffluff=amountoffluff)
            
            if(randomsubject == ""):
                # make the filename, from from a to the first comma
                # find the index of the first comma after "of a" or end of the prompt
                if(randomprompt.find("of a ") != -1):
                    start_index = randomprompt.find("of a ") + len("of a ")
                    end_index = randomprompt.find(",", start_index)
                    if(end_index == -1):
                        end_index=len(randomprompt)
                else:
                    start_index = 0
                    end_index = 128
        
                

                # extract the desired substring using slicing
                filename = randomprompt[start_index:end_index]
            else:
                filename = randomsubject[0:128] # Fix for too long filenames

            # cleanup some unsafe things in the filename
            filename = filename.replace("\"", "")
            filename = filename.replace("[", "")
            filename = filename.replace("|", "")
            filename = filename.replace("]", "")
            filename = filename.replace("<", "")
            filename = filename.replace(">", "")
            filename = filename.replace(":", "_")
            filename = filename.replace(".", "")
            filename = re.sub(r'[0-9]+', '', filename)

            safe_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

            # Use regular expression to filter out any characters not in the whitelist
            filename = re.sub(r"[^{}]+".format(re.escape(''.join(safe_characters))), '', filename)

            if(filename==""):
                filename = str(uuid.uuid4())
            
            # create a datetime object for the current date and time
            now = datetime.now()
            filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip()
            


            #Check if there is any random value we have to choose or not
            if(originalmodel=="all"):
                model = random.choice(modellist)
                #lets not do inpainting models
                while "inpaint" in model:
                    model = random.choice(modellist)
                print("Going to run with model " + model)
            if(originalmodel=="currently selected model"):
                model = currentlyselectedmodel


            # set the model here
            #if(originalmodel!="currently selected model"):
            option_payload = {
                "sd_model_checkpoint": model
                }
            response = requests.post(url=f'{apiurl}/sdapi/v1/options', json=option_payload)
        
            if(originalsamplingmethod=="all"):
                samplingmethod = random.choice(samplerlist)
                print ("Going to run with sampling method " + samplingmethod)   

            if(originalupscaler=="all" and hiresfix == True):
                upscaler = random.choice(upscalerlist)
                print ("Going to run with upscaler " + upscaler)

            # WebUI fix for PLMS and UniPC and hiresfix
            if(samplingmethod in ['PLMS', 'UniPC']):  # PLMS/UniPC do not support hirefix so we just silently switch to DDIM
                samplingmethod = 'DDIM'



                
            txt2img = call_txt2img(randomprompt, size ,hiresfix, 0, filenamecomplete,model ,samplingsteps,cfg, hiressteps, denoisestrength,samplingmethod, upscaler,hiresscale,apiurl,qualitygate,quality,runs,negativeprompt, qualityhiresfix, qualitymode, qualitykeep, basesize)
            originalimage = txt2img[0] #Set this for later use
            originalpnginfo = txt2img[1] #Sort of hacky way of bringing this forward. But if it works, it works
            continuewithnextpart = txt2img[2]

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
        if(img2imgactivate == False or continuewithnextpart == False):  # If we dont want to run, turn it off
            img2imgloops = 0
        else:
            #Check if there is any random value we have to choose or not
            if(originalimg2imgmodel=="all"):
                img2imgmodel = random.choice(modellist)
                #lets not do inpainting models
                while "inpaint" in model:
                    img2imgmodel = random.choice(modellist)
                print("Going to upscale with model " + img2imgmodel)
            if(originalimg2imgmodel=="currently selected model"):
                img2imgmodel = currentlyselectedmodel
            
            # set the model here
            #if(originalimg2imgmodel!="currently selected model"):
            option_payload = {
                "sd_model_checkpoint": img2imgmodel
                }
            response = requests.post(url=f'{apiurl}/sdapi/v1/options', json=option_payload)

            if(originalimg2imgsamplingmethod=="all"):
                img2imgsamplingmethod = random.choice(img2imgsamplerlist)
                print ("Going to upscale with sampling method " + img2imgsamplingmethod)   

            if(originalimg2imgupscaler=="all"):
                img2imgupscaler = random.choice(img2imgupscalerlist)
                print ("Going to run with upscaler " + img2imgupscaler)
            
            # WebUI fix for PLMS and UniPC and img2img
            if(img2imgsamplingmethod in ['PLMS', 'UniPC']):  # PLMS/UniPC do not support img2img so we just silently switch to DDIM
                img2imgsamplingmethod = 'DDIM'

        img2imgsteps = 0
        
        # start the batching!
        img2imgdenoisestrength = originalimg2imgdenoisestrength
        img2imgpadding = originalimg2imgpadding
        
        while img2imgsteps < img2imgloops:

            
            #filenamecomplete = originalfilenamecomplete + "_" + str(img2imgsteps)
            #print(filenamecomplete)
          
            img2img = call_img2img(image, originalimage, originalpnginfo, apiurl, filenamecomplete, randomprompt,negativeprompt,img2imgsamplingsteps, img2imgcfg, img2imgsamplingmethod, img2imgupscaler, img2imgmodel, img2imgdenoisestrength, img2imgscale, img2imgpadding,upscalescript,usdutilewidth, usdutileheight, usdumaskblur, usduredraw, usduSeamsfix, usdusdenoise, usduswidth, usduspadding, usdusmaskblur,controlnetenabled, controlnetmodel,controlnetblockymode)
            
            image = img2img[0]
            if(originalpnginfo==""):
                originalpnginfo = img2img[1]

            img2imgdenoisestrength = str(round(float(img2imgdenoisestrength) + float(img2imgdenoisestrengthmod),2)) # lower or increase the denoise strength for each batch
            img2imgpadding = str(int(int(img2imgpadding) * float(img2imgscale))) # also increase padding by scale

            if(int(img2imgpadding)>256): # but not overdo it :D
                img2imgpadding="256"
            
            # Sometimes, we are too quick to do another call, causing memory issues. So we wait a bit to let the system settle done a bit.
            # Its stupid but it works. Sometimes....
            time.sleep(5)
            
            img2imgsteps += 1

        # upscale via extras upscaler next
        
        if(enableextraupscale==True and continuewithnextpart == True):
            if(extrasupscaler1=="all"):
                extrasupscaler1 = random.choice(img2imgupscalerlist)
                print ("Going to upscale with upscaler 1 " + extrasupscaler1)
            
            if(extrasupscaler2=="all"):
                extrasupscaler2 = random.choice(img2imgupscalerlist)
                print ("Going to upscale with upscaler 2 " + extrasupscaler2)

            image = call_extras(image, originalimage, originalpnginfo, apiurl, filenamecomplete,extrasupscaler1,extrasupscaler2 ,extrasupscaler2visiblity,extrasupscaler2gfpgan,extrasupscaler2codeformer,extrasupscaler2codeformerweight,extrasresize)

        if(continuewithnextpart == True):
            # only count images we actually fully processed
            steps += 1
    

    print("")
    print("All done!")

def tryinterrupt(apiurl="http://127.0.0.1:7860"):
    response = requests.post(url=f'{apiurl}/sdapi/v1/interrupt')
    