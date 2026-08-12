class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def start(self):
        print(f"Starting {self.title}...")

    def stop(self):
        print(f"Stopping {self.title}...")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def earn_points(self, points):
        self.score += points

    def display_score(self):
        print(f"{self.name} Score: {self.score}")

if __name__ == '__main__':
    game = Game('Super Adventure', 'Adventure')
    player = Player('Alice')
    game.start()
    player.earn_points(100)
    player.display_score()
    game.stop()