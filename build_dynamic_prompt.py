import random
import re

if __package__ is None or __package__ == '':
    # A1111 style (standalone script or direct module execution)
    # Use absolute imports for compatibility with A1111 WebUI environment
    from csv_reader import *
    from random_functions import *
    from one_button_presets import OneButtonPresets
    from superprompter.superprompter import *
else:
    # ComfyUI style (imported as a package)
    # Use relative imports for proper integration with ComfyUI
    from .csv_reader import *
    from .random_functions import *
    from .one_button_presets import OneButtonPresets
    from .superprompter.superprompter import *

OBPresets = OneButtonPresets()




#builds a prompt dynamically
# insanity level controls randomness of propmt 0-10
# forcesubject van be used to force a certain type of subject
# Set artistmode to none, to exclude artists 
def build_dynamic_prompt(insanitylevel = 5, forcesubject = "all", artists = "all", imagetype = "all", onlyartists = False, antivalues = "", prefixprompt = "", suffixprompt ="",promptcompounderlevel ="1", seperator = "comma", givensubject="",smartsubject = True,giventypeofimage="", imagemodechance = 20, gender = "all", subtypeobject="all", subtypehumanoid="all", subtypeconcept="all", advancedprompting=True, hardturnoffemojis=False, seed=-1, overrideoutfit="", prompt_g_and_l = False, base_model = "SD1.5", OBP_preset = "", prompt_enhancer = "none", subtypeanimal="all", subtypelocation="all", preset_prefix = "", preset_suffix = ""):

    remove_weights = False
    less_verbose = False
    add_vomit = True
    add_quality = True
    anime_mode = False
    configfilesuffix = ""
    if(forcesubject ==  "------ all"):
        forcesubject = "all"

    superprompter = False
    prompt_enhancer = prompt_enhancer.lower()
    if(prompt_enhancer == "superprompter" or prompt_enhancer == "superprompt" or prompt_enhancer == "superprompt-v1" or prompt_enhancer == "hyperprompt"):
        superprompter = True
    if(superprompter==True):
        base_model = "Stable Cascade"

    # new method of subject choosing from the interface, lets translate this:
    subjectlist = translate_main_subject(forcesubject)
    forcesubject = subjectlist[0]


    # ugly but it works :D Keeps both methods working while the UI changes.
    if(subtypeobject != "all" or subtypeobject != ""):
        subtypeobject = subjectlist[1]
    if(subtypeanimal != "all" or subtypeanimal != ""):
        subtypeanimal = subjectlist[1]
    if(subtypelocation != "all" or subtypelocation != ""):
        subtypelocation = subjectlist[1]
    if(subtypehumanoid != "all" or subtypehumanoid != ""):
        subtypehumanoid = subjectlist[1]
    if(subtypeconcept != "all" or subtypeconcept != ""):
        subtypeconcept = subjectlist[1]

    # set seed
    # For use in ComfyUI (might bring to Automatic1111 as well)
    # lets do it when its larger than 0
    # Otherwise, just do nothing and it will keep on working based on an earlier set seed
    if(seed > 0):
        random.seed(seed)

    originalinsanitylevel = insanitylevel
    if(advancedprompting != False and random.randint(0,max(0, insanitylevel - 2)) <= 0):
        advancedprompting == False

    original_OBP_preset = OBP_preset
    if(OBP_preset == OBPresets.RANDOM_PRESET_OBP):
        obp_options = OBPresets.load_obp_presets()
        random_preset = random.choice(list(obp_options.keys()))
        print("Engaging randomized presets, locking on to: " + random_preset)

        selected_opb_preset = OBPresets.get_obp_preset(random_preset)
        insanitylevel = selected_opb_preset["insanitylevel"]
        forcesubject = selected_opb_preset["subject"]
        artists = selected_opb_preset["artist"]
        subtypeobject = selected_opb_preset["chosensubjectsubtypeobject"]
        subtypehumanoid = selected_opb_preset["chosensubjectsubtypehumanoid"]
        subtypeconcept = selected_opb_preset["chosensubjectsubtypeconcept"]
        gender = selected_opb_preset["chosengender"]
        imagetype = selected_opb_preset["imagetype"]
        imagemodechance = selected_opb_preset["imagemodechance"]
        givensubject = selected_opb_preset["givensubject"]
        smartsubject = selected_opb_preset["smartsubject"]
        overrideoutfit = selected_opb_preset["givenoutfit"]
        prefixprompt = selected_opb_preset["prefixprompt"]
        suffixprompt = selected_opb_preset["suffixprompt"]
        giventypeofimage = selected_opb_preset["giventypeofimage"]
        antistring = selected_opb_preset["antistring"]

        # api support tricks for OBP presets
        OBP_preset = ""

    if(OBP_preset != "" and OBP_preset != 'Custom...'):
        selected_opb_preset = OBPresets.get_obp_preset(OBP_preset)
        insanitylevel = selected_opb_preset["insanitylevel"]
        forcesubject = selected_opb_preset["subject"]
        artists = selected_opb_preset["artist"]
        subtypeobject = selected_opb_preset["chosensubjectsubtypeobject"]
        subtypehumanoid = selected_opb_preset["chosensubjectsubtypehumanoid"]
        subtypeconcept = selected_opb_preset["chosensubjectsubtypeconcept"]
        gender = selected_opb_preset["chosengender"]
        imagetype = selected_opb_preset["imagetype"]
        imagemodechance = selected_opb_preset["imagemodechance"]
        givensubject = selected_opb_preset["givensubject"]
        smartsubject = selected_opb_preset["smartsubject"]
        overrideoutfit = selected_opb_preset["givenoutfit"]
        prefixprompt = selected_opb_preset["prefixprompt"]
        suffixprompt = selected_opb_preset["suffixprompt"]
        giventypeofimage = selected_opb_preset["giventypeofimage"]
        antistring = selected_opb_preset["antistring"]

    prefixprompt = preset_prefix + ", " + prefixprompt
    suffixprompt = suffixprompt + ", " + preset_suffix

    # new method of subject choosing from the interface, lets translate this:
    # really hacky way of doing this now.
    if("-" in forcesubject):
        subjectlist = translate_main_subject(forcesubject)
        forcesubject = subjectlist[0]


        # ugly but it works :D Keeps both methods working while the UI changes.
        if(subtypeobject != "all" or subtypeobject != ""):
            subtypeobject = subjectlist[1]
        if(subtypeanimal != "all" or subtypeanimal != ""):
            subtypeanimal = subjectlist[1]
        if(subtypelocation != "all" or subtypelocation != ""):
            subtypelocation = subjectlist[1]
        if(subtypehumanoid != "all" or subtypehumanoid != ""):
            subtypehumanoid = subjectlist[1]
        if(subtypeconcept != "all" or subtypeconcept != ""):
            subtypeconcept = subjectlist[1]

        
    originalartistchoice = artists
    doartistnormal = True
    outfitmode = 0

    animalashuman = False
    

    partlystylemode = False
    # cheat for presets
    if(OBP_preset=='Waifu''s' or OBP_preset=='Husbando''s'):
        basemodel = "Anime Model"
    # Base model options, used to change things in prompt generation. Might be able to extend to different forms like animatediff as well?
    base_model_options = ["SD1.5", "SDXL", "Stable Cascade", "Anime Model"]
    if base_model not in base_model_options:
        base_model = "SD1.5" # Just in case there is no option here.
    # "SD1.5" -- Standard, future: More original style prompting
    # "SDXL" -- Standard (for now), future: More natural language
    # "Stable Cascade" -- Remove weights
    if(base_model == "Stable Cascade"):
        remove_weights = True
        add_vomit = False
        add_quality = False
    if(base_model == "SD1.5"):
        less_verbose = True
    if(base_model == "Anime Model"):
        less_verbose = True
        advancedprompting = False
        anime_mode = True
        configfilesuffix = "anime"
    
    # Hard overwrite some stuff because people dont config this themselves
    if((anime_mode or imagetype == "all - anime") and (artists == "all" or normal_dist(insanitylevel))):
        artists = "none"


    # load the config file

    config = load_config_csv(configfilesuffix)

       
    # first build up a complete anti list. Those values are removing during list building
    # this uses the antivalues string AND the antilist.csv
    emptylist = []
    antilist = csv_to_list("antilist",emptylist , "./userfiles/",1)
    
    antivaluelist = antivalues.split(",")

    antilist += antivaluelist

    # clean up antivalue list:
    antilist = [s.strip().lower() for s in antilist]

    

    # Some tricks for gender to make sure we can choose Him/Her/It etc on the right time.
    if(gender=="all"):
        genderchoicelist = ["male", "female"]
        gender = random.choice(genderchoicelist)
    heshelist = ["it"]
    hisherlist = ["its"]
    himherlist = ["it"]
    # we also need to oppositegender for some fun!
    oppositegender = "male"
    if(gender=="male"):
        oppositegender = "female"

    # build all lists here

    colorlist = csv_to_list("colors",antilist)
    animallist = csv_to_list("animals",antilist)    
    materiallist = csv_to_list("materials",antilist)
    objectlist = csv_to_list("objects",antilist)
    fictionallist = csv_to_list(csvfilename="fictional characters",antilist=antilist,skipheader=True,gender=gender)
    nonfictionallist = csv_to_list(csvfilename="nonfictional characters",antilist=antilist,skipheader=True,gender=gender)
    oppositefictionallist = csv_to_list(csvfilename="fictional characters",antilist=antilist,skipheader=True,gender=oppositegender)
    oppositenonfictionallist = csv_to_list(csvfilename="nonfictional characters",antilist=antilist,skipheader=True,gender=oppositegender)
    conceptsuffixlist = csv_to_list("concept_suffix",antilist)
    buildinglist = csv_to_list("buildings",antilist)
    vehiclelist = csv_to_list("vehicles",antilist)
    outfitlist = csv_to_list("outfits",antilist)
    locationlist = csv_to_list("locations",antilist)
    backgroundlist = csv_to_list("backgrounds",antilist)

    accessorielist = csv_to_list("accessories",antilist,"./csvfiles/",0,"?",False,False,gender)
    artmovementlist = csv_to_list("artmovements",antilist)
    bodytypelist = csv_to_list("body_types",antilist=antilist,skipheader=True,gender=gender)
    cameralist = csv_to_list("cameras",antilist)
    colorschemelist = csv_to_list("colorscheme",antilist)
    conceptprefixlist = csv_to_list("concept_prefix",antilist)
    culturelist = csv_to_list("cultures",antilist)
    descriptorlist = csv_to_list("descriptors",antilist)
    devmessagelist = csv_to_list("devmessages",antilist)
    directionlist = csv_to_list(csvfilename="directions",antilist=antilist,insanitylevel=insanitylevel)
    emojilist = csv_to_list("emojis",antilist)
    eventlist = csv_to_list("events",antilist)
    focuslist = csv_to_list(csvfilename="focus",antilist=antilist, insanitylevel=insanitylevel)
    greatworklist = csv_to_list("greatworks",antilist)
    haircolorlist = csv_to_list("haircolors",antilist)
    hairstylelist = csv_to_list("hairstyles",antilist)
    hairvomitlist = csv_to_list("hairvomit",antilist,"./csvfiles/",0,"?",False,False)
    
    humanoidlist = csv_to_list("humanoids",antilist)
    if(anime_mode or imagetype=="all - anime"):
        if(imagetype == "all"):
            imagetype = "all - anime"
        imagetypelist = csv_to_list(csvfilename="imagetypes_anime",antilist=antilist, insanitylevel=insanitylevel, delimiter="?")
    else:
        imagetypelist = csv_to_list(csvfilename="imagetypes",antilist=antilist, insanitylevel=insanitylevel, delimiter="?")

    joblist = csv_to_list(csvfilename="jobs",antilist=antilist,skipheader=True,gender=gender)
    lenslist = csv_to_list(csvfilename="lenses",antilist=antilist, insanitylevel=insanitylevel)
    lightinglist = csv_to_list(csvfilename="lighting",antilist=antilist, insanitylevel=insanitylevel)
    malefemalelist = csv_to_list(csvfilename="malefemale",antilist=antilist,skipheader=True,gender=gender)
    manwomanlist = csv_to_list(csvfilename="manwoman",antilist=antilist,skipheader=True,gender=gender)
    moodlist = csv_to_list(csvfilename="moods",antilist=antilist, insanitylevel=insanitylevel)
    othertypelist = csv_to_list("othertypes",antilist)
    poselist = csv_to_list("poses",antilist)
    qualitylist = csv_to_list("quality",antilist)
    shotsizelist = csv_to_list(csvfilename="shotsizes",antilist=antilist, insanitylevel=insanitylevel)
    timeperiodlist = csv_to_list("timeperiods",antilist)
    vomitlist = csv_to_list(csvfilename="vomit",antilist=antilist, insanitylevel=insanitylevel)
    if(anime_mode):
        replacements = {
        "-allstylessuffix-": "-buildfacepart-",
        "-artistdescription-": "-buildfacepart-"
        }

        for i, item in enumerate(vomitlist):
            for old, new in replacements.items():
                item = item.replace(old, new)
            vomitlist[i] = item
        

    foodlist = csv_to_list("foods", antilist)
    genderdescriptionlist = csv_to_list(csvfilename="genderdescription",antilist=antilist,skipheader=True,gender=gender)
    minilocationlist = csv_to_list("minilocations", antilist)
    minioutfitlist = csv_to_list("minioutfits",antilist,"./csvfiles/",0,"?",False,False,gender)
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
    manwomanmultiplelist = csv_to_list(csvfilename="manwomanmultiples",antilist=antilist,skipheader=True,gender=gender,delimiter="?")
    waterlocationlist = csv_to_list("waterlocations", antilist)
    containerlist = csv_to_list("containers", antilist)
    firstnamelist = csv_to_list(csvfilename="firstnames",antilist=antilist,skipheader=True,gender=gender)
    floralist = csv_to_list("flora", antilist)
    printlist = csv_to_list("prints", antilist)
    patternlist = csv_to_list("patterns", antilist)
    chairlist = csv_to_list("chairs", antilist)
    cardnamelist = csv_to_list("card_names", antilist)
    coveringlist = csv_to_list("coverings", antilist)
    facepartlist = csv_to_list("faceparts", antilist)
    outfitvomitlist = csv_to_list(csvfilename="outfitvomit",antilist=antilist,delimiter="?")
    humanvomitlist = csv_to_list("humanvomit", antilist)
    eyecolorlist = csv_to_list("eyecolors", antilist)
    fashiondesignerlist = csv_to_list("fashiondesigners", antilist)
    colorcombinationlist = csv_to_list("colorcombinations", antilist)
    materialcombinationlist = csv_to_list("materialcombinations", antilist)
    agelist = csv_to_list("ages", antilist)
    agecalculatorlist = csv_to_list("agecalculator", antilist)
    elementlist = csv_to_list("elements", antilist)
    settinglist = csv_to_list("settings", antilist)
    charactertypelist = csv_to_list("charactertypes", antilist)
    objectstoholdlist = csv_to_list("objectstohold", antilist)
    episodetitlelist = csv_to_list(csvfilename="episodetitles",antilist=antilist,skipheader=True)
    flufferlist = csv_to_list("fluff", antilist)
    tokenlist = []
    
    # New set of lists
    locationfantasylist = csv_to_list("locationsfantasy", antilist)
    locationscifilist = csv_to_list("locationsscifi", antilist)
    locationvideogamelist = csv_to_list("locationsvideogame", antilist)
    locationbiomelist = csv_to_list("locationsbiome", antilist)
    locationcitylist = csv_to_list("locationscities", antilist)
    birdlist = csv_to_list("birds", antilist)
    catlist = csv_to_list(csvfilename="cats", antilist=antilist,delimiter="?")
    doglist = csv_to_list(csvfilename="dogs", antilist=antilist,delimiter="?")
    insectlist = csv_to_list("insects", antilist)
    pokemonlist = csv_to_list("pokemon", antilist)
    pokemontypelist = csv_to_list("pokemontypes", antilist)
    occultlist = csv_to_list("occult", antilist)
    marinelifelist = csv_to_list("marinelife", antilist)
    

    # additional descriptor lists
    outfitdescriptorlist = csv_to_list("outfitdescriptors",antilist)
    hairdescriptorlist = csv_to_list("hairdescriptors",antilist)
    humandescriptorlist = csv_to_list("humandescriptors",antilist)
    locationdescriptorlist = csv_to_list("locationdescriptors",antilist)
    basicbitchdescriptorlist = csv_to_list("basicbitchdescriptors",antilist)
    animaldescriptorlist = csv_to_list("animaldescriptors",antilist)

    # descriptorlist becomes one with everything
    descriptortotallist = descriptorlist + outfitdescriptorlist + hairdescriptorlist + humandescriptorlist + locationdescriptorlist + basicbitchdescriptorlist + animaldescriptorlist
    # Deduplicate the list while preserving casings
    descriptorlist = []
    seen_items = set()

    for item in descriptortotallist:
        # Convert the item to lowercase to ignore casing
        item_lower = item.lower()
        
        if item_lower not in seen_items:
            seen_items.add(item_lower)
            descriptorlist.append(item)

    humanlist = fictionallist + nonfictionallist + humanoidlist
    objecttotallist = objectlist + buildinglist + vehiclelist + foodlist + spacelist + floralist + containerlist + occultlist
    outfitprinttotallist = objecttotallist + locationlist + colorlist + musicgenrelist + seasonlist + animallist + patternlist
    if(less_verbose):
        humanactivitycheatinglist = ["-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "-miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)"]
    else:
        humanactivitycheatinglist = ["OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)",
                                 "OR(;, -heshe- is;uncommon) -miniactivity- OR(in;at) a OR(-location-;-building-;-waterlocation-)"]
    
    # build artists list
    if artists == "wild":
        artists = "all (wild)"

    # we want to create more cohorence, so we are adding all (wild) mode for the old logic
    
    # all else will be more constrained per type, to produce better images.
    # the popular artists will be used more the lower the insanitylevel is
    # Future: add in personal artists lists as well
    
    # lets maybe go wild "sometimes", based on insanitylevel
    if(artists == "all" and rare_dist(insanitylevel)):
       artists = "all (wild)"
       originalartistchoice = artists

    artisttypes = ["popular", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema",	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
    artiststyleselector = ""
    artiststyleselectormode = "normal"
    if(artists == "all" and normal_dist(insanitylevel + 1)):
        artiststyleselector = random.choice(artisttypes)
        artists = artiststyleselector
    elif(artists == "all"):
        artiststyleselectormode = "custom"
         # then else maybe do nothing??
        if(random.randint(0,6) == 0 and onlyartists == False):
            generateartist = False
        # go popular! Or even worse, we go full greg mode!
        elif(common_dist(max(3,insanitylevel))):
            artists = "popular" 
        elif(random.randint(0,1) == 0):
            # only on lower instanity levels anyway
            if(insanitylevel < 6):
                #too much greg mode!
                
                artists = "greg mode"
            else:
                artists = "popular"
        else:
            artists = "none"

    else:
        artiststyleselectormode = "custom"



    artistlist = []
    # create artist list to use in the code, maybe based on category  or personal lists
    if(artists != "all (wild)" and artists != "all" and artists != "none" and artists.startswith("personal_artists") == False and artists.startswith("personal artists") == False and artists in artisttypes):
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
    portraitartistlist = artist_category_csv_to_list("artists_and_category","portrait")
    characterartistlist = artist_category_csv_to_list("artists_and_category","character")
    landscapeartistlist = artist_category_csv_to_list("artists_and_category","landscape")
    scifiartistlist = artist_category_csv_to_list("artists_and_category","sci-fi")
    graphicdesignartistlist = artist_category_csv_to_list("artists_and_category","graphic design")
    digitalartistlist = artist_category_csv_to_list("artists_and_category","digital")
    architectartistlist = artist_category_csv_to_list("artists_and_category","architecture")
    cinemaartistlist = artist_category_csv_to_list("artists_and_category","cinema")
    gregmodelist = csv_to_list("gregmode", antilist)


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
    customoutfitslist = csv_to_list("custom_outfits",antilist,"./userfiles/")

    # special lists
    backgroundtypelist = csv_to_list("backgroundtypes", antilist,"./csvfiles/special_lists/",0,"?")
    insideshotlist =  csv_to_list("insideshots", antilist,"./csvfiles/special_lists/",0,"?")
    photoadditionlist = csv_to_list("photoadditions", antilist,"./csvfiles/special_lists/",0,"?")
    if(less_verbose):
        buildhairlist = csv_to_list("buildhair_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        buildoutfitlist = csv_to_list("buildoutfit_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        humanadditionlist = csv_to_list("humanadditions_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        objectadditionslist = csv_to_list("objectadditions_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        buildfacelist = csv_to_list("buildface_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        buildaccessorielist = csv_to_list("buildaccessorie_less_verbose", antilist,"./csvfiles/special_lists/",0,"?")
        humanactivitylist = csv_to_list("human_activities_less_verbose",antilist,"./csvfiles/",0,"?",False,False)
        humanexpressionlist = csv_to_list("humanexpressions_less_verbose",antilist,"./csvfiles/",0,"?",False,False)
    else:
        buildhairlist = csv_to_list("buildhair", antilist,"./csvfiles/special_lists/",0,"?")
        buildoutfitlist = csv_to_list("buildoutfit", antilist,"./csvfiles/special_lists/",0,"?")
        humanadditionlist = csv_to_list("humanadditions", antilist,"./csvfiles/special_lists/",0,"?")
        objectadditionslist = csv_to_list("objectadditions", antilist,"./csvfiles/special_lists/",0,"?")
        buildfacelist = csv_to_list("buildface", antilist,"./csvfiles/special_lists/",0,"?")
        buildaccessorielist = csv_to_list("buildaccessorie", antilist,"./csvfiles/special_lists/",0,"?")
        humanactivitylist = csv_to_list("human_activities",antilist,"./csvfiles/",0,"?",False,False)
        humanexpressionlist = csv_to_list("humanexpressions",antilist,"./csvfiles/",0,"?",False,False)

    humanactivitylist = humanactivitylist + humanactivitycheatinglist

    animaladditionlist = csv_to_list("animaladditions", antilist,"./csvfiles/special_lists/",0,"?")
    
    minilocationadditionslist = csv_to_list("minilocationadditions", antilist,"./csvfiles/special_lists/",0,"?")
    overalladditionlist = csv_to_list("overalladditions", antilist,"./csvfiles/special_lists/",0,"?")
    imagetypemodelist = csv_to_list("imagetypemodes", antilist,"./csvfiles/special_lists/",0,"?")
    miniactivitylist = csv_to_list("miniactivity", antilist,"./csvfiles/special_lists/",0,"?")
    animalsuffixadditionlist = csv_to_list("animalsuffixadditions", antilist,"./csvfiles/special_lists/",0,"?")
    buildfacepartlist = csv_to_list("buildfaceparts", antilist,"./csvfiles/special_lists/",0,"?")
    conceptmixerlist = csv_to_list("conceptmixer", antilist,"./csvfiles/special_lists/",0,"?")
    
    
    tokinatorlist = csv_to_list("tokinator", antilist,"./csvfiles/templates/",0,"?")
    styleslist = csv_to_list("styles", antilist,"./csvfiles/templates/",0,"?")
    stylessuffix = [item.split('-subject-')[1] for item in styleslist]
    breakstylessuffix = [item.split(',') for item in stylessuffix]
    allstylessuffixlist = [value for sublist in breakstylessuffix for value in sublist]
    allstylessuffixlist = list(set(allstylessuffixlist))

    artistsuffix = artist_descriptions_csv_to_list("artists_and_category")
    breakartiststylessuffix = [item.split(',') for item in artistsuffix]
    artiststylessuffixlist = [value for sublist in breakartiststylessuffix for value in sublist]
    artiststylessuffixlist = list(set(artiststylessuffixlist))
    allstylessuffixlist += artiststylessuffixlist


    
    dynamictemplatesprefixlist = csv_to_list("dynamic_templates_prefix", antilist,"./csvfiles/templates/",0,"?")
    dynamictemplatessuffixlist = csv_to_list("dynamic_templates_suffix", antilist,"./csvfiles/templates/",0,"?")

       
    # subjects
    mainchooserlist = []
    objectwildcardlist = []
    locationwildcardlist = []
    animalwildcardlist = []
    hybridlist = []
    hybridhumanlist = []
    humanoidsubjectchooserlist = []
    eventsubjectchooserlist = []
    locationsubjectchooserlist = []
    addontolocationinsidelist = []
    addontolocationlist = []

    # load subjects stuff from config
    generatevehicle = True
    generateobject = True
    generatefood = True
    generatebuilding = True
    generatespace = True
    generateflora = True
    generateoccult = True
    generateconcept = True

    generateanimal = True
    generatebird = True
    generatecat = True
    generatedog = True
    generateinsect = True
    generatepokemon = True
    generatemarinelife = True


    generatemanwoman = True
    generatemanwomanrelation = True
    generatemanwomanmultiple = True
    generatefictionalcharacter = True
    generatenonfictionalcharacter = True
    generatehumanoids = True
    generatejob = True
    generatefirstnames = True

    generatelandscape = True
    generatelocation = True
    generatelocationfantasy = True
    generatelocationscifi = True
    generatelocationvideogame = True
    generatelocationbiome = True
    generatelocationcity = True

    generateevent = True
    generateconcepts = True
    generatepoemline = True
    generatesongline = True
    generatecardname = True
    generateepisodetitle = True

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
    buildfacechance = 'legendary'
    humanexpressionchance = 'rare'
    joboractivitychance = 'normal'
    humanvomitchance = 'rare'

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
        if item[0] == 'subject_occult' and item[1] != 'on':
            generateoccult = False
        # animals
        if item[0] == 'subject_animal' and item[1] != 'on':
            generateanimal = False
        if item[0] == 'subject_bird' and item[1] != 'on':
            generatebird = False
        if item[0] == 'subject_cat' and item[1] != 'on':
            generatecat = False
        if item[0] == 'subject_dog' and item[1] != 'on':
            generatedog = False
        if item[0] == 'subject_insect' and item[1] != 'on':
            generateinsect = False
        if item[0] == 'subject_pokemon' and item[1] != 'on':
            generatepokemon = False
        if item[0] == 'subject_marinelife' and item[1] != 'on':
            generatemarinelife = False
        # humanoids
        if item[0] == 'subject_manwoman' and item[1] != 'on':
            generatemanwoman = False
        if item[0] == 'subject_manwomanrelation' and item[1] != 'on':
            generatemanwomanrelation = False
        if item[0] == 'subject_manwomanmultiple' and item[1] != 'on':
            generatemanwomanmultiple = False
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
        if item[0] == 'subject_location' and item[1] != 'on':
            generatelocation = False
        if item[0] == 'subject_location_fantasy' and item[1] != 'on':
            generatelocationfantasy = False
        if item[0] == 'subject_location_scifi' and item[1] != 'on':
            generatelocationscifi = False
        if item[0] == 'subject_location_videogame' and item[1] != 'on':
            generatelocationvideogame = False
        if item[0] == 'subject_location_biome' and item[1] != 'on':
            generatelocationbiome = False
        if item[0] == 'subject_location_city' and item[1] != 'on':
            generatelocationcity = False
        # concept
        if item[0] == 'subject_event' and item[1] != 'on':
            generateevent = False
        if item[0] == 'subject_concept' and item[1] != 'on':
            generateconcepts = False
        if item[0] == 'subject_poemline' and item[1] != 'on':
            generatepoemline = False
        if item[0] == 'subject_songline' and item[1] != 'on':
            generatesongline = False
        if item[0] == 'subject_cardname' and item[1] != 'on':
            generatecardname = False
        if item[0] == 'subject_episodetitle' and item[1] != 'on':
            generateepisodetitle = False
        
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
        if item[0] == 'buildfacechance':
            buildfacechance = item[1]
        if item[0] == 'humanexpressionchance':
            humanexpressionchance = item[1]
        if item[0] == 'humanvomitchance':
            humanvomitchance = item[1]
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
    generateoccult = bool(occultlist) and generateoccult
    generateobject = generatevehicle or generateobject or generatefood or generatebuilding or generatespace or generateflora or generateoccult
    

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

    if(generateoccult):
        objectwildcardlist.append("-occult-")
        hybridlist.append("-occult-")
        addontolocationlist.append("-occult-")
    
    if(generateobject):
        mainchooserlist.append("object")

    if(generatelandscape):
        mainchooserlist.append("landscape")
    
    if(generatelocationfantasy):
        locationwildcardlist.append("-locationfantasy-")
    
    if(generatelocationscifi):
        locationwildcardlist.append("-locationscifi-")
    
    if(generatelocationvideogame):
        locationwildcardlist.append("-locationvideogame-")
    
    if(generatelocationbiome):
        locationwildcardlist.append("-locationbiome-")
    
    if(generatelocationcity):
        locationwildcardlist.append("-locationcity-")
    
    if(generatelocation):
        locationwildcardlist.append("-location-")

    if(generateanimal):
        animalwildcardlist.append("-animal-")

    if(generatebird):
        animalwildcardlist.append("-bird-")
    
    if(generatecat):
        animalwildcardlist.append("-cat-")

    if(generatedog):
        animalwildcardlist.append("-dog-")

    if(generateinsect):
        animalwildcardlist.append("-insect-")

    if(generatepokemon):
        animalwildcardlist.append("-pokemon-")
    
    if(generatemarinelife):
        animalwildcardlist.append("-marinelife-")

    generatefictionalcharacter = bool(fictionallist) and generatefictionalcharacter
    generatenonfictionalcharacter = bool(nonfictionallist) and generatenonfictionalcharacter
    generatehumanoids = bool(humanoidlist) and generatehumanoids
    generatemanwoman = bool(manwomanlist) and generatemanwoman
    generatemanwomanrelation = bool(manwomanrelationlist) and generatemanwomanrelation
    generatemanwomanmultiple = bool(manwomanmultiplelist) and generatemanwomanmultiple
    generatejob = bool(joblist) and generatejob
    generatefirstnames = bool(firstnamelist) and generatefirstnames
    generatehumanoid = generatefictionalcharacter or generatenonfictionalcharacter or generatehumanoids or generatemanwoman or generatejob or generatemanwomanrelation or generatefirstnames or generatemanwomanmultiple


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
    
    if(generatemanwomanmultiple):
        humanoidsubjectchooserlist.append("manwomanmultiple")

    if(generatejob):
        humanoidsubjectchooserlist.append("job")
   
    if(generatehumanoid):
        mainchooserlist.append("humanoid")

    if(generatefirstnames):
        humanoidsubjectchooserlist.append("firstname")
    
    
    generateanimal = bool(animallist) and generateanimal
    generatebird = bool(birdlist) and generatebird
    generatecat = bool(catlist) and generatecat
    generatedog = bool(doglist) and generatedog
    generateinsect = bool(insectlist) and generateinsect
    generatepokemon = bool(pokemonlist) and generatepokemon
    generatemarinelife = bool(marinelifelist) and generatemarinelife

    generateanimaltotal = generateanimal or generatebird or generatecat or generatedog or generateinsect or generatepokemon or generatemarinelife

    if(generateanimal):
        hybridlist.append("-animal-")
    if(generatebird):
        hybridlist.append("-bird-")
    if(generatecat):
        hybridlist.append("-cat-")
    if(generatedog):
        hybridlist.append("-dog-")
    if(generateinsect):
        hybridlist.append("-insect-")
    if(generatepokemon):
        hybridlist.append("-pokemon-")

    if(generatemarinelife):
        hybridlist.append("-marinelife-")

    if(generateanimaltotal):
        mainchooserlist.append("animal")

    generatelocation = bool(locationlist) and generatelocation
    generatelocationfantasy = bool(locationfantasylist) and generatelocationfantasy
    generatelocationscifi = bool(locationscifilist) and generatelocationscifi
    generatelocationvideogame = bool(locationvideogamelist) and generatelocationvideogame
    generatelocationbiome = bool(locationbiomelist) and generatelocationbiome
    generatelocationcity = bool(locationcitylist) and generatelocationcity
    generatelandscape = generatelocation or generatelocationfantasy or generatelocationscifi or generatelocationvideogame or generatelocationbiome or generatelocationcity

    if(generatelandscape):
        addontolocationlist.append("-location-")
        addontolocationlist.append("-background-")
        addontolocationinsidelist.append("-location-")
        addontolocationinsidelist.append("-background-")
        locationsubjectchooserlist.append("landscape")
    
    if(generatelocation):
        locationsubjectchooserlist.append("location")
    if(generatelocationfantasy):
        locationsubjectchooserlist.append("fantasy location")
    if(generatelocationscifi):
        locationsubjectchooserlist.append("sci-fi location")
    if(generatelocationvideogame):
        locationsubjectchooserlist.append("videogame location")
    if(generatelocationbiome):
        locationsubjectchooserlist.append("biome")
    if(generatelocationcity):
        locationsubjectchooserlist.append("city")
    
    generateevent = bool(eventlist) and generateevent
    generateconcepts = bool(conceptprefixlist) and bool(conceptsuffixlist) and generateconcepts
    generatepoemline = bool(poemlinelist) and generatepoemline 
    generatesongline = bool(songlinelist) and generatesongline
    generatecardname = bool(cardnamelist) and generatecardname
    generateepisodetitle = bool(episodetitlelist) and generateepisodetitle
    


    generateconcept = generateevent or generateconcepts or generatepoemline or generatesongline

    if(generateevent):
        eventsubjectchooserlist.append("event")
    
    if(generateconcepts):
        eventsubjectchooserlist.append("concept")

    if(generatepoemline):
        eventsubjectchooserlist.append("poemline")
    
    if(generatesongline):
        eventsubjectchooserlist.append("songline")
    
    if(generatecardname):
        eventsubjectchooserlist.append("cardname")

    if(generateepisodetitle):
        eventsubjectchooserlist.append("episodetitle")

    if(generateconcept):
        mainchooserlist.append("concept")



    # determine wether we have a special mode or not
    if(random.randint(1,int(imagemodechance)) == 1 and (imagetype == "all" or imagetype == "all - anime") and giventypeofimage == "" and onlyartists == False):
        if(less_verbose):
            imagetypemodelist.remove("dynamic templates mode")
        if(anime_mode):
            imagetypemodelist.remove("only templates mode")
            imagetypemodelist.remove("massive madness mode")
            imagetypemodelist.remove("fixed styles mode")
            imagetypemodelist.remove("unique art mode")
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
    thetokinatormode = False
    dynamictemplatesmode = False
    artifymode = False

    # determine wether we should go for a template or not. Not hooked up to insanitylevel
    if(imagetype == "only templates mode"):
        specialmode = True
        templatemode = True
        print("Running with a randomized template instead of a randomized prompt")

    if(imagetype == "art blaster mode"):
        specialmode = True
        if(uncommon_dist(insanitylevel)):
            artblastermode = True
        elif(bool(artistlist)):
            onlysubjectmode = True
            artifymode = True
        else:
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

    if(imagetype == "the tokinator"):
        specialmode = True
        thetokinatormode = True
        # for performance, load the list here
        tokenlist = csv_to_list(csvfilename="tokens",antilist=antilist,skipheader=True)
        print("Running with a completely random set of words")
        print("All safety and logic is turned off")

    if(imagetype == "dynamic templates mode"):
        specialmode = True
        dynamictemplatesmode = True
        print("Running with dynamic templates mode")

    # just for testing, you can't choose this. Artify runs through Art Blaster instead.
    if(imagetype == "artify mode"):
        specialmode = True
        onlysubjectmode = True
        artifymode = True
        print("Running with artify mode")

    # main stuff
    generatetype = not specialmode
    generatesubject = not templatemode
    if(thetokinatormode):
        generatesubject = False

    # normals
    generateartist = bool(artistlist) and not specialmode
    if(thetokinatormode):
        generateartist = bool(artistlist)
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
    generatevomit = bool(vomitlist) and not specialmode and add_vomit
    generatequality = bool(qualitylist) and not specialmode and add_quality
    generateshot = bool(shotsizelist) and not specialmode
    generatetimeperiod = bool(timeperiodlist) and not specialmode
    generateemoji = bool(emojilist) and not templatemode
    generateface = bool(buildfacelist) and not specialmode
    generatehumanexpression = bool(humanexpressionlist) and not specialmode
    generatehumanvomit = bool(humanvomitlist) and not specialmode

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
    generatecardname = bool(cardnamelist) and not specialmode
    generateepisodetitle = bool(episodetitlelist) and not specialmode
    
    generateminilocationaddition = bool(minilocationadditionslist) and not specialmode
    generateminivomit = bool(minivomitlist) and not specialmode and add_vomit
    generateimagetypequality = bool(imagetypequalitylist) and not specialmode and generateimagetypequality 
    generateoveralladdition = bool(overalladditionlist) and not specialmode
    generateimagetype = bool(imagetypelist) and not specialmode and generateimagetype


    # Smart subject logic
    givensubjectlist = []
    
    if(givensubject != "" and smartsubject == True):
        givensubject = givensubject.lower()
    
        # Remove any list that has a matching word in the list
        # Remove any list/logic with keywords, such as:
        # wearing, bodytype, pose, location, hair, background

        # use function to split up the words
        givensubjectlist = split_prompt_to_words(givensubject)

        # Check only for the lists that make sense?
        
        # outfit
        foundinlist = any(word.lower() in [item.lower() for item in outfitlist] for word in givensubjectlist)
        keywordslist = ["wearing","outfit", "dressed"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generateoutfit = False
        
        # bodytype
        foundinlist = any(word.lower() in [item.lower() for item in bodytypelist] for word in givensubjectlist)
        keywordslist = ["bodytype","body type","model"]
        keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        if(foundinlist == True or keywordsinstring == True):
            generatebodytype = False

        # hair
        foundinlist = any(word.lower() in [item.lower() for item in hairstylelist] for word in givensubjectlist)
        keywordslist = ["hair","hairstyle"]
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
        keywordslist = ["location","background", "inside", "at the", "in a"]
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


    # given subject subject override :p
    subjectingivensubject = False
    if("subject" in list(map(str.lower, givensubjectlist)) and smartsubject == True):
        givensubjectpromptlist = givensubject.split("subject")
        subjectingivensubject = True

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
        buildingfullmode = False
        subjectchooser = ""
        mainchooser = ""
      
        #completeprompt += prefixprompt

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
            elif(givensubject != "" and subjectingivensubject == False):
                completeprompt += chosentemplate.replace("-subject-",givensubject )
            elif(givensubject != "" and subjectingivensubject == True):
                completeprompt += chosentemplate.replace("-subject-", givensubjectpromptlist[0] + " " + templatesubjects[templateindex] + " " + givensubjectpromptlist[1])



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

        # ["popular", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
    
        # Some new logic, lets base the main chooser list on the chosen art category, to make it more cohorent
        # first for humanoids
        artiststylelistforchecking = ["popular", "3D",	"anime"	"art nouveau",	"art deco",	"character", "fantasy",	"fashion", "manga", "photography","portrait","sci-fi"]
        if((artiststyleselector in artiststylelistforchecking
           or artists in artiststylelistforchecking)
           and (forcesubject == "all" or forcesubject == "")):

            # remove the shizzle based on chance?
            # we want it to be MORE diverce when the insanity level raises
            # in this case, raise the chance for a humanoid, gets more wierd when going above 5

            if(random.randint(0,6) > max(2,insanitylevel -2) and "concept" in mainchooserlist):
                mainchooserlist.remove("concept")
            if(random.randint(0,6) > max(2,insanitylevel -2) and "landscape" in mainchooserlist):
                mainchooserlist.remove("landscape")
            if(random.randint(0,6) > max(2,insanitylevel -2) and "object" in mainchooserlist):
                mainchooserlist.remove("object")
            if(random.randint(0,6) > max(2,insanitylevel -2) and "animal" in mainchooserlist):
                mainchooserlist.remove("animal")
        
        # second for landscapes
        # Some new logic, lets base the main chooser list on the chosen art category, to make it more cohorent
        artiststylelistforchecking = ["architecture","bauhaus", "cityscape", "cinema", "cloudscape","impressionism",	"installation",	"landscape","magical realism",	"nature", "romanticism","seascape",	"space",	"streetscape"]
    
        if((artiststyleselector in artiststylelistforchecking
           or artists in artiststylelistforchecking)
           and (forcesubject == "all" or forcesubject == "")):
 
            # remove the shizzle based on chance?
            # we want it to be MORE diverce when the insanity level raises
            # in this case, raise the chance for a landscape, gets more wierd when going above 5
            if(random.randint(0,6) > max(2,insanitylevel -2) and "concept" in mainchooserlist):
                mainchooserlist.remove("concept")
            if(random.randint(0,6) > max(2,insanitylevel -2) and "animal" in mainchooserlist):
                mainchooserlist.remove("animal")
            if(random.randint(0,6) > max(2,insanitylevel -2) and "object" in mainchooserlist):
                mainchooserlist.remove("object")
            if(random.randint(0,8) > max(2,insanitylevel -2) and "humanoid" in mainchooserlist):
                mainchooserlist.remove("humanoid")

        #focus in animemode on mostly humans
        if(anime_mode  and (forcesubject == "all" or forcesubject == "")):
            if(random.randint(0,11) > max(2,insanitylevel -2) and "concept" in mainchooserlist):
                mainchooserlist.remove("concept")
            if(random.randint(0,11) > max(2,insanitylevel -2) and "landscape" in mainchooserlist):
                mainchooserlist.remove("landscape")
            if(random.randint(0,11) > max(2,insanitylevel -2) and "object" in mainchooserlist):
                mainchooserlist.remove("object")
            if(random.randint(0,8) > max(2,insanitylevel -2) and "animal" in mainchooserlist):
                mainchooserlist.remove("animal")
    

        # choose the main subject type
        mainchooser = random.choice(mainchooserlist)
        
        if(forcesubject != "" and forcesubject != "all"):
            mainchooser = forcesubject    
        # 0 object, 1 animal, 2 animal as human, 3 ManWoman, 4 Job, 5 fictional, 6 non fictional, 7 humanoid, 8 landscape, 9 event
        if(mainchooser == "object"):
            subjectchooser = "object"
        if(mainchooser == "animal" and (random.randint(0,5) == 5 or anime_mode)):
            # sometimes interpret the animal as a human
            # for anime_mode this is always true
            animalashuman = True
        if(mainchooser == "humanoid"):
            #humanoidsubjectchooserlist = ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "firstname"]
            # Lets put generic humans as a more 'normal' value. Manwoman relation as the least picked.
            # balanced around 5, to have more normal man/woman
            # lower values even more stable
            # Upper values are still quite random
            humanoidsubjectchooserlistbackup = humanoidsubjectchooserlist.copy() # make a backup of the list
            if(random.randint(0,20) > max(2,insanitylevel -2) and "manwomanrelation" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("manwomanrelation")
            if(random.randint(0,30) > max(2,insanitylevel -2) and "manwomanmultiple" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("manwomanmultiple")
            if(random.randint(0,7) > max(2,insanitylevel -2) and "firstname" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("firstname")
            if(random.randint(0,5) > max(2,insanitylevel -2) and "job" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("job")
            if(random.randint(0,5) > max(2,insanitylevel -2) and "fictional" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("fictional")
            if(random.randint(0,5) > max(2,insanitylevel -2) and "non fictional" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("non fictional")
            if(random.randint(0,5) > max(2,insanitylevel -2) and "humanoid" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("humanoid")
            # more random stuff on higher levels
            if(random.randint(0,4) > max(2,insanitylevel -2) and "human" in humanoidsubjectchooserlist):
                humanoidsubjectchooserlist.remove("human")

            # if we accidently remove everything, then restore the backup list
            if(not bool(humanoidsubjectchooserlist)):
                humanoidsubjectchooserlist = humanoidsubjectchooserlistbackup
                        
            subjectchooser = random.choice(humanoidsubjectchooserlist)
            
            
            
            if(subtypehumanoid != "all"):
                if(subtypehumanoid == "generic humans"):
                    subjectchooser = "human"
                elif(subtypehumanoid == "generic human relations"):
                    subjectchooser = "manwomanrelation"
                elif(subtypehumanoid == "multiple humans"):
                    subjectchooser = "manwomanmultiple"
                elif(subtypehumanoid == "celebrities e.a."):
                    subjectchooser = "non fictional"
                elif(subtypehumanoid == "fictional characters"):
                    subjectchooser = "fictional"
                elif(subtypehumanoid == "humanoids"):
                    subjectchooser = "humanoid"
                elif(subtypehumanoid == "based on job or title"):
                    subjectchooser = "job"
                elif(subtypehumanoid == "based on first name"):
                    subjectchooser = "firstname"
                else:
                    subjectchooser = subtypehumanoid
        if(mainchooser == "landscape"):
            subjectchooser = random.choice(locationsubjectchooserlist)

        if(mainchooser == "concept"):
            #eventsubjectchooserlist = ["event", "concept", "poemline", "songline"]
            subjectchooser = random.choice(eventsubjectchooserlist)
            if(subtypeconcept != "all"):
                if(subtypeconcept == "event"):
                    subjectchooser = "event"
                elif(subtypeconcept == "the X of Y concepts"):
                    subjectchooser = "concept"
                elif(subtypeconcept == "lines from poems"):
                    subjectchooser = "poemline"
                elif(subtypeconcept == "lines from songs"):
                    subjectchooser = "songline"
                elif(subtypeconcept == "names from card based games"):
                    subjectchooser = "cardname"
                elif(subtypeconcept == "episode titles from tv shows"):
                    subjectchooser = "episodetitle"
                elif(subtypeconcept == "concept mixer"):
                    subjectchooser = "conceptmixer"
                else:
                    subjectchooser = subtypeconcept

        # After we chose the subject, lets set all things ready for He/She/It etc
        
        if(not less_verbose and subjectchooser in ["manwomanmultiple"] and givensubject != "" and subtypehumanoid != "multiple humans"):
            heshelist = ["they"]
            hisherlist = ["their"]
            himherlist = ["them"]
            # on rare occasions do "one of them"
            if(random.randint(0,20) == 0):
                heshelist = ["one of them"]
                hisherlist = ["one of their"]
                himherlist = ["one of them"]
        elif(not less_verbose and subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","firstname","manwomanmultiple"]):
            if(gender == "male"):
                heshelist = ["he"]
                hisherlist = ["his"]
                himherlist = ["him"]
            if(gender == "female"):
                heshelist = ["she"]
                hisherlist = ["her"]
                himherlist = ["her"]
        if(not less_verbose and subjectchooser in ["manwomanmultiple"] and givensubject == ""):
            heshelist = ["they"]
            hisherlist = ["their"]
            himherlist = ["them"]
            # on rare occasions do "one of them"
            if(random.randint(0,20) == 0):
                heshelist = ["one of them"]
                hisherlist = ["one of their"]
                himherlist = ["one of them"]
        



           
        
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
                if(uncommon_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artiststyle-, "
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
                if(unique_dist(insanitylevel) and bool(artistlist)):
                    completeprompt += "-artistdescription-, "
                
                step = step + 1 

        # start quality vomit here
        if(qualityvomitmode==True):
            step = 0
            end = random.randint(1, insanitylevel) + 1
            while step < end:
                if(uncommon_dist(insanitylevel) and bool(vomitlist)):
                    completeprompt += "-vomit-, "
                if(uncommon_dist(insanitylevel) and bool(flufferlist)):
                    completeprompt += "-fluff-, "
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
                if(unique_dist(insanitylevel) and bool(allstylessuffixlist)):
                    completeprompt += "-allstylessuffix-, "
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
                    completeprompt += "-photoaddition-, "
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
            


        # start styles mode here
        if(stylesmode == True):
            chosenstyle = random.choice(styleslist)
            chosenstyleprefix = chosenstyle.split("-subject-")[0]
            chosenstylesuffix = chosenstyle.split("-subject-")[1]
            completeprompt += chosenstyleprefix

        if(dynamictemplatesmode == True):
            if(artists == "none"):
                dynamictemplatesprefixlist = [sentence for sentence in dynamictemplatesprefixlist if "-artist-" not in sentence.lower()]
            chosenstyleprefix = random.choice(dynamictemplatesprefixlist)
            completeprompt += chosenstyleprefix
            if(chosenstyleprefix[-1] == "."):
                completeprompt += " OR(Capturing a; Describing a;Portraying a;Featuring a)"
            else:
                completeprompt += " OR(with a;capturing a; describing a;portraying a;of a;featuring a)"


        # start artist part


        artistsplacement = "front"
        # remove the artistsatbackchange to be depended on the insanitylevel, we would like this to be a set chance
        if(random.randint(0, 2) == 0 and onlyartists == False):
            artistlocations = ["back", "middle"]
            artistsplacement = random.choice(artistlocations)

        if(artists != "none" and artistsplacement == "front" and generateartist == True):
            doartistnormal = True
            if(artists == "greg mode"):
                artistbylist = ["art by", "designed by", "stylized by", "by"]
                completeprompt += random.choice(artistbylist) + " -gregmode-, "
                doartistnormal = False
            # in case we have ALL, we can also do a specific artist mode per chosen subject. sometimes
            elif(originalartistchoice == "all" and random.randint(0,3) == 0):
                if(mainchooser in ["humanoid", "animal"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-portraitartist-;-characterartist-), OR(-portraitartist-;-characterartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(mainchooser in ["landscape"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-digitalartist-), OR(-landscapeartist-;-graphicdesignartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(subjectchooser in ["building"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-architectartist-), OR(-landscapeartist-;-architectartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                # else sometimes to something like this?
                elif(random.randint(0,5) == 0):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-portraitartist-;-characterartist-;-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-), OR(-portraitartist-;-characterartist-;-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-) and OR(-portraitartist-;-characterartist-;-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-)"
                    doartistnormal = False



            if(doartistnormal):
                    
                # take 1-3 artists, weighted to 1-2
                step = random.randint(0, 1)
                minstep = step
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
                    if(normal_dist(insanitylevel) and remove_weights == False):
                        isweighted = 1
                    
                    if isweighted == 1:
                        completeprompt += " ("

                    #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
                    if(step == minstep):
                        # sometimes do this
                        if(giventypeofimage=="" and imagetype == "all" and random.randint(0, 1) == 0):
                            if(artiststyleselectormode == "normal"):
                                completeprompt += artiststyleselector + " art "
                            else:
                                completeprompt += "-artiststyle- art "
                        artistbylist = ["art by", "designed by", "stylized by", "by"]
                    else:
                        artistbylist = [""]
                    completeprompt += random.choice(artistbylist) + " -artist-"
                    
                    if isweighted == 1:
                        completeprompt += ":" + str(1 + (random.randint(-3,3)/10)) + ")"       
                    
                    if artistmode in ["hybrid"] and not end - step == 1:
                        completeprompt += "|"
                    if artistmode in ["switching"] and not end - step == 1:
                        completeprompt += ":"
                    
                    if artistmode not in ["hybrid", "switching"]and not end - step > 1:
                        completeprompt += ","
                    elif artistmode not in ["hybrid", "switching"]and not end - step == 1:
                        completeprompt += " and "
                    
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
                #Parse or statements
                completeprompt = parse_custom_functions(completeprompt, insanitylevel)

                # replace artist wildcards
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-artist-", artistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-gregmode-", gregmodelist, False, False)

                completeprompt = replacewildcard(completeprompt, insanitylevel, "-fantasyartist-", fantasyartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-popularartist-", popularartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-romanticismartist-", romanticismartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-photographyartist-", photographyartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-portraitartist-", portraitartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-characterartist-", characterartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-landscapeartist-", landscapeartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-scifiartist-", scifiartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-graphicdesignartist-", graphicdesignartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-digitalartist-", digitalartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-architectartist-", architectartistlist, False, False)
                completeprompt = replacewildcard(completeprompt, insanitylevel, "-cinemaartist-", cinemaartistlist, False, False)
                    
                # clean it up
                completeprompt = cleanup(completeprompt, advancedprompting, insanitylevel)

                print("only generated these artists:" + completeprompt)
                return completeprompt


            completeprompt += ", "

            
            # sometimes do this as well
            if(giventypeofimage=="" and imagetype == "all" and random.randint(0, 2) == 0):
                completeprompt += "-artiststyle- art, "


            if artistmode in ["enhancing"]:
                completeprompt += " ["
        

        # start tokinator here
        if(thetokinatormode == True):
            tokinatorsubtype = ["personification", "human form", "object", "landscape", "OR(creature;beast;animal;myth;concept;world;planet)", "building", "location", "shape", "being", "-token-"]
            if(anime_mode and gender == "male"):
                tokinatorsubtype = ["(1boy, solo)"]
            if(anime_mode and gender == "female"):
                tokinatorsubtype = ["(1girl, solo)"]
            if(chance_roll(insanitylevel,"normal")):
                if(chance_roll(insanitylevel,"normal") and remove_weights == False):
                    completeprompt += "(OR(;-imagetypequality-;uncommon) OR(-imagetype-;-othertype-;rare):1.3) "
                else:
                    completeprompt += "OR(;-imagetypequality-;uncommon) OR(-imagetype-;-othertype-;rare) "
            completeprompt += random.choice(tokinatorlist)
            completeprompt = completeprompt.replace("-tokensubtype-", random.choice(tokinatorsubtype))

            if("subject" in givensubject and smartsubject):
                givensubject = givensubject.replace("subject", "-token-")

            if(givensubject == "" and overrideoutfit == ""):
                completeprompt = completeprompt.replace("-subject-", "-token-")
            elif(givensubject == "" and overrideoutfit != "" and "-outfit-" not in completeprompt):
                completeprompt = completeprompt.replace("-subject-", "-token- wearing a OR(-token-;;normal) -outfit-")
            elif(givensubject != "" and overrideoutfit != "" and "-outfit-" not in completeprompt):
                completeprompt = completeprompt.replace("-subject-", givensubject + " wearing a OR(-token-;;normal) -outfit-")
            else:
                completeprompt = completeprompt.replace("-subject-", givensubject)
            
            if(overrideoutfit == ""):
                completeprompt = completeprompt.replace("-outfit-", "-token-")
            else:
                completeprompt = completeprompt.replace("-outfit-", overrideoutfit)

            


        # start image type
        if(giventypeofimage == "" and (imagetype == "none" or giventypeofimage=="none") ):
           generatetype = False
        if(giventypeofimage=="" and generatetype == True):
            if(imagetype != "all" and imagetype != "all - force multiple" and imagetype != "only other types" and imagetype != "all - anime"):
                 
                    completeprompt += " " + imagetype + ", "
            elif(imagetype == "all - force multiple" or unique_dist(insanitylevel) and not anime_mode):
                amountofimagetypes = random.randint(2,3)
            elif(imagetype == "only other types"):
                if(amountofimagetypes < 2 and random.randint(0,2) == 0):
                        partlystylemode = True
                        print("Ohhh! Adding some secret sauce to this prompt")
                        chosenstyle = random.choice(styleslist)
                        chosenstyleprefix = chosenstyle.split("-subject-")[0]
                        chosenstylesuffix = chosenstyle.split("-subject-")[1]

                        completeprompt += " " + chosenstyleprefix + ", "
                else:
                    othertype = 1
                    completeprompt += random.choice(othertypelist)
            
            if((imagetype == "all" or imagetype == "all - anime") and chance_roll(insanitylevel, imagetypechance) and amountofimagetypes <= 1):
                amountofimagetypes = 1

            # on lower insanity levels, almost force this
            if((imagetype == "all" or imagetype == "all - anime") and insanitylevel <= 3 and amountofimagetypes <= 1 and random.randint(0,1)== 0):
                amountofimagetypes = 1

            if((imagetype == "all" or imagetype == "all - anime") and insanitylevel <= 2 and amountofimagetypes <= 1):
                amountofimagetypes = 1


            
            

            for i in range(amountofimagetypes):
            # one in 6 images is a complex/other type
                if((chance_roll(insanitylevel, imagetypequalitychance) or originalartistchoice == "greg mode") and generateimagetypequality):
                    completeprompt += "-imagetypequality- "
              
                if(imagetype == "all - anime" and not anime_mode):
                    completeprompt += " anime"
                if(random.randint(0,4) < 4 and insanitylevel > 3 ):
                    # woops, never to this as wildcards. We need to know as early as possible wether something is a photo. Lets put it back!
                    completeprompt += " " + random.choice(imagetypelist) + ", "
                elif(random.randint(0,1) == 0 and insanitylevel <= 3):
                    completeprompt += " " + random.choice(imagetypelist) + ", "
                elif(not anime_mode):
                    if(amountofimagetypes < 2 and random.randint(0,1) == 0):
                        partlystylemode = True
                        print("Ohhh! Adding some secret sauce to this prompt")
                        chosenstyle = random.choice(styleslist)
                        chosenstyleprefix = chosenstyle.split("-subject-")[0]
                        chosenstylesuffix = chosenstyle.split("-subject-")[1]

                        completeprompt += " " + chosenstyleprefix + ", "
                    else:
                        othertype = 1
                        completeprompt += " " + random.choice(othertypelist) + ", "
            
            if(othertype==1):
                completeprompt += " of a "
            else:
                completeprompt += ", "
        elif(generatetype == True):
            othertype = 1
            completeprompt += giventypeofimage + " of a "


        ## do less insane stuff while working for superprompter
        if(superprompter == True):
            insanitylevel = max(1, insanitylevel-4)
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
        elif("portrait" in completeprompt and generateshot == True and partlystylemode == False):
            completeprompt += " , close up of a "
        elif(mainchooser in ["landscape"] and generateshot == True and partlystylemode == False):
            completeprompt += " landscape of a "
        elif(generateshot == True): 
            completeprompt += ", "
    
        genjoboractivity = False
        # start subject building

        # divider between subject and everything else
        completeprompt += " @@@ "

 
        if(generatesubject == True):
        # start with descriptive qualities
            
            # outfit in front mode?
            # outfitmode = 0 = NO
            # outfitmode = 1 IN FRONT
            # outfitmode = 2 IS NORMAL
            if(overrideoutfit!=""):
                outfitmode = 2
            if(animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple", "firstname"]  and chance_roll(insanitylevel, outfitchance) and generateoutfit == True and humanspecial != 1):
                if(random.randint(0,10)==0):
                    outfitmode = 1
                else:
                    outfitmode = 2
            
            if(outfitmode == 1):
                completeprompt += "OR(wearing;dressed in;in;normal) OR(;OR(;a very;rare) -outfitdescriptor-;normal) OR(;-color-;uncommon) OR(;-culture-;uncommon) OR(;-material-;rare) -outfit-, "
                if(extraordinary_dist(insanitylevel)):
                    completeprompt += " -outfitvomit-, "
            


            if(subjectingivensubject):
                completeprompt += " " + givensubjectpromptlist[0] + " "

            # Once in a very rare while, we get a ... full of ...s
            if(novel_dist(insanitylevel) and (animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","firstname"])):         
                buildingfullmode = True
                insideshot = 1
                heshelist = ["they"]
                hisherlist = ["their"]
                himherlist = ["them"]
                completeprompt += "a OR(-building-;-location-;-waterlocation-;-container-;-background-;rare) full of "


            # Sometimes the descriptors are at the back, in more natural language. Lets determine.
            descriptorsintheback = random.randint(0,2)
            if(descriptorsintheback < 2):
                # Common to have 1 description, uncommon to have 2
                if(chance_roll(insanitylevel, subjectdescriptor1chance) and generatedescriptors == True):
                    if(animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"]):
                        if(anime_mode and random.randint(0,2)<2):
                            completeprompt += "-basicbitchdescriptor- "
                        else:
                            completeprompt += "-humandescriptor- "
                    elif(mainchooser == "landscape"):
                        completeprompt += "-locationdescriptor- "
                    elif(mainchooser == "animal"):
                        completeprompt += "-animaldescriptor- "
                    else:
                        completeprompt += "-descriptor- "

                if(chance_roll(insanitylevel, subjectdescriptor2chance) and generatedescriptors == True):
                    if(animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"]):
                        if(anime_mode and random.randint(0,2)<2):
                            completeprompt += "-basicbitchdescriptor- "
                        else:
                            completeprompt += "-humandescriptor- "
                    elif(mainchooser == "landscape"):
                        completeprompt += "-locationdescriptor- "
                    elif(mainchooser == "animal"):
                        completeprompt += "-animaldescriptor- "
                    else:
                        completeprompt += "-descriptor- "
            
            # color, for animals, landscape, objects and concepts
            if(mainchooser in ["animal", "object", "landscape", "concept"] and unique_dist(insanitylevel)):
                completeprompt += " OR(-color-;-colorcombination-) "
            
            # age, very rare to add.
            if(subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"] and extraordinary_dist(insanitylevel)):
                completeprompt += str(random.randint(20,99)) + " OR(y.o.;year old) "

            if((animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"]) and chance_roll(insanitylevel, subjectbodytypechance) and generatebodytype == True):
                completeprompt += "-bodytype- "

            if((animalashuman or subjectchooser in ["object","human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"]) and chance_roll(insanitylevel, subjectculturechance) and generatedescriptors == True):
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
                    # not varied enough
                    #if(subtypeobject == "occult"):
                    #    objectwildcardlist = ["-occult-"]
                    subjectchooser = subtypeobject

                
                # if we have a given subject, we should skip making an actual subject
                # unless we have "subject" in the given subject
                

                if(givensubject == "" or (subjectingivensubject and givensubject != "")):

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

            if(mainchooser == "animal"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                if(anime_mode 
                   and "1girl" not in givensubject
                   and "1boy" not in givensubject):
                    anthrolist = ["anthro", "anthrophomorphic", "furry"]
                
                        
                    if(gender=="male"):
                        completeprompt += random.choice(anthrolist) + ", 1boy, solo, "
                    else:
                        completeprompt += random.choice(anthrolist) + ", 1girl, solo, "
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == "" or (subjectingivensubject and givensubject != "")):

                    if(subtypeanimal != "all"):
                        if(subtypeanimal=="generic animal"):
                            animalwildcardlist = ["-animal-"]
                        elif(subtypeanimal=="bird"):
                            animalwildcardlist = ["-bird-"]
                        elif(subtypeanimal=="cat"):
                            animalwildcardlist = ["-cat-"]
                        elif(subtypeanimal=="dog"):
                            animalwildcardlist = ["-dog-"]
                        elif(subtypeanimal=="insect"):
                            animalwildcardlist = ["-insect-"]
                        elif(subtypeanimal=="pokemon"):
                            animalwildcardlist = ["-pokemon-"]
                        elif(subtypeanimal=="marine life"):
                            animalwildcardlist = ["-marinelife-"]

                    
                    chosenanimalwildcard = random.choice(animalwildcardlist)

                    if(rare_dist(insanitylevel) and advancedprompting == True):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["
                        
                    if(unique_dist(insanitylevel) and generateanimaladdition == True):
                        animaladdedsomething = 1
                        completeprompt += "-animaladdition- " + chosenanimalwildcard + " "
                    if(animaladdedsomething != 1):
                        completeprompt += chosenanimalwildcard + " "

                   

                    if(hybridorswap == "hybrid"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += "|" + random.choice(hybridlist) + "] "
                        else:
                            completeprompt += "| " + chosenanimalwildcard +  " ] "
                    if(hybridorswap == "swap"):
                        if(uncommon_dist(insanitylevel)):
                            completeprompt += ":" + random.choice(hybridlist) + ":" + str(random.randint(1,5)) +  "] "
                        else:
                            completeprompt += ":" + chosenanimalwildcard +  ":" + str(random.randint(1,5)) +  "] "
                else:
                    completeprompt += " " + givensubject + " "
                
                hybridorswap = ""

             # move job or activity logic here. We want to place it at 2 different places maybe
            
            if((animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation", "manwomanmultiple","firstname"])  and chance_roll(insanitylevel, joboractivitychance) and humanspecial != 1 and generatesubject == True):
                genjoboractivity = True
                genjoboractivitylocationslist = ["front","middle", "middle","back","back", "back"]
                genjoboractivitylocation = random.choice(genjoboractivitylocationslist)
    

            if(genjoboractivity and genjoboractivitylocation=="front"):
                completeprompt += "-job- "
                
            
            # if we have a given subject, we should skip making an actual subject
            if(mainchooser == "humanoid"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                
                if(anime_mode 
                   and "1girl" not in givensubject
                   and "1boy" not in givensubject):
                    if(subjectchooser != "manwomanmultiple"):
                        if(gender=="male"):
                            completeprompt += "1boy, solo, "
                        else:
                            completeprompt += "1girl, solo, "
                    else:
                        if(gender=="male"):
                            completeprompt += "multipleboys, "
                        else:
                            completeprompt += "multiplegirls, "
                
                if(givensubject == "" or (subjectingivensubject and givensubject != "")):

                    if(subjectchooser == "human" and not anime_mode):
                        completeprompt += "-manwoman-"
                    
                    if(subjectchooser == "manwomanrelation"):
                        completeprompt += "-manwomanrelation-"

                    if(subjectchooser == "manwomanmultiple"):
                        completeprompt += "-manwomanmultiple-"

                    if(subjectchooser == "job"):
                        if(not anime_mode):
                            completeprompt += "-malefemale- "
                        completeprompt += "-job-"

                    if(subjectchooser == "fictional"):
                        if(rare_dist(insanitylevel) and advancedprompting == True and buildingfullmode == False):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        # Sometimes, we do a gender swap. Much fun!
                        if(novel_dist(insanitylevel)):
                            completeprompt += gender + " version of -oppositefictional-"
                        else:
                            completeprompt += "-fictional-"

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + " ] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "non fictional"):
                        if(rare_dist(insanitylevel)  and advancedprompting == True and buildingfullmode == False):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        # Sometimes, we do a gender swap. Much fun!
                        if(novel_dist(insanitylevel)):
                            completeprompt += gender + " version of -oppositenonfictional-"
                        else:
                            completeprompt += "-nonfictional-"

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "humanoid"):
                        if(gender != "all"):
                            completeprompt += "-malefemale- "
                        if(rare_dist(insanitylevel)  and advancedprompting == True and buildingfullmode == False):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += "-humanoid-"

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + random.choice(hybridhumanlist) + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + random.choice(hybridhumanlist) + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""

                    if(subjectchooser == "firstname"):
                        if(rare_dist(insanitylevel)  and advancedprompting == True and buildingfullmode == False):
                            hybridorswaplist = ["hybrid", "swap"]
                            hybridorswap = random.choice(hybridorswaplist)
                            completeprompt += "["
                        
                        completeprompt += "-firstname-"

                        if(hybridorswap == "hybrid"):
                            completeprompt += "|" + "-firstname-" + "] "
                        if(hybridorswap == "swap"):
                            completeprompt += ":" + "-firstname-" + ":" + str(random.randint(1,5)) +  "] "
                        hybridorswap = ""
                    if(buildingfullmode == True):
                        completeprompt += "s"
                    completeprompt += " "

                else:
                    if(subjectchooser == "manwomanmultiple" and subtypehumanoid != "multiple humans" and givensubject not in ["1girl", "1boy", "solo"]):
                        if(random.randint(0,1) == 1):
                            completeprompt +=  " " + givensubject + " and a -manwomanmultiple- "
                        else:
                            completeprompt +=  " a OR(group;couple;crowd;bunch) of " + givensubject + " "
                    else:
                        completeprompt += " " + givensubject + " "  
 
            
             # sometimes add a suffix for more fun!
            if( (mainchooser == "humanoid" or mainchooser == "animal" or mainchooser == "object") and  chance_roll(insanitylevel, subjectconceptsuffixchance)):
                completeprompt += " of -conceptsuffix- "

            if(mainchooser == "humanoid" or mainchooser == "animal" or mainchooser == "object"):
            # completion of strenght end
                completeprompt += "-objectstrengthend-"  
            
            if(mainchooser == 'animal' and legendary_dist(insanitylevel)):
                animaladdedsomething = 1
                completeprompt += " -animalsuffixaddition- "
            
            
            if(mainchooser == "landscape"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart-"
                
                # if we have a given subject, we should skip making an actual subject
                if(givensubject == "" or (subjectingivensubject and givensubject != "")):
                    if(rare_dist(insanitylevel) and advancedprompting == True):
                        hybridorswaplist = ["hybrid", "swap"]
                        hybridorswap = random.choice(hybridorswaplist)
                        completeprompt += "["
                    
                    if(subtypelocation != "all"):
                        if(subtypelocation=="location"):
                            locationwildcardlist = ["-location-"]
                        elif(subtypelocation=="fantasy location"):
                            locationwildcardlist = ["-locationfantasy-"]
                        elif(subtypelocation=="videogame location"):
                            locationwildcardlist = ["-locationvideogame-"]
                        elif(subtypelocation=="sci-fi location"):
                            locationwildcardlist = ["-locationscifi-"]
                        elif(subtypelocation=="biome"):
                            locationwildcardlist = ["-locationbiome-"]
                        elif(subtypelocation=="city"):
                            locationwildcardlist = ["-locationcity-"]

                    
                    chosenlocationwildcard = random.choice(locationwildcardlist)
                    completeprompt += chosenlocationwildcard + " "

                    if(hybridorswap == "hybrid"):
                        completeprompt += "|" + chosenlocationwildcard  + "] "
                    if(hybridorswap == "swap"):
                        completeprompt += ":" + chosenlocationwildcard + ":" + str(random.randint(1,5)) +  "] "        
                else:
                    completeprompt += " " + givensubject + " " 
                
                hybridorswap = ""

                # completion of strenght end
                completeprompt += "-objectstrengthend-"

                # shots from inside can create cool effects in landscapes
                if(chance_roll(max(1,insanitylevel-2), subjectlandscapeaddonlocationchance) and insideshot == 0):
                    insideshot = 1
                    # lets cheat a bit here, we can do something cool I saw on reddit
                    if(mainchooser=="humanoid" and legendary_dist(insanitylevel)):
                        completeprompt += " looking at a -addontolocationinside- "
                    elif(mainchooser=="humanoid" and legendary_dist(insanitylevel)):
                        completeprompt += " facing a -addontolocationinside- "
                    elif(legendary_dist(insanitylevel)):
                        completeprompt += " in the distance there is a -addontolocationinside- "
                    else:
                        completeprompt += " from inside of a -addontolocationinside- "

                if(chance_roll(insanitylevel, subjectlandscapeaddonlocationchance) and insideshot == 0):
                    completeprompt += " and "
                    if(chance_roll(insanitylevel, subjectlandscapeaddonlocationdescriptorchance)):
                        completeprompt += "-locationdescriptor- " 
                    if(chance_roll(insanitylevel, subjectlandscapeaddonlocationculturechance)):
                        completeprompt += "-culture- "

                    #addontolocation = [locationlist,buildinglist, vehiclelist]
                    if(random.randint(0,1) == 1):
                        completeprompt += "-addontolocation- "
                    else:
                        completeprompt += "-background- "


            if(mainchooser == "concept"):
                # first add a wildcard that can be used to create prompt strenght
                completeprompt += " -objectstrengthstart- "
                if(subjectchooser == "conceptmixer"):
                        
                        chosenconceptmixerprelist = random.choice(conceptmixerlist)
                        chosenconceptmixerlist = chosenconceptmixerprelist.split("@")
                        chosenconceptmixer = ''.join([chosenconceptmixerlist[0]])
                        chosenconceptmixersubject = ''.join([chosenconceptmixerlist[1]])

                        # if there is a subject override, then replace the subject with that
                        if(givensubject==""):
                            chosenconceptmixer = chosenconceptmixer.replace("-subject-",chosenconceptmixersubject )
                        elif(givensubject != "" and subjectingivensubject == False):
                            chosenconceptmixer = chosenconceptmixer.replace("-subject-",givensubject )
                        
                        if(overrideoutfit!="" and ("-outfit-" in chosenconceptmixer or "-minioutfit-" in chosenconceptmixer)):
                            chosenconceptmixer = chosenconceptmixer.replace("-outfit-",overrideoutfit )
                            chosenconceptmixer = chosenconceptmixer.replace("-minioutfit-",overrideoutfit )
                            outfitmode = 1 # We dont want another outfit in this case
                        
                        completeprompt += chosenconceptmixer
                elif(givensubject == "" or (subjectingivensubject and givensubject != "")):
                    if(subjectchooser == "event"):
                        completeprompt += "  \"-event-\"  "
                    
                    if(subjectchooser == "concept"):
                        completeprompt += "  \"The -conceptprefix- of -conceptsuffix-\"  "

                    if(subjectchooser == "poemline"):
                        completeprompt += "  \"-poemline-\"  "

                    if(subjectchooser == "songline"):
                        completeprompt += "  \"-songline-\"  "

                    if(subjectchooser == "cardname"): 
                        completeprompt += "  \"-cardname-\" "

                    if(subjectchooser == "episodetitle"):
                        completeprompt += "  \"-episodetitle-\"  "


                    
                # making subject override work with X and Y concepts, much fun!
                elif(givensubject != "" and subjectchooser == "concept" and subjectingivensubject == False):
                        if(random.randint(0,3) == 0):
                            completeprompt += " \"The -conceptprefix- of " + givensubject + "\" "
                        else:
                            completeprompt += " \"The " + givensubject + " of -conceptsuffix-\" "
                else:
                    completeprompt += " " + givensubject + " " 

                # completion of strenght end
                completeprompt += " -objectstrengthend-"

            if(subjectingivensubject):
                completeprompt += " " + givensubjectpromptlist[1] + " "
            
            if(genjoboractivity and genjoboractivitylocation=="middle"):
                joboractivitylist = [joblist,humanactivitylist]
                completeprompt += random.choice(random.choice(joboractivitylist)) + ", "
            
            if(descriptorsintheback == 2):
                # Common to have 1 description, uncommon to have 2
                if(chance_roll(insanitylevel, subjectdescriptor1chance) and generatedescriptors == True):
                    if(animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple", "firstname"]):
                        if(less_verbose):
                            if(anime_mode and random.randint(0,2)<2):
                                completeprompt += ", -basicbitchdescriptor- "
                            else:
                                completeprompt += ", -humandescriptor- "
                        elif(random.randint(0,3) > 0):
                            completeprompt += ", OR(;-heshe- is;normal) OR(;very;rare) -humandescriptor- "
                        elif(subjectchooser == "manwomanmultiple"):
                            completeprompt += ", the -samehumansubject- are OR(;very;rare) -humandescriptor-"
                        else:
                            completeprompt += ", OR(the -manwoman-;-samehumansubject-) is OR(;very;rare) -humandescriptor-"
                    elif(mainchooser == "landscape"):
                        if(less_verbose):
                            completeprompt += ", -locationdescriptor- "
                        else:
                            completeprompt += ", OR(;-heshe- is;normal) OR(;very;rare) -locationdescriptor- "
                    elif(mainchooser == "animal"):
                        if(less_verbose):
                            completeprompt += ", -animaldescriptor- "
                        else:
                            completeprompt += ", OR(;-heshe- is;normal) OR(;very;rare) -animaldescriptor- "
                    else:
                        if(less_verbose):
                            completeprompt += ", -descriptor- "
                        else:
                            completeprompt += ", OR(;-heshe- is;normal) OR(;very;rare) -descriptor- "

                    if(chance_roll(insanitylevel, subjectdescriptor2chance) and generatedescriptors == True):
                        if(animalashuman or subjectchooser in ["human", "job", "fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple","firstname"]):
                            if(less_verbose):
                                completeprompt += ", -humandescriptor- "
                            else:
                                completeprompt += " and -humandescriptor- "
                        elif(mainchooser == "landscape"):
                            if(less_verbose):
                                completeprompt += ", -locationdescriptor- "
                            else:
                                completeprompt += " and -locationdescriptor- "
                        elif(mainchooser == "animal"):
                            if(less_verbose):
                                completeprompt += ", -animaldescriptor- "
                            else:
                                completeprompt += " and -animaldescriptor- "
                        else:
                            if(less_verbose):
                                completeprompt += ", -descriptor- "
                            else:
                                completeprompt += " and -descriptor- "
                completeprompt += ", "
        ## set the insanitylevel back
        if(superprompter == True):
            insanitylevel = originalinsanitylevel

        if(thetokinatormode == False):
            # object additions
            for i in range(objectadditionsrepeats):
                if(mainchooser == "object" and chance_roll(insanitylevel, objectadditionschance) and generateobjectaddition == True):
                    completeprompt += ", -objectaddition- , "
            
            
            # riding an animal, holding an object or driving a vehicle, rare
            if((animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple","firstname"]) and chance_roll(insanitylevel, humanadditionchance) and generatehumanaddition == True):
                humanspecial = 1
                completeprompt += "-humanaddition- "
                
            completeprompt += ", "

            # unique additions for all types:
            if(chance_roll(insanitylevel, overalladditionchance) and generateoveralladdition == True):
                completeprompt += "-overalladdition- "





            # SD understands emoji's. Can be used to manipulate facial expressions.
            # emoji, legendary
            if((animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple","firstname"]) and chance_roll(insanitylevel, emojichance) and generateemoji== True):
                completeprompt += "-emoji-, "

            # human expressions
            if((animalashuman or subjectchooser in ["animal as human,","human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple","firstname"]) and chance_roll(insanitylevel, humanexpressionchance) and generatehumanexpression== True):
                completeprompt += "-humanexpression-, "
                

            # cosplaying
            #if(subjectchooser in ["animal as human", "non fictional", "humanoid"] and rare_dist(insanitylevel) and humanspecial != 1):
            #    completeprompt += "cosplaying as " + random.choice(fictionallist) + ", "

            # Job 
            # either go job or activity, not both

            if(genjoboractivity and genjoboractivitylocation=="back"):
                if(random.randint(0,1)==0):
                    completeprompt +=  ", " + random.choice(humanactivitylist)+ ", "
                else:
                    completeprompt +=  ", OR(,; as a;rare) -job-, "


        

            # add face builder sometimes on generic humans
            if(subjectchooser in ["human", "humanoid", "manwomanrelation","firstname"] and chance_roll(insanitylevel, buildfacechance) and generateface== True):
                completeprompt += random.choice(buildfacelist) + ", "




            # custom mid list
            for i in range(custominputmidrepeats):
                if(chance_roll(insanitylevel, custominputmidchance) and generatecustominputmid == True):
                    completeprompt += random.choice(custominputmidlist) + ", "
            
            # add in some more mini vomits
            if(chance_roll(insanitylevel, minivomitmidchance) and generateminivomit == True):
                completeprompt += " -minivomit-, "
            
            # outfit builder
           
            if(outfitmode == 2):
                completeprompt += " " + random.choice(buildoutfitlist) + ", "
                if(extraordinary_dist(insanitylevel)):
                    completeprompt += " -outfitvomit-, "
            elif(outfitmode == 2 and overrideoutfit != "" and imagetype != "only templates mode"):
                completeprompt += " " + random.choice(buildoutfitlist) + ", "
                if(extraordinary_dist(insanitylevel)):
                    completeprompt += " -outfitvomit-, "
            

            
            if((animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple", "firstname"])  and chance_roll(insanitylevel, posechance) and humanspecial != 1 and generatepose == True):
                completeprompt += random.choice(poselist) + ", "
            
            if(subjectchooser in ["human","job","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple", "firstname"]  and chance_roll(insanitylevel, hairchance) and generatehairstyle == True):
                completeprompt += random.choice(buildhairlist) + ", "
                if(unique_dist(insanitylevel)):
                    completeprompt += " -hairvomit-, "

            if((animalashuman or subjectchooser in ["human","fictional", "non fictional", "humanoid", "manwomanrelation","manwomanmultiple", "firstname"])  and chance_roll(insanitylevel, accessorychance) and generateaccessorie == True and generateaccessories == True):
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


            # divider between subject and everything else
            completeprompt += " @@@ "
            

            # Add more quality while in greg mode lol
            if(originalartistchoice == "greg mode" and generatequality == True):
                completeprompt += "-quality-, "

            # landscapes it is nice to always have a time period
            if(chance_roll(insanitylevel, timperiodchance) or subjectchooser=="landscape"):
                if(generatetimeperiod == True):
                    completeprompt += "-timeperiod-, "

            if(mainchooser not in ["landscape"]  and chance_roll(insanitylevel, focuschance) and generatefocus == True):
                completeprompt += "-focus-, "
                

        # artists in the middle, can happen as well:

        if(artists != "none" and artistsplacement == "middle" and generateartist == True):
            completeprompt += ", "
            doartistnormal = True
            if(artists == "greg mode"):
                artistbylist = ["art by", "designed by", "stylized by", "by"]
                completeprompt += random.choice(artistbylist) + " -gregmode-, "
                doartistnormal = False

                # in case we have ALL, we can also do a specific artist mode per chosen subject. sometimes
            elif(originalartistchoice == "all" and random.randint(0,3) == 0):
                if(mainchooser in ["humanoid", "animal"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-portraitartist-;-characterartist-), OR(-portraitartist-;-characterartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(mainchooser in ["landscape"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-digitalartist-), OR(-landscapeartist-;-graphicdesignartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(subjectchooser in ["building"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-architectartist-), OR(-landscapeartist-;-architectartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False
            
            if(doartistnormal):
                
                # sometimes do this as well, but now in the front of the artists
                if(giventypeofimage=="" and imagetype == "all" and random.randint(0, 2) == 0):
                    completeprompt += "-artiststyle- art, "

                # take 1-3 artists, weighted to 1-2
                step = random.randint(0, 1)
                minstep = step
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
                    if(normal_dist(insanitylevel) and remove_weights == False):
                        isweighted = 1
                    
                    if isweighted == 1:
                        completeprompt += " ("

                    #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
                    if(step == minstep):
                        # sometimes do this
                        if(giventypeofimage=="" and imagetype == "all" and random.randint(0, 1) == 0):
                            if(artiststyleselectormode == "normal"):
                                completeprompt += artiststyleselector + " art "
                            else:
                                completeprompt += "-artiststyle- art "
                        artistbylist = ["art by", "designed by", "stylized by", "by"]
                    else:
                        artistbylist = [""]
                    completeprompt += random.choice(artistbylist) + " -artist-"
                    
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
                
                completeprompt += ", "
                # end of the artist stuff
        if(thetokinatormode == False):
                
                # todo
                descriptivemode = False
                # if we have artists, maybe go in artists descriptor mode
                if(not anime_mode and not less_verbose and templatemode == False and specialmode == False and "-artist-" in completeprompt and uncommon_dist(max(8 - insanitylevel,3))):
                    for i in range(random.randint(1,3)):
                        # print("adding artist stuff")
                        completeprompt += ", -artistdescription-"
                        descriptivemode = True
                    completeprompt += ", "

                    

                # if not, we could go in random styles descriptor mode
                elif(not anime_mode and not less_verbose and templatemode == False and specialmode == False and legendary_dist(10 - insanitylevel)):
                    for i in range(random.randint(1,max(7,insanitylevel + 2))):
                        # print("adding random crap")
                        completeprompt += ", -allstylessuffix-"
                        descriptivemode = True
                    completeprompt += ", "

                # and on high levels, DO EVERYTHING :D
                if(descriptivemode == False or rare_dist(insanitylevel)):

                    # Add more quality while in greg mode lol
                    if(originalartistchoice == "greg mode" and generatequality == True):
                        completeprompt += "-quality-, "

                    # others
                    if(chance_roll(max(1,insanitylevel -1), directionchance) and generatedirection == True):
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

                    # human specfic vomit
                    if(mainchooser == "humanoid" and chance_roll(insanitylevel, humanvomitchance) and generatehumanvomit == True):
                        completeprompt += "-humanvomit-, "
                        if(chance_roll(insanitylevel, humanvomitchance)):
                            completeprompt += "-humanvomit-, "

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
                    if((chance_roll(insanitylevel, quality1chance) or originalartistchoice == "greg mode") and generatequality == True):
                        completeprompt += "-quality-, "
                        if((chance_roll(insanitylevel, quality2chance) or originalartistchoice == "greg mode")):
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
            completeprompt += ", "
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
        
        templatesmodechance = 0
        if(uncommon_dist(insanitylevel) and not anime_mode): # not for anime models!
           templatesmodechance = 1

        if(dynamictemplatesmode == True and templatesmodechance == 1):
            for i in range(random.randint(1,max(2,insanitylevel))):
                completeprompt += ", -allstylessuffix-"
            

       
        if(dynamictemplatesmode == True and common_dist(insanitylevel) and templatesmodechance == 0):
            if("-artist-" in completeprompt or artists == "none"):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artist-" not in sentence.lower()]
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artiststyle-" not in sentence.lower()]
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artistdescription-" not in sentence.lower()]
            if("-lighting-" in completeprompt):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-lighting-" not in sentence.lower()]
            if("-shotsize-" in completeprompt):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-shotsize-" not in sentence.lower()]
            if("-artmovement-" in completeprompt):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artmovement-" not in sentence.lower()]
            if("-imagetype-" in completeprompt or "-othertype-" in completeprompt ):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-imagetype-" not in sentence.lower()]
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-othertype-" not in sentence.lower()]
            if("-colorcombination-" in completeprompt or "-colorscheme" in completeprompt ):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-colorcombination-" not in sentence.lower()]
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-colorscheme-" not in sentence.lower()]
            if("-mood-" in completeprompt or "-humanexpression" in completeprompt ):
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-mood-" not in sentence.lower()]
                dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-humanexpression-" not in sentence.lower()]
            chosenstylesuffix = random.choice(dynamictemplatessuffixlist)
            completeprompt += ". " + chosenstylesuffix

            if(normal_dist(insanitylevel)):
                if("-artist-" in completeprompt):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artist-" not in sentence.lower()]
                if("-lighting-" in completeprompt):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-lighting-" not in sentence.lower()]
                if("-shotsize-" in completeprompt):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-shotsize-" not in sentence.lower()]
                if("-artmovement-" in completeprompt):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-artmovement-" not in sentence.lower()]
                if("-imagetype-" in completeprompt or "-othertype-" in completeprompt ):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-imagetype-" not in sentence.lower()]
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-othertype-" not in sentence.lower()]
                if("-colorcombination-" in completeprompt or "-colorscheme" in completeprompt ):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-colorcombination-" not in sentence.lower()]
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-colorscheme-" not in sentence.lower()]
                if("-mood-" in completeprompt or "-humanexpression" in completeprompt ):
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-mood-" not in sentence.lower()]
                    dynamictemplatessuffixlist = [sentence for sentence in dynamictemplatessuffixlist if "-humanexpression-" not in sentence.lower()]
                chosenstylesuffix = random.choice(dynamictemplatessuffixlist)
                completeprompt += " " + chosenstylesuffix

        
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
            doartistnormal = True
            if(artists == "greg mode"):
                artistbylist = ["art by", "designed by", "stylized by", "by"]
                completeprompt += random.choice(artistbylist) + " -gregmode- ,"
                doartistnormal = False

                # in case we have ALL, we can also do a specific artist mode per chosen subject. sometimes
            elif(originalartistchoice == "all" and random.randint(0,3) == 0):
                if(mainchooser in ["humanoid", "animal"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-portraitartist-;-characterartist-), OR(-portraitartist-;-characterartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(mainchooser in ["landscape"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-digitalartist-), OR(-landscapeartist-;-graphicdesignartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False

                elif(subjectchooser in ["building"]):
                    artistbylist = ["art by", "designed by", "stylized by", "by"]
                    completeprompt += random.choice(artistbylist) + " OR(-landscapeartist-;-architectartist-), OR(-landscapeartist-;-architectartist-) OR(;and OR(-fantasyartist-;-scifiartist-;-photographyartist-;-digitalartist-;-graphicdesignartist-);uncommon), "
                    doartistnormal = False
            
            if(doartistnormal):
                # take 1-3 artists, weighted to 1-2
                step = random.randint(0, 1)
                minstep = step
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
                    if(normal_dist(insanitylevel) and remove_weights == False):
                        isweighted = 1
                    
                    if isweighted == 1:
                        completeprompt += " ("

                    #completeprompt = add_from_csv(completeprompt, "artists", 0, "art by ","")
                    if(step == minstep):
                        # sometimes do this
                        if(giventypeofimage=="" and imagetype == "all" and random.randint(0, 1) == 0):
                            if(artiststyleselectormode == "normal"):
                                completeprompt += artiststyleselector + " art "
                            else:
                                completeprompt += "-artiststyle- art "
                        artistbylist = ["art by", "designed by", "stylized by", "by"]
                    else:
                        artistbylist = [""]
                    completeprompt += random.choice(artistbylist) + " -artist-"
                    
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

        
        
        if(partlystylemode == True):
            # add a part of the style to the back
            chosenstylesuffixlist = chosenstylesuffix.split(",")
            for i in range(len(chosenstylesuffixlist)):
                if(random.randint(3, 10)<insanitylevel):
                    chosenstylesuffixlist.pop(random.randint(0, len(chosenstylesuffixlist)-1))
            chosenstylesuffixcomplete = ", ".join(chosenstylesuffixlist)
            

            completeprompt += ", " + chosenstylesuffixcomplete
            
        if(artifymode == True):
            amountofartists = "random"
            if(unique_dist(insanitylevel)):
               mode = "super remix turbo"
            elif(legendary_dist(insanitylevel)):
                 mode = "remix"
            else:
                mode = "standard"
            completeprompt = artify_prompt(insanitylevel=insanitylevel,prompt=completeprompt, artists=artists, amountofartists=amountofartists, mode=mode, seed=seed)
        
        completeprompt += " -tempnewwords- "
        completeprompt += ", "

        completeprompt = prefixprompt + ", " + completeprompt
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


    


    # In front and the back?
    if(dynamictemplatesmode == False):
        completeprompt = parse_custom_functions(completeprompt, insanitylevel)
    
    # Sometimes change he/she to the actual subject
    # Doesnt work if someone puts in a manual subject
    if(mainchooser == "humanoid" and (givensubject == "" or subjectingivensubject and givensubject != "") and subjectchooser != "manwomanmultiple"):
        samehumanreplacementlist = ["-heshe-","-heshe-","-heshe-","-heshe-","-heshe-", "-samehumansubject-", "-samehumansubject-", "-samehumansubject-", "-samehumansubject-", "-samehumansubject-"]
        random.shuffle(samehumanreplacementlist)
        
        # Convert completeprompt to a list to allow character-wise manipulation
        completeprompt_list = list(completeprompt)
        # Iterate over the characters in completeprompt_list
        for i in range(len(completeprompt_list) - len("-heshe-") + 1):
            if "".join(completeprompt_list[i:i+len("-heshe-")]) == "-heshe-":
                # Replace -heshe- with a value from the shuffled list
                replacement = samehumanreplacementlist.pop()
                completeprompt_list[i:i+len("-heshe-")] = replacement

        # Convert the list back to a string
        completeprompt = "".join(completeprompt_list)
    
        # Sometimes change he/she to the actual subject
    if(mainchooser in  ["animal", "object"] and (givensubject == "" or subjectingivensubject and givensubject != "")):
        sameobjectreplacementlist = ["-heshe-","-heshe-","-heshe-","-heshe-","-heshe-", "-sameothersubject-", "-sameothersubject-", "-sameothersubject-", "-sameothersubject-", "-sameothersubject-"]
        random.shuffle(sameobjectreplacementlist)
        # Convert completeprompt to a list to allow character-wise manipulation
        completeprompt_list = list(completeprompt)

        # Iterate over the characters in completeprompt_list
        for i in range(len(completeprompt_list) - len("-heshe-") + 1):
            if "".join(completeprompt_list[i:i+len("-heshe-")]) == "-heshe-":
                # Replace -heshe- with a value from the shuffled list
                replacement = sameobjectreplacementlist.pop()
                completeprompt_list[i:i+len("-heshe-")] = replacement
        # Convert the list back to a string
        completeprompt = "".join(completeprompt_list)

    # hair descriptor
    if(rare_dist(insanitylevel)): # Use base hair descriptor, until we are not.
        completeprompt = completeprompt.replace("-hairdescriptor-", "-descriptor-")
    
    # human descriptor
    if(rare_dist(insanitylevel)): # Use base human descriptor, until we are not.
        completeprompt = completeprompt.replace("-humandescriptor-", "-descriptor-")
    
    # location descriptor
    if(rare_dist(insanitylevel)): # Use base location descriptor, until we are not.
        completeprompt = completeprompt.replace("-locationdescriptor-", "-descriptor-")
    
    # animeal descriptor
    if(rare_dist(insanitylevel)): # Use base animal descriptor, until we are not.
        completeprompt = completeprompt.replace("-animaldescriptor-", "-descriptor-")


    # sometimes, culture becomes traditional!
    if(unique_dist(insanitylevel)):
        completeprompt = completeprompt.replace("-culture-", "traditional -culture-")


    # first some manual stuff for outfit

    if(unique_dist(insanitylevel)): # sometimes, its just nice to have descriptor and a normal "outfit". We use mini outfits for this!
        completeprompt = completeprompt.replace("-outfit-", "-minioutfit-",1)
    if(rare_dist(insanitylevel)): # Use base outfit descriptor, until we are not.
        completeprompt = completeprompt.replace("-outfitdescriptor-", "-descriptor-")
    
    # if -outfit- is in the override, we want a consistent result
    if("-outfit-" in overrideoutfit):
        if(chance_roll(insanitylevel, "common")):
            overrideoutfit = overrideoutfit.replace("-outfit-", random.choice(outfitlist))
        else:
            overrideoutfit = overrideoutfit.replace("-outfit-", random.choice(minioutfitlist))

    if(overrideoutfit != ""):
        completeprompt = completeprompt.replace("-sameoutfit-", overrideoutfit)
        completeprompt = completeprompt.replace("-outfit-", overrideoutfit,1)
        completeprompt = completeprompt.replace("-minioutfit-", overrideoutfit,1)
        completeprompt = completeprompt.replace("-overrideoutfit-", overrideoutfit)

    if(givensubject != "" and subjectingivensubject == False):
        completeprompt = completeprompt.replace("-samehumansubject-", givensubject)
        completeprompt = completeprompt.replace("-sameothersubject-", givensubject)
        
            
    
    # If we don't have an override outfit, then remove this part
    completeprompt = completeprompt.replace("-overrideoutfit-", "")

    # sometimes replace one descriptor with a artmovement, only on high insanitylevels
    if(insanitylevel > 7 and unique_dist(insanitylevel)):
        completeprompt = completeprompt.replace("-descriptor-", "-artmovement-",1)

    # On low insanity levels (lower than 5) ,a chance refer to the basic bitch list on some occasions
    if(random.randint(0,insanitylevel) == 0 and insanitylevel < 5): 
        completeprompt = completeprompt.replace("-locationdescriptor-", "-basicbitchdescriptor-")
        completeprompt = completeprompt.replace("-humandescriptor-", "-basicbitchdescriptor-")
        completeprompt = completeprompt.replace("-outfitdescriptor-", "-basicbitchdescriptor-")
        completeprompt = completeprompt.replace("-descriptor-", "-basicbitchdescriptor-")
        completeprompt = completeprompt.replace("-animaldescriptor-", "-basicbitchdescriptor-")

    # we now have color combinations, which are stronger than just color. So lets change them while we are at it.
    if(random.randint(0,max(0, insanitylevel - 2)) <= 0):
        completeprompt = completeprompt.replace("-color- and -color-", "-colorcombination-") # any color and color becomes a color combination

        colorreplacementlist = ["-color-","-color-","-color-","-colorcombination-","-colorcombination-", "-colorcombination-", "-colorcombination-", "-colorcombination-", "-colorcombination-", "-colorcombination-"]
        random.shuffle(colorreplacementlist)
        
        # Convert completeprompt to a list to allow character-wise manipulation
        completeprompt_list = list(completeprompt)
        # Iterate over the characters in completeprompt_list
        for i in range(len(completeprompt_list) - len("-color-") + 1):
            if "".join(completeprompt_list[i:i+len("-color-")]) == "-color-":
                # Replace -heshe- with a value from the shuffled list
                replacement = colorreplacementlist.pop()
                completeprompt_list[i:i+len("-color-")] = replacement

        # Convert the list back to a string
        completeprompt = "".join(completeprompt_list)


     # we now have material combinations, which are stronger than just one material. So lets change them while we are at it.
    if(random.randint(0,max(0, insanitylevel - 4)) <= 0):
        completeprompt = completeprompt.replace("-material- and -material-", "-materialcombination-") # any color and color becomes a color combination

        materialreplacementlist = ["-material-","-material-","-material-","-materialcombination-","-materialcombination-", "-materialcombination-", "-materialcombination-", "-materialcombination-", "-materialcombination-", "-materialcombination-"]
        random.shuffle(materialreplacementlist)
        
        # Convert completeprompt to a list to allow character-wise manipulation
        completeprompt_list = list(completeprompt)
        # Iterate over the characters in completeprompt_list
        for i in range(len(completeprompt_list) - len("-material-") + 1):
            if "".join(completeprompt_list[i:i+len("-material-")]) == "-material-":
                # Replace -heshe- with a value from the shuffled list
                replacement = materialreplacementlist.pop()
                completeprompt_list[i:i+len("-material-")] = replacement

        # Convert the list back to a string
        completeprompt = "".join(completeprompt_list)

        
    #    print(completeprompt)
    
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
    "-outfitfromfile-" in completeprompt or
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
    "-fantasyartist-" in completeprompt or 
    "-popularartist-" in completeprompt or 
    "-romanticismartist-" in completeprompt or 
    "-photographyartist-" in completeprompt or
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
    "-manwomanmultiple-" in completeprompt or
    "-waterlocation-" in completeprompt or
    "-container-" in completeprompt or
    "-firstname-" in completeprompt or
    "-flora-" in completeprompt or
    "-print-" in completeprompt or
    "-miniactivity-" in completeprompt or
    "-pattern-" in completeprompt or
    "-animalsuffixaddition-" in completeprompt or
    "-chair-" in completeprompt or
    "-cardname-" in completeprompt or
    "-covering-" in completeprompt or
    "-heshe-" in completeprompt or
    "-hisher-" in completeprompt or
    "-himher-" in completeprompt or
    "-outfitdescriptor-" in completeprompt or
    "-hairdescriptor-" in completeprompt or
    "-hairvomit-" in completeprompt or
    "-humandescriptor-" in completeprompt or
    "-facepart-" in completeprompt or
    "-buildfacepart-" in completeprompt or
    "-outfitvomit-" in completeprompt or
    "-locationdescriptor-" in completeprompt or
    "-basicbitchdescriptor-" in completeprompt or
    "-animaldescriptor-" in completeprompt or
    "-humanexpression-" in completeprompt or
    "-humanvomit-" in completeprompt or
    "-eyecolor-" in completeprompt or
    "-fashiondesigner-" in completeprompt or
    "-colorcombination-" in completeprompt or
    "-materialcombination-" in completeprompt or
    "-oppositefictional-" in completeprompt or
    "-oppositenonfictional-" in completeprompt or
    "-photoaddition-" in completeprompt or
    "-age-" in completeprompt or
    "-agecalculator-" in completeprompt or
    "-gregmode-" in completeprompt or
    "-portraitartist-" in completeprompt or
    "-characterartist-" in completeprompt or
    "-landscapeartist-" in completeprompt or
    "-scifiartist-" in completeprompt or
    "-graphicdesignartist-" in completeprompt or
    "-digitalartist-" in completeprompt or
    "-architectartist-" in completeprompt or
    "-cinemaartist-" in completeprompt or
    "-element-" in completeprompt or
    "-setting-" in completeprompt or
    "-charactertype-" in completeprompt or
    "-objectstohold-" in completeprompt or
    "-episodetitle-" in completeprompt or
    "-token-" in completeprompt or
    "-allstylessuffix-" in completeprompt or
    "-fluff-" in completeprompt or
    "-event-" in completeprompt or
    "-background-" in completeprompt or
    "-occult-" in completeprompt or
    "-locationfantasy-" in completeprompt or
    "-locationscifi-" in completeprompt or
    "-locationvideogame-" in completeprompt or
    "-locationbiome-" in completeprompt or
    "-locationcity-" in completeprompt or
    "-bird-" in completeprompt or
    "-cat-" in completeprompt or
    "-dog-" in completeprompt or
    "-insect-" in completeprompt or
    "-pokemon-" in completeprompt or
    "-pokemontype-" in completeprompt or
    "-marinelife-"  in completeprompt):
        allwildcardslistnohybrid = [ "-color-","-object-", "-animal-", "-fictional-","-nonfictional-","-building-","-vehicle-","-location-","-conceptprefix-","-food-","-haircolor-","-hairstyle-","-job-", "-accessory-", "-humanoid-", "-manwoman-", "-human-", "-colorscheme-", "-mood-", "-genderdescription-", "-artmovement-", "-malefemale-", "-bodytype-", "-minilocation-", "-minilocationaddition-", "-pose-", "-season-", "-minioutfit-", "-elaborateoutfit-", "-minivomit-", "-vomit-", "-rpgclass-", "-subjectfromfile-","-outfitfromfile-", "-brand-", "-space-", "-artist-", "-imagetype-", "-othertype-", "-quality-", "-lighting-", "-camera-", "-lens-","-imagetypequality-", "-poemline-", "-songline-", "-greatwork-", "-fantasyartist-", "-popularartist-", "-romanticismartist-", "-photographyartist-", "-emoji-", "-timeperiod-", "-shotsize-", "-musicgenre-", "-animaladdition-", "-addontolocationinside-", "-addontolocation-", "-objectaddition-", "-humanaddition-", "-overalladdition-", "-focus-", "-direction-", "-styletilora-", "-manwomanrelation-", "-waterlocation-", "-container-", "-firstname-", "-flora-", "-print-", "-miniactivity-", "-pattern-", "-animalsuffixaddition-", "-chair-", "-cardname-", "-covering-", "-heshe-", "-hisher-", "-himher-", "-outfitdescriptor-", "-hairdescriptor-", "-hairvomit-", "-humandescriptor-", "-manwomanmultiple-", "-facepart-", "-buildfacepart-", "-outfitvomit-", "-locationdescriptor-", "-basicbitchdescriptor-", "-animaldescriptor-", "-humanexpression-", "-humanvomit-", "-eyecolor-", "-fashiondesigner-", "-colorcombination-", "-materialcombination-", "-oppositefictional-", "-oppositenonfictional-", "-photoaddition-", "-age-", "-agecalculator-", "-gregmode-"
                                    ,"-portraitartist-", "-characterartist-" , "-landscapeartist-", "-scifiartist-", "-graphicdesignartist-", "-digitalartist-", "-architectartist-", "-cinemaartist-", "-setting-", "-charactertype-", "-objectstohold-", "-episodetitle-", "-token-", "-allstylessuffix-", "-fluff-", "-event-", "-background-"
                                    , "-occult-", "-locationfantasy-", "-locationscifi-", "-locationvideogame-", "-locationbiome-", "-locationcity-", "-bird-", "-cat-", "-dog-", "-insect-", "-pokemon-", "-pokemontype-", "-marinelife-"]
        allwildcardslistnohybridlists = [colorlist, objectlist, animallist, fictionallist, nonfictionallist, buildinglist, vehiclelist, locationlist,conceptprefixlist,foodlist,haircolorlist, hairstylelist,joblist, accessorielist, humanoidlist, manwomanlist, humanlist, colorschemelist, moodlist, genderdescriptionlist, artmovementlist, malefemalelist, bodytypelist, minilocationlist, minilocationadditionslist, poselist, seasonlist, minioutfitlist, elaborateoutfitlist, minivomitlist, vomitlist, rpgclasslist, customsubjectslist, customoutfitslist, brandlist, spacelist, artistlist, imagetypelist, othertypelist, qualitylist, lightinglist, cameralist, lenslist, imagetypequalitylist, poemlinelist, songlinelist, greatworklist, fantasyartistlist, popularartistlist, romanticismartistlist, photographyartistlist, emojilist, timeperiodlist, shotsizelist, musicgenrelist, animaladditionlist, addontolocationinsidelist, addontolocationlist, objectadditionslist, humanadditionlist, overalladditionlist, focuslist, directionlist, stylestiloralist, manwomanrelationlist, waterlocationlist, containerlist, firstnamelist, floralist, printlist, miniactivitylist, patternlist, animalsuffixadditionlist, chairlist, cardnamelist, coveringlist, heshelist, hisherlist, himherlist, outfitdescriptorlist, hairdescriptorlist, hairvomitlist, humandescriptorlist, manwomanmultiplelist, facepartlist, buildfacepartlist, outfitvomitlist, locationdescriptorlist, basicbitchdescriptorlist, animaldescriptorlist, humanexpressionlist, humanvomitlist, eyecolorlist, fashiondesignerlist, colorcombinationlist, materialcombinationlist, oppositefictionallist, oppositenonfictionallist, photoadditionlist, agelist, agecalculatorlist, gregmodelist
                                         , portraitartistlist, characterartistlist, landscapeartistlist, scifiartistlist, graphicdesignartistlist, digitalartistlist, architectartistlist, cinemaartistlist, settinglist, charactertypelist, objectstoholdlist, episodetitlelist, tokenlist, allstylessuffixlist, flufferlist, eventlist, backgroundlist
                                         , occultlist, locationfantasylist, locationscifilist, locationvideogamelist, locationbiomelist, locationcitylist, birdlist, catlist, doglist, insectlist, pokemonlist, pokemontypelist, marinelifelist]
        
        allwildcardslistwithhybrid = ["-material-", "-descriptor-", "-outfit-", "-conceptsuffix-","-culture-", "-objecttotal-", "-outfitprinttotal-", "-element-"]
        allwildcardslistwithhybridlists = [materiallist, descriptorlist,outfitlist,conceptsuffixlist,culturelist, objecttotallist, outfitprinttotallist, elementlist]
        
        
        #  keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
        for wildcard in allwildcardslistnohybrid:
            attachedlist = allwildcardslistnohybridlists[allwildcardslistnohybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,False, advancedprompting, artiststyleselector)


        
        for wildcard in allwildcardslistwithhybrid:
            attachedlist = allwildcardslistwithhybridlists[allwildcardslistwithhybrid.index(wildcard)]
            completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,True, advancedprompting, artiststyleselector)


    completeprompt = replace_user_wildcards(completeprompt)  
    # prompt strenght stuff

    # if the given subject already is formed like this ( :1.x)
    # then just ignore this
    
    matches = []
    if(givensubject != ""):
        pattern = r'\(\w+:\d+\.\d+\)'
        matches = re.findall(pattern, givensubject)


    if(len(completeprompt) > 325 and matches == [] and remove_weights == False):
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

    
    # Now, we are going to parse any custom functions we have build in
    # this is OR()
    # OR()
    
    # OR(foo;bar;bla)  --> randomly take foo, bar or bla
    # OR(foo;bar;bla;uncommon) --> Take foo, unless it hits uncommon roll. Then take bar or bla
    # OR(;foo)  --> empty or foo
    # OR(;foo;uncommon) --> empty unless it hits uncommon roll. Then take foo
    # OR(;foo;bar;uncommon) --> empty unless it hits uncommon roll. Then take foo or bar
    
    
    completeprompt = parse_custom_functions(completeprompt, insanitylevel)

    # prompt enhancer!
    if(templatemode == False and specialmode == False and base_model != "Stable Cascade"):
        # how insane do we want it?

        maxamountofwords = max(0, -1 + random.randint(0,4),6 - insanitylevel)
        amountofwords = random.randint(0,maxamountofwords)

        if(amountofwords > 0):
            enhance_positive_words = enhance_positive(completeprompt, amountofwords)
            completeprompt = completeprompt.replace("-tempnewwords-", enhance_positive_words)
    completeprompt = completeprompt.replace("-tempnewwords-", "")
       
    # clean it up
    completeprompt = cleanup(completeprompt, advancedprompting, insanitylevel)

    # Split it up for support for prompt_g (subject) and prompt_l (style)
    if("@@@" in completeprompt and prompt_g_and_l == True):
        promptlist = completeprompt.split("@@@")
        prompt_g = cleanup(promptlist[1], advancedprompting, insanitylevel)
        prompt_l = cleanup((promptlist[0] + ", " + promptlist[2]).replace("of a",""), advancedprompting, insanitylevel)
    if("@@@" in completeprompt and superprompter == True):
        #load_models()
        promptlist = completeprompt.split("@@@")
        subjectprompt = cleanup(promptlist[1], advancedprompting, insanitylevel)
        startprompt = cleanup(promptlist[0], advancedprompting, insanitylevel)
        endprompt = cleanup(promptlist[2], advancedprompting, insanitylevel)
        superpromptresult = one_button_superprompt(insanitylevel=insanitylevel, prompt=subjectprompt, seed=seed, override_subject=givensubject, override_outfit=overrideoutfit, chosensubject=subjectchooser, gender=gender, restofprompt = startprompt + endprompt)
        completeprompt = startprompt + ", " + superpromptresult + ", " + endprompt
        prompt_g = superpromptresult
        prompt_l = startprompt + endprompt
    elif(prompt_g_and_l == False):
        prompt_g = completeprompt
        prompt_l = completeprompt

    completeprompt = completeprompt.replace(" @@@ ", " ")
    completeprompt = completeprompt.replace("@@@ ", " ")
    completeprompt = completeprompt.replace(" @@@", " ")
    completeprompt = completeprompt.replace("@@@", " ")
    completeprompt = cleanup(completeprompt, advancedprompting, insanitylevel)

    #just for me, some fun with posting fake dev messages (ala old sim games)
    if(random.randint(1, 50)==1):
        print("")
        print(random.choice(devmessagelist))
        print("")

    print(completeprompt) # keep this! :D 

    if(prompt_g_and_l == False):
        return completeprompt
    else:
        return completeprompt, prompt_g, prompt_l


# function that takes an existing prompt and tries to create a variant out of it
def createpromptvariant(prompt = "", insanitylevel = 5, antivalues = "" , gender = "all", artists = "all", advancedprompting = True):
    # first load the lists, all copied from above (can that be done better?)
    # do we want to use the same settings or keep it open??

    # strip the prompt, for EVO in ruinedfooocus:
    prompt = prompt.strip()

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
    backgroundlist = csv_to_list("backgrounds",antilist)
    locationlist = locationlist + backgroundlist

    accessorielist = csv_to_list("accessories",antilist,"./csvfiles/",0,"?")
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
    hairvomitlist = csv_to_list("hairvomit",antilist,"./csvfiles/",0,"?",False,False)
    humanactivitylist = csv_to_list("human_activities",antilist,"./csvfiles/",0,"?",False,False)
    humanoidlist = csv_to_list("humanoids",antilist)
    imagetypelist = csv_to_list("imagetypes",antilist)
    joblist = joblist = csv_to_list(csvfilename="jobs",antilist=antilist,skipheader=True,gender=gender)
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
    minioutfitlist = csv_to_list("minioutfits",antilist,"./csvfiles/",0,"?",False,False,gender)
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
    manwomanmultiplelist = csv_to_list(csvfilename="manwomanmultiples",antilist=antilist,skipheader=True,gender=gender,delimiter="?")
    waterlocationlist = csv_to_list("waterlocations", antilist)
    containerlist = csv_to_list("containers", antilist)
    firstnamelist = csv_to_list(csvfilename="firstnames",antilist=antilist,skipheader=True,gender=gender)
    floralist = csv_to_list("flora", antilist)
    printlist = csv_to_list("prints", antilist)
    patternlist = csv_to_list("patterns", antilist)
    chairlist = csv_to_list("chairs", antilist)
    cardnamelist = csv_to_list("card_names", antilist)
    coveringlist = csv_to_list("coverings", antilist)
    facepartlist = csv_to_list("faceparts", antilist)
    humanexpressionlist = csv_to_list(csvfilename="humanexpressions",antilist=antilist,delimiter="?")
    humanvomitlist = csv_to_list("humanvomit", antilist)
    eyecolorlist = csv_to_list("eyecolors", antilist)
    fashiondesignerlist = csv_to_list("fashiondesigners", antilist)
    colorcombinationlist  = csv_to_list("colorcombinations", antilist)
    materialcombinationlist  = csv_to_list("materialcombinations", antilist)
    agelist = csv_to_list("ages", antilist)
    agecalculatorlist = csv_to_list("agecalculator", antilist)
    elementlist = csv_to_list("elements", antilist)
    settinglist = csv_to_list("settings", antilist)
    charactertypelist = csv_to_list("charactertypes", antilist)
    objectstoholdlist = csv_to_list("objectstohold", antilist)
    episodetitlelist = csv_to_list(csvfilename="episodetitles",antilist=antilist,skipheader=True)
    flufferlist = csv_to_list("fluff", antilist)

    outfitdescriptorlist = csv_to_list("outfitdescriptors",antilist)
    hairdescriptorlist = csv_to_list("hairdescriptors",antilist)
    humandescriptorlist = csv_to_list("humandescriptors",antilist)
    locationdescriptorlist = csv_to_list("locationdescriptors",antilist)
    basicbitchdescriptorlist = csv_to_list("basicbitchdescriptors",antilist)
    animaldescriptorlist = csv_to_list("animaldescriptors",antilist)

    humanlist = fictionallist + nonfictionallist + humanoidlist + malefemalelist + manwomanlist + manwomanrelationlist + manwomanmultiplelist
    objecttotallist = objectlist + buildinglist + vehiclelist + foodlist + spacelist + floralist + containerlist
    outfitprinttotallist = objecttotallist + locationlist + colorlist + musicgenrelist + seasonlist + animallist + patternlist

    styleslist = csv_to_list("styles", antilist,"./csvfiles/templates/",0,"?")
    stylessuffix = [item.split('-subject-')[1] for item in styleslist]
    breakstylessuffix = [item.split(',') for item in stylessuffix]
    allstylessuffixlist = [value for sublist in breakstylessuffix for value in sublist]
    allstylessuffixlist = list(set(allstylessuffixlist))

    # build artists list
    if artists == "wild":
        artists = "all (wild)"
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
    portraitartistlist = artist_category_csv_to_list("artists_and_category","portrait")
    characterartistlist = artist_category_csv_to_list("artists_and_category","character")
    landscapeartistlist = artist_category_csv_to_list("artists_and_category","landscape")
    scifiartistlist = artist_category_csv_to_list("artists_and_category","sci-fi")
    graphicdesignartistlist = artist_category_csv_to_list("artists_and_category","graphic design")
    digitalartistlist = artist_category_csv_to_list("artists_and_category","digital")
    architectartistlist = artist_category_csv_to_list("artists_and_category","architecture")
    cinemaartistlist = artist_category_csv_to_list("artists_and_category","cinema")
    gregmodelist = csv_to_list("gregmode", antilist)


    # New set of lists
    locationfantasylist = csv_to_list("locationsfantasy", antilist)
    locationscifilist = csv_to_list("locationsscifi", antilist)
    locationvideogamelist = csv_to_list("locationsvideogame", antilist)
    locationbiomelist = csv_to_list("locationsbiome", antilist)
    locationcitylist = csv_to_list("locationscities", antilist)
    birdlist = csv_to_list("birds", antilist)
    catlist = csv_to_list("cats", antilist)
    doglist = csv_to_list("dogs", antilist)
    insectlist = csv_to_list("insects", antilist)
    pokemonlist = csv_to_list("pokemon", antilist)
    pokemontypelist = csv_to_list("pokemontypes", antilist)
    occultlist = csv_to_list("occult", antilist)
    marinelifelist = csv_to_list("marinelife", antilist)

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
    customoutfitslist = csv_to_list("custom_outfits",antilist,"./userfiles/")

    # special lists
    backgroundtypelist = csv_to_list("backgroundtypes", antilist,"./csvfiles/special_lists/",0,"?")
    insideshotlist =  csv_to_list("insideshots", antilist,"./csvfiles/special_lists/",0,"?")
    photoadditionlist = csv_to_list("photoadditions", antilist,"./csvfiles/special_lists/",0,"?")
    buildhairlist = csv_to_list("buildhair", antilist,"./csvfiles/special_lists/",0,"?")
    buildoutfitlist = csv_to_list("buildoutfit", antilist,"./csvfiles/special_lists/",0,"?")
    objectadditionslist = csv_to_list("objectadditions", antilist,"./csvfiles/special_lists/",0,"?")
    humanadditionlist = csv_to_list("humanadditions", antilist,"./csvfiles/special_lists/",0,"?")
    animaladditionlist = csv_to_list("animaladditions", antilist,"./csvfiles/special_lists/",0,"?")
    buildaccessorielist = csv_to_list("buildaccessorie", antilist,"./csvfiles/special_lists/",0,"?")
    minilocationadditionslist = csv_to_list("minilocationadditions", antilist,"./csvfiles/special_lists/",0,"?")
    overalladditionlist = csv_to_list("overalladditions", antilist,"./csvfiles/special_lists/",0,"?")
    imagetypemodelist = csv_to_list("imagetypemodes", antilist,"./csvfiles/special_lists/",0,"?")
    miniactivitylist = csv_to_list("miniactivity", antilist,"./csvfiles/special_lists/",0,"?")


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
    originaloriginalprompt = prompt
    
    basicenhance = ", OR(-vomit-;-imagetype-;-basicbitchdescriptor-;-mood-;-lighting-;-descriptor-), "
    
    ### Get all combinations of 1 to 4 consecutive words


    words = prompt.split()
    num_words = len(words)
    if(num_words < 15 and common_dist(insanitylevel)):
        # add some random words maybe?
        if(common_dist(insanitylevel)):
            
            if(random.randint(0,1)== 0):
                prompt += basicenhance
            else:
                prompt = basicenhance + prompt
            if(common_dist(insanitylevel)):
                prompt += basicenhance
            prompt = parse_custom_functions(prompt, insanitylevel)

        # then add some enhanced words
        amountofwords = random.randint(0,3)
        if(amountofwords > 0):
            enhance_positive_words = enhance_positive(prompt, amountofwords)
            prompt += enhance_positive_words


        originalprompt = prompt
    
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

                if lowercase_combination in [x.lower() for x in backgroundlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -background- ")

                
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

                if lowercase_combination in [x.lower() for x in eyecolorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -eyecolor- ")

                if lowercase_combination in [x.lower() for x in fashiondesignerlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -fashiondesigner- ")

                if lowercase_combination in [x.lower() for x in colorcombinationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -colorcombination- ")

                if lowercase_combination in [x.lower() for x in materialcombinationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -materialcombination- ")

                if lowercase_combination in [x.lower() for x in photoadditionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -photoaddition- ")

                if lowercase_combination in [x.lower() for x in agelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -age- ")

                if lowercase_combination in [x.lower() for x in agecalculatorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -agecalculator- ")

                if lowercase_combination in [x.lower() for x in gregmodelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -gregmode- ")

                if lowercase_combination in [x.lower() for x in elementlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -element- ")

                if lowercase_combination in [x.lower() for x in settinglist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -setting- ")
                
                if lowercase_combination in [x.lower() for x in charactertypelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -charactertype- ")
                if lowercase_combination in [x.lower() for x in objectstoholdlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -objectstohold- ")
                if lowercase_combination in [x.lower() for x in episodetitlelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -episodetitle- ")
                
                if lowercase_combination in [x.lower() for x in flufferlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -fluff- ")

                if lowercase_combination in [x.lower() for x in occultlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -occult- ")
                if lowercase_combination in [x.lower() for x in locationfantasylist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -locationfantasy- ")
                if lowercase_combination in [x.lower() for x in locationscifilist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -locationscifi- ")
                if lowercase_combination in [x.lower() for x in locationvideogamelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -locationvideogame- ")
                if lowercase_combination in [x.lower() for x in locationbiomelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -locationbiome- ")
                if lowercase_combination in [x.lower() for x in locationcitylist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -locationcity- ")

                if lowercase_combination in [x.lower() for x in birdlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -bird- ")              
                if lowercase_combination in [x.lower() for x in catlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -cat- ")
                if lowercase_combination in [x.lower() for x in doglist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -dog- ")
                if lowercase_combination in [x.lower() for x in insectlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -insect- ")
                if lowercase_combination in [x.lower() for x in pokemonlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -pokemon- ")
                if lowercase_combination in [x.lower() for x in marinelifelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -marinelife- ")

                if lowercase_combination in [x.lower() for x in pokemontypelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -pokemontype- ")
                
                #if lowercase_combination in [x.lower() for x in conceptprefixlist] and chance_roll(insanitylevel, "uncommon"):
                #    prompt = prompt.replace(combination," -conceptprefix- ")

                
                if lowercase_combination in [x.lower() for x in culturelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -culture- ")

                
                if lowercase_combination in [x.lower() for x in descriptorlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -descriptor- ")

                if lowercase_combination in [x.lower() for x in outfitdescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -outfitdescriptor- ")
                if lowercase_combination in [x.lower() for x in hairdescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -hairdescriptor- ")
                if lowercase_combination in [x.lower() for x in hairvomitlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -hairvomit- ")
                if lowercase_combination in [x.lower() for x in humandescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -humandescriptor- ")
                if lowercase_combination in [x.lower() for x in locationdescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -locationdescriptor- ")
                if lowercase_combination in [x.lower() for x in basicbitchdescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -basicbitchdescriptor- ")
                if lowercase_combination in [x.lower() for x in animaldescriptorlist] and chance_roll(insanitylevel, "rare"):
                    prompt = prompt.replace(combination," -animaldescriptor- ")

                if lowercase_combination in [x.lower() for x in directionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -direction- ")

                if lowercase_combination in [x.lower() for x in emojilist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -emoji- ")

                if lowercase_combination in [x.lower() for x in humanexpressionlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -humanexpression- ")
                if lowercase_combination in [x.lower() for x in humanvomitlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -humanvomit- ")
                
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
                if lowercase_combination in [x.lower() for x in manwomanmultiplelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -manwomanmultiple- ")
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
                if lowercase_combination in [x.lower() for x in cardnamelist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -cardname- ")
                if lowercase_combination in [x.lower() for x in coveringlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -covering- ")
                if lowercase_combination in [x.lower() for x in facepartlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -facepart- ")


                if lowercase_combination in [x.lower() for x in fantasyartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -fantasyartist- ")
                if lowercase_combination in [x.lower() for x in popularartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -popularartist- ")
                if lowercase_combination in [x.lower() for x in romanticismartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -romanticismartist- ")
                if lowercase_combination in [x.lower() for x in photographyartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -photographyartist- ")
                if lowercase_combination in [x.lower() for x in portraitartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -portraitartist- ")
                if lowercase_combination in [x.lower() for x in characterartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -characterartist- ")
                if lowercase_combination in [x.lower() for x in landscapeartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -landscapeartist- ")
                if lowercase_combination in [x.lower() for x in scifiartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -scifiartist- ")
                if lowercase_combination in [x.lower() for x in graphicdesignartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -graphicdesignartist- ")
                if lowercase_combination in [x.lower() for x in architectartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -architectartist- ")
                if lowercase_combination in [x.lower() for x in cinemaartistlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -cinemaartist- ")


                if lowercase_combination in [x.lower() for x in stylestiloralist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -styletilora- ")
                if lowercase_combination in [x.lower() for x in waterlocationlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -waterlocation- ")

                if lowercase_combination in [x.lower() for x in allstylessuffixlist] and chance_roll(insanitylevel, "uncommon"):
                    prompt = prompt.replace(combination," -allstylessuffix- ")

            runs += 1
    
    # If nothing changed...  Lets do at least something
    if(prompt.lower().strip() == originaloriginalprompt.lower().strip()):
        if(random.randint(0,1)==0):
            prompt += basicenhance
        else:
            prompt = basicenhance + ", " + prompt

        if(chance_roll(insanitylevel, "common")):
            prompt += basicenhance

        if(chance_roll(insanitylevel, "common")):
            enhance_positive_words = enhance_positive(prompt, 1)
            prompt += enhance_positive_words

        prompt = parse_custom_functions(prompt, insanitylevel)


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
        "-outfitfromfile-" in completeprompt or
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
        "-fantasyartist-" in completeprompt or 
        "-popularartist-" in completeprompt or 
        "-romanticismartist-" in completeprompt or 
        "-photographyartist-" in completeprompt or
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
        "-manwomanmultiple-" in completeprompt or
        "-waterlocation-" in completeprompt or
        "-container-" in completeprompt or
        "-firstname-" in completeprompt or
        "-flora-" in completeprompt or
        "-print-" in completeprompt or
        "-miniactivity-" in completeprompt or
        "-pattern-" in completeprompt or
        "-chair-" in completeprompt or
        "-cardname-" in completeprompt or
        "-covering-" in completeprompt or
        "-outfitdescriptor-" in completeprompt or
        "-hairdescriptor-" in completeprompt or
        "-hairvomit-" in completeprompt or
        "-humandescriptor-" in completeprompt or
        "-facepart-" in completeprompt or
        "-locationdescriptor-" in completeprompt or
        "-basicbitchdescriptor-" in completeprompt or
        "-animaldescriptor-" in completeprompt or
        "-humanexpression-" in completeprompt or
        "-humanvomit-" in completeprompt or
        "-eyecolor-" in completeprompt or
        "-fashiondesigner-" in completeprompt or
        "-colorcombination-" in completeprompt or
        "-materialcombination-" in completeprompt or
        "-photoaddition-" in completeprompt or
        "-age-" in completeprompt or
        "-agecalculator-" in completeprompt or
        "-gregmode-" in completeprompt or
        "-portraitartist-" in completeprompt or
        "-characterartist-" in completeprompt or
        "-landscapeartist-" in completeprompt or
        "-scifiartist-" in completeprompt or
        "-graphicdesignartist-" in completeprompt or
        "-digitalartist-" in completeprompt or
        "-architectartist-" in completeprompt or
        "-cinemaartist-" in completeprompt or
        "-element-" in completeprompt or
        "-setting-" in completeprompt or
        "-charactertype-" in completeprompt or
        "-objectstohold-" in completeprompt or
        "-episodetitle-" in completeprompt or
        "-allstylessuffix-" in completeprompt or
        "-fluff-" in completeprompt or
        "-event-" in completeprompt or
        "-background-" in completeprompt or
        "-occult-" in completeprompt or
        "-locationfantasy-" in completeprompt or
        "-locationscifi-" in completeprompt or
        "-locationvideogame-" in completeprompt or
        "-locationbiome-" in completeprompt or
        "-locationcity-" in completeprompt or
         "-bird-" in completeprompt or
        "-cat-" in completeprompt or
        "-dog-" in completeprompt or
        "-insect-" in completeprompt or
        "-pokemon-" in completeprompt or
        "-pokemontype-" in completeprompt or
        "-marinelife-" in completeprompt
        ):
            allwildcardslistnohybrid = [ "-color-","-object-", "-animal-", "-fictional-","-nonfictional-","-building-","-vehicle-","-location-","-conceptprefix-","-food-","-haircolor-","-hairstyle-","-job-", "-accessory-", "-humanoid-", "-manwoman-", "-human-", "-colorscheme-", "-mood-", "-genderdescription-", "-artmovement-", "-malefemale-", "-bodytype-", "-minilocation-", "-minilocationaddition-", "-pose-", "-season-", "-minioutfit-", "-elaborateoutfit-", "-minivomit-", "-vomit-", "-rpgclass-", "-subjectfromfile-", "-outfitfromfile-", "-brand-", "-space-", "-artist-", "-imagetype-", "-othertype-", "-quality-", "-lighting-", "-camera-", "-lens-","-imagetypequality-", "-poemline-", "-songline-", "-greatwork-", "-fantasyartist-", "-popularartist-", "-romanticismartist-", "-photographyartist-", "-emoji-", "-timeperiod-", "-shotsize-", "-musicgenre-", "-animaladdition-", "-objectaddition-", "-humanaddition-", "-overalladdition-", "-focus-", "-direction-", "-styletilora-", "-manwomanrelation-", "-waterlocation-", "-container-", "-firstname-", "-flora-", "-print-", "-miniactivity-", "-pattern-", "-chair-", "-cardname-", "-covering-", "-outfitdescriptor-", "-hairdescriptor-", "-hairvomit-", "-humandescriptor-", "-manwomanmultiple-", "-facepart-", "-locationdescriptor-", "-basicbitchdescriptor-", "-animaldescriptor-", "-humanexpression-", "-humanvomit-", "-eyecolor-", "-fashiondesigner-", "-colorcombination-", "-materialcombination-", "-photoaddition-", "-age-", "-agecalculator-", "-gregmode-"
                                        ,"-portraitartist-", "-characterartist-" , "-landscapeartist-", "-scifiartist-", "-graphicdesignartist-", "-digitalartist-", "-architectartist-", "-cinemaartist-", "-setting-", "-charactertype-", "-objectstohold-", "-episodetitle-", "-allstylessuffix-", "-fluff-", "-event-", "-background-"
                                        , "-occult-", "-locationfantasy-", "-locationscifi-", "-locationvideogame-", "-locationbiome-", "-locationcity-", "-bird-", "-cat-", "-dog-", "-insect-", "-pokemon-", "-pokemontype-", "-marinelife-"]
            allwildcardslistnohybridlists = [colorlist, objectlist, animallist, fictionallist, nonfictionallist, buildinglist, vehiclelist, locationlist,conceptprefixlist,foodlist,haircolorlist, hairstylelist,joblist, accessorielist, humanoidlist, manwomanlist, humanlist, colorschemelist, moodlist, genderdescriptionlist, artmovementlist, malefemalelist, bodytypelist, minilocationlist, minilocationadditionslist, poselist, seasonlist, minioutfitlist, elaborateoutfitlist, minivomitlist, vomitlist, rpgclasslist, customsubjectslist, customoutfitslist, brandlist, spacelist, artistlist, imagetypelist, othertypelist, qualitylist, lightinglist, cameralist, lenslist, imagetypequalitylist, poemlinelist, songlinelist, greatworklist, fantasyartistlist, popularartistlist, romanticismartistlist, photographyartistlist, emojilist, timeperiodlist, shotsizelist, musicgenrelist, animaladditionlist, objectadditionslist, humanadditionlist, overalladditionlist, focuslist, directionlist, stylestiloralist, manwomanrelationlist, waterlocationlist, containerlist, firstnamelist, floralist, printlist, miniactivitylist, patternlist, chairlist, cardnamelist, coveringlist, outfitdescriptorlist, hairdescriptorlist, hairvomitlist, humandescriptorlist, manwomanmultiplelist, facepartlist, locationdescriptorlist, basicbitchdescriptorlist, animaldescriptorlist, humanexpressionlist, humanvomitlist, eyecolorlist, fashiondesignerlist, colorcombinationlist, materialcombinationlist, photoadditionlist, agelist, agecalculatorlist, gregmodelist
                                             , portraitartistlist, characterartistlist, landscapeartistlist, scifiartistlist, graphicdesignartistlist, digitalartistlist, architectartistlist, cinemaartistlist, settinglist, charactertypelist, objectstoholdlist, episodetitlelist, allstylessuffixlist, flufferlist, eventlist, backgroundlist
                                             , occultlist, locationfantasylist, locationscifilist, locationvideogamelist, locationbiomelist, locationcitylist, birdlist, catlist, doglist, insectlist, pokemonlist, pokemontypelist, marinelifelist]
            
            allwildcardslistwithhybrid = ["-material-", "-descriptor-", "-outfit-", "-conceptsuffix-","-culture-", "-objecttotal-", "-outfitprinttotal-", "-element-"]
            allwildcardslistwithhybridlists = [materiallist, descriptorlist,outfitlist,conceptsuffixlist,culturelist, objecttotallist, outfitprinttotallist, elementlist]
            
            
            #  keywordsinstring = any(word.lower() in givensubject.lower() for word in keywordslist)
            for wildcard in allwildcardslistnohybrid:
                attachedlist = allwildcardslistnohybridlists[allwildcardslistnohybrid.index(wildcard)]
                completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,False, advancedprompting)


            
            for wildcard in allwildcardslistwithhybrid:
                attachedlist = allwildcardslistwithhybridlists[allwildcardslistwithhybrid.index(wildcard)]
                completeprompt = replacewildcard(completeprompt, insanitylevel, wildcard, attachedlist,True, advancedprompting)


        
    # clean it up
    completeprompt = cleanup(completeprompt, advancedprompting, insanitylevel)
    




    return completeprompt

    # function
def replacewildcard(completeprompt, insanitylevel, wildcard,listname, activatehybridorswap, advancedprompting, artiststyleselector = ""):

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
                if(wildcard not in ["-heshe-", "-himher-","-hisher-"]):
                    listname.remove(replacementvalue)


                
            else:
                replacementvalue = ""

            # override for artist and artiststyle, only for first artist
            if(wildcard == "-artist-" and ("-artiststyle-" in completeprompt or "-artistmedium-" in completeprompt or "-artistdescription-" in completeprompt)):
                artiststyles = []
                artiststyle = []
                chosenartiststyle = ""
                artistscomplete = artist_category_by_category_csv_to_list("artists_and_category",replacementvalue)
                artiststyles = artistscomplete[0]
                artistmediums = artistscomplete[1]
                artistdescriptions = artistscomplete[2]
                artiststyle = [x.strip() for x in artiststyles[0].split(",")]

                artiststyle = list(filter(lambda x: len(x) > 0, artiststyle)) # remove empty values

                if(artiststyleselector in artiststyle):
                    artiststyle.remove(artiststyleselector)

                # Sorry folks, this only works when you directly select it as a style
                if("nudity" in artiststyle):
                    artiststyle.remove("nudity")

                # keep on looping until we have no more wildcards or no more styles to choose from
                # leftovers will be removed in the cleaning step
                while bool(artiststyle) and "-artiststyle-" in completeprompt:
                
                    chosenartiststyle = random.choice(artiststyle)
                    completeprompt = completeprompt.replace("-artiststyle-",chosenartiststyle ,1)
                    artiststyle.remove(chosenartiststyle)

                if("-artistmedium-" in completeprompt):
                    if(artistmediums[0].lower() not in completeprompt.lower()):
                        completeprompt = completeprompt.replace("-artistmedium-",artistmediums[0] ,1)

                if("-artistdescription-" in completeprompt):
                    completeprompt = completeprompt.replace("-artistdescription-",artistdescriptions[0] ,1)
                
                while bool(artiststyle) and "-artiststyle-" in completeprompt:
                
                    chosenartiststyle = random.choice(artiststyle)
                    completeprompt = completeprompt.replace("-artiststyle-",chosenartiststyle ,1)
                    artiststyle.remove(chosenartiststyle)

            
            
            # Sneaky overrides for "same" wildcards
            # Are overwritten with their first parent
            if(wildcard == "-outfit-" or wildcard == "-minioutfit-"):
                completeprompt = completeprompt.replace("-sameoutfit-", replacementvalue,1)

            # Why do it in this detail?? Because we can:
            # Check if "from" exists in the string. For example Chun Li from Streetfighter, becomes Chun li
            if "from" in replacementvalue:
                # Find the index of "from" in the string
                from_index = replacementvalue.find("from")

                # Remove everything from and including "from"
                replacementvalueforoverrides = replacementvalue[:from_index].strip()
            else:
                replacementvalueforoverrides = replacementvalue

            if(wildcard in ["-human-"
                            ,"-humanoid-"
                            , "-manwoman-"                            
                            , "-manwomanrelation-"
                            , "-manwomanmultiple-"]
                            and "-samehumansubject-" in completeprompt):
                            if(completeprompt.index(wildcard) < completeprompt.index("-samehumansubject-")):
                                completeprompt = completeprompt.replace("-samehumansubject-", "the " + replacementvalueforoverrides)
            
            if(wildcard in ["-fictional-"
                            , "-nonfictional-"
                            , "-firstname-"
                            , "-oppositefictional-"
                            , "-oppositenonfictional-"]
                            and "-samehumansubject-" in completeprompt):
                            if(completeprompt.index(wildcard) < completeprompt.index("-samehumansubject-")):
                                completeprompt = completeprompt.replace("-samehumansubject-", replacementvalueforoverrides)
            
            # job is here, to prevent issue with a job outfit being replace. So doing it later solves that issue
            if(wildcard in ["-job-"]
                            and "-samehumansubject-" in completeprompt):
                            if(completeprompt.index(wildcard) < completeprompt.index("-samehumansubject-")):
                                completeprompt = completeprompt.replace("-samehumansubject-", "the " + replacementvalueforoverrides)
            
            
            # This one last, since then it is the only subject we have left
            if(wildcard in ["-malefemale-"]
               and "-samehumansubject-" in completeprompt):
               if(completeprompt.index(wildcard) < completeprompt.index("-samehumansubject-")):
                    completeprompt = completeprompt.replace("-samehumansubject-", "the " + replacementvalueforoverrides)

            if(wildcard in ["-animal-"                         
                            , "-object-"
                            , "-vehicle-"
                            , "-food-"
                            , "-objecttotal-" 
                            , "-space-"
                            , "-flora-"
                            , "-location-"
                            , "-building-"]
                        and "-sameothersubject-" in completeprompt):
                if(completeprompt.index(wildcard) < completeprompt.index("-sameothersubject-")):
                            completeprompt = completeprompt.replace("-sameothersubject-", "the " + replacementvalueforoverrides)



            completeprompt = completeprompt.replace(wildcard, replacementvalue,1)
            
            


    return completeprompt

def build_dynamic_negative(positive_prompt = "", insanitylevel = 0, enhance = False, existing_negative_prompt = "", base_model="SD1.5"):


    negative_primer = []
    negative_result = []
    all_negative_words_list = []
    remove_weights = False

    # Base model options, used to change things in prompt generation. Might be able to extend to different forms like animatediff as well?
    base_model_options = ["SD1.5", "SDXL", "Stable Cascade"]
    if base_model not in base_model_options:
        base_model = "SD1.5" # Just in case there is no option here.
    # "SD1.5" -- Standard, future: More original style prompting
    # "SDXL" -- Standard (for now), future: More natural language
    # "Stable Cascade" -- Remove weights
    if base_model == "Stable Cascade":
        remove_weights = True
    
    # negavite_primer, all words that should trigger a negative result
    # the negative words to put in the negative prompt
    negative_primer, negative_result = load_negative_list()

    # do a trick for artists, replace with their tags instead
    artistlist, categorylist = load_all_artist_and_category()
    # lower them
    artist_names = [artist.strip().lower() for artist in artistlist]

    # note, should we find a trick for some shorthands of artists??
    artistshorthands = csv_to_list(csvfilename="artistshorthands",directory="./csvfiles/special_lists/",delimiter="?")
    for shorthand in artistshorthands:
        parts = shorthand.split(';')
        if parts[0] in positive_prompt:
            positive_prompt = positive_prompt.lower().replace(parts[0].lower(), parts[1].lower())


    for artist_name, category in zip(artist_names, categorylist):
        positive_prompt = positive_prompt.lower().replace(artist_name, category)


    allwords = split_prompt_to_words(positive_prompt)

    
    #lower all!
    
    for word in allwords:
        if(word.lower() in negative_primer):
            index_of_word = negative_primer.index(word.lower())
            all_negative_words_list.append(negative_result[index_of_word])
    
    all_negative_words = ", ".join(all_negative_words_list)
    all_negative_words_list = all_negative_words.split(",")
    all_negative_words_list = [elem.strip().lower() for elem in all_negative_words_list]

    

            

    if enhance == True:
        enhancelist = ["worst quality", "low quality", "normal quality", "lowres", "low details", "oversaturated", "undersaturated", "overexposed", "underexposed", "grayscale", "bw", "bad photo", "bad photography", "bad art", "watermark", "signature", "text font", "username", "error", "logo", "words", "letters", "digits", "autograph", "trademark", "name", "blur", "blurry", "grainy", "ugly", "asymmetrical", "poorly lit", "bad shadow", "draft", "cropped", "out of frame", "cut off", "censored", "jpeg artifacts", "out of focus", "glitch", "duplicate"]
        all_negative_words_list += enhancelist
    

    # new lets remove some based on the reverse insanitylevel
    removalchance = int((insanitylevel) * 10)

    for i in range(len(all_negative_words_list)):
        if(random.randint(1, 100)<removalchance):
            all_negative_words_list.pop(random.randint(0, len(all_negative_words_list)-1))

    # remove anything that is in the prompt itself, so no conflict of words!
            
    all_negative_words_list = [word for word in all_negative_words_list if word not in allwords]
    
    # Now compound it, and use the (word:1.3) type syntax:
    # Use a dictionary to count occurrences
    word_count = {}
    for word in all_negative_words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Convert the list to unique values or (word:count) format
    unique_words = []
    for word, count in word_count.items():
        if(count > 2 and remove_weights == False):
            #counttotal = int(count/2)
            counttotal = count
            if(counttotal > 3):
                counttotal = 3
            unique_words.append(f"({word}:1.{counttotal})")
        else:
            unique_words.append(word)

    negative_result = ", ".join(unique_words)

    negative_result += ", " + existing_negative_prompt

    return negative_result

def enhance_positive(positive_prompt = "", amountofwords = 3):

 
    wordcombilist = csv_to_list(csvfilename="wordcombis", directory="./csvfiles/special_lists/",delimiter="?")

    # do a trick for artists, replace with their tags instead
    artistlist, categorylist = load_all_artist_and_category()
    # lower them
    artist_names = [artist.strip().lower() for artist in artistlist]

    # note, should we find a trick for some shorthands of artists??
    artistshorthands = csv_to_list(csvfilename="artistshorthands",directory="./csvfiles/special_lists/",delimiter="?")
    for shorthand in artistshorthands:
        parts = shorthand.split(';')
        if parts[0] in positive_prompt:
            positive_prompt = positive_prompt.lower().replace(parts[0].lower(), parts[1].lower())


    for artist_name, category in zip(artist_names, categorylist):
        positive_prompt = positive_prompt.lower().replace(artist_name, category)

    allwords = split_prompt_to_words(positive_prompt)
    allwords = [elem.strip().lower() for elem in allwords] # lower them

    newwordlist = []
    addwords = ""
    wordsfound = 0
   
    #lower all!

    for combiset in wordcombilist:

        combiwords = set(combiset.split(', '))
        for combiword in combiwords:
            for word in allwords:
                if(word.lower() == combiword.lower()):

                    wordsfound += 1
                    combiwords2 = set(combiset.split(', '))
                    # remove and only take one
                    combiwords2 = [word for word in combiwords2 if word not in allwords]
                    #for combiword2 in combiwords2:
                    if(combiwords2):
                        newwordlist.append(random.choice(combiwords2))
                    
    
    
    newwordlist = [word for word in newwordlist if word not in allwords]
    newwordlist = list(set(newwordlist)) # make unique
    
    
    for i in range(0,amountofwords):
        if(len(newwordlist) > 0):
               addwords += ", " + newwordlist.pop(random.randrange(len(newwordlist)))
               #print(addwords)
    

    return addwords

def artify_prompt(insanitylevel = 5, prompt = "", artists = "all", amountofartists = "1", mode="standard", seed = -1):
    if(amountofartists=="random"):
        intamountofartists = random.randint(1,int((insanitylevel/3) + 1.20))
    else:    
        intamountofartists = int(amountofartists)


    # set seed
    # For use in ComfyUI (might bring to Automatic1111 as well)
    # lets do it when its larger than 0
    # Otherwise, just do nothing and it will keep on working based on an earlier set seed
    if(seed > 0):
        random.seed(seed)


    # first build up a complete anti list. Those values are removing during list building
    # this uses the antivalues string AND the antilist.csv
    emptylist = []
    antilist = csv_to_list("antilist",emptylist , "./userfiles/",1)
    
    # clean up antivalue list:
    antilist = [s.strip().lower() for s in antilist]

     # build artists list
    if artists == "wild":
        artists = "all (wild)"

    # we want to create more cohorence, so we are adding all (wild) mode for the old logic
    
    artisttypes = ["popular", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", "cinema",	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
    artiststyleselector = ""
    artiststyleselectormode = "normal"
    artiststyleselector = random.choice(artisttypes)

    artistlist = []
    # create artist list to use in the code, maybe based on category  or personal lists
    if(artists != "all (wild)" and artists != "all" and artists != "none" and artists.startswith("personal_artists") == False and artists.startswith("personal artists") == False and artists in artisttypes):
        artistlist = artist_category_csv_to_list("artists_and_category",artists)
    elif(artists.startswith("personal_artists") == True or artists.startswith("personal artists") == True):
        artists = artists.replace(" ","_",-1) # add underscores back in
        artistlist = csv_to_list(artists,antilist,"./userfiles/")
    elif(artists != "none"):
        artistlist = csv_to_list("artists",antilist)
    

    # load up the styles list for the other modes
    styleslist = csv_to_list("styles", antilist,"./csvfiles/templates/",0,"?")
    stylessuffix = [item.split('-subject-')[1] for item in styleslist]
    breakstylessuffix = [item.split(',') for item in stylessuffix]
    allstylessuffixlist = [value for sublist in breakstylessuffix for value in sublist]
    allstylessuffixlist = list(set(allstylessuffixlist))

    artistsuffix = artist_descriptions_csv_to_list("artists_and_category")
    breakartiststylessuffix = [item.split(',') for item in artistsuffix]
    artiststylessuffixlist = [value for sublist in breakartiststylessuffix for value in sublist]
    artiststylessuffixlist = list(set(artiststylessuffixlist))
    allstylessuffixlist += artiststylessuffixlist

    completeprompt = ""
    if(common_dist(insanitylevel)):
        completeprompt += "-artiststyle- "
    completeprompt += "art by "
    #Lets go effing artify this MF'er
        
    for i in range(0,intamountofartists):
        if(intamountofartists > 1 and i == intamountofartists - 2):
            completeprompt += "-artist- and "
        else:
            completeprompt += "-artist-, "
    
    if(uncommon_dist(insanitylevel)):
        completeprompt += "-artistmedium-, " 
            
    # now add the prompt in
    completeprompt += prompt

    if(mode.lower() == "remix"):
        for i in range(0,intamountofartists):
            completeprompt += ", " + artistsuffix.pop(artistsuffix.index(random.choice(artistsuffix)))

    elif(mode.lower() == "super remix turbo"):
        for i in range(0,intamountofartists*4):
            completeprompt += ", " + allstylessuffixlist.pop(allstylessuffixlist.index(random.choice(allstylessuffixlist)))

    else:
        # else just go standard
        for i in range(0,intamountofartists):
            completeprompt += ", -artistdescription-"
    
    
    
    
    while ("-artist-" in completeprompt):

        completeprompt = replacewildcard(completeprompt,5,"-artist-", artistlist,"","",artiststyleselector)


    return completeprompt


def flufferizer(prompt = "", amountoffluff = "dynamic", seed = -1, reverse_polarity = False):
    if(amountoffluff == "none"):
        return prompt
    
    # set seed
    # For use in ComfyUI (might bring to Automatic1111 as well)
    # lets do it when its larger than 0
    # Otherwise, just do nothing and it will keep on working based on an earlier set seed
    if(seed > 0):
        random.seed(seed)
    
    if(reverse_polarity):
        flufferlist = csv_to_list("antifluff") # all negative words
    else:
        flufferlist = csv_to_list("fluff")

    # dynamic = based on prompt length + insanitylevel
    minfluff = 4
    maxfluff = 6
    # short = 4-6
    # medium = 5-8
    # long = 8-12
    if(amountoffluff == "dynamic"):
        
        if(len(prompt) < 150):
            amountoffluff = "long"
        elif(len(prompt) < 250):
            amountoffluff = "medium"
        else:
            amountoffluff = "short"

    if(amountoffluff == "long"):
        minfluff = 8
        maxfluff = 12
    if(amountoffluff == "medium"):
        minfluff = 5
        maxfluff = 8
    
    for i in range(0,random.randint(minfluff, maxfluff)):
        prompt += ", " + flufferlist.pop(flufferlist.index(random.choice(flufferlist)))
    
    return prompt


    

def replace_match(match):
    # Extract the first word from the match
    words = match.group(0)[1:-1].split('|')
    return words[0]

def cleanup(completeprompt, advancedprompting, insanitylevel = 5):

    # This part is turned off, will bring it back later as an option
    
    # first, move LoRA's to the back dynamically

    # Find all occurrences of text between < and > using regex
    # allLoRA = re.findall(r"<[^>]+>", completeprompt)

    # Remove the extracted matches from completeprompt
    # completeprompt = re.sub(r"<[^>]+>", "", completeprompt)


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
    completeprompt = re.sub(r'\(\:\d+\.\d+\)', '', completeprompt)

    # lets also remove some wierd stuff on lower insanitylevels
    if(insanitylevel < 7):
        completeprompt = completeprompt.replace("DayGlo", " ")
        completeprompt = completeprompt.replace("fluorescent", " ")

    # all cleanup steps moved here
    completeprompt = re.sub(r'\[ ', '[', completeprompt)
    completeprompt = re.sub(r'\[,', '[', completeprompt)
    completeprompt = re.sub(r' \]', ']', completeprompt)
    completeprompt = re.sub(r' \|', '|', completeprompt)
    #completeprompt = re.sub(r' \"', '\"', completeprompt)
    #completeprompt = re.sub(r'\" ', '\"', completeprompt)
    completeprompt = re.sub(r'\( ', '(', completeprompt)
    completeprompt = re.sub(r' \(', '(', completeprompt)
    completeprompt = re.sub(r'\) ', ')', completeprompt)
    completeprompt = re.sub(r' \)', ')', completeprompt)

    completeprompt = re.sub(' :', ':', completeprompt)
    completeprompt = re.sub(',::', '::', completeprompt)
    completeprompt = re.sub(',:', ':', completeprompt)

    completeprompt = re.sub(',,', ', ', completeprompt)
    completeprompt = re.sub(',,', ', ', completeprompt)
    completeprompt = re.sub(',,,', ', ', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(' , ', ', ', completeprompt)
    completeprompt = re.sub(' ,', ',', completeprompt)
    completeprompt = re.sub(' ,', ',', completeprompt)
    completeprompt = re.sub(' ,', ',', completeprompt)
    completeprompt = re.sub(r',\(', ', (', completeprompt)



    while "  " in completeprompt:
        completeprompt = re.sub('  ', ' ', completeprompt)
    completeprompt = re.sub('a The', 'The', completeprompt)
    completeprompt = re.sub('the the', 'the', completeprompt)
    completeprompt = re.sub(', ,', ',', completeprompt)
    completeprompt = re.sub(',,', ',', completeprompt)

    completeprompt = re.sub(', of a', ' of a', completeprompt)
    completeprompt = re.sub('of a,', 'of a', completeprompt)
    completeprompt = re.sub('of a of a', 'of a', completeprompt)
    completeprompt = re.sub(' a a ', ' a ', completeprompt)

    # a / an
    completeprompt = re.sub(' a a', ' an a', completeprompt)
    completeprompt = re.sub(' a e', ' an e', completeprompt)
    completeprompt = re.sub(' a i', ' an i', completeprompt)
    completeprompt = re.sub(' a u', ' an u', completeprompt)
    completeprompt = re.sub(' a o', ' an o', completeprompt)


    completeprompt = re.sub('art art', 'art', completeprompt)
    completeprompt = re.sub('Art art', 'art', completeprompt)
    completeprompt = re.sub('lighting lighting', 'lighting', completeprompt)
    completeprompt = re.sub('Lighting lighting', 'lighting', completeprompt)
    completeprompt = re.sub('light lighting', 'light', completeprompt)
    completeprompt = re.sub('-artiststyle- art,', '', completeprompt)
    completeprompt = re.sub('-artiststyle- art', '', completeprompt)
    completeprompt = re.sub('-artiststyle-', '', completeprompt)
    completeprompt = re.sub('-artistmedium-', '', completeprompt)
    completeprompt = re.sub('-artistdescription-', '', completeprompt)
    completeprompt = re.sub('- art ', '', completeprompt)

    completeprompt = re.sub('anime anime', 'anime', completeprompt)
    completeprompt = re.sub('anime, anime', 'anime', completeprompt)

    completeprompt = re.sub('shot shot', 'shot', completeprompt)
    

    completeprompt = re.sub('a his', 'his', completeprompt)
    completeprompt = re.sub('a her', 'her', completeprompt)
    completeprompt = re.sub('they is', 'they are', completeprompt)
    completeprompt = re.sub('they has', 'they have', completeprompt)

    # some space tricks
    completeprompt = re.sub('- shaped', '-shaped', completeprompt)
    completeprompt = re.sub('echa- ', 'echa-', completeprompt)
    completeprompt = re.sub('style -', 'style-', completeprompt)
    completeprompt = re.sub(', as a', ' as a', completeprompt)


    #small fix for multisubject thing
    completeprompt = re.sub('a 2', '2', completeprompt)
    completeprompt = re.sub('a 3', '3', completeprompt)
    completeprompt = re.sub('a 4', '4', completeprompt)
    completeprompt = re.sub('a 5', '5', completeprompt)


    # clean up some hacky multiples with adding a s to the end
    completeprompt = re.sub('fs ', 'ves ', completeprompt)
    completeprompt = re.sub('fs,', 'ves,', completeprompt)
    completeprompt = re.sub('sss ', 'ss ', completeprompt)
    completeprompt = re.sub('sss,', 'ss,', completeprompt)
    completeprompt = re.sub(' Mans', ' Men,', completeprompt)
    completeprompt = re.sub(' mans', ' men', completeprompt)
    completeprompt = re.sub(' Womans,', ' Women', completeprompt)
    completeprompt = re.sub(' womans,', ' women,', completeprompt)
    completeprompt = re.sub(r'\(Mans', '(Men,', completeprompt)
    completeprompt = re.sub(r'\(mans', '(men', completeprompt)
    completeprompt = re.sub(r'\(Womans', '(Women', completeprompt)
    completeprompt = re.sub(r'\(womans', '(women', completeprompt)

    completeprompt = re.sub('-sameothersubject-', 'it', completeprompt)
    completeprompt = re.sub('-samehumansubject-', 'the person', completeprompt)

    
    completeprompt = re.sub(r'(?<!\()\s?\(', ' (', completeprompt)
    completeprompt = re.sub(r'\)(?![\s)])', ') ', completeprompt)

    # Move the extracted LoRA's to the end of completeprompt
    #completeprompt += " " + " ".join(allLoRA)   

    completeprompt = completeprompt.replace(' . ', '. ')
    completeprompt = completeprompt.replace(', . ', '. ')
    completeprompt = completeprompt.replace(',. ', '. ')
    completeprompt = completeprompt.replace('., ', '. ')
    completeprompt = completeprompt.replace('. . ', '. ')

    completeprompt = completeprompt.strip(", ")

    return completeprompt

def custom_or(values, insanitylevel = 5):
    # Check if the last element is one of the specific values
    last_element = values[-1]
    first_element = values[0]

   
    if last_element in ['always', 'common', 'normal','uncommon', 'rare', 'legendary','unique', 'extraordinary', 'novel', 'never']:
        # If we do not hit the change roll, then take the first element.
        if not(chance_roll(insanitylevel, last_element)):
            return first_element
        # Else anything but the first or last element
        else:
            values.remove(first_element)
            values.remove(last_element)
            selected_value = random.choice(values)
            return selected_value


    else:
        # Randomly select one element from the list
        selected_value = random.choice(values)
    return selected_value

def parse_custom_functions(completeprompt, insanitylevel = 5):
    #print(completeprompt)

    # Regular expression pattern to match 'or()' function calls and their arguments
    ORpattern = r'OR\((.*?)\)'
    ORbasesearch = 'OR('



    while re.findall(ORpattern, completeprompt):

        # basically start from right to left to start replacing, so we can do nesting
        # probably not very stable, but seems to work :)
        startofOR = completeprompt.rfind(ORbasesearch)

        lastpartofcompleteprompt = completeprompt[startofOR:]
 
        # Find all 'or()' function calls and their arguments in the text
        matches = re.findall(ORpattern, lastpartofcompleteprompt)

        # Sort the matches based on the length of the OR expressions
        matches.sort(key=len)


        match = matches[0] # get the first value, so smallest goes first!

        or_replacement = ""


        # Split the arguments by ';'
        arguments = [arg.strip() for arg in match.split(';')]
        
        # Evaluate the 'or()' function and append the result to the results list

        # For debugging, enable these lines
        #print(completeprompt)
        #print(arguments)
        or_replacement = custom_or(arguments, insanitylevel)
        completematch = 'OR(' + match + ')'
        completeprompt = completeprompt.replace(completematch, or_replacement)

    

    return completeprompt

def split_prompt_to_words(text):
        # first get all the words

        # Use a regular expression to replace non-alphabetic characters with spaces
        text = re.sub(r'[^a-zA-Z,-]', ' ', text)

        # Split the string by commas and spaces
        words = re.split(r'[,\s]+', text)
        # Remove leading/trailing whitespaces from each word
        words = [word.strip() for word in words]

        # Filter out empty words
        words = [word for word in words if word]

        # Convert the list to a set to remove duplicates, then convert it back to a list
        listsinglewords = list(set(words))

        # now get all words clumped together by commas
        if ',' in text:
            allwords = text.split(',')
        else:
            allwords = [text]
        # Remove leading/trailing whitespaces from each word and convert to lowercase
        words = [word.strip().lower() for word in allwords]

        # Filter out empty words and duplicates
        listwords = list(set(filter(None, words)))

        totallist = listsinglewords + listwords

        totallist = list(set(filter(None, totallist)))

        return totallist

def one_button_superprompt(insanitylevel = 5, prompt = "", seed = -1, override_subject = "" , override_outfit = "", chosensubject ="", gender = "", restofprompt = "", superpromptstyle = "", setnewtokens = 0, remove_bias = True):

    if(seed <= 0):
        seed = random.randint(1,1000000)
    
    done = False
    load_models()

    superprompterstyleslist = csv_to_list("superprompter_styles")
    descriptorlist = csv_to_list("descriptors")
    devmessagessuperpromptlist = csv_to_list("devmessages_superprompt")

    usestyle = False
    if(superpromptstyle != "" and superpromptstyle != "all"):
        usestyle = True

    restofprompt = restofprompt.lower()
    question = ""

    # first, move LoRA's to the back dynamically

    # Find all occurrences of text between < and > using regex
    allLoRA = re.findall(r"<[^>]+>", prompt)

    # Remove the extracted matches from completeprompt
    prompt = re.sub(r"<[^>]+>", "", prompt)
    override_subject = re.sub(r"<[^>]+>", "", override_subject)
    
    temperature_lookup = {
    1: 0.01,
    2: 0.1,
    3: 0.3,
    4: 0.5,
    5: 0.6,
    6: 0.7,
    7: 1.0,
    8: 2.5,
    9: 5.0,
    10: 10.0
    }

    max_new_tokens_lookup = {
    1: 45,
    2: 45,
    3: 50,
    4: 55,
    5: 60,
    6: 70,
    7: 90,
    8: 100,
    9: 150,
    10: 255
    }

    top_p_lookup = {
    1: 0.1,
    2: 1.0,
    3: 1.3,
    4: 1.5,
    5: 1.6,
    6: 1.75,
    7: 2.0,
    8: 3.0,
    9: 5.0,
    10: 15.0
    }

    chosensubject_lookup = {
    "humanoid": "fantasy character",
    "manwomanrelation": "person",
    "manwomanmultiple": "people",
    "firstname": "",
    "job": "person",
    "fictional": "fictional character",
    "non fictional": "person",
    "human": "person",
    "animal": "animal",
    "animal as human": "human creature",
    "landscape": "landscape",
    "concept": "concept",
    "event": "concept",
    "concept": "concept",
    "poemline": "concept",
    "songline": "concept",
    "cardname": "concept",
    "episodetitle": "concept",
    "generic objects": "object",
    "vehicles": "vehicle",
    "food": "food",
    "building": "building",
    "space": "space",
    "flora": "nature",
    }
    # for insanitylevel in range(1,11):
    j = 0
    temperature = temperature_lookup.get(insanitylevel, 0.5)
    if(setnewtokens < 1):
        max_new_tokens = max_new_tokens_lookup.get(insanitylevel, 70)
    else:
        max_new_tokens = setnewtokens
    top_p = top_p_lookup.get(insanitylevel, 1.6)
    subject_to_generate = chosensubject_lookup.get(chosensubject, "")

    translation_table_remove_stuff = str.maketrans('', '', '.,:()<>|[]"" ')
    translation_table_remove_numbers = str.maketrans('', '', '0123456789:()<>|[]""')

     # check if its matching all words from the override:
    possible_words_to_check = override_subject.lower().split() + override_outfit.lower().split()
    #print(possible_words_to_check)
    words_to_check = []
    words_to_remove = ['subject', 'solo', '1girl', '1boy']
    for word in possible_words_to_check:
        word = word.translate(translation_table_remove_stuff)
        #print(word)
        if word not in words_to_remove:
            if (not word.startswith("-") and not word.endswith("-")) and (not word.startswith("_") and not word.endswith("_")) :
                words_to_check.append(word)

    #print(words_to_check)
    if chosensubject not in ("humanoid","firstname","job","fictional","non fictional","human"):
        gender = ""
    if(superpromptstyle == "" or superpromptstyle == "all"):
        if "fantasy" in restofprompt or "d&d" in restofprompt or "dungeons and dragons" in restofprompt or "dungeons and dragons" in restofprompt:
            superpromptstyle = "fantasy style"
        elif "sci-fi" in restofprompt or "scifi" in restofprompt or "science fiction" in restofprompt:
            superpromptstyle = random.choice(["sci-fi style","futuristic"])
        elif "cyberpunk" in restofprompt:
            superpromptstyle = "cyberpunk"
        elif "horror" in restofprompt:
            superpromptstyle = "horror themed"
        elif "evil" in restofprompt:
            superpromptstyle = "evil"
        elif "cinestill" in restofprompt or "movie still" in restofprompt or "cinematic" in restofprompt or "epic" in restofprompt:
            superpromptstyle = random.choice(["cinematic","epic"])
        elif "fashion" in restofprompt:
            superpromptstyle = random.choice(["elegant","glamourous"])
        elif "cute" in restofprompt or "adorable" in restofprompt or "kawaii" in restofprompt:
            superpromptstyle = random.choice(["cute","adorable", "kawaii"])

        else:
            superpromptstyle = random.choice(superprompterstyleslist)

    if(words_to_check):
        question += "Make sure the subject is used: " + ', '.join(words_to_check) + " \n"

    imagetype = ""
    if "portrait" in restofprompt:
        imagetype = "a portrait"
    elif "painting" in restofprompt:
        imagetype = "a painting"
    elif "digital art" in restofprompt:
        imagetype = "a digital artwork"
    elif "concept" in restofprompt:
        imagetype = "concept art"
    elif "pixel" in restofprompt:
        imagetype = "pixel art"
    elif "game" in restofprompt:
        imagetype = "video game artwork"
    
    if imagetype != "" and (normal_dist(insanitylevel) or usestyle == True):
        question += "Expand the following " + gender + " " + subject_to_generate + " prompt to describe " + superpromptstyle + " " + imagetype + ": "
    elif imagetype != "":
        question += "Expand the following " + gender + " " + subject_to_generate + " prompt to describe " + imagetype + ": "
    elif(normal_dist(insanitylevel) or usestyle == True):
        question += "Expand the following " + gender + " " + subject_to_generate + " prompt to make it more " + superpromptstyle
    else:
        question += "Expand the following " + gender + " " + subject_to_generate + " prompt to add more detail: "



    prompt = prompt.translate(translation_table_remove_numbers)

    while done == False:
        #print(seed)
        #print(temperature)
        #print(top_p)
        #print(question)
        #print("chosen subject: " + chosensubject)
        
    	
        superpromptresult = answer(input_text=question + prompt, max_new_tokens=max_new_tokens, repetition_penalty=2.0, temperature=temperature, top_p=top_p, top_k=10, seed=seed)

        #print("orignal: " + prompt)
        #print("insanitylevel: " + str(insanitylevel))
        #print("")
        #print("complete superprompt: " + superpromptresult)
        #print("")

        # Find the indices of the nearest period and comma
        period_index = superpromptresult.rfind('.')
        comma_index = superpromptresult.rfind(',')

        # Determine the index to cut off the string
        cut_off_index = max(period_index, comma_index)

        # Cut off the string at the determined index
        if cut_off_index != -1:  # If either period or comma exists
            superpromptresult = superpromptresult[:cut_off_index + 1]  # Include the period or comma
        else:
            superpromptresult = superpromptresult  # If neither period nor comma exists, keep the entire text

        # piercing green eyes problem
        # basically, the model has some biasses, lets get rid of it, OBP style!
        if(common_dist(insanitylevel) and remove_bias): # but not always
            superpromptresult = remove_superprompt_bias(superpromptresult=superpromptresult, insanitylevel=insanitylevel, override_outfit=override_outfit)
            
       
        #print(words_to_check)
        # Iterate through each word and check if it exists in the other string
        i = 0
        for word in words_to_check:
            if word not in superpromptresult.lower() and word != "subject":
                i += 1
                
        
        if(i==0 or j == 20 or insanitylevel >= 9):
            done = True
        # slowly converge and change
        else:
            seed += 100
            j += 1
            if(temperature < 0.5):
                temperature += 0.05 + round((1/random.randint(15,25)),2)
            else:
                temperature -= 0.1

            if(top_p < 1.0):
                top_p += 0.2 + round((1/random.randint(25,35)),2)
            else:
                top_p -= 0.3
            max_new_tokens += 3
            print("")
            print(random.choice(devmessagessuperpromptlist) + "... Retrying...")
            print("")
            
        

    superpromptresult += " " + " ".join(allLoRA)

    return superpromptresult

def remove_superprompt_bias(superpromptresult = "", insanitylevel = 5, override_outfit = ""):

    if(" green eye" in superpromptresult):
        eyecolorslist = csv_to_list("eyecolors")
        eyecolorslist = [x for x in eyecolorslist if not x.startswith('-')]
        neweyecolor = " " + random.choice(eyecolorslist).lower() + " eye"
        #print(neweyecolor)
        superpromptresult = superpromptresult.replace(" green eye", neweyecolor)
    #  white gown  or white dress
    if(" white gown" in superpromptresult 
        or " white dress" in superpromptresult
        or " black suit" in superpromptresult):
        colorcombinationslist = csv_to_list("colorcombinations")
        colorcombinationslist = [x for x in colorcombinationslist if not x.startswith('-')]
        colorslist = csv_to_list("colors")
        colorslist = [x for x in colorslist if not x.startswith('-')]
        if(normal_dist(insanitylevel)):
            newcolordress = " " + random.choice(colorcombinationslist).lower() + " dress"
            newcolorgown = " " + random.choice(colorcombinationslist).lower() + " gown"
            newcolorsuit = " " + random.choice(colorcombinationslist).lower() + " suit"
        else:
            newcolordress = " " + random.choice(colorslist).lower() + " dress"
            newcolorgown = " " + random.choice(colorslist).lower() + " gown"
            newcolorsuit = " " + random.choice(colorcombinationslist).lower() + " suit"
        #print(newcolordress)                
        #print(newcolorgown)                
        #print(newcolorsuit)
        superpromptresult = superpromptresult.replace(" white dress", newcolordress)
        superpromptresult = superpromptresult.replace(" white gown", newcolorgown)
        superpromptresult = superpromptresult.replace(" black suit", newcolorsuit)
    if(" gown" in superpromptresult 
        or " dress" in superpromptresult 
        or " suit" in superpromptresult
        and not "gown" in override_outfit 
        and not "dress" in override_outfit
        and not "suit " in override_outfit
        and not " dressed" in superpromptresult
        and not " suited" in superpromptresult):
        if(override_outfit == ""):
            outfitslist = csv_to_list("outfits")
            outfitslist = [x for x in outfitslist if not x.startswith('-')]
            newoutfit = " " + random.choice(outfitslist).lower()
        else:
            newoutfit = " " + override_outfit
        superpromptresult = superpromptresult.replace(" dress", newoutfit)
        superpromptresult = superpromptresult.replace(" gown", newoutfit)
        superpromptresult = superpromptresult.replace(" suit", newoutfit)
    if(" sleek " in superpromptresult):
        
        descriptorslist = csv_to_list("descriptors")
        descriptorslist = [x for x in descriptorslist if not x.startswith('-')]
        newdescriptor = " " + random.choice(descriptorslist).lower() + " "
        #print(newdescriptor)

        superpromptresult = superpromptresult.replace(" sleek ", newdescriptor)
    ## lush green (meadow), sun shines down
    # A graceful woman with long, flowing hair stands on a lush green lawn, her arms spread wide as she kneels gently in the breeze. The sun shines down on her
    if("lush green meadow" in superpromptresult):
        
        backgroundlist = csv_to_list("backgrounds")
        backgroundlist = [x for x in backgroundlist if not x.startswith('-')]
        newbackground = random.choice(backgroundlist).lower()
        #print(newbackground)

        superpromptresult = superpromptresult.replace("lush green meadow", newbackground)

    if("long, flowing hair" in superpromptresult):
        
        hairstylelist = csv_to_list("hairstyles2")
        hairstylelist = [x for x in hairstylelist if not x.startswith('-')]
        newhairstyle = random.choice(hairstylelist).lower()
        #print(newhairstyle)

        superpromptresult = superpromptresult.replace("long, flowing hair", newhairstyle)
    
    return superpromptresult

def replace_user_wildcards(completeprompt):
    for i in range(0,10):
        user_wildcards_list = re.findall(r'-[\w_]*-', completeprompt)
        for user_wildcard in user_wildcards_list:
            user_wildcard_clean = user_wildcard.strip("-")
            wordlist = csv_to_list(csvfilename=user_wildcard_clean, directory="./userfiles/wildcards/")
            if(wordlist):
                completeprompt = completeprompt.replace(user_wildcard, random.choice(wordlist),1)

    return completeprompt

def translate_main_subject(main_subject=""):
    subjecttype_lookup = {
        "all": ["all", "all"],
        "random": ["all", "all"],
        "--- all": ["all", "all"],
        "------all": ["all", "all"],
        "------ all": ["all", "all"],

        "object - all": ["object", "all"],
        "--- object - all": ["object", "all"],
        "object": ["object", "all"],
        "object - generic": ["object", "all"],
        "generic object": ["object", "generic objects"],
        "generic objects": ["object", "generic objects"],
        "genericobject": ["object", "generic objects"],
        "genericobjects": ["object", "generic objects"],
        "object - vehicle": ["object", "vehicles"],
        "vehicle": ["object", "vehicles"],
        "vehicles": ["object", "vehicles"],
        "object - food": ["object", "food"],
        "food": ["object", "food"],
        "object - building": ["object", "buildings"],
        "building": ["object", "buildings"],
        "buildings": ["object", "buildings"],
        "object - space": ["object", "space"],
        "space": ["object", "space"],
        "object - flora": ["object", "flora"],
        "flora": ["object", "flora"],
        "nature": ["object", "flora"],

        "animal - all": ["animal", "all"],
        "--- animal - all": ["animal", "all"],
        "animal": ["animal", "all"],
        "animals": ["animal", "all"],
        "animal - generic": ["animal", "generic animal"],
        "generic animal": ["animal", "generic animal"],
        "generic animals": ["animal", "generic animal"],
        "genericanimal": ["animal", "generic animal"],
        "genericanimals": ["animal", "generic animal"],
        "animal - cat": ["animal", "cat"],
        "cat": ["animal", "cat"],
        "cats": ["animal", "cat"],
        "animal - dog": ["animal", "dog"],
        "dog": ["animal", "dog"],
        "dogs": ["animal", "dog"],
        "animal - bird": ["animal", "bird"],
        "bird": ["animal", "bird"],
        "birds": ["animal", "bird"],
        "animal - insect": ["animal", "insect"],
        "insect": ["animal", "insect"],
        "insects": ["animal", "insect"],
        "animal - pokémon": ["animal", "pokemon"],
        "animal - pokemon": ["animal", "pokemon"],
        "pokemon": ["animal", "pokemon"],
        "pokemons": ["animal", "pokemon"],
        "pokémon": ["animal", "pokemon"],
        "pokémons": ["animal", "pokemon"],
        "animal - marine life": ["animal", "marine life"],
        "marine life": ["animal", "marine life"],
        "marinelife": ["animal", "marine life"],
        "ocean gang": ["animal", "marine life"],
        "oceangang": ["animal", "marine life"],
        "marine": ["animal", "marine life"],

        "human - all": ["humanoid", "all"],
        "--- human - all": ["humanoid", "all"],
        "human": ["humanoid", "all"],
        "humans": ["humanoid", "all"],
        "person": ["humanoid", "all"],
        "persons": ["humanoid", "all"],
        "people": ["humanoid", "all"],
        "man": ["humanoid", "all"],
        "woman": ["humanoid", "all"],
        "male": ["humanoid", "all"],
        "female": ["humanoid", "all"],
        "guy": ["humanoid", "all"],
        "girl": ["humanoid", "all"],
        "human - generic": ["humanoid", "human"],
        "generic human": ["humanoid", "human"],
        "generic humans": ["humanoid", "human"],
        "generichuman": ["humanoid", "human"],
        "generichumans": ["humanoid", "human"],
        "human - relations": ["humanoid","manwomanrelation"],
        "relations": ["humanoid","manwomanrelation"],
        "human relations": ["humanoid","manwomanrelation"],
        "humanrelations": ["humanoid","manwomanrelation"],
        "human - celebrity": ["humanoid","non fictional"],
        "celebrities": ["humanoid","non fictional"],
        "celebrity": ["humanoid","non fictional"],
        "human - fictional": ["humanoid","fictional"],
        "fictional characters": ["humanoid","fictional"],
        "fictional character": ["humanoid","fictional"],
        "fictionalcharacters": ["humanoid","fictional"],
        "fictionalcharacter": ["humanoid","fictional"],
        "fictional": ["humanoid","fictional"],
        "human - humanoids": ["humanoid","humanoid"],
        "humanoid": ["humanoid","humanoid"],
        "humanoids": ["humanoid","humanoid"],
        "human - job/title": ["humanoid","job"],
        "job": ["humanoid","job"],
        "jobs": ["humanoid","job"],
        "title": ["humanoid","job"],
        "titles": ["humanoid","job"],
        "human - first name": ["humanoid","firstname"],
        "first name": ["humanoid","firstname"],
        "firstname": ["humanoid","firstname"],
        "human - multiple": ["humanoid","manwomanmultiple"], 
        "multiplehumans": ["humanoid","manwomanmultiple"], 
        "multiple": ["humanoid","manwomanmultiple"], 

        "landscape - all": ["landscape","all"],
        "--- landscape - all": ["landscape","all"],
        "landscape": ["landscape","all"],
        "landscapes": ["landscape","all"],
        "landscape - generic": ["landscape","location"],
        "landscape generic": ["landscape","location"],
        "landscapes generic": ["landscape","location"],
        "landscapegeneric": ["landscape","location"],
        "landscapesgeneric": ["landscape","location"],
        "genericlandscape": ["landscape","location"],
        "generic landscape": ["landscape","location"],
        "genericlandscapes": ["landscape","location"],
        "generic landscapes": ["landscape","location"],
        "landscape - fantasy": ["landscape","fantasy location"],
        "landscape fantasy": ["landscape","fantasy location"],
        "landscapefantasy": ["landscape","fantasy location"],
        "fantasylandscape": ["landscape","fantasy location"],
        "fantasy landscape": ["landscape","fantasy location"],
        "landscape - videogame": ["landscape","videogame location"],
        "landscape videogame": ["landscape","videogame location"],
        "landscapevideogame": ["landscape","videogame location"],
        "videogamelandscape": ["landscape","videogame location"],
        "videogame landscape": ["landscape","videogame location"],
        "landscape - sci-fi": ["landscape","sci-fi location"],
        "landscape sci-fi": ["landscape","sci-fi location"],
        "landscapesci-fi": ["landscape","sci-fi location"],
        "sci-filandscape": ["landscape","sci-fi location"],
        "sci-fi landscape": ["landscape","sci-fi location"],
        "landscape - scifi": ["landscape","sci-fi location"],
        "landscape scifi": ["landscape","sci-fi location"],
        "landscapescifi": ["landscape","sci-fi location"],
        "scifilandscape": ["landscape","sci-fi location"],
        "scifi landscape": ["landscape","sci-fi location"],
        "landscape - biome": ["landscape","biome"],
        "landscape biome": ["landscape","biome"],
        "landscapebiome": ["landscape","biome"],
        "biomelandscape": ["landscape","biome"],
        "biome landscape": ["landscape","biome"],
        "biome": ["landscape","biome"],
        "biomes": ["landscape","biome"],
        "landscape - city": ["landscape","city"],
        "landscape city": ["landscape","city"],
        "landscapecity": ["landscape","city"],
        "citylandscape": ["landscape","city"],
        "city landscape": ["landscape","city"],
        "city": ["landscape","city"],
        "cities": ["landscape","city"],

        "concept - all": ["concept", "all"],
        "--- concept - all": ["concept", "all"],
        "concept": ["concept", "all"],
        "concepts": ["concept", "all"],
        "concept - event": ["concept", "event"],
        "event": ["concept", "event"],
        "events": ["concept", "event"],
        "concept - the x of y": ["concept", "concept"],
        "xofy": ["concept", "concept"],
        "thexofy": ["concept", "concept"],
        "concept - poem lines": ["concept", "poemline"],
        "poem": ["concept", "poemline"],
        "poems": ["concept", "poemline"],
        "poemline": ["concept", "poemline"],
        "poemlines": ["concept", "poemline"],
        "concept - song lines": ["concept", "songline"],
        "song": ["concept", "songline"],
        "songs": ["concept", "songline"],
        "songline": ["concept", "songline"],
        "songlines": ["concept", "songline"],
        "concept - card names": ["concept", "cardname"],
        "cards": ["concept", "cardname"],
        "card": ["concept", "cardname"],
        "cardgame": ["concept", "cardname"],
        "cardgames": ["concept", "cardname"],
        "cardname": ["concept", "cardname"],
        "cardnames": ["concept", "cardname"],
        "concept - episode titles": ["concept", "episodetitle"],
        "episode": ["concept", "episodetitle"],
        "episodes": ["concept", "episodetitle"],
        "episodetitle": ["concept", "episodetitle"],
        "episodetitles": ["concept", "episodetitle"],
        "tv": ["concept", "episodetitle"],
        "tv shows": ["concept", "episodetitle"],
        "tvshows": ["concept", "episodetitle"],
        "concept - mixer": ["concept", "conceptmixer"],
        "concept mixer": ["concept", "conceptmixer"],
        "conceptmixer": ["concept", "conceptmixer"],
        "mixer": ["concept", "conceptmixer"],
    }

    subjecttype = subjecttype_lookup.get(main_subject, ["all", "all"])

    return subjecttype