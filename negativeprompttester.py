import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,positive_prompt = "",insanitylevel="5"):
    loops = int(amount)  # amount of images to generate
    steps = 0
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
        result = build_dynamic_negative(postive_prompt=positive_prompt, insanitylevel=insanitylevel)
        print("")
        print("loop " + str(steps))
        print("")
       

        steps += 1
    

    print("")
    print("All done!")

generateprompts(1,"",5)