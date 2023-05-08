import os
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin
from modules import shared


def call_img2img(imagelocation,originalimage, originalpnginfo ="", apiurl="http://127.0.0.1:7860",filename="", prompt = "", negativeprompt = "", img2imgsamplingsteps = "20", img2imgcfg = "7", img2imgsamplingmethod = "DPM++ SDE Karras", img2imgupscaler = "R-ESRGAN 4x+", img2imgmodel = "currently selected model", denoising_strength = "0.3", scale = "2", padding = "64",upscalescript="SD upscale"):

    negativepromptfound = 0
    #params to stay the same
    url = apiurl
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputimg2imgfolder = os.path.join(script_dir, "./automated_outputs/img2img/" )
    if(filename==""):
        filename = str(uuid.uuid4())
    outputimg2imgpng = '.png'
    outputimg2imgFull = '{}{}{}'.format(outputimg2imgfolder,filename,outputimg2imgpng)


    encodedstringlist = []
    #rest of prompt things

    sampler_index = img2imgsamplingmethod
    steps = img2imgsamplingsteps
    cfg_scale = img2imgcfg
    upscaler = img2imgupscaler


    with open(imagelocation, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    encodedstringlist.append(encoded_string.decode('utf-8'))
    
    # If we don't have a prompt, get it from the original image file
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

    if(upscalescript=="SD upscale"):
        payload.update({"script_name": upscalescript})
        payload.update({"script_args": ["",int(padding),upscaler,scale]})

    if(upscalescript=="Ultimate SD upscale"):
        upscaler_index = [x.name.lower() for x in shared.sd_upscalers].index(upscaler.lower())
        payload.update({"script_name": upscalescript})
        payload.update({"script_args": ["",512,0,8,int(padding), 64, 0.35,32,
                                        upscaler_index,True,2,False,8,
                                        0,2,"","",2]})
    
    # Ultimate SD Upscale params:
    #_, tile_width, tile_height, mask_blur, padding, seams_fix_width, seams_fix_denoise, seams_fix_padding,
    #        upscaler_index, save_upscaled_image, redraw_mode, save_seams_fix_image, seams_fix_mask_blur,
    #        seams_fix_type, target_size_type, custom_width, custom_height, custom_scale):

# target_size_type = 2
# custom_scale = 2
    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)


    r = response.json()


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

    return outputimg2imgFull
