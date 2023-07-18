import os
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin
from modules import shared
from model_lists import *
import time


def call_img2img(imagelocation,originalimage, originalpnginfo ="", apiurl="http://127.0.0.1:7860",filename="", prompt = "", negativeprompt = "", img2imgsamplingsteps = "20", img2imgcfg = "7", img2imgsamplingmethod = "DPM++ SDE Karras", img2imgupscaler = "R-ESRGAN 4x+", img2imgmodel = "currently selected model", denoising_strength = "0.3", scale = "2", padding = "64",upscalescript="SD upscale",usdutilewidth = "512", usdutileheight = "0", usdumaskblur = "8", usduredraw ="Linear", usduSeamsfix = "None", usdusdenoise = "0.35", usduswidth = "64", usduspadding ="32", usdusmaskblur = "8",controlnetenabled=False, controlnetmodel="",controlnetblockymode=False):

    negativepromptfound = 0
    #params to stay the same
    url = apiurl
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputimg2imgfolder = os.path.join(script_dir, "./automated_outputs/img2img/" )
    outputimg2imgfolder.replace("./", "/")
    if(filename==""):
        filename = str(uuid.uuid4())
    outputimg2imgpng = '.png'
    outputimg2imgFull = '{}{}{}'.format(outputimg2imgfolder,filename,outputimg2imgpng)


    encodedstringlist = []
    # need to convert the values to the correct index number for Ultimate SD Upscaler
    redrawmodelist =["Linear","Chess","None"]
    seamsfixmodelist = ["None","Band pass","Half tile offset pass","Half tile offset pass + intersections"]
    usduredrawint = int(redrawmodelist.index(usduredraw))
    seamsfixmodeint = int(seamsfixmodelist.index(usduSeamsfix))
    




    #rest of prompt things

    sampler_index = img2imgsamplingmethod
    steps = img2imgsamplingsteps
    cfg_scale = img2imgcfg

   





    with open(imagelocation, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    encodedstringlist.append(encoded_string.decode('utf-8'))
    
    # If we don't have a prompt, get it from the original image file
    # This is used when only_upscale is activated
    if(prompt==""):
        with open(originalimage, "rb") as originalimage_file:
            originalencoded_string = base64.b64encode(originalimage_file.read())
        encodedstring2 = originalencoded_string.decode('utf-8')


        # get prompt from picture
        png_payload = {
                "image": encodedstring2
            }
        response3 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = str(response3.json().get("info"))


        prompt = pnginfo[:pnginfo.rfind("Steps")]


        if(prompt.rfind("Negative prompt") != -1):
            prompt = prompt[:prompt.rfind("Negative prompt")]

            negativepromptfound = 1
        
        if(negativepromptfound == 1):
            negativeprompt = pnginfo[:pnginfo.rfind("Steps")]
            negativeprompt = negativeprompt.replace(prompt,"")
        

     # set the automatic upscale
    
    checkprompt = prompt.lower()
    if(img2imgupscaler != "automatic"):
        upscaler = img2imgupscaler
    else:
        upscalerlist = get_upscalers_for_img2img()
        # on automatic, make some choices about what upscaler to use
        # photos, prefer 4x ultrasharp
        # anime, cartoon or drawing, go for R-ESRGAN 4x+ Anime6B
        # else, R-ESRGAN 4x+"
        if("hoto" in checkprompt and "4x-UltraSharp" in upscalerlist):
            upscaler = "4x-UltraSharp"
        elif("anime" in checkprompt or "cartoon" in checkprompt or "draw" in checkprompt or "vector" in checkprompt or "cel shad" in checkprompt or "visual novel" in checkprompt):
            upscaler = "R-ESRGAN 4x+ Anime6B"
        else:
            upscaler = "R-ESRGAN 4x+"
        
        if(upscaler== "4x-UltraSharp"):
            denoising_strength = "0.35"
        if(upscaler== "R-ESRGAN 4x+ Anime6B"):
            denoising_strength = "0.6" # 0.6 is fine for the anime upscaler
        if(upscaler== "R-ESRGAN 4x+"):
            denoising_strength = "0.5" # default 0.6 is a lot and changes a lot of details


    #wierd blocky mode comes up when the treshold is set way too high and the denoising strenght is strong
    if(controlnetblockymode==True):
        treshold = int(padding)
        if(float(denoising_strength) < 0.65):
            denoising_strength = "0.65"
    else:
        treshold = 1

    payload = {
        "resize_mode": 0,
        "denoising_strength": denoising_strength,
        "sampler_index": sampler_index,  
        "batch_size": "1",
        "n_iter": "1",
        "prompt": prompt,
        "negative_prompt": negativeprompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        #"width": width,
        #"height": height,
        "include_init_images": "true",
        "init_images": encodedstringlist,
    }

    if(img2imgmodel != "currently selected model"):
        payload.update({"sd_model": img2imgmodel})
    #
    
    # https://github.com/Mikubill/sd-webui-controlnet/wiki/API
    #


    if(controlnetenabled==True and controlnetmodel!=""):
        payload.update({"alwayson_scripts": {
                            "controlnet": {
                                    "args": [
                                        {
                                            "module": "tile_resample",
                                            "model": controlnetmodel, # control_v11f1e_sd15_tile [a371b31b]
                                            #"input_image": encodedstringlist, 
                                            "control_mode": 2, #"ControlNet is more important" : the controlnet model has more impact than the prompt
                                            #"resize_mode": 0
                                            "threshold_a": treshold
                                            }
                                            ]
                                            }
                                }
                        })
    if(upscalescript=="SD upscale"):
        payload.update({"script_name": upscalescript})
        payload.update({"script_args": ["",int(padding),upscaler,round(float(scale),1)]})

    if(upscalescript=="Ultimate SD upscale"):
        upscaler_index = [x.name.lower() for x in shared.sd_upscalers].index(upscaler.lower())
        payload.update({"script_name": upscalescript})
        payload.update({"script_args": ["",int(usdutilewidth),int(usdutileheight),int(usdumaskblur),int(padding), int(usduswidth), round(float(usdusdenoise),2),int(usduspadding),
                                        upscaler_index,True,usduredrawint,False,int(usdusmaskblur),
                                        seamsfixmodeint,2,"","",round(float(scale),1)]})
    
    # Ultimate SD Upscale params:
    #_, tile_width, tile_height, mask_blur, padding, seams_fix_width, seams_fix_denoise, seams_fix_padding,
    #        upscaler_index, save_upscaled_image, redraw_mode, save_seams_fix_image, seams_fix_mask_blur,
    #        seams_fix_type, target_size_type, custom_width, custom_height, custom_scale):

    # target_size_type = 2
    # custom_scale = 2

    r = []
    # If we don't get an image back, we want to retry a few times. Max 3 times
    for i in range(4):
        response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)


        r = response.json()
        if('images' in r):
            break # this means if we have the images object, then we "break" out of the for loop.
        else:
            if(i == 3):
                print("If this keeps happening: Is WebUI started with --api enabled?")
                print("")
                raise ValueError("API has not been responding after several retries. Stopped processing.")
            print("")
            print("We haven't received an image from the API. Maybe something went wrong. Will retry after waiting a bit.")
                

            time.sleep(10 * (i+1) ) # incremental waiting time

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        if(originalpnginfo==""):
            png_payload = {
            "image": "data:image/png;base64," + i
            }

            #print("and here!")
            #print(png_payload)
            response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

            #print("here!")
            #print(response2)
    


            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))

            originalpnginfo = pnginfo
        image.save(outputimg2imgFull, pnginfo=originalpnginfo)

    return [outputimg2imgFull,originalpnginfo]
