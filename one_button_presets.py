import json
import os
import shutil


class OneButtonPresets:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
    DEFAULT_OBP_FILE = os.path.join(script_dir, "./presets/obp_presets.default")
    OBP_FILE = os.path.join(script_dir, "./userfiles/obp_presets.json")
    CUSTOM_OBP = "Custom..."
    RANDOM_PRESET_OBP = "All (random)..."

    def __init__(self):
        self.opb_presets = self.load_obp_presets()

    def load_obp_presets(self):
        default_data = self._load_data(self.DEFAULT_OBP_FILE)
        data = self._load_data(self.OBP_FILE)

        for name, settings in default_data.items():
            if name not in data:
                data[name] = settings

        self._save_data(self.OBP_FILE, data)
        return data

    def _load_data(self, file_path):
        if not os.path.isfile(file_path):
            shutil.copy(self.DEFAULT_OBP_FILE, file_path)
        return json.load(open(file_path))

    def _save_data(self, file_path, data):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

    def save_obp_preset(self, perf_options):
        with open(self.OBP_FILE, "w") as f:
            json.dump(perf_options, f, indent=2)
        self.opb_presets = self.load_obp_presets()

    def get_obp_preset(self, name):
        return self.opb_presets[name]
