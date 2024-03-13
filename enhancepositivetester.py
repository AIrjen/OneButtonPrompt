import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,positive_prompt = "",amountofwords="3"):
    loops = int(amount)  # amount of images to generate
    steps = 0
    originalpositiveprompt = positive_prompt
  
    while steps < loops:
        # build prompt
        if originalpositiveprompt == "":
            result = build_dynamic_prompt(insanitylevel=3)
        else: 
            result = enhance_positive(positive_prompt=positive_prompt, amountofwords=amountofwords)
        print("enhanced prompt: " + result)
        print("")
        print("loop " + str(steps))
        print("")
       

        steps += 1
    

    print("")
    print("All done!")

if __name__ == "__main__":
    generateprompts(10,"",5)