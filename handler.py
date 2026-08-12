from typing import Any, Dict

class GameHandler:
    def __init__(self, game_data: Dict[str, Any]) -> None:
        self.game_data = game_data

    def start_game(self) -> str:
        return "Game started!"

    def end_game(self) -> str:
        return "Game ended!"

    def get_score(self) -> int:
        return self.game_data.get('score', 0)

    def update_score(self, score: int) -> None:
        self.game_data['score'] = score

    def reset_game(self) -> None:
        self.game_data.clear()
        self.game_data['score'] = 0

    def is_game_active(self) -> bool:
        return 'active' in self.game_data and self.game_data['active']

    def toggle_game_state(self) -> None:
        if 'active' in self.game_data:
            self.game_data['active'] = not self.game_data['active']
        else:
            self.game_data['active'] = True