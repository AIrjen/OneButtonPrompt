import json
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin



def call_img2img(imagelocation, denoising_strength = 0.25, scale = 1.5, padding = 64):

       #params to stay the same
    url = "http://127.0.0.1:7860"
    outputimg2imgfolder = 'C:\\automated_output\\img2img\\'
    outputimg2imgfilename = str(uuid.uuid4())
    outputimg2imgpng = '.png'
    outputimg2imgFull = '{}{}{}'.format(outputimg2imgfolder,outputimg2imgfilename,outputimg2imgpng)


    encodedstringlist = []
    #rest of prompt things

    sampler_index = "DPM2 Karras"
    steps = "20"
    prompt = "hello world"
    cfg_scale = "7"
    width = "512"
    height = "512"

    with open(imagelocation, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    encodedstringlist.append(encoded_string.decode('utf-8'))
    encodedstring2 = encoded_string.decode('utf-8')


    # prompt from picture?
    png_payload = {
            "image": encodedstring2
        }
    response3 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = str(response3.json().get("info"))

    prompt = pnginfo[:pnginfo.rfind("Steps")]

    payload = {
        "resize_mode": 0,
        "denoising_strength": denoising_strength,
        "sampler_index": sampler_index,  
        "batch_size": "1",
        "n_iter": "1",
        "prompt": prompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": width,
        "height": height,
        "include_init_images": "true",
        "init_images": encodedstringlist,
        "script_name": "SD upscale",
        "script_args": ["",padding,"4x-UltraSharp",scale]
    }


    #
    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
        "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(outputimg2imgFull, pnginfo=pnginfo)

    return outputimg2imgFull

