import json
import requests
import io
import base64
import uuid
import os
from PIL import Image, PngImagePlugin

def call_txt2img(passingprompt,ratio,upscale,debugmode,filename="",model = "currently selected model",samplingsteps = "40",cfg= "7",hiressteps ="0",denoisestrength="0.6",samplingmethod="DPM++ SDE Karras", upscaler="R-ESRGAN 4x+",apiurl="http://127.0.0.1:7860"):

    #set the prompt!
    prompt = passingprompt

    #set the URL for the API
    url = apiurl

    #rest of prompt things
    sampler_index = samplingmethod
    steps = samplingsteps
    if(debugmode==1):
        steps="10"
    cfg_scale = cfg

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
    denoising_strength = denoisestrength
    hr_upscaler = upscaler
    hr_second_pass_steps = hiressteps
    #hr_upscaler = "LDSR" # We have the time, why not use LDSR

    #if(hr_upscaler== "4x-UltraSharp"):
    #    denoising_strength = "0.35"
    #    hr_second_pass_steps = hiressteps
    #if(hr_upscaler== "LDSR"):
    #    denoising_strength = "0.5"
    #    hr_second_pass_steps = hiressteps
    #    hr_scale = "2" # So LDSR wants to always scale up by 4, lower and it starts downsampling the image. But my PC can't handle it.
    #if(hr_upscaler== "R-ESRGAN 4x+"):
    #    denoising_strength = "0.5" # default 0.6 is a lot and changes a lot of details
    #    hr_second_pass_steps = hiressteps

    

    #params to stay the same

    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputTXT2IMGfolder = os.path.join(script_dir, "./automated_outputs/txt2img/" )
    if(filename==""):
        filename = str(uuid.uuid4())
    
    outputTXT2IMGpng = '.png'
    outputTXT2IMGFull = '{}{}{}'.format(outputTXT2IMGfolder,filename,outputTXT2IMGpng)
    outputTXT2IMGtxtfolder = os.path.join(script_dir, "./automated_outputs/prompts/")
    outputTXT2IMGtxt = '.txt'
    outputTXT2IMGtxtFull = '{}{}{}'.format(outputTXT2IMGtxtfolder,filename,outputTXT2IMGtxt)



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

    if(model != "currently selected model"):
        payload.update({"sd_model": model})

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