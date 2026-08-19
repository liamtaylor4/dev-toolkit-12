import json
from typing import Any, Dict

class GameDataHandler:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load_data(self) -> Dict[str, Any]:
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_data(self, data: Dict[str, Any]) -> None:
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def update_data(self, key: str, value: Any) -> None:
        data = self.load_data()
        data[key] = value
        self.save_data(data)