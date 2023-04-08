import json
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin

def call_txt2img(passingprompt,ratio,upscale,debugmode):

    #set the prompt!
    prompt = passingprompt

    #rest of prompt things
    sampler_index = "DPM2 Karras"
    steps = "20"
    if(debugmode==1):
        steps="10"
    cfg_scale = "7"

    #size
    if(ratio=='wide'):
        width = "768"
        height = "512"
    elif(ratio=='portait'):
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
    denoising_strength = "0.35"
    hr_scale = "2"
    hr_upscaler = "4x-UltraSharp"
    hr_second_pass_steps = str(round(int(steps)/2))

    

    #params to stay the same
    url = "http://127.0.0.1:7860"
    outputTXT2IMGfolder = 'C:\\automated_output\\txt2img\\'
    outputTXT2IMGfilename = str(uuid.uuid4())
    outputTXT2IMGpng = '.png'
    outputTXT2IMGFull = '{}{}{}'.format(outputTXT2IMGfolder,outputTXT2IMGfilename,outputTXT2IMGpng)
    outputTXT2IMGtxtfolder = 'C:\\automated_output\\prompts\\'
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