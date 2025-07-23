import os
import sys
import folder_paths

onebuttonprompt_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(onebuttonprompt_path)

from .OneButtonPromptNodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']