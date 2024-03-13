import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,positive_prompt = "",insanitylevel="0",enhance=False,existing_negative_prompt="", base_model= "SD1.5"):
    loops = int(amount)  # amount of images to generate
    steps = 0
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
        if positive_prompt == "":
                    positive_prompt = build_dynamic_prompt()
        result = build_dynamic_negative(positive_prompt=positive_prompt, insanitylevel=insanitylevel,enhance=enhance, existing_negative_prompt=existing_negative_prompt, base_model=base_model)
        print("negative prompt: " + result)
        print("")
        print("loop " + str(steps))
        print("")
       

        steps += 1
    

    print("")
    print("All done!")

if __name__ == "__main__":
    generateprompts(1,"photo, photograph, realism",0,False,"", base_model="Stable Cascade")
