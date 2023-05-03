import json
import requests
import io
import base64
import uuid
import os
from PIL import Image, PngImagePlugin

def call_txt2img(passingprompt,ratio,upscale,debugmode):

    #set the prompt!
    prompt = passingprompt

    #rest of prompt things
    sampler_index = "DPM++ SDE Karras"
    steps = "40"
    if(debugmode==1):
        steps="10"
    cfg_scale = "7"

    #size
    if(ratio=='wide'):
        width = "768"
        height = "512"
    elif(ratio=='portrait'):
        width = "512"
        height = "768"
    elif(ratio=='ultrawide'):
        width = "1280"
        height = "360"
    else:
        width = "512"
        height = "512"
    #upscaler
    enable_hr = upscale
    if(debugmode==1):
        enable_hr="False"
    
    #defaults
    hr_scale = "2"
    denoising_strength = "0.6"
    hr_upscaler = "4x-UltraSharp"
    #hr_upscaler = "LDSR" # We have the time, why not use LDSR

    if(hr_upscaler== "4x-UltraSharp"):
        denoising_strength = "0.35"
        hr_second_pass_steps = str(round(int(steps)/2))
    if(hr_upscaler== "LDSR"):
        denoising_strength = "0.5"
        hr_second_pass_steps = 40
        hr_scale = "2" # So LDSR wants to always scale up by 4, lower and it starts downsampling the image. But my PC can't handle it.
    if(hr_upscaler== "R-ESRGAN 4x+"):
        denoising_strength = "0.5" # default 0.6 is a lot and changes a lot of details
        hr_second_pass_steps = str(round(int(steps)/2))

    

    #params to stay the same
    url = "http://127.0.0.1:7860"
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputTXT2IMGfolder = os.path.join(script_dir, "./automated_outputs/txt2img/" )
    outputTXT2IMGfilename = str(uuid.uuid4())
    outputTXT2IMGpng = '.png'
    outputTXT2IMGFull = '{}{}{}'.format(outputTXT2IMGfolder,outputTXT2IMGfilename,outputTXT2IMGpng)
    outputTXT2IMGtxtfolder = os.path.join(script_dir, "./automated_outputs/prompts/")
    outputTXT2IMGtxt = '.txt'
    outputTXT2IMGtxtFull = '{}{}{}'.format(outputTXT2IMGtxtfolder,outputTXT2IMGfilename,outputTXT2IMGtxt)



    #call TXT2IMG

    payload = {
        "prompt": prompt,
        "sampler_index": sampler_index,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": width,
        "height": height,
        "enable_hr": enable_hr,
        "denoising_strength": denoising_strength,
        "hr_scale": hr_scale,
        "hr_upscaler": hr_upscaler,
        "hr_second_pass_steps": hr_second_pass_steps

    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(outputTXT2IMGFull, pnginfo=pnginfo)
    

    with open(outputTXT2IMGtxtFull,'w',encoding="utf8") as txt:
        json_object = json.dumps(payload, indent = 4)
        txt.write(json_object)

    return outputTXT2IMGFull