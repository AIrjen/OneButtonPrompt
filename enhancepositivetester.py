import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,positive_prompt = "",insanitylevel="0",enhance=False,existing_negative_prompt=""):
    loops = int(amount)  # amount of images to generate
    steps = 0
    originalpositiveprompt = positive_prompt
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
        if originalpositiveprompt == "":
                    positive_prompt = build_dynamic_prompt(insanitylevel=insanitylevel)
        result = enhance_positive(positive_prompt=positive_prompt, insanitylevel=insanitylevel)
        print("enhanced prompt: " + result)
        print("")
        print("loop " + str(steps))
        print("")
       

        steps += 1
    

    print("")
    print("All done!")

generateprompts(10,"",5,False,"")