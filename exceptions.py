class GameError(Exception):
    """Base class for exceptions in the game toolkit."""

class InvalidInputError(GameError):
    """Exception raised for invalid input arguments."""

    def __init__(self, message: str) -> None:
        super().__init__(message)

class ResourceNotFoundError(GameError):
    """Exception raised when a required resource is not found."""

    def __init__(self, resource_name: str) -> None:
        message = f'Resource not found: {resource_name}'
        super().__init__(message)

class GameOverError(GameError):
    """Exception raised when the game is over."""

    def __init__(self) -> None:
        super().__init__('The game is over.')

class ConnectionError(GameError):
    """Exception raised for connection issues."""

    def __init__(self, host: str, port: int) -> None:
        message = f'Connection failed to {host}:{port}'
        super().__init__(message)