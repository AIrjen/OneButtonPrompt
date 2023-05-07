import os
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin



def call_img2img(imagelocation,originalimage, apiurl="http://127.0.0.1:7860",filename="", prompt = "", negativeprompt = "", denoising_strength = "0.25", scale = "1.5", padding = "64"):

    negativepromptfound = 0
    negativeprompt = ""
    prompt = ""
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

    sampler_index = "DPM2 Karras"
    steps = "20"
    prompt = "hello world"
    cfg_scale = "7"
    # width = "512"
    # height = "512"

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
        "script_name": "SD upscale",
        "script_args": ["",padding,"4x-UltraSharp",scale]
    }


    #
    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)

    r = response.json()


    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        #note, this doesn't seem to work yet <_<

        #png_payload = {
        #"image": "data:image/png;base64," + i
        #}

        #print("and here!")
        #print(png_payload)
        #response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        #print("here!")
        #print(response2)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text('parameters', originalimage.image.info["parameters"]) # Get the generation info from the original image
        #pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(outputimg2imgFull, pnginfo=pnginfo)

    return outputimg2imgFull
