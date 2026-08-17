import os
import json

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

class Config:
    def __init__(self, config_file):
        self.settings = load_config(config_file)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value

    def save(self, config_file):
        with open(config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)