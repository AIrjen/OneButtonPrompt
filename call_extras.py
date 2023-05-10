import os
import requests
import io
import base64
import uuid
from PIL import Image



def call_extras(imagelocation,originalimage, originalpnginfo ="", apiurl="http://127.0.0.1:7860",filename=""):


    #rest of prompt things
    upscaling_resize = "2"
    upscaler_1 = "4x-UltraSharp"
    upscaler_2 = "R-ESRGAN 4x+"
    
    with open(imagelocation, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    encodedstring2 = encoded_string.decode('utf-8')
    #params to stay the same
    url = apiurl
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputextrasfolder = os.path.join(script_dir, "./automated_outputs/extras/" )
    if(filename==""):
        filename = str(uuid.uuid4())
    outputextrasilename = filename
    outputextraspng = '.png'
    outputextrasFull = '{}{}{}'.format(outputextrasfolder,outputextrasilename,outputextraspng)


    payload = {
        "upscaling_resize": upscaling_resize,
        "upscaler_1": upscaler_1,
        "image": encodedstring2,
        "resize_mode": 0,
        "show_extras_results": "false",
        "gfpgan_visibility": 0,
        "codeformer_visibility": 0.15,
        "codeformer_weight": 0.1,
        "upscaling_crop": "false",
        "upscaler_2": upscaler_2,
        "extras_upscaler_2_visibility": 0.5,
        "upscale_first": "true",
        "rb_enabled": "false",  # the remove backgrounds plugin is  automatically turned on, need to turn it off
        "models": "None" # the remove backgrounds plugin is  automatically turned on, need to turn it off
    }


    response = requests.post(url=f'{url}/sdapi/v1/extra-single-image', json=payload)

    image = Image.open(io.BytesIO(base64.b64decode(response.json().get("image"))))
    image.save(outputextrasFull, pnginfo=originalpnginfo)

    return outputextrasFull
