class GameError(Exception):
    pass

class PlayerError(GameError):
    def __init__(self, message):
        super().__init__(message)

class LevelError(GameError):
    def __init__(self, level, message):
        self.level = level
        super().__init__(message)

class InventoryError(GameError):
    def __init__(self, item, message):
        self.item = item
        super().__init__(message)

class NetworkError(GameError):
    def __init__(self, message):
        super().__init__(message)
        self.retry_count = 0

    def increment_retry(self):
        self.retry_count += 1

    def reset_retry(self):
        self.retry_count = 0

class ResourceError(GameError):
    def __init__(self, resource, message):
        self.resource = resource
        super().__init__(message)