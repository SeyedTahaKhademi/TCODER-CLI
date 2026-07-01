import os
from pathlib import Path
import sys
from typing import Optional

from tcoder.config.models import Config, Settings
from tcoder.core.exceptions import ConfigError

# Handle tomllib for Python <3.11
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

import tomli_w


class ConfigManager:
    """Manages configuration loading and saving."""

    def __init__(self, settings: Optional[Settings] = None, config_dir: Optional[Path] = None):
        self.settings = settings or Settings()
        self.config_dir = config_dir or Path(self.settings.tcoder_home).expanduser()
        self.config_file = self.config_dir / "config.toml"
        self._config: Optional[Config] = None

    def ensure_config_dir(self) -> None:
        """Ensure config directory exists."""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            # If we can't create the directory, use current directory for testing
            self.config_dir = Path.cwd()
            self.config_file = self.config_dir / "config.toml"

    def load_config(self) -> Config:
        """Load configuration from file."""
        self.ensure_config_dir()

        if not self.config_file.exists():
            self._config = Config()
            self.save_config(self._config)
            return self._config

        try:
            with open(self.config_file, "rb") as f:
                data = tomllib.load(f)
            self._config = Config(**data)
            return self._config
        except Exception as e:
            raise ConfigError(f"Failed to load config: {e}") from e

    def save_config(self, config: Config) -> None:
        """Save configuration to file."""
        self.ensure_config_dir()
        try:
            with open(self.config_file, "wb") as f:
                tomli_w.dump(config.model_dump(exclude_none=True), f)
            self._config = config
        except Exception as e:
            raise ConfigError(f"Failed to save config: {e}") from e

    @property
    def config(self) -> Config:
        """Get current config, loading if needed."""
        if self._config is None:
            self._config = self.load_config()
        return self._config
