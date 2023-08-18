from fastapi import FastAPI, Body
import gradio as gr
from build_dynamic_prompt import *
from scripts.onebuttonprompt import subjects, artists, imagetypes

def one_button_prompt_api(_: gr.Blocks, app: FastAPI):
    @app.get("/one_button_prompt/version")
    async def version():
        return {"version": 1.0}

    @app.get("/one_button_prompt/config")
    async def get_config():

        config ={
             "subjects": subjects,
             "artists": artists,
             "imagetypes": imagetypes,

        }
        return config 

    @app.post("/one_button_prompt/prompt/random")
    async def random_prompts(numberofprompts:int = Body(1,title="number of prompts"),
        insanitylevel: int= Body(5,title="insanity level"),
        forcesubject: str =Body('all',title="force subject"),
        artists : str =Body('all',title="artists"),
        imagetype : str =Body('all',title="image type"),
        onlyartists: bool =Body(False,title="only artists"),
        antivalues : str =Body('',title="anti values"),
        prefixprompt: str =Body('',title="prefix prompt"),
        suffixprompt: str =Body('',title="suffix prompt"),
        promptcompounderlevel: str =Body('1',title="prompt compounder level"),
        seperator: str =Body('comma',title="seperator"),
        givensubject: str =Body('',title="givensubject"),
        smartsubject:bool = Body(True,title='smart subject'),
        giventypeofimage: str = Body('',title='given type of image'),
        imagemodechance: int  = Body(20,title='image mode chance'),
        gender: str = Body('all',title='gender'),
        subtypeobject: str = Body('all',title='subtypeobject'),
        subtypehumanoid: str = Body('all', title='subtypehumanoid'), 
        subtypeconcept: str = Body('all', title='subtypeconcept'),
        advancedprompting:bool = Body(True,title='advancedprompting'),
        hardturnoffemojis:bool = Body(False,title='hardturnoffemojis')
        ):

            
            keys = ['insanitylevel', 'forcesubject', 'artists', 'imagetype', 'onlyartists', 'antivalues', 'prefixprompt',
            'suffixprompt', 'promptcompounderlevel', 'seperator', 'givensubject', 'smartsubject', 'giventypeofimage',
            'imagemodechance', 'gender', 'subtypeobject','subtypehumanoid','subtypeconcept','advancedprompting','hardturnoffemojis']
            payload = {}
            for key in keys:
                payload[key] = locals()[key]
            
            prompts = [build_dynamic_prompt(**payload) for _ in range(numberofprompts)]
            return {"prompts": prompts}


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(one_button_prompt_api)
except:
    pass
