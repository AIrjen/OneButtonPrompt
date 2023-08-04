import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generatepromptvariants(amount = 1,prompt="",insanitylevel="5"):
    loops = int(amount)  # amount of images to generate
    steps = 0
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
        if(prompt == ""):
            prompt = build_dynamic_prompt(insanitylevel)

        result = createpromptvariant(prompt, insanitylevel)

        print(result)

        print("")
        print("loop " + str(steps))
        print("")
              

        steps += 1
    

    print("")
    print("All done!")

generatepromptvariants(1,"purple (galaxy) in a (bottle:1.2), <bla:1>, background is a lush jungle and a woman wearing a summer dress, -artmovement-", 5)