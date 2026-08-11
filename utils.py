import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_dict(data, keys):
    return {key: data[key] for key in keys if key in data}


def paginate_list(data, page, page_size):
    start = (page - 1) * page_size
    return data[start:start + page_size}