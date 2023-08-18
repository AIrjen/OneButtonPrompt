import sys
import os
import folder_paths
from datetime import datetime
import uuid
 
custom_nodes_path = os.path.join(folder_paths.base_path, "custom_nodes")
onebuttonprompt_path = os.path.join(custom_nodes_path, "OneButtonPrompt")

sys.path.append(onebuttonprompt_path)

from build_dynamic_prompt import *

artists = ["all", "none", "popular", "greg mode", "3D",	"abstract",	"angular", "anime"	,"architecture",	"art nouveau",	"art deco",	"baroque",	"bauhaus", 	"cartoon",	"character",	"children's illustration", 	"cityscape", 	"clean",	"cloudscape",	"collage",	"colorful",	"comics",	"cubism",	"dark",	"detailed", 	"digital",	"expressionism",	"fantasy",	"fashion",	"fauvism",	"figurativism",	"gore",	"graffiti",	"graphic design",	"high contrast",	"horror",	"impressionism",	"installation",	"landscape",	"light",	"line drawing",	"low contrast",	"luminism",	"magical realism",	"manga",	"melanin",	"messy",	"monochromatic",	"nature",	"nudity",	"photography",	"pop art",	"portrait",	"primitivism",	"psychedelic",	"realism",	"renaissance",	"romanticism",	"scene",	"sci-fi",	"sculpture",	"seascape",	"space",	"stained glass",	"still life",	"storybook realism",	"street art",	"streetscape",	"surrealism",	"symbolism",	"textile",	"ukiyo-e",	"vibrant",	"watercolor",	"whimsical"]
imagetypes = ["all", "all - force multiple",  "photograph", "octane render","digital art","concept art", "painting", "portrait", "anime key visual", "only other types", "only templates mode", "art blaster mode", "quality vomit mode", "color cannon mode", "unique art mode", "massive madness mode", "photo fantasy mode", "subject only mode", "fixed styles mode"]
subjects =["all", "object", "animal", "humanoid", "landscape", "concept"]
genders = ["all", "male", "female"]

subjectsubtypesobject = ["all", "generic objects", "vehicles", "food", "buildings", "space", "flora"]
subjectsubtypeshumanoid = ["all", "generic humans", "generic human relations", "celebrities e.a.", "fictional characters", "humanoids", "based on job or title", "based on first name"]
subjectsubtypesconcept = ["all", "event", "the X of Y concepts", "lines from poems", "lines from songs"]
    

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
                
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "Comfy_OBP"

    #OUTPUT_NODE = False

    CATEGORY = "OneButtonPrompt"
    
    def Comfy_OBP(self, insanitylevel, custom_subject,seed, artist,imagetype, subject, imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts):
        generatedprompt = build_dynamic_prompt(insanitylevel,subject,artist,imagetype,False,"","","",1,"",custom_subject,True,"",imagemodechance, humanoids_gender, subject_subtype_objects, subject_subtypes_humanoids, subject_subtypes_concepts, False)
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
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive_prompt": ("STRING",{"multiline": True}),
                "negative_prompt": ("STRING",{"multiline": True}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = "saveprompttofile"

    CATEGORY = "OneButtonPrompt"

    def saveprompttofile(self, positive_prompt, negative_prompt):
        
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
        filename = re.sub(r'[0-9]+', '', filename)

        safe_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

        # Use regular expression to filter out any characters not in the whitelist
        filename = re.sub(r"[^{}]+".format(re.escape(''.join(safe_characters))), '', filename)
        

        if(filename==""):
            filename = str(uuid.uuid4())
        
        # create a datetime object for the current date and time
        now = datetime.now()
        filenamecomplete = now.strftime("%Y%m%d%H%M%S") + "_" + filename.replace(" ", "_").strip() + ".txt"
       
        
        # Get the output folder from comfy
        output_directory = folder_paths.output_directory
        
        directoryandfilename = os.path.abspath(os.path.join(output_directory, filenamecomplete))
        

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
