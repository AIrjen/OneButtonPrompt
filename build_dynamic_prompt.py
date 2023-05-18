import random
import re
from csv_reader import *
from random_functions import *




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all", onlyartists = False, antivalues = "", prefixprompt = "", suffixprompt ="",promptcompounderlevel ="1", seperator = "comma", givensubject="",smartsubject = True):

    
    # first build up a complete anti list. Those values are removing during list building
    # this uses the antivalues string AND the antilist.csv
    emptylist = []
    antilist = csv_to_list("antilist",emptylist , "./userfiles/",1)
    antivaluelist = antivalues.split(",")

    antilist += antivaluelist

    # build all lists here

    colorlist = csv_to_list("colors",antilist)
    animallist = csv_to_list("animals",antilist)    
    materiallist = csv_to_list("materials",antilist)
    objectlist = csv_to_list("objects",antilist)
    fictionallist = csv_to_list("fictional characters",antilist)
    nonfictionallist = csv_to_list("nonfictional characters",antilist)
    conceptsuffixlist = csv_to_list("concept_suffix",antilist)
    buildinglist = csv_to_list("buildings",antilist)
    vehiclelist = csv_to_list("vehicles",antilist)
    outfitlist = csv_to_list("outfits",antilist)
    locationlist = csv_to_list("locations",antilist)

    accessorielist = csv_to_list("accessories",antilist)
    artmovementlist = csv_to_list("artmovements",antilist)
    bodytypelist = csv_to_list("body_types",antilist)
    cameralist = csv_to_list("cameras",antilist)
    colorschemelist = csv_to_list("colorscheme",antilist)
    conceptprefixlist = csv_to_list("concept_prefix",antilist)
    culturelist = csv_to_list("cultures",antilist)
    descriptorlist = csv_to_list("descriptors",antilist)
    devmessagelist = csv_to_list("devmessages",antilist)
    directionlist = csv_to_list("directions",antilist)
    emojilist = csv_to_list("emojis",antilist)
    eventlist = csv_to_list("events",antilist)
    focuslist = csv_to_list("focus",antilist)
    greatworklist = csv_to_list("greatworks",antilist)
    haircolorlist = csv_to_list("haircolors",antilist)
    hairstylelist = csv_to_list("hairstyles",antilist)
    humanactivitylist = csv_to_list("human_activities",antilist)
    humanoidlist = csv_to_list("humanoids",antilist)
    imagetypelist = csv_to_list("imagetypes",antilist)
    joblist = csv_to_list("jobs",antilist)
    lenslist = csv_to_list("lenses",antilist)
    lightinglist = csv_to_list("lighting",antilist)
    malefemalelist = csv_to_list("malefemale",antilist)
    manwomanlist = csv_to_list("manwoman",antilist)
    moodlist = csv_to_list("moods",antilist)
    othertypelist = csv_to_list("othertypes",antilist)
    poselist = csv_to_list("poses",antilist)
    qualitylist = csv_to_list("quality",antilist)
    shotsizelist = csv_to_list("shotsizes",antilist)
    timeperiodlist = csv_to_list("timeperiods",antilist)
    vomitlist = csv_to_list("vomit",antilist)

    # build artists list
    # create artist list to use in the code, maybe based on category  or personal lists
    if(artists != "all" and artists != "none" and artists.startswith("personal_artists") == False and artists.startswith("personal artists") == False):
        artistlist = artist_category_csv_to_list("artists_and_category",artists)
    elif(artists.startswith("personal_artists") == True or artists.startswith("personal artists") == True):
        artists = artists.replace(" ","_",-1) # add underscores back in
        artistlist = csv_to_list(artists,antilist,"./userfiles/")
    else:
        artistlist = csv_to_list("artists",antilist)


    # add any other custom lists
    stylestiloralist = csv_to_list("styles_ti_lora",antilist,"./userfiles/")
    generatestyle = bool(stylestiloralist) # True of not empty

    custominputprefixlist = csv_to_list("custom_input_prefix",antilist,"./userfiles/")
    generatecustominputprefix = bool(custominputprefixlist) # True of not empty

    custominputmidlist = csv_to_list("custom_input_mid",antilist,"./userfiles/")
    generatecustominputmid = bool(custominputmidlist) # True of not empty

    custominputsuffixlist = csv_to_list("custom_input_suffix",antilist,"./userfiles/")
    generatecustominputsuffix = bool(custominputsuffixlist) # True of not empty


    generateoutfit = True
    generatebodytype = True
    generateaccesorie = True
    generateartmovement = True
    generatebackground = True
    generatecamera = True
    generatecolorscheme = True
    generatedescriptors = True
    generatedirection = True
    generatefocus = True
    generatehairstyle = True
    generatelens = True
    generatelighting = True
    generatemood = True
    generatepose = True
    generatevomit = True
    generatequality = True
    generateshot = True
    generatetimeperiod = True

    # Smart subject logic
    if(givensubject !="" and smartsubject == True):
    
        # Remove any list that has a matching word in the list
        # Remove any list/logic with keywords, such as:
        # wearing, bodytype, pose, location, hair, background

        # first get all the words

        # Split the string by commas and spaces
        words = re.split(r'[,\s]+', givensubject)
        # Remove leading/trailing whitespaces from each word
        words = [word.strip() for word in words]

        # Filter out empty words
        words = [word for word in words if word]

        # Convert the list to a set to remove duplicates, then convert it back to a list
        givensubjectlistsinglewords = list(set(words))

        # now get all words clumped together by commas
        if ',' in givensubject:
            allwords = givensubject.split(',')
        else:
            allwords = [givensubject]
        # Remove leading/trailing whitespaces from each word and convert to lowercase
        words = [word.strip().lower() for word in allwords]

        # Filter out empty words and duplicates
        givensubjectlistwords = list(set(filter(None, words)))

        givensubjectlist = givensubjectlistsinglewords + givensubjectlistwords


        # Check only for the lists that make sense?
        
        # outfit
        foundinlist = any(word.lower() in [item.lower() for item in outfitlist] for word in givensubjectlist)
        keywordslist = ["wearing","outfit", "dressed"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generateoutfit = False
        
        # bodytype
        foundinlist = any(word.lower() in [item.lower() for item in bodytypelist] for word in givensubjectlist)
        keywordslist = ["bodytype","body type"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatebodytype = False

        # hair
        foundinlist = any(word.lower() in [item.lower() for item in hairstylelist] for word in givensubjectlist)
        keywordslist = ["hair"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatehairstyle = False
        
        # descriptorlist
        foundinlist = any(word.lower() in [item.lower() for item in descriptorlist] for word in givensubjectlist)
        foundinlist2 = any(word.lower() in [item.lower() for item in culturelist] for word in givensubjectlist)
        if(foundinlist == True or foundinlist2 == True):
            generatedescriptors = False

        # background
        foundinlist = any(word.lower() in [item.lower() for item in locationlist] for word in givensubjectlist)
        foundinlist2 = any(word.lower() in [item.lower() for item in buildinglist] for word in givensubjectlist)
        keywordslist = ["location","background"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or foundinlist2 == True or keywordsinstring == True):
            generatebackground = False

        # accessorielist
        foundinlist = any(word.lower() in [item.lower() for item in accessorielist] for word in givensubjectlist)
        if(foundinlist == True):
            generateaccesorie = False

        # lenslist
        foundinlist = any(word.lower() in [item.lower() for item in lenslist] for word in givensubjectlist)
        if(foundinlist == True):
            generatelens = False

        # lightinglist
        foundinlist = any(word.lower() in [item.lower() for item in lightinglist] for word in givensubjectlist)
        keywordslist = ["lighting"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatelighting = False

        # mood
        foundinlist = any(word.lower() in [item.lower() for item in moodlist] for word in givensubjectlist)
        keywordslist = ["mood"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatemood = False


        # poselist
        foundinlist = any(word.lower() in [item.lower() for item in poselist] for word in givensubjectlist)
        keywordslist = ["pose", "posing"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatepose = False

        # qualitylist
        foundinlist = any(word.lower() in [item.lower() for item in qualitylist] for word in givensubjectlist)
        keywordslist = ["quality"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatequality = False

        # shotsize
        foundinlist = any(word.lower() in [item.lower() for item in shotsizelist] for word in givensubjectlist)
        keywordslist = ["shot"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generateshot = False

        # timeperiodlist
        foundinlist = any(word.lower() in [item.lower() for item in timeperiodlist] for word in givensubjectlist)
        if(foundinlist == True):
            generatetimeperiod = False

        # vomit
        foundinlist = any(word.lower() in [item.lower() for item in vomitlist] for word in givensubjectlist)
        if(foundinlist == True):
            generatevomit = False

        # directionlist
        foundinlist = any(word.lower() in [item.lower() for item in directionlist] for word in givensubjectlist)
        if(foundinlist == True):
            generatedirection = False

        # focus
        foundinlist = any(word.lower() in [item.lower() for item in focuslist] for word in givensubjectlist)
        if(foundinlist == True):
            generatefocus = False

        # artmovementlist
        foundinlist = any(word.lower() in [item.lower() for item in artmovementlist] for word in givensubjectlist)
        if(foundinlist == True):
            generateartmovement = False
        
        # camera
        foundinlist = any(word.lower() in [item.lower() for item in cameralist] for word in givensubjectlist)
        if(foundinlist == True):
            generatecamera = False

        # colorschemelist
        foundinlist = any(word.lower() in [item.lower() for item in colorschemelist] for word in givensubjectlist)
        if(foundinlist == True):
            generatecolorscheme = False





    # Start of building prompt
    completeprompt = ""


    
    
    promptstocompound = int(promptcompounderlevel)
    compoundcounter = 0

    while compoundcounter < promptstocompound:
        isphoto = 0
        othertype = 0
        humanspecial = 0
        animaladdedsomething = 0
        isweighted = 0
        amountofimagetypes = 0
        hybridorswap = ""
        artistmode = "normal"
        insideshot = 0
      
        completeprompt += prefixprompt

        completeprompt += ", "


        # custom prefix list
        if(uncommon_dist(insanitylevel) and generatecustominputprefix == True):
            completeprompt += random.choice(custominputprefixlist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(custominputprefixlist) + ", "



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


            completeprompt += ", "



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
                completeprompt += ", " + random.choice(imagetypelist) + " "
            else:
                othertype = 1
                completeprompt += ", " + random.choice(othertypelist) + " "
        
        if(othertype==1):
            completeprompt += " of a "


        # start shot size

        if(mainchooser in ["object", "animal", "humanoid", "concept"] and othertype == 0 and "portrait" not in completeprompt and generateshot == True):
            completeprompt += random.choice(shotsizelist) + " of a "
        elif("portrait" in completeprompt):
            completeprompt += " ,close up of a "
        elif(mainchooser in ["landscape"]):
            completeprompt += " landscape of a "
    

        # start subject building
        
        # start with descriptive qualities
        
        # Common to have 1 description, uncommon to have 2
        if(common_dist(insanitylevel) and generatedescriptors == True):
            completeprompt += random.choice(descriptorlist) + " "

        if(uncommon_dist(insanitylevel) and generatedescriptors == True):
            completeprompt += random.choice(descriptorlist) + " "

        if(subjectchooser in ["animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel) and generatebodytype == True):
            completeprompt += random.choice(bodytypelist) + " "

        if(subjectchooser in ["object","animal as human,","human", "job", "fictional", "non fictional", "humanoid"] and normal_dist(insanitylevel) and generatedescriptors == True):
            completeprompt += random.choice(culturelist) + " "

        if(mainchooser == "object"):
            objecttypelist = [objectlist, buildinglist, vehiclelist]  # first select a random list, then randomly select from the corresponding list
            
            # if we have a given subject, we should skip making an actual subject
            if(givensubject == ""):

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
            else:
                completeprompt += " " + givensubject + " "
            
            hybridorswap = ""

        if(mainchooser == "animal"):
            
            # if we have a given subject, we should skip making an actual subject
            if(givensubject == ""):

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
            else:
                completeprompt += " " + givensubject + " "
            
            hybridorswap = ""
        
        # if we have a given subject, we should skip making an actual subject
        if(mainchooser == "humanoid"):
            if(givensubject==""):

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
            else:
                completeprompt += " " + givensubject + " "     

        
        if(subjectchooser == "landscape"):
            
            # if we have a given subject, we should skip making an actual subject
            if(givensubject == ""):
                if rare_dist(insanitylevel):
                    hybridorswaplist = ["hybrid", "swap"]
                    hybridorswap = random.choice(hybridorswaplist)
                    completeprompt += "["
                
                completeprompt += random.choice(locationlist) + " "

                if(hybridorswap == "hybrid"):
                    completeprompt += "|" + "-location-"  + "]"
                if(hybridorswap == "swap"):
                    completeprompt += ":" + "-location-" + ":" + str(random.randint(1,5)) +  "]"        
            else:
                completeprompt += " " + givensubject + " " 
            
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


        if(mainchooser == "concept"):
            if(givensubject == ""):
                if(subjectchooser == "event"):
                    completeprompt += " \"" + random.choice(eventlist) + "\" "
                
                if(subjectchooser == "concept"):
                    completeprompt += " \" The " + random.choice(conceptprefixlist) + " of " + random.choice(conceptsuffixlist) + "\" "
            else:
                completeprompt += " " + givensubject + " " 

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

        # custom mid list
        if(uncommon_dist(insanitylevel) and generatecustominputmid == True):
            completeprompt += random.choice(custominputmidlist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(custominputmidlist) + ", "
        
        
        # outfit builder
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generateoutfit == True):
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

        
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and uncommon_dist(insanitylevel) and humanspecial != 1 and generatepose == True):
            completeprompt += random.choice(poselist) + ", "
        
        if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generatehairstyle == True):
            completeprompt += random.choice(haircolorlist) + " "
            completeprompt += " hair styled as " + random.choice(hairstylelist) + ", "

        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generateaccesorie == True):
            completeprompt += random.choice(accessorielist) + ", "
            # Sometimes get 2
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(accessorielist) + ", "
            # or even three, these are fun and often minor :)
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(accessorielist) + ", "

        if(legendary_dist(insanitylevel) and subjectchooser not in ["landscape", "concept"] and generatebackground == True):
            insideshot = 1
            completeprompt += ", from inside of a "
            addontolocation = [locationlist,buildinglist]
            completeprompt += random.choice(random.choice(addontolocation)) + ", "
        
        if(subjectchooser not in ["landscape", "concept"] and humanspecial != 1 and insideshot == 0 and normal_dist(insanitylevel) and generatebackground == True):
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
            if(generatetimeperiod == True):
                completeprompt += random.choice(timeperiodlist) + ", "

        if(mainchooser not in ["landscape"]  and rare_dist(insanitylevel) and generatefocus == True):
            completeprompt += random.choice(focuslist) + ", "
            


        # others
        if(normal_dist(insanitylevel) and generatedirection == True):
            completeprompt += random.choice(directionlist) + ", "

        if(normal_dist(insanitylevel) and generatemood == True):
            completeprompt += random.choice(moodlist) + ", " 

        if(normal_dist(insanitylevel) and generateartmovement == True):
            completeprompt += random.choice(artmovementlist) + ", "  
        
        if(normal_dist(insanitylevel) and generatelighting == True):
            completeprompt += random.choice(lightinglist) + ", "  

        # determine wether we have a photo or not
        if("hoto" in completeprompt):
            isphoto = 1
            if(common_dist(insanitylevel) and not "film grain" in antilist):
                completeprompt += ", film grain, "
                
        if(isphoto == 1 and generatecamera == True):
            completeprompt += random.choice(cameralist) + ", "  

        if(normal_dist(insanitylevel) or isphoto == 1):
            if(generatelens == True):
                completeprompt += random.choice(lenslist) + ", "

        if(normal_dist(insanitylevel) and generatecolorscheme == True):
            completeprompt += random.choice(colorschemelist) + ", "

        # vomit some cool/wierd things into the prompt
        if(uncommon_dist(insanitylevel) and generatevomit == True):
            completeprompt += random.choice(vomitlist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(vomitlist) + ", "

        #adding a great work of art, like starry night has cool effects. But this should happen only very rarely.
        if(novel_dist(insanitylevel)):
            completeprompt += " in the style of " + random.choice(greatworklist) + ", "

        # everyone loves the adding quality. The better models don't need this, but lets add it anyway
        if(uncommon_dist(insanitylevel) and generatequality == True):
            completeprompt += random.choice(qualitylist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(qualitylist) + ", "

        # custom style list
        if(uncommon_dist(insanitylevel) and generatestyle == True):
            completeprompt += random.choice(stylestiloralist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(stylestiloralist) + ", "


        # custom suffix list
        if(uncommon_dist(insanitylevel) and generatecustominputsuffix == True):
            completeprompt += random.choice(custominputsuffixlist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(custominputsuffixlist) + ", "



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
            # end of the artist stuff

        
        completeprompt += ", "
        completeprompt += suffixprompt

        # and then up the compounding stuff
        compoundcounter += 1
        
        # Here comes all the seperator stuff for prompt compounding
        if(compoundcounter < promptstocompound):
            if(seperator == "comma"):
                completeprompt += " \n , "
            else:
                completeprompt += " \n " + seperator + " "





    #end of the while loop, now clean up the prompt
    
    # lol, this needs a rewrite :D
    while "-color-" in completeprompt or "-material-" in completeprompt or "-animal-" in completeprompt or "-object-" in completeprompt or "-fictional-" in completeprompt or "-nonfictional-" in completeprompt or "-conceptsuffix-" in completeprompt or "-building-" in completeprompt or "-vehicle-" in completeprompt or "-outfit-" in completeprompt or "-location-" in completeprompt or "-conceptprefix-" in completeprompt or "-descriptor-" in completeprompt:
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
        
        while "-conceptprefix-" in completeprompt:
            completeprompt = completeprompt.replace('-conceptprefix-', random.choice(conceptprefixlist),1)

        while "-descriptor-" in completeprompt:
            completeprompt = completeprompt.replace('-descriptor-', random.choice(descriptorlist),1)

    

    
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
    completeprompt = re.sub(', ,', ',', completeprompt)


    completeprompt = completeprompt.strip(", ")



    #just for me, some fun with posting fake dev messages (ala old sim games)
    if(random.randint(1, 50)==1):
        print("")
        print(random.choice(devmessagelist))
        print("")

    print(completeprompt)
    return completeprompt
    