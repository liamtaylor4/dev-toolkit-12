import json

class InputError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InputError('Input must be a dictionary')
    required_keys = ['name', 'age']
    for key in required_keys:
        if key not in data:
            raise InputError(f'Missing required key: {key}')
    if not isinstance(data['age'], int) or data['age'] < 0:
        raise InputError('Age must be a non-negative integer')

def process_data(data):
    validate_input(data)
    return {'status': 'success', 'processed': data}

def main_loop():
    inputs = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': -1},
        {'name': 'Charlie'}
    ]
    for input_data in inputs:
        try:
            result = process_data(input_data)
            print(json.dumps(result))
        except InputError as e:
            print(f'Input Error: {e}')

if __name__ == '__main__':
    main_loop()