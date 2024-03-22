import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,prompt = "",artists="all",amountofartists = "1", mode="standard"):
    loops = int(amount)  # amount of images to generate
    steps = 0
    originalpositiveprompt = prompt
  
    while steps < loops:
        # build prompt
        if originalpositiveprompt == "":
            result = build_dynamic_prompt(insanitylevel=3)
        else: 
            result = artify_prompt(prompt=prompt, artists=artists, amountofartists=amountofartists, mode=mode)
            result = flufferizer(prompt=result, reverse_polarity=True)
        print("ARTIFY COMPLETE: " + result)
        print("")
        print("loop " + str(steps))
        print("")
       

        steps += 1
    

    print("")
    print("All done!")

if __name__ == "__main__":
    generateprompts(10,"a norwegian forest cat", "all","random", "standard")