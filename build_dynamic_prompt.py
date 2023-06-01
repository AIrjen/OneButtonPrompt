import random
import re
from csv_reader import *
from random_functions import *




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all", onlyartists = False, antivalues = "", prefixprompt = "", suffixprompt ="",promptcompounderlevel ="1", seperator = "comma", givensubject="",smartsubject = True,giventypeofimage=""):

    
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
    foodlist = csv_to_list("foods", antilist)
    genderdescriptionlist = csv_to_list("genderdescription", antilist)
    minilocationlist = csv_to_list("minilocations", antilist)
    minioutfitlist = csv_to_list("minioutfits", antilist)
    seasonlist = csv_to_list("seasons", antilist)

    humanlist = fictionallist + nonfictionallist + humanoidlist
    objecttotallist = objectlist + buildinglist + vehiclelist + foodlist

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

    # special lists
    backgroundtypelist = csv_to_list("backgroundtypes", antilist,"./csvfiles/special_lists/")
    insideshotlist =  csv_to_list("insideshots", antilist,"./csvfiles/special_lists/")
    photoadditionlist = csv_to_list("photoadditions", antilist,"./csvfiles/special_lists/")
    buildhairlist = csv_to_list("buildhair", antilist,"./csvfiles/special_lists/")
    buildoutfitlist = csv_to_list("buildoutfit", antilist,"./csvfiles/special_lists/")
    objectadditionslist = csv_to_list("objectadditions", antilist,"./csvfiles/special_lists/")
    humanadditionlist = csv_to_list("humanadditions", antilist,"./csvfiles/special_lists/")
    animaladditionlist = csv_to_list("animaladditions", antilist,"./csvfiles/special_lists/")
    buildaccessorielist = csv_to_list("buildaccessorie", antilist,"./csvfiles/special_lists/")
    minilocationadditionslist = csv_to_list("minilocationadditions", antilist,"./csvfiles/special_lists/")



    
    # subjects
    mainchooserlist = []
    objectwildcardlist = []
    hybridlist = []
    hybridhumanlist = []
    humanoidsubjectchooserlist = []
    eventsubjectchooserlist = []
    addontolocationinside = []
    addontolocation = []

    generatevehicle = bool(vehiclelist)
    generateobject = bool(objectlist)
    generatefood = bool(foodlist)
    generatebuilding = bool(buildinglist)
    generateobject = generatevehicle + generateobject + generatefood + generatebuilding
    

    if(generatevehicle):
        objectwildcardlist.append("-vehicle-")
        hybridlist.append("-vehicle-")
        addontolocation.append(vehiclelist)
    
    if(generateobject):
        objectwildcardlist.append("-object-")
        hybridlist.append("-object-")

    if(generatefood):
        objectwildcardlist.append("-food-")
        hybridlist.append("-food-")

    if(generatebuilding):
        objectwildcardlist.append("-building-")
        hybridlist.append("-building-")
        addontolocation.append(buildinglist)
        addontolocationinside.append(buildinglist)
    
    if(generateobject):
        mainchooserlist.append("object")

    generatefictionalcharacter = bool(fictionallist)
    generatenonfictionalcharacter = bool(nonfictionallist)
    generatehumanoids = bool(humanoidlist)
    generatemanwoman = bool(manwomanlist)
    generatejob = bool(joblist)
    generatehumanoid = generatefictionalcharacter + generatenonfictionalcharacter + generatehumanoids + generatemanwoman + generatejob


    if(generatefictionalcharacter):
        humanoidsubjectchooserlist.append("fictional")
        hybridlist.append("-fictional-")
        hybridhumanlist.append("-fictional-")

    if(generatefictionalcharacter):
        humanoidsubjectchooserlist.append("non fictional")
        hybridlist.append("-nonfictional-")
        hybridhumanlist.append("-nonfictional-")
    
    if(generatehumanoids):
        humanoidsubjectchooserlist.append("humanoid")
        hybridlist.append("-humanoid-")
        hybridhumanlist.append("-humanoid-")
    
    if(generatemanwoman):
        humanoidsubjectchooserlist.append("human")

    if(generatejob):
        humanoidsubjectchooserlist.append("job")
   
    if(generatehumanoid):
        mainchooserlist.append("humanoid")
    
    
    generateanimal = bool(animallist)

    if(generateanimal):
        mainchooserlist.append("animal")
        hybridlist.append("-animal-")

    generatelandscape = bool(locationlist)

    if(generatelandscape):
        mainchooserlist.append("landscape")
        addontolocation.append(locationlist)
        addontolocationinside.append(locationlist)
    
    generateevent = bool(eventlist)
    generateconcepts = bool(conceptprefixlist) + bool(conceptsuffixlist)

    
    generateconcept = generateevent + generateconcepts

    if(generateevent):
        eventsubjectchooserlist.append("event")
    
    if(generateconcepts):
        eventsubjectchooserlist.append("concept")

    if(generateconcept):
        mainchooserlist.append("concept")

    # determine wether we should go for a template or not
    templatemode = False
    if(rare_dist(insanitylevel) or imagetype == "only templates"):
        templatemode = True


    # main stuff
    generatetype = not templatemode
    generatesubject = not templatemode

    # normals
    generateartist = bool(artistlist) and not templatemode
    generateoutfit = bool(outfitlist) and not templatemode
    generatebodytype = bool(bodytypelist) and not templatemode
    generateaccessorie = bool(accessorielist) and not templatemode
    generateartmovement = bool(artmovementlist) and not templatemode
    generatecamera = bool(cameralist) and not templatemode
    generatecolorscheme = bool(colorschemelist) and not templatemode
    generatedescriptors = bool(descriptorlist) and not templatemode
    generatedirection = bool(directionlist) and not templatemode
    generatefocus = bool(focuslist) and not templatemode
    generatehairstyle = bool(hairstylelist) and not templatemode
    generatelens = bool(lenslist) and not templatemode
    generatelighting = bool(lightinglist) and not templatemode
    generatemood = bool(moodlist) and not templatemode
    generatepose = bool(poselist) and not templatemode
    generatevomit = bool(vomitlist) and not templatemode
    generatequality = bool(qualitylist) and not templatemode
    generateshot = bool(shotsizelist) and not templatemode
    generatetimeperiod = bool(timeperiodlist) and not templatemode
    generateemoji = bool(emojilist) and not templatemode

    # specials:
    generatebackground = bool(backgroundtypelist) and not templatemode
    generateinsideshot = bool(insideshotlist) and not templatemode
    generatephotoaddition = bool(photoadditionlist) and not templatemode
    generatehairstyle = bool(buildhairlist) and not templatemode
    generateoutfit = bool(buildoutfitlist) and not templatemode
    generateobjectaddition = bool(objectadditionslist) and not templatemode
    generatehumanaddition = bool(humanadditionlist) and not templatemode
    generateanimaladdition = bool(animaladditionlist) and not templatemode
    generateaccessories = bool(buildaccessorielist) and not templatemode
    generategreatwork = bool(greatworklist) and not templatemode

    generateminilocationaddition = bool(minilocationadditionslist) and not templatemode


    # Smart subject logic
    if(givensubject != "" and smartsubject == True):
    
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
        keywordslist = ["location","background", "inside"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or foundinlist2 == True or keywordsinstring == True):
            generatebackground = False
            generateinsideshot = False

        # accessorielist
        foundinlist = any(word.lower() in [item.lower() for item in accessorielist] for word in givensubjectlist)
        if(foundinlist == True):
            generateaccessorie = False

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

        if(templatemode==True):
            templatelist = csv_to_list("templates", antilist,"./csvfiles/templates/",1,";",True)

            
            # templateenvironments = [templateenvironment[1] for templateenvironment in templatelist]
            # templateenvironmentsources = [templateenvironmentsource[2] for templateenvironmentsource in templatelist]
            # templatesubjecttypes = [templatesubjecttype[3] for templatesubjecttype in templatelist]

            targettemplateenvironment = "all"
            templateenvironmentsources = "all"

            # takes the prompt based on filters:
            # targettemplateenvironment: either civitai model or website
            # templateenvironmentsources: either
            templateprompts = [templateprompt[0] for templateprompt in templatelist if( (templateprompt[1] == targettemplateenvironment or targettemplateenvironment =="all") and (templateprompt[2] == templateenvironmentsources or templateenvironmentsources == "all") and (templateprompt[3] == forcesubject or forcesubject == "all") ) ]

            templatesubjects= [templateprompt[4] for templateprompt in templatelist if( (templateprompt[1] == targettemplateenvironment or targettemplateenvironment =="all") and (templateprompt[2] == templateenvironmentsources or templateenvironmentsources == "all") and (templateprompt[3] == forcesubject or forcesubject == "all") )]
            
            # choose the template
            chosentemplate = random.choice(templateprompts)
            templateindex = templateprompts.index(chosentemplate)


            # if there is a subject override, then replace the subject with that
            if(givensubject==""):
                completeprompt += chosentemplate.replace("-subject-",templatesubjects[templateindex] )
            else:
                completeprompt += chosentemplate.replace("-subject-",givensubject )


        # custom prefix list
        for i in range(2):
            if(uncommon_dist(insanitylevel) and generatecustominputprefix == True):
                completeprompt += random.choice(custominputprefixlist) + ", "



        if(insanitylevel==0):
            insanitylevel =  random.randint(1, 10)  # 10 = add everything, 1 is add almost nothing
        insanitylevel3 = int((insanitylevel/3) + 1.20)

        print("Setting insanity level to " + str(insanitylevel))

        # main chooser: 0 object, 1 animal, 2 humanoid, 3 landscape, 4 event/concept
        #mainchooserlist = ["object","animal","humanoid", "landscape", "concept"]
        mainchooser = random.choice(mainchooserlist)
        
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
            #humanoidsubjectchooserlist = ["human", "job", "fictional", "non fictional", "humanoid"]
            subjectchooser = random.choice(humanoidsubjectchooserlist)
        if(mainchooser == "landscape"):
            subjectchooser = "landscape"
        if(mainchooser == "concept"):
            #eventsubjectchooserlist = ["event", "concept"]
            subjectchooser = random.choice(eventsubjectchooserlist)


        #hybridlist = ["-animal-", "-object-", "-fictional-", "-nonfictional-", "-building-", "-vehicle-","-food-"]
        #hybridhumanlist = ["-fictional-", "-nonfictional-"]
        

        # start artist part

        artistsplacement = "front"
        if(uncommon_dist(insanitylevel) and onlyartists == False):
            artistsplacement = "back"

        if(artists != "none" and artistsplacement == "front" and generateartist == True):
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
                completeprompt += "] "


            if(onlyartists == True):
                    
                # clean it up
                completeprompt = cleanup(completeprompt)

                print("only generated these artists:" + completeprompt)
                return completeprompt


            completeprompt += ", "



            if artistmode in ["enhancing"]:
                completeprompt += " ["
        
        # start image type

        if(giventypeofimage=="" and generatetype == True):
            if(imagetype != "all" and imagetype != "all - force multiple" and imagetype != "only other types"):
                    completeprompt += " " + imagetype + ", "
            elif(imagetype == "all - force multiple" or unique_dist(insanitylevel)):
                amountofimagetypes = random.randint(2,3)
            elif(imagetype == "only other types"):
                othertype = 1
                completeprompt += random.choice(othertypelist)
            
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
            else:
                completeprompt += ", "
        elif(generatetype == True):
            othertype = 1
            completeprompt += giventypeofimage + " of a "


        
        ### here we can do some other stuff to spice things up
        if(unique_dist(insanitylevel) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "
        
        if(unique_dist(insanitylevel) and generateartmovement == True):
            generateartmovement = False
            completeprompt += " -artmovement-, "
        
        # start shot size

        if(mainchooser in ["object", "animal", "humanoid", "concept"] and othertype == 0 and "portrait" not in completeprompt and generateshot == True and uncommon_dist(insanitylevel)):
            completeprompt += random.choice(shotsizelist) + " of a "
        elif("portrait" in completeprompt and generateshot == True):
            completeprompt += " ,close up of a "
        elif(mainchooser in ["landscape"] and generateshot == True):
            completeprompt += " landscape of a "
        elif(generateshot == True): 
            completeprompt += ", "
    

        # start subject building
        if(generatesubject == True):
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
                # objectwildcardlist = ["-object-", "-building-","-vehicle-","-food-"]  # using wildcards for replacements
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == ""):

                    if rare_dist(insanitylevel):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["

                    chosenobjectwildcard = random.choice(objectwildcardlist)

                    completeprompt += chosenobjectwildcard + " "

                    if(hybridorswap == "hybrid"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += "|" + random.choice(hybridlist) + "] "
                        else:
                            completeprompt += "|" 
                            completeprompt += random.choice(chosenobjectwildcard) + " "
                            completeprompt += "] "
                    if(hybridorswap == "swap"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "] "
                        else:
                            completeprompt += ":"
                            completeprompt += chosenobjectwildcard + " "
                            completeprompt += ":" + str(random.randint(1,5)) +  "] "
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
                        
                    if(unique_dist(insanitylevel) and generateanimaladdition == True):
                        animaladdedsomething = 1
                        completeprompt += random.choice(animaladditionlist) + " -animal- "
                    if(animaladdedsomething != 1):
                        completeprompt += random.choice(animallist) + " "

                    if(hybridorswap == "hybrid"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += "|" + random.choice(hybridlist) + "] "
                        else:
                            completeprompt += "| -animal- ] "
                    if(hybridorswap == "swap"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "] "
                        else:
                            completeprompt += ":-animal-:" + str(random.randint(1,5)) +  "] "
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
                            completeprompt += "|" + random.choice(hybridhumanlist) + " ] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "non fictional"):
                        if rare_dist(insanitylevel):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["

                        completeprompt += random.choice(nonfictionallist) + " "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "humanoid"):
                        if rare_dist(insanitylevel):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += random.choice(humanoidlist) + " "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
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
                        completeprompt += "|" + "-location-"  + "] "
                    if(hybridorswap == "swap"):
                        completeprompt += ":" + "-location-" + ":" + str(random.randint(1,5)) +  "] "        
                else:
                    completeprompt += " " + givensubject + " " 
                
                hybridorswap = ""

                # shots from inside can create cool effects in landscapes
                if(unique_dist(insanitylevel)):
                    insideshot = 1
                    completeprompt += " from inside of a "
                    #addontolocationinside = [locationlist,buildinglist]
                    completeprompt += random.choice(random.choice(addontolocationinside)) + " "

                if(normal_dist(insanitylevel) and insideshot == 0):
                    completeprompt += " and "
                    if(rare_dist(insanitylevel)):
                        completeprompt += random.choice(descriptorlist) + " " 
                    if(rare_dist(insanitylevel)):
                        completeprompt += random.choice(culturelist) + " "

                    #addontolocation = [locationlist,buildinglist, vehiclelist]
                    completeprompt += random.choice(random.choice(addontolocation)) + " "


            if(mainchooser == "concept"):
                if(givensubject == ""):
                    if(subjectchooser == "event"):
                        completeprompt += " \"" + random.choice(eventlist) + "\" "
                    
                    if(subjectchooser == "concept"):
                        completeprompt += " \" The -conceptprefix- of -conceptsuffix- \" "
                else:
                    completeprompt += " " + givensubject + " " 

        # object additions
        for i in range(2):
            if(mainchooser == "object" and uncommon_dist(insanitylevel) and generateobjectaddition == True):
                completeprompt += ", " + random.choice(objectadditionslist) + ", "
        
        
        # riding an animal, holding an object or driving a vehicle, rare
        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and rare_dist(insanitylevel) and generatehumanaddition == True):
            humanspecial = 1
            completeprompt += random.choice(humanadditionlist) + " "
            
        completeprompt += ", "

        # SD understands emoji's. Can be used to manipulate facial expressions.
        # emoji, legendary
        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel) and generateemoji== True):
            completeprompt += random.choice(emojilist) + ", "
            

        # cosplaying
        #if(subjectchooser in ["animal as human", "non fictional", "humanoid"] and rare_dist(insanitylevel) and humanspecial != 1):
        #    completeprompt += "cosplaying as " + random.choice(fictionallist) + ", "

        # Job 
        # either go job or activity, not both

        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and humanspecial != 1 and generatesubject == True):
            joboractivitylist = [joblist,humanactivitylist]
            completeprompt += random.choice(random.choice(joboractivitylist)) + ", "


        # if(subjectchooser in ["animal as human","human","job", "fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        #    skintypelist = ["-color-", "-material-"]
        #    completeprompt += ", with " + random.choice(skintypelist) + " skin, "

        # custom mid list
        if(uncommon_dist(insanitylevel) and generatecustominputmid == True):
            completeprompt += random.choice(custominputmidlist) + ", "
            if(uncommon_dist(insanitylevel)):
                completeprompt += random.choice(custominputmidlist) + ", "
        
        
        # outfit builder
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generateoutfit == True):
            completeprompt += ", wearing " + random.choice(buildoutfitlist) + ", "
        
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid"]  and uncommon_dist(insanitylevel) and humanspecial != 1 and generatepose == True):
            completeprompt += random.choice(poselist) + ", "
        
        if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generatehairstyle == True):
            completeprompt += random.choice(buildhairlist) + ", "

        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid"]  and normal_dist(insanitylevel) and generateaccessorie == True and generateaccessories == True):
            completeprompt += random.choice(buildaccessorielist) + ", "

        if(legendary_dist(insanitylevel) and subjectchooser not in ["landscape", "concept"] and generateinsideshot == True):
            insideshot = 1
            completeprompt += random.choice(insideshotlist) + ", "
        
        if(subjectchooser not in ["landscape", "concept"] and humanspecial != 1 and insideshot == 0 and uncommon_dist(insanitylevel) and generatebackground == True):
            completeprompt += random.choice(backgroundtypelist) + ", "

        # minilocation bit
        if(subjectchooser in ["landscape"] and uncommon_dist(insanitylevel) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "
            
        if(rare_dist(insanitylevel) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "



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
        if("photo" in completeprompt.lower()):
            isphoto = 1
            
        if(common_dist(insanitylevel) and isphoto == 1 and generatephotoaddition == True):
            completeprompt += random.choice(photoadditionlist) + ", "
                
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
        if(novel_dist(insanitylevel) and generategreatwork == True):
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
            completeprompt += "::" + str(random.randint(1,17)) + "] "



        if(artists != "none" and artistsplacement == "back" and generateartist == True):
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
                completeprompt += "] "
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

    # first some manual stuff for outfit

    if(unique_dist(insanitylevel)): # sometimes, its just nice to have descriptor and a normal "outfit". We use mini outfits for this!
                 completeprompt = completeprompt.replace("-outfit-", "-minioutfit-",1)

            # do the hybrid/swap thing in here instead
            # if(rare_dist(insanitylevel)):
            #        hybridorswaplist = ["hybrid", "swap"]
            #        hybridorswap = random.choice(hybridorswaplist)
            #        hybridorswapreplacementvalue = "[" + random.choice(outfitlist)
            #        
            #        if(hybridorswap == "hybrid"):
            #                hybridorswapreplacementvalue += "|" + random.choice(outfitlist) + "] "
            #        if(hybridorswap == "swap"):
            #            if(uncommon_dist(insanitylevel)):
            #                hybridorswapreplacementvalue += ":" + random.choice(outfitlist) + ":" + str(random.randint(1,20)) +  "] "
            #        
            #        completeprompt = completeprompt.replace('-outfit-', hybridorswapreplacementvalue,1)
    
    # lol, this needs a rewrite :D
    while "-color-" in completeprompt or "-material-" in completeprompt or "-animal-" in completeprompt or "-object-" in completeprompt or "-fictional-" in completeprompt or "-nonfictional-" in completeprompt or "-conceptsuffix-" in completeprompt or "-building-" in completeprompt or "-vehicle-" in completeprompt or "-outfit-" in completeprompt or "-location-" in completeprompt or "-conceptprefix-" in completeprompt or "-descriptor-" in completeprompt or "-food-" in completeprompt or "-haircolor-" in completeprompt or "-hairstyle-" in completeprompt or "-job-" in completeprompt or "-culture-" in completeprompt or "-accessory-" in completeprompt or "-humanoid-" in completeprompt or "manwoman" in completeprompt or "-human-" in completeprompt or "-colorscheme-" in completeprompt or "-mood-" in completeprompt or "-genderdescription-" in completeprompt or "-artmovement-" in completeprompt or "-malefemale-" in completeprompt or "-objecttotal-" in completeprompt or "-bodytype-" in completeprompt or "-minilocation-" in completeprompt or "-minilocationaddition-" in completeprompt or "-pose-" in completeprompt or "-season-" in completeprompt or "-minioutfit-" in completeprompt:
        allwildcardslistnohybrid = [ "-color-","-object-", "-animal-", "-fictional-","-nonfictional-","-building-","-vehicle-","-location-","-conceptprefix-","-food-","-haircolor-","-hairstyle-","-job-", "-accessory-", "-humanoid-", "-manwoman-", "-human-", "-colorscheme-", "-mood-", "-genderdescription-", "-artmovement-", "-malefemale-", "-bodytype-", "-minilocation-", "-minilocationaddition-", "-pose-", "-season-", "-minioutfit-" ]
        allwildcardslistnohybridlists = [colorlist, objectlist, animallist, fictionallist, nonfictionallist, buildinglist, vehiclelist, locationlist,conceptprefixlist,foodlist,haircolorlist, hairstylelist,joblist, accessorielist, humanoidlist, manwomanlist, humanlist, colorschemelist, moodlist, genderdescriptionlist, artmovementlist, malefemalelist, bodytypelist, minilocationlist, minilocationadditionslist, poselist, seasonlist, minioutfitlist]
        allwildcardslistwithhybrid = ["-material-", "-descriptor-", "-outfit-", "-conceptsuffix-","-culture-", "-objecttotal-"]
        allwildcardslistwithhybridlists =[materiallist, descriptorlist,outfitlist,conceptsuffixlist,culturelist, objecttotallist]
        
        #  keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        for wildcard in allwildcardslistnohybrid:
            attachedlist = allwildcardslistnohybridlists[allwildcardslistnohybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,False)

        
        for wildcard in allwildcardslistwithhybrid:
            attachedlist = allwildcardslistwithhybridlists[allwildcardslistwithhybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,True)

      
    
    # clean it up
    completeprompt = cleanup(completeprompt)

    #just for me, some fun with posting fake dev messages (ala old sim games)
    if(random.randint(1, 50)==1):
        print("")
        print(random.choice(devmessagelist))
        print("")

    print(completeprompt)
    return completeprompt


    # function
def replacewildcard(completeprompt, insanitylevel, wildcard,listname, activatehybridorswap):
    if(len(listname) == 0):
        # handling empty lists
        completeprompt = completeprompt.replace(wildcard, "",1)
    else:

        while wildcard in completeprompt:
            if(unique_dist(insanitylevel) and activatehybridorswap == True):
                hybridorswaplist = ["hybrid", "swap"]
                hybridorswap = random.choice(hybridorswaplist)
                hybridorswapreplacementvalue = "[" + random.choice(listname)
                
                if(hybridorswap == "hybrid"):
                        hybridorswapreplacementvalue += "|" + random.choice(listname) + "] "
                if(hybridorswap == "swap"):
                        hybridorswapreplacementvalue += ":" + random.choice(listname) + ":" + str(random.randint(1,20)) +  "] "
                
                completeprompt = completeprompt.replace(wildcard, hybridorswapreplacementvalue,1)

            completeprompt = completeprompt.replace(wildcard, random.choice(listname),1)

    return completeprompt

def cleanup(completeprompt):
    # all cleanup steps moved here
    completeprompt = re.sub('\[ ', '[', completeprompt)
    completeprompt = re.sub('\[,', '[', completeprompt) 
    completeprompt = re.sub(' \]', ']', completeprompt)
    completeprompt = re.sub(' \|', '|', completeprompt)
    completeprompt = re.sub(' \"', '\"', completeprompt)
    completeprompt = re.sub('\" ', '\"', completeprompt)
    completeprompt = re.sub('\( ', '(', completeprompt)
    completeprompt = re.sub(' \(', '(', completeprompt)
    completeprompt = re.sub('\) ', ')', completeprompt)
    completeprompt = re.sub(' \)', ')', completeprompt)

    completeprompt = re.sub(' :', ':', completeprompt)
    completeprompt = re.sub(',::', '::', completeprompt)

    completeprompt = re.sub(',,', ', ', completeprompt)
    completeprompt = re.sub(',,,', ', ', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(' , ', ', ', completeprompt)
    completeprompt = re.sub(',\(', ', (', completeprompt)

    completeprompt = re.sub('  ', ' ', completeprompt)
    completeprompt = re.sub('a The', 'The', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(',,', ',', completeprompt)

    completeprompt = re.sub(', of a', ' of a', completeprompt)
    completeprompt = re.sub('of a,', 'of a', completeprompt)
    completeprompt = re.sub('of a of a', 'of a', completeprompt)


    completeprompt = completeprompt.strip(", ")

    return completeprompt