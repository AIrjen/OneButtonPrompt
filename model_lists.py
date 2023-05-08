import modules.scripts as scripts
import os
from modules import modelloader, paths, shared
from modules.paths import models_path


def get_models():
    model_dir = "Stable-diffusion"
    model_path = os.path.abspath(os.path.join(paths.models_path, model_dir))
    model_url = None
    modellist = modelloader.load_models(model_path=model_path, model_url=model_url, command_path=shared.cmd_opts.ckpt_dir, ext_filter=[".ckpt", ".safetensors"], download_name="v1-5-pruned-emaonly.safetensors", ext_blacklist=[".vae.ckpt", ".vae.safetensors"])
    modellist = [s.replace(model_path, "") for s in modellist]
    modellist = [s.replace("\\\\", "") for s in modellist]
    modellist = [s.replace("\\", "") for s in modellist]
    modellist = [s.replace(".ckpt", "") for s in modellist]
    modellist = [s.replace(".safetensors", "") for s in modellist]
    return modellist

def get_upscalers():
    #Upscalers are sort of hardcoded as well for Latent, but not for the 2 others. So build it up!
    latentlist=["Latent","Latent (antialiased)","Latent (bicubic)","Latent (bicubic antialiased)","Latent (nearest)","Latent (nearest-exact)","Lanczos","Nearest"]

    RealESRGAN_dir = "RealESRGAN"
    RealESRGAN_path = os.path.abspath(os.path.join(paths.models_path, RealESRGAN_dir))
    model_url = None
    RealESRGANlist = modelloader.load_models(model_path=RealESRGAN_path, model_url=model_url, command_path=shared.cmd_opts.ckpt_dir, ext_filter=[".pt", ".pth"], download_name="", ext_blacklist=[".vae.ckpt", ".vae.safetensors"])
    RealESRGANlist = [s.replace(RealESRGAN_path, "") for s in RealESRGANlist]
    RealESRGANlist = [s.replace("\\\\", "") for s in RealESRGANlist]
    RealESRGANlist = [s.replace("\\", "") for s in RealESRGANlist]
    RealESRGANlist = [s.replace(".pth", "") for s in RealESRGANlist]
    RealESRGANlist = [s.replace(".pt", "") for s in RealESRGANlist]

    ESRGAN_dir = "ESRGAN"
    ESRGAN_path = os.path.abspath(os.path.join(paths.models_path, ESRGAN_dir))
    ESRGANlist = modelloader.load_models(model_path=ESRGAN_path, model_url=model_url, command_path=shared.cmd_opts.ckpt_dir, ext_filter=[".pt", ".pth"], download_name="", ext_blacklist=[".vae.ckpt", ".vae.safetensors"])
    ESRGANlist = [s.replace(ESRGAN_path, "") for s in ESRGANlist]
    ESRGANlist = [s.replace("\\\\", "") for s in ESRGANlist]
    ESRGANlist = [s.replace("\\", "") for s in ESRGANlist]
    ESRGANlist = [s.replace(".pth", "") for s in ESRGANlist]
    ESRGANlist = [s.replace(".pt", "") for s in ESRGANlist]

    #hardcode some things for Real ESGRAN, because its named differently (note, I could have just hardcoded this. Oh well...)
    RealESRGANlist = [s.replace("RealESRGAN_x4plus","R-ESRGAN 4x+") for s in RealESRGANlist]
    RealESRGANlist = [s.replace("RealESRGAN x4plus_anime_6B","R-ESRGAN 4x+ Anime6B") for s in RealESRGANlist]
    RealESRGANlist = [s.replace("R-ESRGAN 4x+_anime_6B","R-ESRGAN 4x+ Anime6B") for s in RealESRGANlist]

    upscalerlist = latentlist + RealESRGANlist + ESRGANlist
    return upscalerlist

def get_samplers():
    #Samplers are hardcoded in WEBui, so lets do it here as well
    samplerlist = ["Euler a", "Euler", "LMS","Heun","DPM2","DPM2 a","DPM++ 2S a","DPM++ 2M","DPM++ SDE","DPM fast","DPM adaptive","LMS Karras","DPM2 Karras","DPM2 a Karras","DPM++ 2S a Karras","DPM++ 2M Karras","DPM++ SDE Karras"]
    samplerlist += ["DDIM","UniPC", "PLMS"]
    return samplerlist

def get_upscalers_for_img2img():
    upscalerlist = get_upscalers()
    # basically have to remove a lot of these, these aren't supported
    upscalerlist.remove("Latent")
    upscalerlist.remove("Latent (antialiased)")
    upscalerlist.remove("Latent (bicubic)")
    upscalerlist.remove("Latent (bicubic antialiased)")
    upscalerlist.remove("Latent (nearest)")
    upscalerlist.remove("Latent (nearest-exact)")
    return upscalerlist
