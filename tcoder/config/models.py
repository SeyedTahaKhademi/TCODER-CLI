from typing import Dict, Optional, Any
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ThemeSettings(BaseModel):
    """Theme configuration."""
    name: str = "dark"


class ProviderSettings(BaseModel):
    """Provider-specific configuration."""
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    model: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    timeout: Optional[int] = None


class GeneralSettings(BaseModel):
    """General application settings."""
    provider: str = "openai"
    theme: ThemeSettings = Field(default_factory=ThemeSettings)
    profile: str = "default"


class SecuritySettings(BaseModel):
    """Security-related settings."""
    allowed_directories: list[str] = Field(default_factory=list)
    blocked_directories: list[str] = Field(default_factory=list)
    sandbox_mode: bool = True


class Config(BaseModel):
    """Main configuration model."""
    general: GeneralSettings = Field(default_factory=GeneralSettings)
    providers: Dict[str, ProviderSettings] = Field(default_factory=dict)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    profiles: Dict[str, "Config"] = Field(default_factory=dict)


class Settings(BaseSettings):
    """Environment-based settings."""
    tcoder_home: str = "~/.config/tcoder"
    tcoder_data_dir: str = "~/.local/share/tcoder"
