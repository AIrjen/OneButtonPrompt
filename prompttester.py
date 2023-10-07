import sys, os
import random
import uuid
import re
from datetime import datetime
sys.path.append(os.path.abspath(".."))


from build_dynamic_prompt import *



def generateprompts(amount = 1,insanitylevel="5",subject="all", artist="all", imagetype="all",onlyartists=False, workprompt="", antistring="",prefixprompt="", suffixprompt="", negativeprompt="",promptcompounderlevel = "1", seperator="comma",givensubject="",smartsubject=True,giventypeofimage="",imagemodechance=20, gender = "all", subtypeobject = "all", subtypehumanoid = "all", subtypeconcept = "all", advancedprompting = True, hardturnoffemojis=False, seed=0, overrideoutfit=""):
    loops = int(amount)  # amount of images to generate
    steps = 0
   
    insanitylevel = int(insanitylevel)
    while steps < loops:
        # build prompt
    
        result = build_dynamic_prompt(insanitylevel,subject,artist,imagetype, onlyartists,antistring,prefixprompt,suffixprompt,promptcompounderlevel, seperator,givensubject,smartsubject,giventypeofimage,imagemodechance, gender, subtypeobject, subtypehumanoid, subtypeconcept, advancedprompting, hardturnoffemojis, seed, overrideoutfit)

        print("")
        print("loop " + str(steps))
        print("")
        if(onlyartists == True):
            print(result)
            print("")
        
        if(result.count("-")>1 and imagetype == "only templates"):
            print("Is there a mistake in wildcards?")
            print("")
            print(result)
            break
            
        if(givensubject != "" and givensubject not in result and imagetype == "only templates"):
            print("No givensubject, there must be an issue:")
            print("")
            print(result)
            break

        if(" OR " in result):
            print("There is a mistake in a OR statement")
            print("")
            print(result)
            break

        steps += 1
    

    print("")
    print("All done!")

generateprompts(10,5
                ,"humanoid" # subject
                ,"character" # artists
                ,"all",False,"","","PREFIXPROMPT" 
                ,"SUFFIXPROMPT -humanexpression-"
                ,"",1,""
                ,"" # subject override
                ,True,
                "",100, "all"
                , "all" # object types
                , "all"  # humanoid types
                , "all" # concept types
                , False, True, 0
                , "" #outfit override
                )