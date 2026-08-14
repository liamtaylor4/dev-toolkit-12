import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, custom_config_path=None):
        self.default_config_path = default_config_path
        self.custom_config_path = custom_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_json(self.default_config_path)
        if self.custom_config_path:
            custom_config = self.load_json(self.custom_config_path)
            config.update(custom_config)
        return config

    def load_json(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json', 'custom_config.json')
    print(config_loader.get('some_key', 'default_value'))