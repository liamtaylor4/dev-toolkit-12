from typing import Any, Dict, List

def validate_integer(value: Any) -> bool:
    """Validates if the provided value is an integer."""
    return isinstance(value, int)


def validate_string(value: Any) -> bool:
    """Validates if the provided value is a string."""
    return isinstance(value, str)


def validate_range(value: int, min_value: int, max_value: int) -> bool:
    """Validates if the integer value is within the specified range."""
    return min_value <= value <= max_value


def validate_list_of_integers(values: List[Any]) -> bool:
    """Validates if all elements in the list are integers."""
    return all(validate_integer(val) for val in values)


def validate_config(config: Dict[str, Any]) -> bool:
    """Validates the configuration dictionary for required types."""
    return (validate_integer(config.get('max_players')) and 
            validate_string(config.get('game_mode')) and 
            validate_list_of_integers(config.get('player_scores', [])))
