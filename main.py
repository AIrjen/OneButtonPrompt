import sys, os
sys.path.append(os.path.abspath(".."))

from call_txt2img import *
from call_img2img import *
from build_dynamic_prompt import *
from call_extras import *


# needs following directories to exist:
# C:\automated_output\
# C:\automated_output\extras\
# C:\automated_output\img2img\
# C:\automated_output\txt2img\
# C:\automated_output\Prompts\

loops = 20  # amount of images to generate
steps = 0

while steps < loops:
    # build prompt
    randomprompt = build_dynamic_prompt(7,"all","all","all")
    
    # prompt + size

    #txt2img = call_txt2img(randomprompt, "portait",True,0)
    #txt2img = call_txt2img(randomprompt, "wide" ,True, 0)
    #txt2img = call_txt2img(randomprompt, "ultrawide",True,0)
    #txt2img = call_txt2img(randomprompt, "square",True,0)
    
    # upscale via img2img first
    #img2img = call_img2img(txt2img,0.25,1.5,256)

    # upscale via extras upscaler next
    #finalfile = call_extras(img2img)

    steps += 1