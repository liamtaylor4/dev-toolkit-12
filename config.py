from typing import Dict, Any

class Config:
    """Handles configuration settings for the application."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings

    def get(self, key: str) -> Any:
        """Retrieve a setting by key."""
        return self.settings.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self.settings[key] = value

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update multiple settings at once."""
        self.settings.update(new_settings)

    def all_settings(self) -> Dict[str, Any]:
        """Return all settings as a dictionary."""
        return self.settings
