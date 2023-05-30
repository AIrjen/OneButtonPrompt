import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,insanitylevel="5",subject="all", artist="all", imagetype="all",onlyartists=False, workprompt="", antistring="",prefixprompt="", suffixprompt="", negativeprompt="",promptcompounderlevel = "1", seperator="comma",givensubject="",smartsubject=True,giventypeofimage=""):
    loops = int(amount)  # amount of images to generate
    steps = 0
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
    
        result = build_dynamic_prompt(insanitylevel,subject,artist,imagetype, onlyartists,antistring,prefixprompt,suffixprompt,promptcompounderlevel, seperator,givensubject,smartsubject,giventypeofimage)

        print("")
        print("loop " + str(steps))
        print("")
        if(onlyartists == True):
            print(result)
            print("")

            

        steps += 1
    

    print("")
    print("All done!")

generateprompts(10,7,"object","all","only templates",False,"","","PREFIXPROMPT" ,"SUFFIXPROMPT","",1,"","")