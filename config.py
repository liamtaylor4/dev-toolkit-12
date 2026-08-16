import json
import os

DEFAULTS = {
    'setting1': 'default_value1',
    'setting2': 10,
    'setting3': True
}

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    config = json.load(file)
                except json.JSONDecodeError:
                    return DEFAULTS
            return {**DEFAULTS, **config}
        return DEFAULTS

    def get(self, key):
        return self.config.get(key, DEFAULTS.get(key))

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)