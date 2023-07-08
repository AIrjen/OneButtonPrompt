import os
import requests
import io
import base64
import uuid
from PIL import Image, PngImagePlugin
import time



def call_extras(imagelocation,originalimage, originalpnginfo ="", apiurl="http://127.0.0.1:7860",filename="",extrasupscaler1 = "all",extrasupscaler2 ="all",extrasupscaler2visiblity="0.5",extrasupscaler2gfpgan="0",extrasupscaler2codeformer="0.15",extrasupscaler2codeformerweight="0.1",extrasresize="2"):


    #rest of prompt things
    upscaling_resize = extrasresize
    upscaler_1 = extrasupscaler1
    upscaler_2 = extrasupscaler2
    
    with open(imagelocation, "rb") as image_file:
       encoded_string = base64.b64encode(image_file.read())
    encodedstring2 = encoded_string.decode('utf-8')
    #params to stay the same
    url = apiurl
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    outputextrasfolder = os.path.join(script_dir, "./automated_outputs/extras/" )
    outputextrasfolder.replace("./", "/")
    if(filename==""):
        filename = str(uuid.uuid4())
    outputextrasilename = filename
    outputextraspng = '.png'
    outputextrasFull = '{}{}{}'.format(outputextrasfolder,outputextrasilename,outputextraspng)


    payload = {
        "upscaling_resize": float(upscaling_resize),
        "upscaler_1": upscaler_1,
        "image": encodedstring2,
        "resize_mode": 0,
        "show_extras_results": "false",
        "gfpgan_visibility": extrasupscaler2gfpgan ,
        "codeformer_visibility": extrasupscaler2visiblity,
        "codeformer_weight": extrasupscaler2codeformerweight,
        "upscaling_crop": "false",
        "upscaler_2": upscaler_2,
        "extras_upscaler_2_visibility": extrasupscaler2visiblity,
        "upscale_first": "true",
        "rb_enabled": "false",  # the remove backgrounds plugin is  automatically turned on, need to turn it off
        "models": "None" # the remove backgrounds plugin is  automatically turned on, need to turn it off
    }

    response = []
        
    # If we don't get an image back, we want to retry a few times. Max 3 times
    for i in range(4):
        response = requests.post(url=f'{url}/sdapi/v1/extra-single-image', json=payload)

        r = response.json()
        if("image" in r):
            break # this means if we have the images object, then we "break" out of the for loop.
        else:
            if(i == 3):
                print("If this keeps happening: Is WebUI started with --api enabled?")
                print("")
                raise ValueError("API has not been responding after several retries. Stopped processing.")
            print("")
            print("We haven't received an image from the API. Maybe something went wrong. Will retry after waiting a bit.")
            

            time.sleep(10 * (i+1) ) # incremental waiting time

    image = Image.open(io.BytesIO(base64.b64decode(response.json().get("image"))))

    # when using just upscale, we somehow can't get the png info. Unless we do IMG2IMG or TXT2IMG first, then it is added.
    # minor issue, so this solves it for now

    #if(originalpnginfo==""):
    #        png_payload = {
    #        "image": "data:image/png;base64," + image[0]
    #        }

            #print("and here!")
            #print(png_payload)
    #        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

            #print("here!")
            #print(response2)
    


        #    pnginfo = PngImagePlugin.PngInfo()
        #    pnginfo.add_text("parameters", response2.json().get("info"))

        #    originalpnginfo = pnginfo

    
    image.save(outputextrasFull, pnginfo=originalpnginfo)

    return outputextrasFull
