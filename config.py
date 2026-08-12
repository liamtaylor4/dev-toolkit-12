import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                return {**self.default_config, **json.load(file)}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    default_config = {
        'game_name': 'MyGame',
        'version': '1.0',
        'window_size': [800, 600],
        'fullscreen': False
    }
    config_loader = ConfigLoader(default_config)
    print(config_loader.get('game_name'))