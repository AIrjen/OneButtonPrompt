import sys
import os
import folder_paths
from datetime import datetime
import uuid
import platform
 
custom_nodes_path = os.path.join(folder_paths.base_path, "custom_nodes")
onebuttonprompt_path = os.path.join(custom_nodes_path, "OneButtonPrompt")

sys.path.append(onebuttonprompt_path)

from build_dynamic_prompt import *
from csv_reader import *

artists = ["all", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types", "only templates mode", "art blaster mode", "quality vomit mode", "color cannon mode", "unique art mode", "massive madness mode", "photo fantasy mode", "subject only mode", "fixed styles mode"]
subjects =["all", "object", "animal", "humanoid", "landscape", "concept"]
genders = ["all", "male", "female"]
emojis = [False, True]

subjects =["all"]
subjectsubtypesobject = ["all"]
subjectsubtypeshumanoid = ["all"]
subjectsubtypesconcept = ["all"]
#subjectsubtypesobject = ["all", "generic objects", "vehicles", "food", "buildings", "space", "flora"]
#subjectsubtypeshumanoid = ["all", "generic humans", "generic human relations", "celebrities e.a.", "fictional characters", "humanoids", "based on job or title", "based on first name"]
#subjectsubtypesconcept = ["all", "event", "the X of Y concepts", "lines from poems", "lines from songs"]


# Load up stuff for personal artists list, if any
# find all artist files starting with personal_artits in userfiles
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
userfilesfolder = os.path.join(script_dir, "./userfiles/" )
for filename in os.listdir(userfilesfolder):
    if(filename.endswith(".csv") and filename.startswith("personal_artists") and filename != "personal_artists_sample.csv"):
        name = os.path.splitext(filename)[0]
        name = name.replace("_"," ",-1).lower()
        # directly insert into the artists list
        artists.insert(2, name)

# on startup, check if we have a config file, or else create it
config = load_config_csv()  


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

# build up all subjects we can choose based on the loaded config file
if(generatevehicle or generateobject or generatefood or generatebuilding or generatespace):
     subjects.append("object")
if(generateanimal):
     subjects.append("animal")
if(generatemanwoman or generatemanwomanrelation or generatefictionalcharacter or generatenonfictionalcharacter or generatehumanoids or generatejob):
     subjects.append("humanoid")
if(generatelandscape):
     subjects.append("landscape")
if(generateevent or generateconcepts or generatepoemline or generatesongline):
     subjects.append("concept")


# do the same for the subtype subjects
# subjectsubtypesobject = ["all"]
# subjectsubtypeshumanoid = ["all"]
# subjectsubtypesconcept = ["all"]

# objects first
if(generateobject):
     subjectsubtypesobject.append("generic objects")
if(generatevehicle):
     subjectsubtypesobject.append("vehicles")
if(generatefood):
     subjectsubtypesobject.append("food")
if(generatebuilding):
     subjectsubtypesobject.append("buildings")
if(generatespace):
     subjectsubtypesobject.append("space")
if(generateflora):
     subjectsubtypesobject.append("flora")

# humanoids (should I review descriptions??)
if(generatemanwoman):
     subjectsubtypeshumanoid.append("generic humans")
if(generatemanwomanrelation):
     subjectsubtypeshumanoid.append("generic human relations")
if(generatenonfictionalcharacter):
     subjectsubtypeshumanoid.append("celebrities e.a.")
if(generatefictionalcharacter):
     subjectsubtypeshumanoid.append("fictional characters")
if(generatehumanoids):
     subjectsubtypeshumanoid.append("humanoids")
if(generatejob):
     subjectsubtypeshumanoid.append("based on job or title")
if(generatefirstnames):
     subjectsubtypeshumanoid.append("based on first name")

# concepts
if(generateevent):
     subjectsubtypesconcept.append("event")
if(generateconcepts):
     subjectsubtypesconcept.append("the X of Y concepts")
if(generatepoemline):
     subjectsubtypesconcept.append("lines from poems")
if(generatesongline):
     subjectsubtypesconcept.append("lines from songs")

class OneButtonPrompt:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "insanitylevel": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                },
            "optional": {
                "artist": (artists, {"default": "all"}),
                "imagetype": (imagetypes, {"default": "all"}),
                "imagemodechance": ("INT", {
                    "default": 20,
                    "min": 1, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1 #Slider's step
                }),
                "subject": (subjects, {"default": "all"}),
                "custom_subject": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": ""
                }),
                "subject_subtype_objects": (subjectsubtypesobject, {"default": "all"}),
                "subject_subtypes_humanoids": (subjectsubtypeshumanoid, {"default": "all"}),
                "humanoids_gender": (genders, {"default": "all"}),
                "subject_subtypes_concepts": (subjectsubtypesconcept, {"default": "all"}),
                "emojis":(emojis, {"default": False}),
                
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP"

    #OUTPUT_NODE = False

    CATEGORY = "OneButtonPrompt"
    
    def Comfy_OBP(self, insanitylevel, custom_subject,seed, artist,imagetype, subject, imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts, emojis):
        generatedprompt = build_dynamic_prompt(insanitylevel,subject,artist,imagetype,False,"","","",1,"",custom_subject,True,"",imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts, False, emojis)
        #print(generatedprompt)
        return (generatedprompt,)


