class GameError(Exception):
    """Base class for exceptions in the game."
    pass

class PlayerError(GameError):
    """Exception raised for errors related to the player."
    def __init__(self, message: str) -> None:
        super().__init__(message)

class LevelError(GameError):
    """Exception raised for errors related to game levels."
    def __init__(self, level: int, message: str) -> None:
        self.level = level
        super().__init__(message)

class ItemError(GameError):
    """Exception raised for errors related to game items."
    def __init__(self, item_name: str, message: str) -> None:
        self.item_name = item_name
        super().__init__(message)

class NetworkError(GameError):
    """Exception raised for network-related errors."
    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        super().__init__(message)