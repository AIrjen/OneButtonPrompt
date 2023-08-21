import random
import re
from csv_reader import *
from random_functions import *




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all", onlyartists = False, antivalues = "", prefixprompt = "", suffixprompt ="",promptcompounderlevel ="1", seperator = "comma", givensubject="",smartsubject = True,giventypeofimage="", imagemodechance = 20, gender = "all", subtypeobject="all", subtypehumanoid="all", subtypeconcept="all", advancedprompting=True, hardturnoffemojis=False):

    
    # load the config file
    config = load_config_csv()

    
    
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
    fictionallist = csv_to_list(csvfilename="fictional characters",antilist=antilist,skipheader=True,gender=gender)
    nonfictionallist = csv_to_list(csvfilename="nonfictional characters",antilist=antilist,skipheader=True,gender=gender)
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
    malefemalelist = csv_to_list(csvfilename="malefemale",antilist=antilist,skipheader=True,gender=gender)
    manwomanlist = csv_to_list(csvfilename="manwoman",antilist=antilist,skipheader=True,gender=gender)
    moodlist = csv_to_list("moods",antilist)
    othertypelist = csv_to_list("othertypes",antilist)
    poselist = csv_to_list("poses",antilist)
    qualitylist = csv_to_list("quality",antilist)
    shotsizelist = csv_to_list("shotsizes",antilist)
    timeperiodlist = csv_to_list("timeperiods",antilist)
    vomitlist = csv_to_list("vomit",antilist)
    foodlist = csv_to_list("foods", antilist)
    genderdescriptionlist = csv_to_list(csvfilename="genderdescription",antilist=antilist,skipheader=True,gender=gender)
    minilocationlist = csv_to_list("minilocations", antilist)
    minioutfitlist = csv_to_list("minioutfits", antilist)
    seasonlist = csv_to_list("seasons", antilist)
    elaborateoutfitlist = csv_to_list("elaborateoutfits", antilist)
    minivomitlist = csv_to_list("minivomit", antilist)
    imagetypequalitylist = csv_to_list("imagetypequality", antilist)
    rpgclasslist = csv_to_list("rpgclasses", antilist)
    brandlist = csv_to_list("brands", antilist)
    spacelist = csv_to_list("space", antilist)
    poemlinelist = csv_to_list("poemlines", antilist)
    songlinelist = csv_to_list("songlines", antilist)
    musicgenrelist = csv_to_list("musicgenres", antilist)
    manwomanrelationlist = csv_to_list(csvfilename="manwomanrelations",antilist=antilist,skipheader=True,gender=gender)
    waterlocationlist = csv_to_list("waterlocations", antilist)
    containerlist = csv_to_list("containers", antilist)
    firstnamelist = csv_to_list(csvfilename="firstnames",antilist=antilist,skipheader=True,gender=gender)
    floralist = csv_to_list("flora", antilist)
    printlist = csv_to_list("prints", antilist)
    patternlist = csv_to_list("patterns", antilist)
    chairlist = csv_to_list("chairs", antilist)

    humanlist = fictionallist + nonfictionallist + humanoidlist
    objecttotallist = objectlist + buildinglist + vehiclelist + foodlist + spacelist + floralist + containerlist
    outfitprinttotallist = objecttotallist + locationlist + colorlist + musicgenrelist + seasonlist + animallist + patternlist

    # build artists list
    artistlist = []
    # create artist list to use in the code, maybe based on category  or personal lists
    if(artists != "all" and artists != "none" and artists.startswith("personal_artists") == False and artists.startswith("personal artists") == False):
        artistlist = artist_category_csv_to_list("artists_and_category",artists)
    elif(artists.startswith("personal_artists") == True or artists.startswith("personal artists") == True):
        artists = artists.replace(" ","_",-1) # add underscores back in
        artistlist = csv_to_list(artists,antilist,"./userfiles/")
    elif(artists != "none"):
        artistlist = csv_to_list("artists",antilist)

    # create special artists lists, used in templates
    fantasyartistlist = artist_category_csv_to_list("artists_and_category","fantasy")
    popularartistlist = artist_category_csv_to_list("artists_and_category","popular")
    romanticismartistlist = artist_category_csv_to_list("artists_and_category","romanticism")
    photographyartistlist = artist_category_csv_to_list("artists_and_category","photography")


    # add any other custom lists
    stylestiloralist = csv_to_list("styles_ti_lora",antilist,"./userfiles/")
    generatestyle = bool(stylestiloralist) # True of not empty

    custominputprefixlist = csv_to_list("custom_input_prefix",antilist,"./userfiles/")
    generatecustominputprefix = bool(custominputprefixlist) # True of not empty

    custominputmidlist = csv_to_list("custom_input_mid",antilist,"./userfiles/")
    generatecustominputmid = bool(custominputmidlist) # True of not empty

    custominputsuffixlist = csv_to_list("custom_input_suffix",antilist,"./userfiles/")
    generatecustominputsuffix = bool(custominputsuffixlist) # True of not empty

    customsubjectslist = csv_to_list("custom_subjects",antilist,"./userfiles/")

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
    overalladditionlist = csv_to_list("overalladditions", antilist,"./csvfiles/special_lists/")
    imagetypemodelist = csv_to_list("imagetypemodes", antilist,"./csvfiles/special_lists/")
    miniactivitylist = csv_to_list("miniactivity", antilist,"./csvfiles/special_lists/")
    animalsuffixadditionlist = csv_to_list("animalsuffixadditions", antilist,"./csvfiles/special_lists/")
    
    styleslist = csv_to_list("styles", antilist,"./csvfiles/templates/")


    
    # subjects
    mainchooserlist = []
    objectwildcardlist = []
    hybridlist = []
    hybridhumanlist = []
    humanoidsubjectchooserlist = []
    eventsubjectchooserlist = []
    addontolocationinsidelist = []
    addontolocationlist = []

    # load subjects stuff from config
    generatevehicle = True
    generateobject = True
    generatefood = True
    generatebuilding = True
    generatespace = True
    generateflora = True
    generateanimal = True
    generatemanwoman = True
    generatemanwomanrelation = True
    generatefictionalcharacter = True
    generatenonfictionalcharacter = True
    generatehumanoids = True
    generatejob = True
    generatefirstnames = True
    generatelandscape = True
    generateevent = True
    generateconcepts = True
    generatepoemline = True
    generatesongline = True

    custominputprefixrepeats = 2
    custominputprefixchance = 'uncommon'

    imagetypechance = 'normal'
    generateimagetype = True
    imagetypequalitychance = 'rare'
    generateimagetypequality = True
    generateminilocationaddition = True
    minilocationadditionchance = 'unique'
    artmovementprefixchance = 'unique'
    minivomitprefix1chance = 'rare'
    minivomitprefix2chance = 'unique'
    shotsizechance = 'uncommon'

    subjectdescriptor1chance = 'common'
    subjectdescriptor2chance = 'uncommon'
    subjectbodytypechance = 'normal'
    subjectculturechance = 'normal'
    subjectconceptsuffixchance = 'unique'

    subjectlandscapeinsideshotchance = 'unique'
    subjectlandscapeaddonlocationchance = 'normal'
    subjectlandscapeaddonlocationdescriptorchance = 'rare'
    subjectlandscapeaddonlocationculturechance = 'rare'

    objectadditionsrepeats = 2
    objectadditionschance = 'uncommon'
    humanadditionchance = 'rare'
    overalladditionchance = 'extraordinary'

    emojichance = 'legendary'
    joboractivitychance = 'normal'

    custominputmidrepeats = 2
    custominputmidchance = 'uncommon'
    minivomitmidchance = 'unique'

    outfitchance = 'normal'
    posechance = 'uncommon'
    hairchance = 'normal'
    accessorychance = 'normal'
    humanoidinsideshotchance = 'legendary'
    humanoidbackgroundchance = 'uncommon'

    landscapeminilocationchance = 'uncommon'
    generalminilocationchance = 'rare'

    timperiodchance = 'normal'
    focuschance = 'normal'
    directionchance = 'normal'
    moodchance = 'normal'
    minivomitsuffixchance = 'unique'
    artmovementchance = 'normal'
    lightingchance = 'normal'
    photoadditionchance = 'common'
    lenschance = 'normal'
    colorschemechance = 'normal'
    vomit1chance = 'uncommon'
    vomit2chance= 'uncommon'
    greatworkchance = 'novel'
    poemlinechance = 'novel'
    songlinechance = 'novel'
    quality1chance = 'uncommon'
    quality2chance = 'uncommon'

    customstyle1chance = 'uncommon'
    customstyle2chance = 'uncommon'

    custominputsuffixrepeats = 2
    custominputsuffixchance = 'uncommon'

    artistsatbackchance = 'uncommon'

    for item in config:
        # objects
        if item[0] == 'subject_vehicle' and item[1] != 'on':
            generatevehicle = False
        if item[0] == 'subject_object' and item[1] != 'on':
            generateobject = False
        if item[0] == 'subject_food' and item[1] != 'on':
            generatefood = False
        if item[0] == 'subject_building' and item[1] != 'on':
            generatebuilding = False
        if item[0] == 'subject_space' and item[1] != 'on':
            generatespace = False
        if item[0] == 'subject_flora' and item[1] != 'on':
            generateflora = False
        # animals
        if item[0] == 'subject_animal' and item[1] != 'on':
            generateanimal = False
        # humanoids
        if item[0] == 'subject_manwoman' and item[1] != 'on':
            generatemanwoman = False
        if item[0] == 'subject_manwomanrelation' and item[1] != 'on':
            generatemanwomanrelation = False
        if item[0] == 'subject_fictional' and item[1] != 'on':
            generatefictionalcharacter = False
        if item[0] == 'subject_nonfictional' and item[1] != 'on':
            generatenonfictionalcharacter = False
        if item[0] == 'subject_humanoid' and item[1] != 'on':
            generatehumanoids = False
        if item[0] == 'subject_job' and item[1] != 'on':
            generatejob = False
        if item[0] == 'subject_firstnames' and item[1] != 'on':
            generatefirstnames = False
        # landscape
        if item[0] == 'subject_landscape' and item[1] != 'on':
            generatelandscape = False
        # concept
        if item[0] == 'subject_event' and item[1] != 'on':
            generateevent = False
        if item[0] == 'subject_concept' and item[1] != 'on':
            generateconcepts = False
        if item[0] == 'poemline' and item[1] != 'on':
            generatepoemline = False
        if item[0] == 'songline' and item[1] != 'on':
            generatesongline = False
        
        # main list stuff
        if item[0] == 'custominputprefixrepeats':
            custominputprefixrepeats = int(item[1])
        if item[0] == 'custominputprefixchance':
            custominputprefixchance = item[1]
            if(custominputprefixchance == 'never'):
                generatecustominputprefix = False
        if item[0] == 'imagetypechance':
            imagetypechance = item[1]
            if(imagetypechance == 'never'):
                generateimagetype = False
        if item[0] == 'imagetypequalitychance':
            imagetypequalitychance = item[1]
            if(imagetypequalitychance == 'never'):
                generateimagetypequality = False
        if item[0] == 'minilocationadditionchance':
            minilocationadditionchance = item[1]
        if item[0] == 'artmovementprefixchance':
            artmovementprefixchance = item[1]
        if item[0] == 'minivomitprefix1chance':
            minivomitprefix1chance = item[1]
        if item[0] == 'minivomitprefix2chance':
            minivomitprefix2chance = item[1]
        
        if item[0] == 'shotsizechance':
            shotsizechance = item[1]

        if item[0] == 'subjectdescriptor1chance':
            subjectdescriptor1chance = item[1]
        if item[0] == 'subjectdescriptor2chance':
            subjectdescriptor2chance = item[1]
        if item[0] == 'subjectbodytypechance':
            subjectbodytypechance = item[1]
        if item[0] == 'subjectculturechance':
            subjectculturechance = item[1]
        if item[0] == 'subjectconceptsuffixchance':
            subjectconceptsuffixchance = item[1]

        if item[0] == 'subjectlandscapeinsideshotchance':
            subjectlandscapeinsideshotchance = item[1]
        if item[0] == 'subjectlandscapeaddonlocationchance':
            subjectlandscapeaddonlocationchance = item[1]
        if item[0] == 'subjectlandscapeaddonlocationdescriptorchance':
            subjectlandscapeaddonlocationdescriptorchance = item[1]
        if item[0] == 'subjectlandscapeaddonlocationculturechance':
            subjectlandscapeaddonlocationculturechance = item[1]

        if item[0] == 'objectadditionsrepeats':
            objectadditionsrepeats = int(item[1])
        if item[0] == 'objectadditionschance':
            objectadditionschance = item[1]
        if item[0] == 'humanadditionchance':
            humanadditionchance = item[1]
        if item[0] == 'overalladditionchance':
            overalladditionchance = item[1]

        if item[0] == 'emojichance':
            emojichance = item[1]
            if(hardturnoffemojis==True):
                emojichance='never'
        if item[0] == 'joboractivitychance':
            joboractivitychance = item[1]

        if item[0] == 'custominputmidrepeats':
            custominputmidrepeats = int(item[1])
        if item[0] == 'custominputmidchance':
            custominputmidchance = item[1]
        if item[0] == 'minivomitmidchance':
            minivomitmidchance = item[1]
        
        if item[0] == 'outfitchance':
            outfitchance = item[1]
        if item[0] == 'posechance':
            posechance = item[1]
        if item[0] == 'hairchance':
            hairchance = item[1]
        if item[0] == 'accessorychance':
            accessorychance = item[1]
        if item[0] == 'humanoidinsideshotchance':
            humanoidinsideshotchance = item[1]
        if item[0] == 'humanoidbackgroundchance':
            humanoidbackgroundchance = item[1]

        if item[0] == 'landscapeminilocationchance':
            landscapeminilocationchance = item[1]
        if item[0] == 'generalminilocationchance':
            generalminilocationchance = item[1]

        if item[0] == 'timperiodchance':
            timperiodchance = item[1]
        if item[0] == 'focuschance':
            focuschance = item[1]
        if item[0] == 'directionchance':
            directionchance = item[1]
        if item[0] == 'moodchance':
            moodchance = item[1]
        if item[0] == 'minivomitsuffixchance':
            minivomitsuffixchance = item[1]
        if item[0] == 'artmovementchance':
            artmovementchance = item[1]
        if item[0] == 'lightingchance':
            lightingchance = item[1]
        if item[0] == 'photoadditionchance':
            photoadditionchance = item[1]
        if item[0] == 'lenschance':
            lenschance = item[1]
        if item[0] == 'colorschemechance':
            colorschemechance = item[1]
        if item[0] == 'vomit1chance':
            vomit1chance = item[1]
        if item[0] == 'vomit2chance':
            vomit2chance = item[1]
        if item[0] == 'greatworkchance':
            greatworkchance = item[1]
        if item[0] == 'poemlinechance':
            poemlinechance = item[1]
        if item[0] == 'songlinechance':
            songlinechance = item[1]
        if item[0] == 'quality1chance':
            quality1chance = item[1]
        if item[0] == 'quality2chance':
            quality2chance = item[1]

        if item[0] == 'customstyle1chance':
            customstyle1chance = item[1]
        if item[0] == 'customstyle2chance':
            customstyle2chance = item[1]
        
        if item[0] == 'custominputsuffixrepeats':
            custominputsuffixrepeats = int(item[1])
        if item[0] == 'custominputsuffixchance':
            custominputsuffixchance = item[1]

        if item[0] == 'artistsatbackchance':
            artistsatbackchance = item[1]


    generatevehicle = bool(vehiclelist) and generatevehicle
    generateobject = bool(objectlist) and generateobject
    generatefood = bool(foodlist) and generatefood
    generatebuilding = bool(buildinglist) and generatebuilding
    generatespace = bool(spacelist) and generatespace
    generateflora = bool(floralist) and generateflora
    generateobject = generatevehicle or generateobject or generatefood or generatebuilding or generatespace or generateflora
    

    if(generatevehicle):
        objectwildcardlist.append("-vehicle-")
        hybridlist.append("-vehicle-")
        addontolocationlist.append("-vehicle-")
    
    if(generateobject):
        objectwildcardlist.append("-object-")
        hybridlist.append("-object-")

    if(generatefood):
        objectwildcardlist.append("-food-")
        hybridlist.append("-food-")
    
    if(generatespace):
        objectwildcardlist.append("-space-")
        hybridlist.append("-space-")
        addontolocationlist.append("-space-")

    if(generatebuilding):
        objectwildcardlist.append("-building-")
        hybridlist.append("-building-")
        addontolocationlist.append("-building-")
        addontolocationinsidelist.append("-building-")
    
    if(generateflora):
        objectwildcardlist.append("-flora-")
        hybridlist.append("-flora-")
        addontolocationlist.append("-flora-")
    
    if(generateobject):
        mainchooserlist.append("object")

    generatefictionalcharacter = bool(fictionallist) and generatefictionalcharacter
    generatenonfictionalcharacter = bool(nonfictionallist) and generatenonfictionalcharacter
    generatehumanoids = bool(humanoidlist) and generatehumanoids
    generatemanwoman = bool(manwomanlist) and generatemanwoman
    generatemanwomanrelation = bool(manwomanrelationlist) and generatemanwomanrelation
    generatejob = bool(joblist) and generatejob
    generatefirstnames = bool(firstnamelist) and generatefirstnames
    generatehumanoid = generatefictionalcharacter or generatenonfictionalcharacter or generatehumanoids or generatemanwoman or generatejob or generatemanwomanrelation or generatefirstnames


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

    if(generatemanwomanrelation):
        humanoidsubjectchooserlist.append("manwomanrelation")

    if(generatejob):
        humanoidsubjectchooserlist.append("job")
   
    if(generatehumanoid):
        mainchooserlist.append("humanoid")

    if(generatefirstnames):
        humanoidsubjectchooserlist.append("firstname")
    
    
    generateanimal = bool(animallist) and generateanimal

    if(generateanimal):
        mainchooserlist.append("animal")
        hybridlist.append("-animal-")

    generatelandscape = bool(locationlist) and generatelandscape

    if(generatelandscape):
        mainchooserlist.append("landscape")
        addontolocationlist.append("-location-")
        addontolocationinsidelist.append("-location-")
    
    generateevent = bool(eventlist) and generateevent
    generateconcepts = bool(conceptprefixlist) and bool(conceptsuffixlist) and generateconcepts
    generatepoemline = bool(poemlinelist) and generatepoemline 
    generatesongline = bool(songlinelist) and generatesongline
    


    generateconcept = generateevent or generateconcepts or generatepoemline or generatesongline

    if(generateevent):
        eventsubjectchooserlist.append("event")
    
    if(generateconcepts):
        eventsubjectchooserlist.append("concept")

    if(generatepoemline):
        eventsubjectchooserlist.append("poemline")
    
    if(generatesongline):
        eventsubjectchooserlist.append("songline")

    if(generateconcept):
        mainchooserlist.append("concept")

    # determine wether we have a special mode or not
    if(random.randint(1,int(imagemodechance)) == 1 and imagetype == "all" and giventypeofimage == ""):
        imagetype = random.choice(imagetypemodelist)  # override imagetype with a random "mode" value


    specialmode = False
    templatemode = False
    artblastermode = False
    qualityvomitmode = False
    uniqueartmode = False
    colorcannonmode = False
    photofantasymode = False
    massivemadnessmode = False
    onlysubjectmode = False
    stylesmode = False

    # determine wether we should go for a template or not. Not hooked up to insanitylevel
    if(imagetype == "only templates mode"):
        specialmode = True
        templatemode = True
        print("Running with a randomized template instead of a randomized prompt")

    if(imagetype == "art blaster mode"):
        specialmode = True
        artblastermode = True
        print("Running in art blaster mode")

    if(imagetype == "unique art mode"):
        specialmode = True
        uniqueartmode = True
        print("Running in unique art mode")

    if(imagetype == "quality vomit mode"):
        specialmode = True
        qualityvomitmode = True
        print("Running in quality vomit mode")

    if(imagetype == "color cannon mode"):
        specialmode = True
        colorcannonmode = True
        print("Running in color cannon mode")

    if(imagetype == "photo fantasy mode"):
        specialmode = True
        photofantasymode = True
        print("Running in photo fantasy mode")

    if(imagetype == "massive madness mode"):
        specialmode = True
        massivemadnessmode = True
        print("Running in massive madness mode")
        print("Are you ready for this?")

    if(imagetype == "subject only mode"):
        specialmode = True
        onlysubjectmode = True
        print("Running in only subject mode")

    if(imagetype == "fixed styles mode"):
        specialmode = True
        stylesmode = True
        print("Running with a randomized style instead of a randomized prompt")


    # main stuff
    generatetype = not specialmode
    generatesubject = not templatemode

    # normals
    generateartist = bool(artistlist) and not specialmode
    generateoutfit = bool(outfitlist) and not templatemode
    generatebodytype = bool(bodytypelist) and not templatemode
    generateaccessorie = bool(accessorielist) and not specialmode
    generateartmovement = bool(artmovementlist) and not specialmode
    generatecamera = bool(cameralist) and not specialmode
    generatecolorscheme = bool(colorschemelist) and not specialmode
    generatedescriptors = bool(descriptorlist) and not templatemode
    generatedirection = bool(directionlist) and not specialmode
    generatefocus = bool(focuslist) and not specialmode
    generatehairstyle = bool(hairstylelist) and not templatemode
    generatelens = bool(lenslist) and not specialmode
    generatelighting = bool(lightinglist) and not specialmode
    generatemood = bool(moodlist) and not specialmode
    generatepose = bool(poselist) and not templatemode
    generatevomit = bool(vomitlist) and not specialmode
    generatequality = bool(qualitylist) and not specialmode
    generateshot = bool(shotsizelist) and not specialmode
    generatetimeperiod = bool(timeperiodlist) and not specialmode
    generateemoji = bool(emojilist) and not templatemode

    # specials:
    generatebackground = bool(backgroundtypelist) and not specialmode
    generateinsideshot = bool(insideshotlist) and not specialmode
    generatephotoaddition = bool(photoadditionlist) and not specialmode
    generatehairstyle = bool(buildhairlist) and not templatemode
    generateoutfit = bool(buildoutfitlist) and not templatemode
    generateobjectaddition = bool(objectadditionslist) and not templatemode
    generatehumanaddition = bool(humanadditionlist) and not templatemode
    generateanimaladdition = bool(animaladditionlist) and not templatemode
    generateaccessories = bool(buildaccessorielist) and not templatemode
    generategreatwork = bool(greatworklist) and not specialmode
    generatepoemline = bool(poemlinelist) and not specialmode
    generatesongline = bool(songlinelist) and not specialmode
    
    generateminilocationaddition = bool(minilocationadditionslist) and not specialmode
    generateminivomit = bool(minivomitlist) and not specialmode
    generateimagetypequality = bool(imagetypequalitylist) and not specialmode and generateimagetypequality
    generateoveralladdition = bool(overalladditionlist) and not specialmode
    generateimagetype = bool(imagetypelist) and not specialmode and generateimagetype


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
            templatepromptcreator = [templateprompt[1] for templateprompt in templatelist if( (templateprompt[1] == targettemplateenvironment or targettemplateenvironment =="all") and (templateprompt[2] == templateenvironmentsources or templateenvironmentsources == "all") and (templateprompt[3] == forcesubject or forcesubject == "all") ) ]
            templatesubjects= [templateprompt[4] for templateprompt in templatelist if( (templateprompt[1] == targettemplateenvironment or targettemplateenvironment =="all") and (templateprompt[2] == templateenvironmentsources or templateenvironmentsources == "all") and (templateprompt[3] == forcesubject or forcesubject == "all") )]
            
            # choose the template
            chosentemplate = random.choice(templateprompts)
            templateindex = templateprompts.index(chosentemplate)

            print("Processing a prompt that was inspired from: " + templatepromptcreator[templateindex])

            # if there is a subject override, then replace the subject with that
            if(givensubject==""):
                completeprompt += chosentemplate.replace("-subject-",templatesubjects[templateindex] )
            else:
                completeprompt += chosentemplate.replace("-subject-",givensubject )


        # custom prefix list
        for i in range(custominputprefixrepeats):
            if(chance_roll(insanitylevel, custominputprefixchance) and generatecustominputprefix == True):
                completeprompt += random.choice(custominputprefixlist) + ", "



        if(insanitylevel==0):
            insanitylevel =  random.randint(1, 10)  # 10 = add everything, 1 is add almost nothing
        insanitylevel3 = int((insanitylevel/3) + 1.20)

        # print("Setting insanity level to " + str(insanitylevel))

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
            #humanoidsubjectchooserlist = ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]
            subjectchooser = random.choice(humanoidsubjectchooserlist)
            if(subtypehumanoid != "all"):
                if(subtypehumanoid == "generic humans"):
                    subjectchooser = "human"
                if(subtypehumanoid == "generic human relations"):
                    subjectchooser = "manwomanrelation"
                if(subtypehumanoid == "celebrities e.a."):
                    subjectchooser = "non fictional"
                if(subtypehumanoid == "fictional characters"):
                    subjectchooser = "fictional"
                if(subtypehumanoid == "humanoids"):
                    subjectchooser = "humanoid"
                if(subtypehumanoid == "based on job or title"):
                    subjectchooser = "job"
                if(subtypehumanoid == "based on first name"):
                    subjectchooser = "firstname"
        if(mainchooser == "landscape"):
            subjectchooser = "landscape"
        if(mainchooser == "concept"):
            #eventsubjectchooserlist = ["event", "concept", "poemline", "songline"]
            subjectchooser = random.choice(eventsubjectchooserlist)
            if(subtypeconcept != "all"):
                if(subtypeconcept == "event"):
                    subjectchooser = "event"
                if(subtypeconcept == "the X of Y concepts"):
                    subjectchooser = "concept"
                if(subtypeconcept == "lines from poems"):
                    subjectchooser = "poemline"
                if(subtypeconcept == "lines from songs"):
                    subjectchooser = "songline"


        
        # special modes        

        # start art blaster here
        if(artblastermode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artist-, "
                if(uncommon_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(unique_dist(insanitylevel) and bool(imagetypelist)):
                    completeprompt += "-imagetype-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1 

        # start unique art here
        if(uniqueartmode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(othertypelist)):
                    completeprompt += "-othertype-, "
                if(uncommon_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(uncommon_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(rare_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(unique_dist(insanitylevel) and bool(imagetypelist)):
                    completeprompt += "-imagetype-, "
                if(unique_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                
                step = step + 1 

        # start quality vomit here
        if(qualityvomitmode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(uncommon_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                if(unique_dist(insanitylevel) and bool(minivomitlist)):
                    completeprompt += "-minivomit-, "
                if(unique_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1

        # start mood color here
        if(colorcannonmode == True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(uncommon_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(unique_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                step = step + 1 

        # start photo fantasy here
        if(photofantasymode == True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            if(common_dist(insanitylevel)):
                if(uncommon_dist(insanitylevel)):
                    completeprompt += "-imagetypequality- "
                completeprompt += " photograph, "
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(uncommon_dist(insanitylevel) and bool(cameralist)):
                    completeprompt += "-camera-, "
                if(rare_dist(insanitylevel) and bool(lenslist)):
                    completeprompt += "-lens-, "
                if(unique_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1 

        # start massive madness here
        if(massivemadnessmode == True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(rare_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artist-, "
                if(rare_dist(insanitylevel) and bool(descriptorlist)):
                    completeprompt += "-descriptor-, "
                if(rare_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(rare_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(rare_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(rare_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(rare_dist(insanitylevel) and bool(minilocationadditionslist)):
                    completeprompt += "-minilocationaddition-, "
                if(rare_dist(insanitylevel) and bool(materiallist)):
                    completeprompt += "-material-, "
                if(rare_dist(insanitylevel) and bool(conceptsuffixlist)):
                    completeprompt += "-conceptsuffix-, "
                if(rare_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                if(rare_dist(insanitylevel) and bool(cameralist)):
                    completeprompt += "-camera-, "
                if(rare_dist(insanitylevel) and bool(lenslist)):
                    completeprompt += "-lens-, "
                if(rare_dist(insanitylevel) and bool(imagetypelist)):
                    completeprompt += "-imagetype-, "
                step = step + 1 
            completeprompt += " ("


         # start styles mode here
        if(stylesmode == True):
            chosenstyle = random.choice(styleslist)
            chosenstyleprefix = chosenstyle.split("-subject-")[0]
            chosenstylesuffix= chosenstyle.split("-subject-")[1]
            completeprompt += chosenstyleprefix



        # start artist part

        artistsplacement = "front"
        if(chance_roll(insanitylevel, artistsatbackchance) and onlyartists == False):
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
                if(advancedprompting == False):
                    artistmode = "normal"
                if (artistmode in ["hybrid","switching"] and end - step == 1):
                    artistmode = "normal"
            
            if(onlyartists == True and artistmode == "enhancing"):
                artistmode = "normal"
            # if there are not enough artists in the list, then just go normal
            if(len(artistlist) < 3):
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
                completeprompt += "-artist-"
                
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

                # replace artist wildcards
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-artist-", artistlist, False, False)
                    
                # clean it up
                completeprompt = cleanup(completeprompt, advancedprompting)

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
            
            if(imagetype == "all" and chance_roll(insanitylevel, imagetypechance) and amountofimagetypes <= 1):
                amountofimagetypes = 1
            
            

            for i in range(amountofimagetypes):
            # one in 6 images is a complex/other type
                if(chance_roll(insanitylevel, imagetypequalitychance) and generateimagetypequality):
                    completeprompt += "-imagetypequality- "
                if(random.randint(0,5) < 5):
                    completeprompt += " -imagetype-, "
                else:
                    othertype = 1
                    completeprompt += " -othertype-, "
            
            if(othertype==1):
                completeprompt += " of a "
            else:
                completeprompt += ", "
        elif(generatetype == True):
            othertype = 1
            completeprompt += giventypeofimage + " of a "


        
        ### here we can do some other stuff to spice things up
        if(chance_roll(insanitylevel, minilocationadditionchance) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "
        
        if(chance_roll(insanitylevel, artmovementprefixchance) and generateartmovement == True):
            generateartmovement = False
            completeprompt += " -artmovement-, "
        
        if(chance_roll(insanitylevel, minivomitprefix1chance) and generateminivomit == True):
            completeprompt += " -minivomit-, "
        
        if(chance_roll(insanitylevel, minivomitprefix2chance) and generateminivomit == True):
            completeprompt += " -minivomit-, "

        # start shot size

        if(mainchooser in ["object", "animal", "humanoid", "concept"] and othertype == 0 and "portrait" not in completeprompt and generateshot == True and chance_roll(insanitylevel,shotsizechance)):
            completeprompt += "-shotsize- of a "
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
            if(chance_roll(insanitylevel, subjectdescriptor1chance) and generatedescriptors == True):
                completeprompt += "-descriptor- "

            if(chance_roll(insanitylevel, subjectdescriptor2chance) and generatedescriptors == True):
                completeprompt += "-descriptor- "

            if(subjectchooser in ["animal as human,","human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","firstname"] and chance_roll(insanitylevel, subjectbodytypechance) and generatebodytype == True):
                completeprompt += "-bodytype- "

            if(subjectchooser in ["object","animal as human,","human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","firstname"] and chance_roll(insanitylevel, subjectculturechance) and generatedescriptors == True):
                completeprompt += "-culture- "

            if(mainchooser == "object"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                # if we have an overwrite, then make sure we only take the override
                if(subtypeobject != "all"):
                    if(subtypeobject == "generic objects"):
                        objectwildcardlist = ["-object-"]
                    if(subtypeobject == "vehicles"):
                        objectwildcardlist = ["-vehicle-"]
                    if(subtypeobject == "food"):
                        objectwildcardlist = ["-food-"]
                    if(subtypeobject == "buildings"):
                        objectwildcardlist = ["-building-"]
                    if(subtypeobject == "space"):
                        objectwildcardlist = ["-space-"]
                    if(subtypeobject == "flora"):
                        objectwildcardlist = ["-flora-"]
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == ""):

                    if(rare_dist(insanitylevel) and advancedprompting == True):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["

                    chosenobjectwildcard = random.choice(objectwildcardlist)

                    completeprompt += chosenobjectwildcard + " "

                    if(hybridorswap == "hybrid"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += "|" + random.choice(objectwildcardlist) + "] "
                        else:
                            completeprompt += "|" 
                            completeprompt += chosenobjectwildcard + " "
                            completeprompt += "] "
                    if(hybridorswap == "swap"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += ":" + random.choice(objectwildcardlist) + ":" + str(random.randint(1,5)) +  "] "
                        else:
                            completeprompt += ":"
                            completeprompt += chosenobjectwildcard + " "
                            completeprompt += ":" + str(random.randint(1,5)) +  "] "
                else:
                    completeprompt += " " + givensubject + " "
                
                hybridorswap = ""
                # completion of strenght end
                completeprompt += "-objectstrengthend-"

            if(mainchooser == "animal"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == ""):

                    if(rare_dist(insanitylevel) and advancedprompting == True):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["
                        
                    if(unique_dist(insanitylevel) and generateanimaladdition == True):
                        animaladdedsomething = 1
                        completeprompt += "-animaladdition- -animal- "
                    if(animaladdedsomething != 1):
                        completeprompt += "-animal- "

                   

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

                # completion of strenght end
                completeprompt += "-objectstrengthend-"

                if(legendary_dist(insanitylevel)):
                    animaladdedsomething = 1
                    completeprompt += "-animalsuffixaddition- "
            
            # if we have a given subject, we should skip making an actual subject
            if(mainchooser == "humanoid"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                if(givensubject==""):

                    if(subjectchooser == "human"):
                        completeprompt += "-manwoman- "
                    
                    if(subjectchooser == "manwomanrelation"):
                        completeprompt += "-manwomanrelation- "

                    if(subjectchooser == "job"):
                        completeprompt += "-malefemale- "
                        completeprompt += "-job- "

                    if(subjectchooser == "fictional"):
                        if(rare_dist(insanitylevel) and advancedprompting == True):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += "-fictional- "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + " ] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "non fictional"):
                        if(rare_dist(insanitylevel)  and advancedprompting == True):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["

                        completeprompt += "-nonfictional- "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "humanoid"):
                        if(gender != "all"):
                            completeprompt += "-malefemale- "
                        if(rare_dist(insanitylevel)  and advancedprompting == True):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += "-humanoid- "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "firstname"):
                        if(rare_dist(insanitylevel)  and advancedprompting == True):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += "-firstname- "

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + "-firstname-" + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + "-firstname-" + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""


                else:
                    completeprompt += " " + givensubject + " "  

                # completion of strenght end
                completeprompt += "-objectstrengthend-"   
            
             # sometimes add a suffix for more fun!
            if( (mainchooser == "humanoid" or mainchooser == "animal" or mainchooser == "object") and  chance_roll(insanitylevel, subjectconceptsuffixchance)):
                completeprompt += " of -conceptsuffix- "
            
            if(subjectchooser == "landscape"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == ""):
                    if(rare_dist(insanitylevel) and advancedprompting == True):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["
                    
                    completeprompt += "-location- "

                    if(hybridorswap == "hybrid"):
                        completeprompt += "|" + "-location-"  + "] "
                    if(hybridorswap == "swap"):
                        completeprompt += ":" + "-location-" + ":" + str(random.randint(1,5)) +  "] "        
                else:
                    completeprompt += " " + givensubject + " " 
                
                hybridorswap = ""

                # completion of strenght end
                completeprompt += "-objectstrengthend-"

                # shots from inside can create cool effects in landscapes
                if(chance_roll(insanitylevel, subjectlandscapeaddonlocationchance)):
                    insideshot = 1
                    completeprompt += " from inside of a -addontolocationinside- "

                if(chance_roll(insanitylevel, subjectlandscapeaddonlocationchance) and insideshot == 0):
                    completeprompt += " and "
                    if(chance_roll(insanitylevel, subjectlandscapeaddonlocationdescriptorchance)):
                        completeprompt += "-descriptor- " 
                    if(chance_roll(insanitylevel, subjectlandscapeaddonlocationculturechance)):
                        completeprompt += "-culture- "

                    #addontolocation = [locationlist,buildinglist, vehiclelist]
                    completeprompt += "-addontolocation- "


            if(mainchooser == "concept"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                if(givensubject == ""):
                    if(subjectchooser == "event"):
                        completeprompt += " \"" + random.choice(eventlist) + "\" "
                    
                    if(subjectchooser == "concept"):
                        completeprompt += " \" The -conceptprefix- of -conceptsuffix- \" "

                    if(subjectchooser == "poemline"):
                        completeprompt += " \" -poemline- \" "

                    if(subjectchooser == "songline"):
                        completeprompt += " \" -songline- \" "
                else:
                    completeprompt += " " + givensubject + " " 

                # completion of strenght end
                completeprompt += "-objectstrengthend-"



        # object additions
        for i in range(objectadditionsrepeats):
            if(mainchooser == "object" and chance_roll(insanitylevel, objectadditionschance) and generateobjectaddition == True):
                completeprompt += ", -objectaddition- , "
        
        
        # riding an animal, holding an object or driving a vehicle, rare
        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid", "manwomanrelation","firstname"] and chance_roll(insanitylevel, humanadditionchance) and generatehumanaddition == True):
            humanspecial = 1
            completeprompt += "-humanaddition- "
            
        completeprompt += ", "

        # unique additions for all types:
        if(chance_roll(insanitylevel, overalladditionchance) and generateoveralladdition == True):
            completeprompt += "-overalladdition- "





        # SD understands emoji's. Can be used to manipulate facial expressions.
        # emoji, legendary
        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid", "manwomanrelation","firstname"] and chance_roll(insanitylevel, emojichance) and generateemoji== True):
            completeprompt += "-emoji-, "
            

        # cosplaying
        #if(subjectchooser in ["animal as human", "non fictional", "humanoid"] and rare_dist(insanitylevel) and humanspecial != 1):
        #    completeprompt += "cosplaying as " + random.choice(fictionallist) + ", "

        # Job 
        # either go job or activity, not both

        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid", "manwomanrelation","firstname"]  and chance_roll(insanitylevel, joboractivitychance) and humanspecial != 1 and generatesubject == True):
            joboractivitylist = [joblist,humanactivitylist]
            completeprompt += random.choice(random.choice(joboractivitylist)) + ", "


        # if(subjectchooser in ["animal as human","human","job", "fictional", "non fictional", "humanoid"] and legendary_dist(insanitylevel)):
        #    skintypelist = ["-color-", "-material-"]
        #    completeprompt += ", with " + random.choice(skintypelist) + " skin, "

        # custom mid list
        for i in range(custominputmidrepeats):
            if(chance_roll(insanitylevel, custominputmidchance) and generatecustominputmid == True):
                completeprompt += random.choice(custominputmidlist) + ", "
        
        # add in some more mini vomits
        if(chance_roll(insanitylevel, minivomitmidchance) and generateminivomit == True):
            completeprompt += " -minivomit-, "
        
        # outfit builder
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]  and chance_roll(insanitylevel, outfitchance) and generateoutfit == True and humanspecial != 1):
            completeprompt += ", wearing " + random.choice(buildoutfitlist) + ", "
        
        if(subjectchooser in ["animal as human","human","fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]  and chance_roll(insanitylevel, posechance) and humanspecial != 1 and generatepose == True):
            completeprompt += random.choice(poselist) + ", "
        
        if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]  and chance_roll(insanitylevel, hairchance) and generatehairstyle == True):
            completeprompt += random.choice(buildhairlist) + ", "

        if(subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]  and chance_roll(insanitylevel, accessorychance) and generateaccessorie == True and generateaccessories == True):
            completeprompt += random.choice(buildaccessorielist) + ", "

        if(chance_roll(insanitylevel, humanoidinsideshotchance) and subjectchooser not in ["landscape", "concept"] and generateinsideshot == True):
            insideshot = 1
            completeprompt += random.choice(insideshotlist) + ", "
        
        if(subjectchooser not in ["landscape", "concept"] and humanspecial != 1 and insideshot == 0 and chance_roll(insanitylevel, humanoidbackgroundchance) and generatebackground == True):
            completeprompt += random.choice(backgroundtypelist) + ", "

        # minilocation bit
        if(subjectchooser in ["landscape"] and chance_roll(insanitylevel, landscapeminilocationchance) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "
            
        if(chance_roll(insanitylevel, generalminilocationchance) and generateminilocationaddition == True):
            completeprompt += " -minilocationaddition-, "



        # landscapes it is nice to always have a time period
        if(chance_roll(insanitylevel, timperiodchance) or subjectchooser=="landscape"):
            if(generatetimeperiod == True):
                completeprompt += "-timeperiod-, "

        if(mainchooser not in ["landscape"]  and chance_roll(insanitylevel, focuschance) and generatefocus == True):
            completeprompt += "-focus-, "
            


        # others
        if(chance_roll(insanitylevel, directionchance) and generatedirection == True):
            completeprompt += "-direction-, "

        if(chance_roll(insanitylevel, moodchance) and generatemood == True):
            completeprompt += "-mood-, " 

        # add in some more mini vomits
        if(chance_roll(insanitylevel, minivomitsuffixchance) and generateminivomit == True):
            completeprompt += " -minivomit-, "
       
        if(chance_roll(insanitylevel, artmovementchance) and generateartmovement == True):
            completeprompt += "-artmovement-, "  
        
        if(chance_roll(insanitylevel, lightingchance) and generatelighting == True):
            completeprompt += "-lighting-, "  

        # determine wether we have a photo or not
        if("photo" in completeprompt.lower()):
            isphoto = 1
            
        if(chance_roll(insanitylevel, photoadditionchance) and isphoto == 1 and generatephotoaddition == True):
            completeprompt += random.choice(photoadditionlist) + ", "
                
        if(isphoto == 1 and generatecamera == True):
            completeprompt += "-camera-, "  

        if(chance_roll(insanitylevel, lenschance) or isphoto == 1):
            if(generatelens == True):
                completeprompt += "-lens-, "

        if(chance_roll(insanitylevel, colorschemechance) and generatecolorscheme == True):
            completeprompt += "-colorscheme-, "

        # vomit some cool/wierd things into the prompt
        if(chance_roll(insanitylevel, vomit1chance) and generatevomit == True):
            completeprompt += "-vomit-, "
            if(chance_roll(insanitylevel, vomit2chance)):
                completeprompt += "-vomit-, "

        #adding a great work of art, like starry night has cool effects. But this should happen only very rarely.
        if(chance_roll(insanitylevel, greatworkchance) and generategreatwork == True):
            completeprompt += " in the style of -greatwork-, "

        #adding a poemline. But this should happen only very rarely.
        if(chance_roll(insanitylevel, poemlinechance) and generatepoemline == True):
            completeprompt += " \"-poemline-\", "

        #adding a songline. But this should happen only very rarely.
        if(chance_roll(insanitylevel, songlinechance) and generatesongline == True):
            completeprompt += " \"-songline-\", "

        # everyone loves the adding quality. The better models don't need this, but lets add it anyway
        if(chance_roll(insanitylevel, quality1chance) and generatequality == True):
            completeprompt += "-quality-, "
            if(chance_roll(insanitylevel, quality2chance)):
                completeprompt += "-quality-, "

        
        
        # start second part of art blaster here
        if(artblastermode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artist-, "
                if(uncommon_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(unique_dist(insanitylevel) and bool(imagetypelist)):
                    completeprompt += "-imagetype-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1 
        
         # start second part of unique art here
        if(uniqueartmode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(uncommon_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(rare_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(unique_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                if(unique_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artist-, "
                if(novel_dist(insanitylevel) and bool(greatworklist)):
                    completeprompt += "in style of -greatwork-, "
                if(novel_dist(insanitylevel) and bool(poemlinelist)):
                    completeprompt += "\"-poemline-\", "
                if(novel_dist(insanitylevel) and bool(songlinelist)):
                    completeprompt += "\"-songline-\", "
                
                step = step + 1 
        
        
        # start second part of quality vomit here
        if(qualityvomitmode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(uncommon_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                if(unique_dist(insanitylevel) and bool(minivomitlist)):
                    completeprompt += "-minivomit-, "
                if(unique_dist(insanitylevel) and bool(artmovementlist)) :
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1 
        
        # start second part of mood color here
        if(colorcannonmode == True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(uncommon_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(unique_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(unique_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                step = step + 1 

        
        # start second part of photo fantasy here
        if(photofantasymode == True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(uncommon_dist(insanitylevel) and bool(cameralist)):
                    completeprompt += "-camera-, "
                if(rare_dist(insanitylevel) and bool(lenslist)):
                    completeprompt += "-lens-, "
                if(unique_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(unique_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                step = step + 1 
        
        # start second part of massive madness here
        if(massivemadnessmode == True):
            completeprompt += ":1.3), "
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(rare_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artist-, "
                if(rare_dist(insanitylevel) and bool(descriptorlist)):
                    completeprompt += "-descriptor-, "
                if(rare_dist(insanitylevel) and bool(moodlist)):
                    completeprompt += "-mood-, "
                if(rare_dist(insanitylevel) and bool(colorschemelist)):
                    completeprompt += "-colorscheme-, "
                if(rare_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(rare_dist(insanitylevel) and bool(artmovementlist)):
                    completeprompt += "-artmovement-, "
                if(rare_dist(insanitylevel) and bool(lightinglist)):
                    completeprompt += "-lighting-, "
                if(rare_dist(insanitylevel) and bool(minilocationadditionslist)):
                    completeprompt += "-minilocationaddition-, "
                if(rare_dist(insanitylevel) and bool(materiallist)):
                    completeprompt += "-material-, "
                if(rare_dist(insanitylevel) and bool(conceptsuffixlist)):
                    completeprompt += "-conceptsuffix-, "
                if(rare_dist(insanitylevel) and bool(qualitylist)):
                    completeprompt += "-quality-, "
                if(rare_dist(insanitylevel) and bool(cameralist)):
                    completeprompt += "-camera-, "
                step = step + 1 

        # start styles mode here
        if(stylesmode == True):
            completeprompt += chosenstylesuffix

        
        # custom style list
        if(chance_roll(insanitylevel, customstyle1chance) and generatestyle == True):
            completeprompt += "-styletilora-, "
            if(chance_roll(insanitylevel, customstyle2chance)):
                completeprompt += "-styletilora-, "


        # custom suffix list
        for i in range(custominputsuffixrepeats):
            if(chance_roll(insanitylevel, custominputsuffixchance) and generatecustominputsuffix == True):
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
                if(advancedprompting == False):
                    artistmode = "normal"
                if artistmode in ["hybrid","switching"] and end - step == 1:
                    artistmode = "normal"
            # if there are not enough artists in the list, then just go normal
            if(len(artistlist) < 3):
                artistmode = "normal"
            
            if artistmode in ["hybrid", "stopping", "adding","switching"]:
                completeprompt += " ["
                
            while step < end: 
                if(normal_dist(insanitylevel)):
                    isweighted = 1
                
                if isweighted == 1:
                    completeprompt += " ("

                #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
                completeprompt += "-artist-"
                
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

    

    
    # lol, this needs a rewrite :D
    while (
    "-color-" in completeprompt or
    "-material-" in completeprompt or
    "-animal-" in completeprompt or
    "-object-" in completeprompt or
    "-fictional-" in completeprompt or
    "-nonfictional-" in completeprompt or
    "-conceptsuffix-" in completeprompt or
    "-building-" in completeprompt or
    "-vehicle-" in completeprompt or
    "-outfit-" in completeprompt or
    "-location-" in completeprompt or
    "-conceptprefix-" in completeprompt or
    "-descriptor-" in completeprompt or
    "-food-" in completeprompt or
    "-haircolor-" in completeprompt or
    "-hairstyle-" in completeprompt or
    "-job-" in completeprompt or
    "-culture-" in completeprompt or
    "-accessory-" in completeprompt or
    "-humanoid-" in completeprompt or
    "-manwoman-" in completeprompt or
    "-human-" in completeprompt or
    "-colorscheme-" in completeprompt or
    "-mood-" in completeprompt or
    "-genderdescription-" in completeprompt or
    "-artmovement-" in completeprompt or
    "-malefemale-" in completeprompt or
    "-objecttotal-" in completeprompt or
    "-outfitprinttotal-" in completeprompt or
    "-bodytype-" in completeprompt or
    "-minilocation-" in completeprompt or
    "-minilocationaddition-" in completeprompt or
    "-pose-" in completeprompt or
    "-season-" in completeprompt or
    "-minioutfit-" in completeprompt or
    "-elaborateoutfit-" in completeprompt or
    "-minivomit-" in completeprompt or
    "-vomit-" in completeprompt or
    "-rpgclass-" in completeprompt or
    "-subjectfromfile-" in completeprompt or
    "-brand-" in completeprompt or
    "-space-" in completeprompt or
    "-artist-" in completeprompt or
    "-imagetype-" in completeprompt or
    "-othertype-" in completeprompt or
    "-quality-" in completeprompt or
    "-lighting-" in completeprompt or
    "-camera-" in completeprompt or
    "-lens-" in completeprompt or
    "-imagetypequality-" in completeprompt or
    "-poemline-" in completeprompt or
    "-songline-" in completeprompt or
    "-greatwork-" in completeprompt or
    "-artistfantasy-" in completeprompt or 
    "-artistpopular-" in completeprompt or 
    "-artistromanticism-" in completeprompt or 
    "-artistphotography-" in completeprompt or
    "-emoji-" in completeprompt or
    "-timeperiod-" in completeprompt or
    "-shotsize-" in completeprompt or
    "-musicgenre-" in completeprompt or
    "-animaladdition-" in completeprompt or
    "-addontolocationinside-" in completeprompt or
    "-addontolocation-" in completeprompt or
    "-objectaddition-" in completeprompt or
    "-humanaddition-" in completeprompt or
    "-overalladdition-" in completeprompt or
    "-focus-" in completeprompt or
    "-direction-" in completeprompt or
    "-styletilora-" in completeprompt or
    "-manwomanrelation-" in completeprompt or
    "-waterlocation-" in completeprompt or
    "-container-" in completeprompt or
    "-firstname-" in completeprompt or
    "-flora-" in completeprompt or
    "-print-" in completeprompt or
    "-miniactivity-" in completeprompt or
    "-pattern-" in completeprompt or
    "-animalsuffixaddition-" in completeprompt or
    "-chair-" in completeprompt):
        allwildcardslistnohybrid = [ "-color-","-object-", "-animal-", "-fictional-","-nonfictional-","-building-","-vehicle-","-location-","-conceptprefix-","-food-","-haircolor-","-hairstyle-","-job-", "-accessory-", "-humanoid-", "-manwoman-", "-human-", "-colorscheme-", "-mood-", "-genderdescription-", "-artmovement-", "-malefemale-", "-bodytype-", "-minilocation-", "-minilocationaddition-", "-pose-", "-season-", "-minioutfit-", "-elaborateoutfit-", "-minivomit-", "-vomit-", "-rpgclass-", "-subjectfromfile-", "-brand-", "-space-", "-artist-", "-imagetype-", "-othertype-", "-quality-", "-lighting-", "-camera-", "-lens-","-imagetypequality-", "-poemline-", "-songline-", "-greatwork-", "-artistfantasy-", "-artistpopular-", "-artistromanticism-", "-artistphotography-", "-emoji-", "-timeperiod-", "-shotsize-", "-musicgenre-", "-animaladdition-", "-addontolocationinside-", "-addontolocation-", "-objectaddition-", "-humanaddition-", "-overalladdition-", "-focus-", "-direction-", "-styletilora-", "-manwomanrelation-", "-waterlocation-", "-container-", "-firstname-", "-flora-", "-print-", "-miniactivity-", "-pattern-", "-animalsuffixaddition-", "-chair-"]
        allwildcardslistnohybridlists = [colorlist, objectlist, animallist, fictionallist, nonfictionallist, buildinglist, vehiclelist, locationlist,conceptprefixlist,foodlist,haircolorlist, hairstylelist,joblist, accessorielist, humanoidlist, manwomanlist, humanlist, colorschemelist, moodlist, genderdescriptionlist, artmovementlist, malefemalelist, bodytypelist, minilocationlist, minilocationadditionslist, poselist, seasonlist, minioutfitlist, elaborateoutfitlist, minivomitlist, vomitlist, rpgclasslist, customsubjectslist, brandlist, spacelist, artistlist, imagetypelist, othertypelist, qualitylist, lightinglist, cameralist, lenslist, imagetypequalitylist, poemlinelist, songlinelist, greatworklist, fantasyartistlist, popularartistlist, romanticismartistlist, photographyartistlist, emojilist, timeperiodlist, shotsizelist, musicgenrelist, animaladditionlist, addontolocationinsidelist, addontolocationlist, objectadditionslist, humanadditionlist, overalladditionlist, focuslist, directionlist, stylestiloralist, manwomanrelationlist, waterlocationlist, containerlist, firstnamelist, floralist, printlist, miniactivitylist, patternlist, animalsuffixadditionlist, chairlist]
        
        allwildcardslistwithhybrid = ["-material-", "-descriptor-", "-outfit-", "-conceptsuffix-","-culture-", "-objecttotal-", "-outfitprinttotal-"]
        allwildcardslistwithhybridlists = [materiallist, descriptorlist,outfitlist,conceptsuffixlist,culturelist, objecttotallist, outfitprinttotallist]
        
        
        #  keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        for wildcard in allwildcardslistnohybrid:
            attachedlist = allwildcardslistnohybridlists[allwildcardslistnohybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,False, advancedprompting)


        
        for wildcard in allwildcardslistwithhybrid:
            attachedlist = allwildcardslistwithhybridlists[allwildcardslistwithhybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,True, advancedprompting)


      
    # prompt strenght stuff

    # if the given subject already is formed like this ( :1.x)
    # then just ignore this
    
    matches = []
    if(givensubject != ""):
        pattern = r'\(\w+:\d+\.\d+\)'
        matches = re.findall(pattern, givensubject)


    if(len(completeprompt) > 325 and matches == []):
        if(len(completeprompt) < 375):
            strenght = "1.1"  
        elif(len(completeprompt) < 450):
            strenght = "1.2"  
        else:
            strenght = "1.3"  
        completeprompt = completeprompt.replace("-objectstrengthstart-","(")
        completeprompt = completeprompt.replace("-objectstrengthend-",":" + strenght + ")")
    else:
        completeprompt = completeprompt.replace("-objectstrengthstart-","")
        completeprompt = completeprompt.replace("-objectstrengthend-","")

    # clean it up
    completeprompt = cleanup(completeprompt, advancedprompting)

    #just for me, some fun with posting fake dev messages (ala old sim games)
    if(random.randint(1, 50)==1):
        print("")
        print(random.choice(devmessagelist))
        print("")

    print(completeprompt)
    return completeprompt


# function that takes an existing prompt and tries to create a variant out of it
def createpromptvariant(prompt = "", insanitylevel = 5, antivalues = "" , gender = "all", artists = "all", advancedprompting = True):
    # first load the lists, all copied from above (can that be done better?)
    # do we want to use the same settings or keep it open??

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
    fictionallist = csv_to_list(csvfilename="fictional characters",antilist=antilist,skipheader=True,gender=gender)
    nonfictionallist = csv_to_list(csvfilename="nonfictional characters",antilist=antilist,skipheader=True,gender=gender)
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
    malefemalelist = csv_to_list(csvfilename="malefemale",antilist=antilist,skipheader=True,gender=gender)
    manwomanlist = csv_to_list(csvfilename="manwoman",antilist=antilist,skipheader=True,gender=gender)
    moodlist = csv_to_list("moods",antilist)
    othertypelist = csv_to_list("othertypes",antilist)
    poselist = csv_to_list("poses",antilist)
    qualitylist = csv_to_list("quality",antilist)
    shotsizelist = csv_to_list("shotsizes",antilist)
    timeperiodlist = csv_to_list("timeperiods",antilist)
    vomitlist = csv_to_list("vomit",antilist)
    foodlist = csv_to_list("foods", antilist)
    genderdescriptionlist = csv_to_list(csvfilename="genderdescription",antilist=antilist,skipheader=True,gender=gender)
    minilocationlist = csv_to_list("minilocations", antilist)
    minioutfitlist = csv_to_list("minioutfits", antilist)
    seasonlist = csv_to_list("seasons", antilist)
    elaborateoutfitlist = csv_to_list("elaborateoutfits", antilist)
    minivomitlist = csv_to_list("minivomit", antilist)
    imagetypequalitylist = csv_to_list("imagetypequality", antilist)
    rpgclasslist = csv_to_list("rpgclasses", antilist)
    brandlist = csv_to_list("brands", antilist)
    spacelist = csv_to_list("space", antilist)
    poemlinelist = csv_to_list("poemlines", antilist)
    songlinelist = csv_to_list("songlines", antilist)
    musicgenrelist = csv_to_list("musicgenres", antilist)
    manwomanrelationlist = csv_to_list(csvfilename="manwomanrelations",antilist=antilist,skipheader=True,gender=gender)
    waterlocationlist = csv_to_list("waterlocations", antilist)
    containerlist = csv_to_list("containers", antilist)
    firstnamelist = csv_to_list(csvfilename="firstnames",antilist=antilist,skipheader=True,gender=gender)
    floralist = csv_to_list("flora", antilist)
    printlist = csv_to_list("prints", antilist)
    patternlist = csv_to_list("patterns", antilist)
    chairlist = csv_to_list("chairs", antilist)

    humanlist = fictionallist + nonfictionallist + humanoidlist + malefemalelist + manwomanlist + manwomanrelationlist
    objecttotallist = objectlist + buildinglist + vehiclelist + foodlist + spacelist + floralist + containerlist
    outfitprinttotallist = objecttotallist + locationlist + colorlist + musicgenrelist + seasonlist + animallist + patternlist

    # build artists list
    artistlist = []
    # create artist list to use in the code, maybe based on category  or personal lists
    if(artists != "all" and artists != "none" and artists.startswith("personal_artists") == False and artists.startswith("personal artists") == False):
        artistlist = artist_category_csv_to_list("artists_and_category",artists)
    elif(artists.startswith("personal_artists") == True or artists.startswith("personal artists") == True):
        artists = artists.replace(" ","_",-1) # add underscores back in
        artistlist = csv_to_list(artists,antilist,"./userfiles/")
    elif(artists != "none"):
        artistlist = csv_to_list("artists",antilist)

    # create special artists lists, used in templates
    fantasyartistlist = artist_category_csv_to_list("artists_and_category","fantasy")
    popularartistlist = artist_category_csv_to_list("artists_and_category","popular")
    romanticismartistlist = artist_category_csv_to_list("artists_and_category","romanticism")
    photographyartistlist = artist_category_csv_to_list("artists_and_category","photography")


    # add any other custom lists
    stylestiloralist = csv_to_list("styles_ti_lora",antilist,"./userfiles/")
    generatestyle = bool(stylestiloralist) # True of not empty

    custominputprefixlist = csv_to_list("custom_input_prefix",antilist,"./userfiles/")
    generatecustominputprefix = bool(custominputprefixlist) # True of not empty

    custominputmidlist = csv_to_list("custom_input_mid",antilist,"./userfiles/")
    generatecustominputmid = bool(custominputmidlist) # True of not empty

    custominputsuffixlist = csv_to_list("custom_input_suffix",antilist,"./userfiles/")
    generatecustominputsuffix = bool(custominputsuffixlist) # True of not empty

    customsubjectslist = csv_to_list("custom_subjects",antilist,"./userfiles/")

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
    overalladditionlist = csv_to_list("overalladditions", antilist,"./csvfiles/special_lists/")
    imagetypemodelist = csv_to_list("imagetypemodes", antilist,"./csvfiles/special_lists/")
    miniactivitylist = csv_to_list("miniactivity", antilist,"./csvfiles/special_lists/")


    prompt = prompt.replace(",", " , ")
    prompt = prompt.replace("(", " ( ")
    prompt = prompt.replace(")", " ) ")
    prompt = prompt.replace("[", " [ ")
    prompt = prompt.replace("]", " ] ")
    prompt = prompt.replace("|", " | ")
    prompt = prompt.replace(":", " : ")

    prompt = " " + prompt
    # store the (sort of) original prompt
    originalprompt = prompt
    ### Get all combinations of 1 to 4 consecutive words


    words = prompt.split()
    num_words = len(words)
    
    combinations_list = []
    
    for length in range(1, 5):  # Generate combinations of length 1 to 4
        for start_idx in range(num_words - length + 1):
            end_idx = start_idx + length
            combination = ' '.join(words[start_idx:end_idx])
            combinations_list.append(combination)
    
    maxamountofruns = 4
    runs = 0

    if(insanitylevel != 0):
        print("")
        print("Creating a prompt variation")
        print("")
        while(originalprompt == prompt and runs != maxamountofruns):
            for combination in combinations_list:
                lowercase_combination = combination.lower()
                combination = " " + combination + " "

               # some rare changes if needed
                if lowercase_combination in [x.lower() for x in humanlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -human- ")

                if lowercase_combination in [x.lower() for x in objecttotallist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -objecttotal- ")
                
                if lowercase_combination in [x.lower() for x in artistlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -artist- ")
                

                if lowercase_combination in [x.lower() for x in colorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -color- ")

                if lowercase_combination in [x.lower() for x in animallist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -animal- ")
                
                if lowercase_combination in [x.lower() for x in objectlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -object- ")
                            
                if lowercase_combination in [x.lower() for x in fictionallist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -fictional- ")

                
                if lowercase_combination in [x.lower() for x in nonfictionallist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -nonfictional- ")

                
                #if lowercase_combination in [x.lower() for x in conceptsuffixlist] and chance_roll(insanitylevel, "uncommon"):
                #   prompt = prompt.replace(combination," -conceptsuffix- ")

                
                if lowercase_combination in [x.lower() for x in buildinglist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -building- ")

                
                if lowercase_combination in [x.lower() for x in vehiclelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -vehicle- ")

                
                if lowercase_combination in [x.lower() for x in outfitlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -outfit- ")

                
                if lowercase_combination in [x.lower() for x in locationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -location- ")

                
                if lowercase_combination in [x.lower() for x in accessorielist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -accessory- ")

                
                if lowercase_combination in [x.lower() for x in artmovementlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -artmovement- ")

                
                if lowercase_combination in [x.lower() for x in bodytypelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -bodytype- ")

                
                if lowercase_combination in [x.lower() for x in cameralist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -camera- ")

                
                if lowercase_combination in [x.lower() for x in colorschemelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -colorscheme- ")

                
                #if lowercase_combination in [x.lower() for x in conceptprefixlist] and chance_roll(insanitylevel, "uncommon"):
                #    prompt = prompt.replace(combination," -conceptprefix- ")

                
                if lowercase_combination in [x.lower() for x in culturelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -culture- ")

                
                if lowercase_combination in [x.lower() for x in descriptorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -descriptor- ")

                if lowercase_combination in [x.lower() for x in directionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -direction- ")

                if lowercase_combination in [x.lower() for x in emojilist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -emoji- ")
                    
                if lowercase_combination in [x.lower() for x in eventlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -event- ")

                if lowercase_combination in [x.lower() for x in focuslist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -focus- ")

                if lowercase_combination in [x.lower() for x in greatworklist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -greatwork- ")

                if lowercase_combination in [x.lower() for x in haircolorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -haircolor- ")

                if lowercase_combination in [x.lower() for x in hairstylelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -hairstyle- ")

                if lowercase_combination in [x.lower() for x in directionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -direction- ")

                if lowercase_combination in [x.lower() for x in humanoidlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -humanoid- ")

                if lowercase_combination in [x.lower() for x in joblist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -job- ")

                if lowercase_combination in [x.lower() for x in lenslist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -lens- ")
                if lowercase_combination in [x.lower() for x in lightinglist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -lighting- ")
                if lowercase_combination in [x.lower() for x in malefemalelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -malefemale- ")
                if lowercase_combination in [x.lower() for x in manwomanlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -manwoman- ")
                if lowercase_combination in [x.lower() for x in moodlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -mood- ")
                if lowercase_combination in [x.lower() for x in othertypelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -othertype- ")
                if lowercase_combination in [x.lower() for x in poselist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -pose- ")
                if lowercase_combination in [x.lower() for x in qualitylist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -quality- ")
                if lowercase_combination in [x.lower() for x in shotsizelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -shotsize- ")
                if lowercase_combination in [x.lower() for x in timeperiodlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -timeperiod- ")
                if lowercase_combination in [x.lower() for x in vomitlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -vomit- ")
                if lowercase_combination in [x.lower() for x in foodlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -food- ")
                if lowercase_combination in [x.lower() for x in genderdescriptionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -genderdescription- ")
                if lowercase_combination in [x.lower() for x in minilocationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -minilocation- ")
                if lowercase_combination in [x.lower() for x in minioutfitlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -minioutfit- ")
                if lowercase_combination in [x.lower() for x in lenslist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -lens- ")
                if lowercase_combination in [x.lower() for x in seasonlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -season- ")
                if lowercase_combination in [x.lower() for x in imagetypequalitylist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -imagetypequality- ")
                if lowercase_combination in [x.lower() for x in rpgclasslist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -rpgclass- ")
                if lowercase_combination in [x.lower() for x in brandlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -brand- ")
                if lowercase_combination in [x.lower() for x in spacelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -space- ")
                if lowercase_combination in [x.lower() for x in poemlinelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -poemline- ")
                if lowercase_combination in [x.lower() for x in songlinelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -songline- ")
                if lowercase_combination in [x.lower() for x in musicgenrelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -musicgenre- ")
                if lowercase_combination in [x.lower() for x in manwomanrelationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -manwomanrelation- ")
                if lowercase_combination in [x.lower() for x in waterlocationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -waterlocation- ")
                if lowercase_combination in [x.lower() for x in containerlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -container- ")
                if lowercase_combination in [x.lower() for x in firstnamelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -firstname- ")
                if lowercase_combination in [x.lower() for x in floralist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -flora- ")
                if lowercase_combination in [x.lower() for x in printlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -print- ")
                if lowercase_combination in [x.lower() for x in miniactivitylist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -miniactivity- ")
                if lowercase_combination in [x.lower() for x in patternlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -pattern- ")
                if lowercase_combination in [x.lower() for x in chairlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -chair- ")


                if lowercase_combination in [x.lower() for x in fantasyartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -artistfantasy- ")
                if lowercase_combination in [x.lower() for x in popularartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -artistpopular- ")
                if lowercase_combination in [x.lower() for x in romanticismartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -artistromanticism- ")
                if lowercase_combination in [x.lower() for x in photographyartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -artistphotography- ")

                if lowercase_combination in [x.lower() for x in stylestiloralist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -styletilora- ")
                if lowercase_combination in [x.lower() for x in waterlocationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -waterlocation- ")

            runs += 1
         
        

    prompt = prompt.replace(" :", ":")
    prompt = prompt.replace(": ", ":")

    completeprompt = prompt



    while (
        "-color-" in completeprompt or
        "-material-" in completeprompt or
        "-animal-" in completeprompt or
        "-object-" in completeprompt or
        "-fictional-" in completeprompt or
        "-nonfictional-" in completeprompt or
        "-conceptsuffix-" in completeprompt or
        "-building-" in completeprompt or
        "-vehicle-" in completeprompt or
        "-outfit-" in completeprompt or
        "-location-" in completeprompt or
        "-conceptprefix-" in completeprompt or
        "-descriptor-" in completeprompt or
        "-food-" in completeprompt or
        "-haircolor-" in completeprompt or
        "-hairstyle-" in completeprompt or
        "-job-" in completeprompt or
        "-culture-" in completeprompt or
        "-accessory-" in completeprompt or
        "-humanoid-" in completeprompt or
        "-manwoman-" in completeprompt or
        "-human-" in completeprompt or
        "-colorscheme-" in completeprompt or
        "-mood-" in completeprompt or
        "-genderdescription-" in completeprompt or
        "-artmovement-" in completeprompt or
        "-malefemale-" in completeprompt or
        "-objecttotal-" in completeprompt or
        "-outfitprinttotal-" in completeprompt or
        "-bodytype-" in completeprompt or
        "-minilocation-" in completeprompt or
        "-minilocationaddition-" in completeprompt or
        "-pose-" in completeprompt or
        "-season-" in completeprompt or
        "-minioutfit-" in completeprompt or
        "-elaborateoutfit-" in completeprompt or
        "-minivomit-" in completeprompt or
        "-vomit-" in completeprompt or
        "-rpgclass-" in completeprompt or
        "-subjectfromfile-" in completeprompt or
        "-brand-" in completeprompt or
        "-space-" in completeprompt or
        "-artist-" in completeprompt or
        "-imagetype-" in completeprompt or
        "-othertype-" in completeprompt or
        "-quality-" in completeprompt or
        "-lighting-" in completeprompt or
        "-camera-" in completeprompt or
        "-lens-" in completeprompt or
        "-imagetypequality-" in completeprompt or
        "-poemline-" in completeprompt or
        "-songline-" in completeprompt or
        "-greatwork-" in completeprompt or
        "-artistfantasy-" in completeprompt or 
        "-artistpopular-" in completeprompt or 
        "-artistromanticism-" in completeprompt or 
        "-artistphotography-" in completeprompt or
        "-emoji-" in completeprompt or
        "-timeperiod-" in completeprompt or
        "-shotsize-" in completeprompt or
        "-musicgenre-" in completeprompt or
        "-animaladdition-" in completeprompt or
        "-objectaddition-" in completeprompt or
        "-humanaddition-" in completeprompt or
        "-overalladdition-" in completeprompt or
        "-focus-" in completeprompt or
        "-direction-" in completeprompt or
        "-styletilora-" in completeprompt or
        "-manwomanrelation-" in completeprompt or
        "-waterlocation-" in completeprompt or
        "-container-" in completeprompt or
        "-firstname-" in completeprompt or
        "-flora-" in completeprompt or
        "-print-" in completeprompt or
        "-miniactivity-" in completeprompt or
        "-pattern-" in completeprompt):
            allwildcardslistnohybrid = [ "-color-","-object-", "-animal-", "-fictional-","-nonfictional-","-building-","-vehicle-","-location-","-conceptprefix-","-food-","-haircolor-","-hairstyle-","-job-", "-accessory-", "-humanoid-", "-manwoman-", "-human-", "-colorscheme-", "-mood-", "-genderdescription-", "-artmovement-", "-malefemale-", "-bodytype-", "-minilocation-", "-minilocationaddition-", "-pose-", "-season-", "-minioutfit-", "-elaborateoutfit-", "-minivomit-", "-vomit-", "-rpgclass-", "-subjectfromfile-", "-brand-", "-space-", "-artist-", "-imagetype-", "-othertype-", "-quality-", "-lighting-", "-camera-", "-lens-","-imagetypequality-", "-poemline-", "-songline-", "-greatwork-", "-artistfantasy-", "-artistpopular-", "-artistromanticism-", "-artistphotography-", "-emoji-", "-timeperiod-", "-shotsize-", "-musicgenre-", "-animaladdition-", "-objectaddition-", "-humanaddition-", "-overalladdition-", "-focus-", "-direction-", "-styletilora-", "-manwomanrelation-", "-waterlocation-", "-container-", "-firstname-", "-flora-", "-print-", "-miniactivity-", "-pattern-"]
            allwildcardslistnohybridlists = [colorlist, objectlist, animallist, fictionallist, nonfictionallist, buildinglist, vehiclelist, locationlist,conceptprefixlist,foodlist,haircolorlist, hairstylelist,joblist, accessorielist, humanoidlist, manwomanlist, humanlist, colorschemelist, moodlist, genderdescriptionlist, artmovementlist, malefemalelist, bodytypelist, minilocationlist, minilocationadditionslist, poselist, seasonlist, minioutfitlist, elaborateoutfitlist, minivomitlist, vomitlist, rpgclasslist, customsubjectslist, brandlist, spacelist, artistlist, imagetypelist, othertypelist, qualitylist, lightinglist, cameralist, lenslist, imagetypequalitylist, poemlinelist, songlinelist, greatworklist, fantasyartistlist, popularartistlist, romanticismartistlist, photographyartistlist, emojilist, timeperiodlist, shotsizelist, musicgenrelist, animaladditionlist, objectadditionslist, humanadditionlist, overalladditionlist, focuslist, directionlist, stylestiloralist, manwomanrelationlist, waterlocationlist, containerlist, firstnamelist, floralist, printlist, miniactivitylist, patternlist]
            
            allwildcardslistwithhybrid = ["-material-", "-descriptor-", "-outfit-", "-conceptsuffix-","-culture-", "-objecttotal-", "-outfitprinttotal-"]
            allwildcardslistwithhybridlists = [materiallist, descriptorlist,outfitlist,conceptsuffixlist,culturelist, objecttotallist, outfitprinttotallist]
            
            
            #  keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
            for wildcard in allwildcardslistnohybrid:
                attachedlist = allwildcardslistnohybridlists[allwildcardslistnohybrid.index(wildcard)]
                completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,False, advancedprompting)


            
            for wildcard in allwildcardslistwithhybrid:
                attachedlist = allwildcardslistwithhybridlists[allwildcardslistwithhybrid.index(wildcard)]
                completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,True, advancedprompting)


        
        
    # clean it up
    completeprompt = cleanup(completeprompt, advancedprompting)
    




    return completeprompt

    # function
def replacewildcard(completeprompt, insanitylevel, wildcard,listname, activatehybridorswap, advancedprompting):

    if(len(listname) == 0):
        # handling empty lists
        completeprompt = completeprompt.replace(wildcard, "",1)
    else:

        while wildcard in completeprompt:
            if(unique_dist(insanitylevel) and activatehybridorswap == True and len(listname)>2 and advancedprompting==True):
                hybridorswaplist = ["hybrid", "swap"]
                hybridorswap = random.choice(hybridorswaplist)
                replacementvalue = random.choice(listname)
                listname.remove(replacementvalue)
                hybridorswapreplacementvalue = "[" + replacementvalue
                
                if(hybridorswap == "hybrid"):
                        replacementvalue = random.choice(listname)
                        listname.remove(replacementvalue)
                        hybridorswapreplacementvalue += "|" + replacementvalue + "] "
                if(hybridorswap == "swap"):
                        replacementvalue = random.choice(listname)
                        listname.remove(replacementvalue)
                        hybridorswapreplacementvalue += ":" + replacementvalue + ":" + str(random.randint(1,20)) +  "] "
                
                completeprompt = completeprompt.replace(wildcard, hybridorswapreplacementvalue,1)

            #if list is not empty
            if(bool(listname)):
                replacementvalue = random.choice(listname)
                listname.remove(replacementvalue)
                if(wildcard == "-artist-"):
                    replacementvalue = "art by " + replacementvalue
                
            else:
                replacementvalue = ""
            
            completeprompt = completeprompt.replace(wildcard, replacementvalue,1)


    return completeprompt

def replace_match(match):
    # Extract the first word from the match
    words = match.group(0)[1:-1].split('|')
    return words[0]

def cleanup(completeprompt, advancedprompting):

    # first, move LoRA's to the back dynamically

    # Find all occurrences of text between < and > using regex
    allLoRA = re.findall(r"<[^>]+>", completeprompt)

    # Remove the extracted matches from completeprompt
    completeprompt = re.sub(r"<[^>]+>", "", completeprompt)


    # if we are not using advanced prompting, remove any hybrid stuff:
    if(advancedprompting==False):
        hybridpattern = r'\[\w+\|\w+\]'
        # Replace the matched pattern with the first word in the group
        completeprompt = re.sub(hybridpattern, replace_match, completeprompt)

        # Doesnt work if there are multiple words, so then just get rid of things as is :D
        completeprompt = completeprompt.replace("[", " ")
        completeprompt = completeprompt.replace("]", " ")
        completeprompt = completeprompt.replace("|", " ")

    # sometimes if there are not enough artist, we get left we things formed as (:1.2)
    completeprompt = re.sub('\(\:\d+\.\d+\)', '', completeprompt) 

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
    completeprompt = re.sub(',:', ':', completeprompt)

    completeprompt = re.sub(',,', ', ', completeprompt)
    completeprompt = re.sub(',,,', ', ', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(' , ', ', ', completeprompt)
    completeprompt = re.sub(' ,', ',', completeprompt)
    completeprompt = re.sub(',\(', ', (', completeprompt)

    while "  " in completeprompt:
        completeprompt = re.sub('  ', ' ', completeprompt)
    completeprompt = re.sub('a The', 'The', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(',,', ',', completeprompt)

    completeprompt = re.sub(', of a', ' of a', completeprompt)
    completeprompt = re.sub('of a,', 'of a', completeprompt)
    completeprompt = re.sub('of a of a', 'of a', completeprompt)

    
    completeprompt = re.sub('(?<!\()\s?\(', ' (', completeprompt)
    completeprompt = re.sub('\)(?![\s)])', ') ', completeprompt)

    # Move the extracted LoRA's to the end of completeprompt
    completeprompt += " " + " ".join(allLoRA)   

    completeprompt = completeprompt.strip(", ")

    return completeprompt