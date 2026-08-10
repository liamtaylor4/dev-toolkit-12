import json

class CustomError(Exception):
    pass

class DataHandler:
    def __init__(self, data: str):
        self.data = data

    def process_data(self) -> dict:
        try:
            data_dict = json.loads(self.data)
            self.validate_data(data_dict)
            return data_dict
        except json.JSONDecodeError:
            raise CustomError('Invalid JSON format')
        except Exception as e:
            raise CustomError(f'An error occurred: {str(e)}')

    def validate_data(self, data: dict) -> None:
        if not isinstance(data, dict):
            raise CustomError('Data must be a dictionary')
        if 'required_key' not in data:
            raise CustomError('Missing required key in data')

# Example usage
if __name__ == '__main__':
    handler = DataHandler('{"required_key": "value"}')
    try:
        processed_data = handler.process_data()
        print(processed_data)
    except CustomError as e:
        print(e)