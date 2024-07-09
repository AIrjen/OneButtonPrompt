#!/usr/bin/env python
import os
import random
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

if __package__ is None or __package__ == '':
    # A1111 style (standalone script or direct module execution)
    # Use absolute imports for compatibility with A1111 WebUI environment
    from download_models import download_models
else:
    # ComfyUI style (imported as a package)
    # Use relative imports for proper integration with ComfyUI
    from .download_models import download_models

global tokenizer, model
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
modelDir = os.path.join(script_dir, "./model_files/" )

def load_models():
 
    if not all(os.path.exists(modelDir) for file in modelDir):
        print("Model files not found. Downloading...\n")
        download_models()
    # else:
        # print("Model files found. Skipping download.\n")

    # print("Loading SuperPrompt-v1 model...\n")


    global tokenizer, model
    tokenizer = T5Tokenizer.from_pretrained(modelDir)
    model = T5ForConditionalGeneration.from_pretrained(modelDir, torch_dtype=torch.float16)

    # print("SuperPrompt-v1 model loaded successfully.\n")

def unload_models():
    global tokenizer, model
    del tokenizer
    del model

    for file in os.listdir(modelDir):
        os.remove(os.path.join(modelDir, file))
    os.rmdir(modelDir)



def answer(input_text="", max_new_tokens=512, repetition_penalty=1.2, temperature=0.5, top_p=1, top_k = 1 , seed=-1):
       
    if seed == -1:
        seed = random.randint(1, 1000000)

    torch.manual_seed(seed)

    if torch.cuda.is_available():
        device = 'cuda'
    else:
        device = 'cpu'

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
    if torch.cuda.is_available():
        model.to('cuda')

    outputs = model.generate(input_ids, max_new_tokens=max_new_tokens, repetition_penalty=repetition_penalty,
                            do_sample=True, temperature=temperature, top_p=top_p, top_k=top_k)

    dirty_text = tokenizer.decode(outputs[0])
    text = dirty_text.replace("<pad>", "").replace("</s>", "").strip()

    return text
