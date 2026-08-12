import json

class ConfigLoader:
    def __init__(self, defaults):
        self.defaults = defaults
        self.config = defaults.copy()

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON file')

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    defaults = {'volume': 70, 'resolution': '1920x1080', 'fullscreen': True}
    config_loader = ConfigLoader(defaults)
    config_loader.load('config.json')
    print(config_loader.get('volume'))