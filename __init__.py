import os
import sys

import folder_paths

from OneButtonPromptNodes import (NODE_CLASS_MAPPINGS,
                                  NODE_DISPLAY_NAME_MAPPINGS)

custom_nodes_path = os.path.join(folder_paths.base_path, "custom_nodes")
onebuttonprompt_path = os.path.join(custom_nodes_path, "OneButtonPrompt")
sys.path.append(onebuttonprompt_path)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
