import json

class GameProcessor:
    def __init__(self):
        self.valid_inputs = ['start', 'stop', 'pause', 'resume']

    def process_input(self, user_input):
        if self.validate_input(user_input):
            # process the valid input
            return json.dumps({'status': 'success', 'action': user_input})
        return json.dumps({'status': 'error', 'message': 'Invalid input'})

    def validate_input(self, user_input):
        return user_input in self.valid_inputs

    def main_loop(self):
        while True:
            user_input = input('Enter command: ')
            response = self.process_input(user_input)
            print(response)
            if user_input == 'stop':
                break

if __name__ == '__main__':
    processor = GameProcessor()
    processor.main_loop()