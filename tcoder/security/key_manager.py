import keyring
from typing import Optional


class KeyManager:
    """Manages secure storage of API keys and secrets."""

    SERVICE_NAME = "tcoder"

    @classmethod
    def get_key(cls, provider_name: str) -> Optional[str]:
        """Get a stored API key for a provider."""
        try:
            return keyring.get_password(cls.SERVICE_NAME, provider_name)
        except Exception:
            return None

    @classmethod
    def set_key(cls, provider_name: str, api_key: str) -> None:
        """Store an API key for a provider."""
        keyring.set_password(cls.SERVICE_NAME, provider_name, api_key)

    @classmethod
    def delete_key(cls, provider_name: str) -> None:
        """Delete a stored API key for a provider."""
        try:
            keyring.delete_password(cls.SERVICE_NAME, provider_name)
        except keyring.errors.PasswordDeleteError:
            pass
