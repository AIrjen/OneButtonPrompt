import os

from call_extras import *
from call_img2img import *

# C:\automated_output\extras\
# C:\automated_output\img2img\
# C:\automated_output\upscale me\

# takes all images with prompt info in their PNG, from the upscale directory, and upscales them

directory = 'C:\\automated_output\\Upscale me\\'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
  
        img2img1 = call_img2img(f,0.25,1.5,256)
        
        finalfile = call_extras(img2img1)
