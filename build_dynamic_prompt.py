import random
import re
from csv_reader import *
from random_functions import *




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all", onlyartists = False):

    completeprompt = ", "

    isphoto = 0
    othertype = 0
    humanspecial = 0
    animaladdedsomething = 0
    isweighted = 0
    amountofimagetypes = 0
    hybridorswap = ""
    artistmode = "normal"
    insideshot = 0


    # build all lists here

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

    accessorielist = csv_to_list("accessories")
    artmovementlist = csv_to_list("artmovements")
    bodytypelist = csv_to_list("body_types")
    cameralist = csv_to_list("cameras")
    colorschemelist = csv_to_list("colorscheme")
    conceptprefixlist = csv_to_list("concept_prefix")
    culturelist = csv_to_list("cultures")
    descriptorlist = csv_to_list("descriptors")
    devmessagelist = csv_to_list("devmessages")
    directionlist = csv_to_list("directions")
    emojilist = csv_to_list("emojis")
    eventlist = csv_to_list("events")
    focuslist = csv_to_list("focus")
    greatworklist = csv_to_list("greatworks")
    haircolorlist = csv_to_list("haircolors")
    hairstylelist = csv_to_list("hairstyles")
    humanactivitylist = csv_to_list("human_activities")
    humanoidlist = csv_to_list("humanoids")
    imagetypelist = csv_to_list("imagetypes")
    joblist = csv_to_list("jobs")
    lenslist = csv_to_list("lenses")
    lightinglist = csv_to_list("lighting")
    malefemalelist = csv_to_list("malefemale")
    manwomanlist = csv_to_list("manwoman")
    moodlist = csv_to_list("moods")
    othertypelist = csv_to_list("othertypes")
    poselist = csv_to_list("poses")
    qualitylist = csv_to_list("quality")
    shotsizelist = csv_to_list("shotsizes")
    timeperiodlist = csv_to_list("timeperiods")
    vomitlist = csv_to_list("vomit")



    # create artist list to use in the code, maybe based on category
    if(artists != "all" and artists != "none"):
        artistlist = artist_category_csv_to_list("artists_and_category",artists)
    else:
        artistlist = csv_to_list("artists")



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
    

    # start artist part

    artistsplacement = "front"
    if(uncommon_dist(insanitylevel) and onlyartists == False):
        artistsplacement = "back"

    if(artists != "none" and artistsplacement == "front"):
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
            if (artistmode in ["hybrid","switching"] and end - step == 1):
                artistmode = "normal"
        
        if(onlyartists == True and artistmode == "enhancing"):
            artistmode = "normal"
        if(onlyartists == True and step == end):
            step = step - 1

        if artistmode in ["hybrid", "stopping", "adding","switching"]:
            completeprompt += " ["
            
        while step < end: 
            if(normal_dist(insanitylevel)):
                isweighted = 1
            
            if isweighted == 1:
                completeprompt += " ("

            #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
            completeprompt += "art by " + random.choice(artistlist)
            
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


        if(onlyartists == True):
            completeprompt = completeprompt.strip(", ")
            print("only generated these artists:" + completeprompt)
            return completeprompt


        completeprompt = completeprompt + ", "



        if artistmode in ["enhancing"]:
            completeprompt += " ["
    
    # start image type

    if(imagetype != "all" and imagetype != "all - force multiple" and imagetype != "only other types"):
            completeprompt += " " + imagetype + ", "
    elif(imagetype == "all - force multiple" or unique_dist(insanitylevel)):
        amountofimagetypes = random.randint(2,3)
    elif(imagetype == "only other types"):
        othertype = 1
        completeprompt += random.choice(othertypelist) + " of a "
    
    if(imagetype == "all" and normal_dist(insanitylevel) and amountofimagetypes <= 1):
        amountofimagetypes = 1
    
    for i in range(amountofimagetypes):
    # one in 6 images is a complex/other type
        if(random.randint(0,5) < 5):
            completeprompt += random.choice(imagetypelist) + ", "
        else:
            othertype = 1
            completeprompt += random.choice(othertypelist) + " of a "


    # start shot size

    if(mainchooser in ["object", "animal", "humanoid", "concept"] and othertype == 0 and "portrait" not in completeprompt):
        completeprompt += random.choice(shotsizelist) + " of a "
    elif("portrait" in completeprompt):
        completeprompt += " ,close up of a "
   

    # start subject building
    
    # start with descriptive qualities
    
    # Common to have 1 description, uncommon to have 2
    if(common_dist(insanitylevel)):
        completeprompt += random.choice(descriptorlist) + " "

    if(uncommon_dist(insanitylevel)):
        completeprompt += random.choice(descriptorlist) + " "

    if(subjectchooser in ["animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel)):
        completeprompt += random.choice(bodytypelist) + " "

    if(subjectchooser in ["object","animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel)):
        completeprompt += random.choice(culturelist) + " "

    if(mainchooser == "object"):
        objecttypelist = [objectlist, buildinglist, vehiclelist]  # first select a random list, then randomly select from the corresponding list
        
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["

        chosenobjecttype = random.choice(objecttypelist)

        completeprompt += random.choice(chosenobjecttype) + " "

        if(hybridorswap == "hybrid"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += "|" + random.choice(hybridlist) + "]"
            else:
                completeprompt += "|" 
                completeprompt += random.choice(chosenobjecttype) + " "
                completeprompt += "]"
        if(hybridorswap == "swap"):
            if(uncommon_dist(insanitylevel)):
                completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "]"
            else:
                completeprompt += ":"
                completeprompt += random.choice(chosenobjecttype) + " "
                completeprompt += ":" + str(random.randint(1,5)) +  "]"
        hybridorswap = ""

    if(mainchooser == "animal"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
            
        if unique_dist(insanitylevel):
            animaladdlist = ["baby", "were", "giant", "monster"]
            animaladdedsomething = 1
            completeprompt += random.choice(animaladdlist) + " -animal-"
        if(animaladdedsomething != 1):
            completeprompt += random.choice(animallist) + " "

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
        completeprompt += random.choice(manwomanlist) + " "

    if(subjectchooser == "job"):
        completeprompt += random.choice(malefemalelist) + " "
        completeprompt += random.choice(joblist) + " "

    if(subjectchooser == "fictional"):
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt += random.choice(fictionallist) + " "

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

        completeprompt += random.choice(nonfictionallist) + " "

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
        
        completeprompt += random.choice(humanoidlist) + " "

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
        
        completeprompt += random.choice(locationlist) + " "

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + "-location-"  + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + "-location-" + ":" + str(random.randint(1,5)) +  "]"        
        hybridorswap = ""

        # shots from inside can create cool effects in landscapes
        if(unique_dist(insanitylevel)):
            insideshot = 1
            completeprompt += " from inside of a "
            addontolocation = [locationlist,buildinglist]
            completeprompt += random.choice(random.choice(addontolocation)) + " "

        if(normal_dist(insanitylevel) and insideshot == 0):
            completeprompt += " and "
            if(rare_dist(insanitylevel)):
                completeprompt += random.choice(descriptorlist) + " " 
            if(rare_dist(insanitylevel)):
                completeprompt += random.choice(culturelist) + " "

            addontolocation = [locationlist,buildinglist, vehiclelist]
            completeprompt += random.choice(random.choice(addontolocation)) + " "


    if(subjectchooser == "event"):
        completeprompt += " \"" + random.choice(eventlist) + "\" "
    
    if(subjectchooser == "concept"):
        completeprompt += " \" The " + random.choice(conceptprefixlist) + " of " + random.choice(conceptsuffixlist) + "\" "

    # object with a face
    if(mainchooser == "object" and unique_dist(insanitylevel)):
        completeprompt += " with a face "

    # object materials
    if(mainchooser == "object" and uncommon_dist(insanitylevel)):
        completeprompt += " made from -material- "

    # object detailing
    if(mainchooser == "object" and rare_dist(insanitylevel)):
        completeprompt += " detailed with "
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(descriptorlist) + " "
        completeprompt += "-material- patterns "
        
    
    # riding an animal, holding an object or driving a vehicle, rare
    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and rare_dist(insanitylevel)):
        humanspecial = 1
        speciallist = [" riding a -animal- ", " holding a -object- ", " driving a -vehicle-", " visiting a -building-", " with a -animal-", " surrounded by -object-s"]
        completeprompt += random.choice(speciallist)
        


    completeprompt += ", "

    # SD understands emoji's. Can be used to manipulate facial expressions.
    # emoji, legendary
    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        completeprompt += random.choice(emojilist) + ", "
        

    # cosplaying
    if(subjectchooser in ["animal as human", "non fictional", "humanoid"] and rare_dist(insanitylevel) and humanspecial != 1):
        completeprompt += "cosplaying as " + random.choice(fictionallist) + ", "

    # Job 
    # either go job or activity, not both

    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and humanspecial != 1):
        joboractivitylist = [joblist,humanactivitylist]
        completeprompt += random.choice(random.choice(joboractivitylist)) + ", "


    if(subjectchooser in ["animal as human","human","job", "fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        skintypelist = ["-color-", "-material-"]
        completeprompt += ", with " + random.choice(skintypelist) + " skin, "

    # outfit builder
    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt += ", wearing "
        if(normal_dist(insanitylevel)):
            completeprompt += random.choice(descriptorlist) + " "
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(culturelist) + " "
        if(normal_dist(insanitylevel)):
            completeprompt += " -color- "
        if(rare_dist(insanitylevel)):
            completeprompt += " -material- "
        
        if rare_dist(insanitylevel):
            hybridorswaplist = ["hybrid", "swap"]
            hybridorswap = random.choice(hybridorswaplist)
            completeprompt += "["
        
        completeprompt += random.choice(outfitlist) + " "

        if(hybridorswap == "hybrid"):
            completeprompt += "|" + "-outfit-" + "]"
        if(hybridorswap == "swap"):
            completeprompt += ":" + "-outfit-" + ":" + str(random.randint(1,5)) +  "]"  
        hybridorswap = ""
        completeprompt += ", "      

    
    if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and uncommon_dist(insanitylevel) and humanspecial != 1):
        completeprompt += random.choice(poselist) + ", "
    
    if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt += random.choice(haircolorlist) + " "
        completeprompt += " hair styled as " + random.choice(hairstylelist) + ", "

    if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel)):
        completeprompt += random.choice(accessorielist) + ", "
        # Sometimes get 2
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(accessorielist) + ", "
        # or even three, these are fun and often minor :)
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(accessorielist) + ", "

    if(legendary_dist(insanitylevel) and subjectchooser not in ["landscape", "concept"]):
        insideshot = 1
        completeprompt += ", from inside of a "
        addontolocation = [locationlist,buildinglist]
        completeprompt += random.choice(random.choice(addontolocation)) + ", "
    
    if(subjectchooser not in ["landscape", "concept"] and humanspecial != 1 and insideshot == 0 and normal_dist(insanitylevel)):
        backgroundtypelist = ["landscape", "buildingbackground", "insidebuilding"]
        backgroundtype = random.choice(backgroundtypelist)
        if(backgroundtype == "landscape"):
            completeprompt += "background is " + random.choice(locationlist) + ", "
        elif(backgroundtype == "buildingbackground"):
            completeprompt += ", background is "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(descriptorlist) + " "
            completeprompt += random.choice(buildinglist) + ", "
        elif(backgroundtype == "insidebuilding"):
            completeprompt += ", inside a "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(descriptorlist) + " "
            completeprompt += random.choice(buildinglist) + ", "





    # landscapes it is nice to always have a time period
    if(normal_dist(insanitylevel) or subjectchooser=="landscape"):
        completeprompt += random.choice(timeperiodlist) + ", "

    if(mainchooser not in ["landscape"]  and rare_dist(insanitylevel)):
        completeprompt += random.choice(focuslist) + ", "
        


    # others
    if(normal_dist(insanitylevel)):
        completeprompt += random.choice(directionlist) + ", "

    if(normal_dist(insanitylevel)):
        completeprompt += random.choice(moodlist) + ", " 

    if(normal_dist(insanitylevel)):
        completeprompt += random.choice(artmovementlist) + ", "  
    
    if(normal_dist(insanitylevel)):
        completeprompt += random.choice(lightinglist) + ", "  

    # determine wether we have a photo or not
    if("hoto" in completeprompt):
        isphoto = 1
        if(common_dist(insanitylevel)):
            completeprompt += ", film grain, "
            
    if(isphoto == 1):
        completeprompt += random.choice(cameralist) + ", "  

    if(normal_dist(insanitylevel) or isphoto == 1):
        completeprompt += random.choice(lenslist) + ", "

    if(normal_dist(insanitylevel)):
        completeprompt += random.choice(colorschemelist) + ", "

    # vomit some cool/wierd things into the prompt
    if(uncommon_dist(insanitylevel)):
        completeprompt += random.choice(vomitlist) + ", "
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(vomitlist) + ", "

    #adding a great work of art, like starry night has cool effects. But this should happen only very rarely.
    if(novel_dist(insanitylevel)):
        completeprompt += " in the style of " + random.choice(greatworklist) + ", "

    # everyone loves the adding quality. The better models don't need this, but lets add it anyway
    if(uncommon_dist(insanitylevel)):
        completeprompt += random.choice(qualitylist) + ", "
        if(uncommon_dist(insanitylevel)):
            completeprompt += random.choice(qualitylist) + ", "


    if artistmode in ["enhancing"]:
        completeprompt += "::" + str(random.randint(1,17)) + "]"



    if(artists != "none" and artistsplacement == "back"):
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

            #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
            completeprompt += "art by " + random.choice(artistlist)
            
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

    completeprompt = re.sub(',,', ', ', completeprompt)
    completeprompt = re.sub(',,,', ', ', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(' , ', ', ', completeprompt)
    completeprompt = re.sub(',\(', ', (', completeprompt)

    completeprompt = re.sub('a The', 'The', completeprompt)

    completeprompt = re.sub(' +', ' ', completeprompt[2:]) # remove first character, that is always a comma. Remove any excess spaces

    completeprompt = completeprompt.strip(", ")

    #just for me, some fun with posting fake dev messages (ala old sim games)
    if(random.randint(1, 50)==1):
        print("")
        print(random.choice(devmessagelist))
        print("")

    print(completeprompt)
    return completeprompt
    