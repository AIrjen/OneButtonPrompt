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
    originalprompt = prompt
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
        if(originalprompt == ""):
            prompt = build_dynamic_prompt(insanitylevel)

        result = createpromptvariant(prompt, insanitylevel)

        print(result)

        print("")
        print("loop " + str(steps))
        print("")
              

        steps += 1
    

    print("")
    print("All done!")

if __name__ == "__main__":
    generatepromptvariants(100
                       ,"" #purple (galaxy) in a (bottle:1.2), <bla:1>, background is a lush jungle and a woman wearing a summer dress, -artmovement-
                       , 5)
