import json

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, new_data):
    data = load_game_data(file_path)
    data.update(new_data)
    save_game_data(file_path, data)


def get_player_score(data, player_id):
    return data.get('players', {}).get(player_id, {}).get('score', 0)


def set_player_score(data, player_id, score):
    if 'players' not in data:
        data['players'] = {}
    data['players'][player_id] = data['players'].get(player_id, {})
    data['players'][player_id]['score'] = score


def initialize_game_data():
    return {'players': {}, 'settings': {}}