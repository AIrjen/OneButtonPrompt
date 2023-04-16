import random
import re
from csv_reader import *
from random_functions import *




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all"):

    completeprompt = ", "

    isphoto = 0
    othertype = 0
    humanspecial = 0
    wereanimaladded = 0
    isweighted = 0
    amountofimagetypes = 0
    hybridorswap = ""
    artistmode = "normal"

    if(insanitylevel==0):
        insanitylevel =  random.randint(1, 10)  # 10 = add everything, 1 is add almost nothing
    insanitylevel3 = int((insanitylevel/3) + 1.20)

    print("Setting insanity level to " + str(insanitylevel))

   # main chooser: 0 object, 1 animal, 2 humanoid, 3 landscape, 4 event/concept
    mainchooserlist = ["object","animal","humanoid", "landscape", "concept"]
    mainchooser = mainchooserlist[random.randint(0, 4)]
    
    if(forcesubject != "" and forcesubject != "all"):
        mainchooser = forcesubject    
    # 0 object, 1 animal, 2 animal as human, 3 ManWoman, 4 Job, 5 fictional, 6 non fictional, 7 humanoid, 8 landscape, 9 event
    if(mainchooser == "object"):
        subjectchooser = "object"
    if(mainchooser == "animal"):
        # sometimes interpret the animal as a human
        if(random.randint(0,5) < 5):
            subjectchooser = "animal"
        else:
            subjectchooser = "animal as human"
    if(mainchooser == "humanoid"):
        subjectchooserlist = ["human", "job", "fictional", "non fictional", "humanoid"]
        subjectchooser = subjectchooserlist[random.randint(0, 4)]
    if(mainchooser == "landscape"):
        subjectchooser = "landscape"
    if(mainchooser == "concept"):
        subjectchooserlist = ["event", "concept"]
        subjectchooser = subjectchooserlist[random.randint(0, 1)] 


    hybridlist = ["-animal-", "-object-", "-fictional-", "-nonfictional-", "-building-", "-vehicle-"]
    hybridhumanlist = ["-fictional-", "-nonfictional-"]
    
    # possible?: think about curated artist list?
    artistsplacement = "front"
    if(uncommon_dist(insanitylevel)):
        artistsplacement = "back"

    if(artists == "all" and artistsplacement == "front"):
        # take 1-3 artists, weighted to 1-2
        step = random.randint(0, 1)
        end = random.randint(1, insanitylevel3)




        # determine artist mode:
        # normal
        # hybrid |
        # switching A:B:X
        # adding at step x  a:X
        # stopping at step x ::X
        # enhancing from step  x




        modeselector = random.randint(0,10)
        if modeselector < 5 and end - step >= 2:
            artistmodeslist = ["hybrid", "stopping", "adding", "switching", "enhancing"]
            artistmode = artistmodeslist[modeselector]
            if artistmode in ["hybrid","switching"] and end - step == 1:
                artistmode = "normal"
        
        if artistmode in ["hybrid", "stopping", "adding","switching"]:
            completeprompt += " ["
            
        while step < end: 
            if(normal_dist(insanitylevel)):
                isweighted = 1
            
            if isweighted == 1:
                completeprompt += " ("

            completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
            
            if isweighted == 1:
                completeprompt += ":" + str(1 + (random.randint(-3,3)/10)) + ")"       
            
            if artistmode in ["hybrid"] and not end - step == 1:
                completeprompt += "|"
            if artistmode in ["switching"] and not end - step == 1:
                completeprompt += ":"
        
            if artistmode not in ["hybrid", "switching"]and not end - step == 1:
                completeprompt += ","
            
            isweighted = 0
            
            step = step + 1

        if artistmode in ["stopping"]:
            completeprompt += "::"
            completeprompt += str(random.randint(1,19))
        
        if artistmode in ["switching","adding"]:
            completeprompt += ":" + str(random.randint(1,18))
        if artistmode in ["hybrid", "stopping","adding", "switching"]:
            completeprompt += "]"


        completeprompt = completeprompt + ", "

        if artistmode in ["enhancing"]:
            completeprompt += " ["
    
    if(imagetype != "all" and imagetype != "all - force multiple" and imagetype != "only other types"):
            completeprompt += " " + imagetype + " "
    elif(imagetype == "all - force multiple"):
        amountofimagetypes = random.randint(2,3)
    elif(imagetype == "only other types"):
        othertype = 1
        completeprompt = add_from_csv(completeprompt, "othertypes", 1, ""," of a ")
    
    if(imagetype == "all" and normal_dist(insanitylevel)):
        amountofimagetypes = 1
    
    for i in range(amountofimagetypes):
    # one in 6 images is a complex/other type
        if(random.randint(0,5) < 5):
            completeprompt = add_from_csv(completeprompt, "imagetypes", 1, "",",")
        else:
            othertype = 1
            completeprompt = add_from_csv(completeprompt, "othertypes", 1, ""," of a ")


    if(mainchooser in ["object", "animal", "humanoid", "concept"] and othertype == 0 and "portait" not in completeprompt):
        completeprompt = add_from_csv(completeprompt, "shotsizes", 0, ""," of a ")
    elif("portait" in completeprompt):
        completeprompt += " ,close up of a "
   # Multiple subjects doesnt really work, need to think of other way to do multiple subjects. Maybe AND in the prompt?
   # if(subjectchooser in ["object", "animal", "humanoid"] and rare_dist(insanitylevel)):
   #     completeprompt = completeprompt[:-2] # remove a from 
   #     completeprompt = add_from_csv(completeprompt, "amounts", 0, "","")      

    
    # Common to have 1 description, uncommon to have 2
    if(common_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")

    if(uncommon_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")

    if(subjectchooser in ["animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "body_types", 0, "","")

    if(subjectchooser in ["object","animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "cultures", 0, "","")

    if(mainchooser == "object"):
        objecttypelist = ["objects", "buildings", "vehicles"]
        
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["

        chosenobjecttype = random.choice(objecttypelist)
        completeprompt = add_from_csv(completeprompt, chosenobjecttype, 0, "","")

        if(hybridorswap == "hybrid"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += "|" + random.choice(hybridlist) + "]"
            else:
                completeprompt += "|" 
                completeprompt = add_from_csv(completeprompt, chosenobjecttype, 0, "","") 
                completeprompt += "]"
        if(hybridorswap == "swap"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "]"
            else:
                completeprompt += ":"
                completeprompt = add_from_csv(completeprompt, chosenobjecttype, 0, "","") 
                completeprompt += ":" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""

    if(mainchooser == "animal"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
            
        if unique_dist(insanitylevel):
            wereanimaladded = 1
            completeprompt += "were-animal-"
        if(wereanimaladded != 1):
            completeprompt = add_from_csv(completeprompt, "animals", 0, "","")

        if(hybridorswap == "hybrid"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += "|" + random.choice(hybridlist) + "]"
            else:
                completeprompt += "| -animal- ]"
        if(hybridorswap == "swap"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "]"
            else:
                completeprompt += ":-animal-:" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""
    
    if(subjectchooser == "human"):
        completeprompt = add_from_csv(completeprompt, "manwoman", 0, "","")

    if(subjectchooser == "job"):
        completeprompt = add_from_csv(completeprompt, "malefemale", 0, "","")
        completeprompt = add_from_csv(completeprompt, "jobs", 0, "","")

    if(subjectchooser == "fictional"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt = add_from_csv(completeprompt, "fictional characters", 0, "","")

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + random.choice(hybridhumanlist) + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""

    if(subjectchooser == "non fictional"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["

        completeprompt = add_from_csv(completeprompt, "nonfictional characters", 0, "","")

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + random.choice(hybridhumanlist) + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""

    if(subjectchooser == "humanoid"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt = add_from_csv(completeprompt, "humanoids", 0, "","")

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + random.choice(hybridhumanlist) + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""

    if(subjectchooser == "landscape"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt = add_from_csv(completeprompt, "locations", 0, "","")

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + "-location-"  + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + "-location-" + ":" + str(random.randint(1,5)) +  "]"        
        hybridorswap = ""

        if(normal_dist(insanitylevel)):
            completeprompt += " and "
            if(rare_dist(insanitylevel)):
                completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")
            if(rare_dist(insanitylevel)):
                completeprompt = add_from_csv(completeprompt, "cultures", 0, "","")

            addontolocation = ["locations","buildings", "vehicles"]
            completeprompt = add_from_csv(completeprompt, random.choice(addontolocation), 0, "","")
    
    if(subjectchooser == "event"):
        completeprompt = add_from_csv(completeprompt, "events", 0, "\"","\"")
    
    if(subjectchooser == "concept"):
        completeprompt = add_from_csv(completeprompt, "concept_prefix", 0, "\" The "," of ")
        completeprompt = add_from_csv(completeprompt, "concept_suffix", 0, "","\"")

    # object with a face
    if(mainchooser == "object" and unique_dist(insanitylevel)):
        completeprompt += " with a face "

    # object materials
    if(mainchooser == "object" and uncommon_dist(insanitylevel)):
        completeprompt += "made from -material- "

    # object detailing
    if(mainchooser == "object" and rare_dist(insanitylevel)):
        completeprompt += "detailed with "
        if(uncommon_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")
        completeprompt += "-material- patterns "
        
    
    # riding an animal, holding an object or driving a vehicle, rare
    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and rare_dist(insanitylevel)):
        humanspecial = 1
        speciallist = [" riding a -animal- ", "holding a -object- ", " driving a -vehicle-", " visiting a -building-", "with a -animal-", "surrounded by -object-s"]
        completeprompt += random.choice(speciallist)

    # SD understands emoji's. Can be used to manipulate facial expressions.
    # emoji, legendary
    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "emojis", 1, "","")
        completeprompt += " ,"

    # cosplaying
    if(subjectchooser in ["animal as human", "non fictional", "humanoid"] and rare_dist(insanitylevel) and humanspecial != 1):
        completeprompt = add_from_csv(completeprompt, "fictional characters", 0, "cosplaying as ","")

    # Job 
    # either go job or activity, not both

    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and humanspecial != 1):
        joboractivitylist = ["jobs","human_activities"]
        completeprompt = add_from_csv(completeprompt, random.choice(joboractivitylist), 1, "","")


    if(subjectchooser in ["animal as human","human","job", "fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        skintypelist = ["-color-", "-material-"]
        completeprompt += ", with " + random.choice(skintypelist) + " skin, "

    # outfit builder
    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt += ", wearing"
        if(normal_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")
        if(uncommon_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "cultures", 0, "","")
        if(normal_dist(insanitylevel)):
            completeprompt += " -color- "
        if(rare_dist(insanitylevel)):
            completeprompt += " -material- "
        
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt = add_from_csv(completeprompt, "outfits", 0, "","")

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + "-outfit-" + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + "-outfit-" + ":" + str(random.randint(1,5)) +  "]"  
        hybridorswap = ""      

    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and uncommon_dist(insanitylevel) and humanspecial != 1):
        completeprompt = add_from_csv(completeprompt, "poses", 1, "","")
    
    if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt += ", "
        completeprompt = add_from_csv(completeprompt, "haircolors", 0, "","")
        completeprompt = add_from_csv(completeprompt, "hairstyles", 0, " hair styled as ","")

    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "accessories", 1, "","")
        # Sometimes get 2
        if(uncommon_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "accessories", 1, "","")

    
    if(subjectchooser not in ["landscape", "concept"] and humanspecial != 1 and normal_dist(insanitylevel)):
        backgroundtype = ["landscape", "buildingbackground", "insidebuilding"]
        match random.choice(backgroundtype):
            case "landscape":
                completeprompt = add_from_csv(completeprompt, "locations", 1, " background is ","")
            case "buildingbackground":
                completeprompt += ", background is "
                if(uncommon_dist(insanitylevel)):
                    completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")
                completeprompt = add_from_csv(completeprompt, "buildings", 0, "","")
            case "insidebuilding":
                completeprompt += ", inside a "
                if(uncommon_dist(insanitylevel)):
                    completeprompt = add_from_csv(completeprompt, "descriptors", 0, "","")
                completeprompt = add_from_csv(completeprompt, "buildings", 0, "","")





    # landscapes it is nice to always have a time period
    if(normal_dist(insanitylevel) or subjectchooser=="landscape"):
        completeprompt = add_from_csv(completeprompt, "timeperiods", 1, "","")

    if(mainchooser not in ["landscape"]  and rare_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "focus", 1, "","")
        
    # others
    if(normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "directions", 1, "","")   

    if(normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "moods", 1, "","")    

    if(normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "artmovements", 1, "","")     
    
    if(normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "lighting", 1, "","")    

    # determine wether we have a photo or not
    if("hoto" in completeprompt):
        isphoto = 1
        if(common_dist(insanitylevel)):
            completeprompt += ", film grain"
            
    if(isphoto == 1):
        completeprompt = add_from_csv(completeprompt, "cameras", 1, "","")   

    if(normal_dist(insanitylevel) or isphoto == 1):
        completeprompt = add_from_csv(completeprompt, "lenses", 1, "","")   

    if(normal_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "colorscheme", 1, "","")

    # vomit some cool/wierd things into the prompt
    if(uncommon_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "vomit", 1, "","")
        if(uncommon_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "vomit", 1, "","")


    # everyone loves the adding quality. The better models don't need this, but lets add it anyway
    if(uncommon_dist(insanitylevel)):
        completeprompt = add_from_csv(completeprompt, "quality", 1, "","")
        if(uncommon_dist(insanitylevel)):
            completeprompt = add_from_csv(completeprompt, "quality", 1, "","")


    if artistmode in ["enhancing"]:
        completeprompt += "::" + str(random.randint(1,17)) + "]"



    if(artists == "all" and artistsplacement == "back"):
        completeprompt += ", "
        # take 1-3 artists, weighted to 1-2
        step = random.randint(0, 1)
        end = random.randint(1, insanitylevel3)




        # determine artist mode:
        # normal
        # hybrid |
        # switching A:B:X
        # adding at step x  a:X
        # stopping at step x ::X

        
        modeselector = random.randint(0,10)
        if modeselector < 4 and end - step >= 2:
            artistmodeslist = ["hybrid", "stopping", "adding", "switching"]
            artistmode = artistmodeslist[modeselector]
            if artistmode in ["hybrid","switching"] and end - step == 1:
                artistmode = "normal"
        
        if artistmode in ["hybrid", "stopping", "adding","switching"]:
            completeprompt += " ["
            
        while step < end: 
            if(normal_dist(insanitylevel)):
                isweighted = 1
            
            if isweighted == 1:
                completeprompt += " ("

            completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
            
            if isweighted == 1:
                completeprompt += ":" + str(1 + (random.randint(-3,3)/10)) + ")"       
            
            if artistmode in ["hybrid"] and not end - step == 1:
                completeprompt += "|"
            if artistmode in ["switching"] and not end - step == 1:
                completeprompt += ":"
        
            if artistmode not in ["hybrid", "switching"]and not end - step == 1:
                completeprompt += ","
            
            isweighted = 0
            
            step = step + 1

        if artistmode in ["stopping"]:
            completeprompt += "::"
            completeprompt += str(random.randint(1,19))
        
        if artistmode in ["switching","adding"]:
            completeprompt += ":" + str(random.randint(1,18))
        if artistmode in ["hybrid", "stopping","adding", "switching"]:
            completeprompt += "]"


        completeprompt += ", "


    #replace any values
    colorlist = csv_to_list("colors")
    animallist = csv_to_list("animals")    
    materiallist = csv_to_list("materials")
    objectlist = csv_to_list("objects")
    fictionallist = csv_to_list("fictional characters")
    nonfictionallist = csv_to_list("nonfictional characters")
    conceptsuffixlist = csv_to_list("concept_suffix")
    buildinglist = csv_to_list("buildings")
    vehiclelist = csv_to_list("vehicles")
    outfitlist = csv_to_list("outfits")
    locationlist = csv_to_list("locations")
    
    # lol, this needs a rewrite :D
    while "-color-" in completeprompt or "-material-" in completeprompt or "-animal-" in completeprompt or "-object-" in completeprompt or "-fictional-" in completeprompt or "-nonfictional-" in completeprompt or "-conceptsuffix-" in completeprompt or "-building-" in completeprompt or "-vehicle-" in completeprompt or "-outfit-" in completeprompt or "-location-" in completeprompt:
        while "-object-" in completeprompt:
            completeprompt = completeprompt.replace('-object-', random.choice(objectlist),1)

        while "-location-" in completeprompt:
            completeprompt = completeprompt.replace('-location-', random.choice(locationlist),1)

        while "-outfit-" in completeprompt:
            completeprompt = completeprompt.replace('-outfit-', random.choice(outfitlist),1)
        
        while "-building-" in completeprompt:
            completeprompt = completeprompt.replace('-building-', random.choice(buildinglist),1)

        while "-vehicle-" in completeprompt:
            completeprompt = completeprompt.replace('-vehicle-', random.choice(vehiclelist),1)
        
        while "-conceptsuffix-" in completeprompt:
            completeprompt = completeprompt.replace('-conceptsuffix-', random.choice(conceptsuffixlist),1)
        
        while "-color-" in completeprompt:
            completeprompt = completeprompt.replace('-color-', random.choice(colorlist),1)

        while "-material-" in completeprompt:
            completeprompt = completeprompt.replace('-material-', random.choice(materiallist),1)
        
        while "-fictional-" in completeprompt:
            completeprompt = completeprompt.replace('-fictional-', random.choice(fictionallist),1)
        
        while "-nonfictional-" in completeprompt:
            completeprompt = completeprompt.replace('-nonfictional-', random.choice(nonfictionallist),1)

        while "-animal-" in completeprompt:
            completeprompt = completeprompt.replace('-animal-', random.choice(animallist),1)

    completeprompt = re.sub('\[ ', '[', completeprompt)
    completeprompt = re.sub(' \]', ']', completeprompt)
    completeprompt = re.sub(' \|', '|', completeprompt)
    completeprompt = re.sub(' \"', '\"', completeprompt)
    completeprompt = re.sub('\" ', '\"', completeprompt)
    completeprompt = re.sub('\( ', '(', completeprompt)
    completeprompt = re.sub(' \(', '(', completeprompt)
    completeprompt = re.sub('\) ', ')', completeprompt)
    completeprompt = re.sub(' \)', ')', completeprompt)

    completeprompt = re.sub(' :', ':', completeprompt)

    completeprompt = re.sub(',,', ',', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(' , ', ', ', completeprompt)
    completeprompt = re.sub(',\(', ', (', completeprompt)

    completeprompt = re.sub('a The', 'The', completeprompt)
    completeprompt = re.sub('ss ', 's ', completeprompt)

    completeprompt = re.sub(' +', ' ', completeprompt[2:]) # remove first character, that is always a comma. Remove any excess spaces

    completeprompt = completeprompt.strip(", ")
    print(completeprompt)
    return completeprompt
    