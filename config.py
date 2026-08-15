import json
import os

class ConfigLoader:
    def __init__(self, default_config=None, config_file='config.json'):
        self.default_config = default_config or {}
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
            return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

# Example default configuration
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'volume': 75,
    'language': 'en'
}

if __name__ == '__main__':
    config_loader = ConfigLoader(DEFAULT_CONFIG)
    print(config_loader.get('volume'))