class CreatePromptVariant:


    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {
                "prompt_input": ("STRING", {"default": '', "multiline": True}),
            },
            "optional": {
                "insanitylevel": ("INT", {
                    "default": 5,
                    "min": 1, #Minimum value
                    "max": 10, #Maximum value
                    "step": 1 #Slider's step
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP_PromptVariant"

    #OUTPUT_NODE = False

    CATEGORY = "OneButtonPrompt"
    
    def Comfy_OBP_PromptVariant(self, prompt_input, insanitylevel, seed):
        generatedprompt = createpromptvariant(prompt_input, insanitylevel)
        
        print(generatedprompt)
        
        return (generatedprompt,)

# Let us create our own prompt saver. Not everyone has WAS installed
class SavePromptToFile:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename_prefix": ("STRING", {"default": "Prompt"}),
                "positive_prompt": ("STRING",{"multiline": True}),
                "negative_prompt": ("STRING",{"multiline": True}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = "saveprompttofile"

    CATEGORY = "OneButtonPrompt"

    def saveprompttofile(self, positive_prompt, negative_prompt, filename_prefix):
        # Some stuff for the prefix
        filename_prefix += self.prefix_append

        # turns out there is some hardcoded stuff on saveimage we have to kind of repeat here
        # Find the %date:yyyy-M-d% pattern using regular expression
        pattern = r'%date:([^\%]+)%'
        match = re.search(pattern, filename_prefix)

        if match:
            # Extract the date format from the match
            date_format = match.group(1)

            # Get the current date
            current_date = datetime.now()

            # convert the ComfyUI standard into Python standard format.
            # What a crazy way of doing this
            # first lol, I got to make sure it doesn't overlap things
            date_format = date_format.replace('M', 'X')
            date_format = date_format.replace('m', 'Z')
            
            # This is so bad

            # lets make it even worse, it work differently on windows than in Linux
            if(platform.system() == 'Windows'):

                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%#y')
                date_format = date_format.replace('X', '%#m')
                date_format = date_format.replace('d', '%#d')
                date_format = date_format.replace('h', '%#H')
                date_format = date_format.replace('Z', '%#M')
                date_format = date_format.replace('s', '%#S')
            else:
                date_format = date_format.replace('yyyy', '%Y')
                date_format = date_format.replace('yy', '%-y')
                date_format = date_format.replace('X', '%-m')
                date_format = date_format.replace('d', '%-d')
                date_format = date_format.replace('h', '%-H')
                date_format = date_format.replace('Z', '%-M')
                date_format = date_format.replace('s', '%-S')


            # Format the date using the extracted format
            formatted_date = current_date.strftime(date_format)

            # Replace the matched pattern with the formatted date
            filename_prefix = re.sub(pattern, formatted_date, filename_prefix)
            

           

        full_output_folder, filename_short, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir)

        # make the filename, from from a to the first comma
        # find the index of the first comma after "of a" or end of the prompt
        if(positive_prompt.find("of a ") != -1):
            start_index = positive_prompt.find("of a ") + len("of a ")
            end_index = positive_prompt.find(",", start_index)
            if(end_index == -1):
                end_index=len(positive_prompt)
        else:
            start_index = 0
            end_index = 128
  
        # extract the desired substring using slicing
        filename = positive_prompt[start_index:end_index]

        # cleanup some unsafe things in the filename
        filename = filename.replace("\"", "")
        filename = filename.replace("[", "")
        filename = filename.replace("|", "")
        filename = filename.replace("]", "")
        filename = filename.replace("<", "")
        filename = filename.replace(">", "")
        filename = filename.replace(":", "_")
        filename = filename.replace(".", "")
        filename = re.sub(r'[0-9]+', '', filename)

        safe_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

        # Use regular expression to filter out any characters not in the whitelist
        filename = re.sub(r"[^{}]+".format(re.escape(''.join(safe_characters))), '', filename)
        

        if(filename==""):
            filename = str(uuid.uuid4())
        
        if(filename_prefix == ""):
        # create a datetime object for the current date and time
        # if there is no prefix
            now = datetime.now()
            filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip() + ".txt"
        
        else:
            # lol since we insert a file, the counter of the image goes up by 1.
            # So we add 1 here, so the prompt file matches the image file
            formatted_counter = str(counter + 1).zfill(5)
            filenamecomplete = filename_short + "_" + formatted_counter + "_" + filename.replace(" ", "_").strip() + ".txt"
    
        
        directoryandfilename = os.path.abspath(os.path.join(full_output_folder, filenamecomplete))
        

        with open(directoryandfilename, 'w', encoding="utf-8") as file:
            file.write("prompt: " + positive_prompt + "\n")
            file.write("negative prompt: " + negative_prompt + "\n")



        return ("done")

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OneButtonPrompt": OneButtonPrompt,
    "CreatePromptVariant": CreatePromptVariant,
    "SavePromptToFile": SavePromptToFile
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OneButtonPrompt": "One Button Prompt",
    "CreatePromptVariant": "Create Prompt Variant",
    "SavePromptToFile": "Save Prompt To File"
}
