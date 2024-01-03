import modules.scripts as scripts
import os
from modules import modelloader, paths, shared, sd_models, sd_samplers
from modules.paths import models_path, script_path
import importlib

def get_models():
    modellist = sd_models.checkpoint_tiles()
    return modellist

def get_upscalers():
    # Upscalers are sort of hardcoded as well for Latent, but not for the 2 others. So build it up!
    latentlist=["Latent","Latent (antialiased)","Latent (bicubic)","Latent (bicubic antialiased)","Latent (nearest)","Latent (nearest-exact)","Lanczos","Nearest"]

    
    # From 1.4 onwards, the shared.sd_upscalers isn't available on startup. Run load_upscalers first
    # It doesn't work perfectly, I have to call this each time to make sure it stays working.
    upscalerlistfromwWebUI = upscalers_on_startup()
    
    # deduplicate the list
    upscalerlistfromwWebUI = list(dict.fromkeys(upscalerlistfromwWebUI))

    if("None" in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.remove("None")


    upscalerlist = latentlist + upscalerlistfromwWebUI

    # Just to be sure, deduplicate again
    upscalerlist = list(dict.fromkeys(upscalerlist))

    return upscalerlist

def get_samplers():
    samplerlist = list(sd_samplers.all_samplers_map.keys())

    # fallback method
    if(samplerlist==[]):
        samplerlist = [
            "DDIM",
            "DPM adaptive",
            "DPM fast",
            "DPM++ 2M Karras",
            "DPM++ 2M",
            "DPM++ 2S a Karras",
            "DPM++ 2S a",
            "DPM++ SDE Karras",
            "DPM++ SDE",
            "DPM2 Karras",
            "DPM2 a Karras",
            "DPM2 a",
            "DPM2",
            "Euler a",
            "Euler",
            "Heun",
            "LMS Karras",
            "LMS",
            "PLMS",
            "UniPC",
        ]

    return samplerlist

def get_upscalers_for_img2img():
        
    # From 1.4 onwards, the shared.sd_upscalers isn't available on startup. Run load_upscalers first
    # It doesn't work perfectly, I have to call this each time to make sure it stays working.
    upscalerlistfromwWebUI = upscalers_on_startup()
    
    # deduplicate the list
    upscalerlistfromwWebUI = list(dict.fromkeys(upscalerlistfromwWebUI))

    if("None" in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.remove("None")

    return upscalerlistfromwWebUI

def get_samplers_for_img2img():
    samplerlist = get_samplers().copy()

    #UniPC and PLMS dont support upscaling apparently
    for s in ["UniPC", "PLMS"]:
        if samplerlist and s in samplerlist:
            samplerlist.remove(s)

    return samplerlist

def upscalers_on_startup():
    try:
        modelloader.cleanup_models()
    except:
        pass
    modelloader.load_upscalers()
    upscalerlistfromwWebUI = [x.name for x in shared.sd_upscalers]

    # In vlad this seems to work, but in WebUI some of these aren't loaded yet
    # lets just hardcode it, and get it over with
    if('LDSR' not in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.append('LDSR')
    if('ScuNET GAN' not in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.append('ScuNET GAN')
    if('ScuNET PSNR' not in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.append('ScuNET PSNR')
    if('SwinIR_4x' not in upscalerlistfromwWebUI and 'SwinIR 4x' not in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.append('SwinIR_4x')
    
    return upscalerlistfromwWebUI
