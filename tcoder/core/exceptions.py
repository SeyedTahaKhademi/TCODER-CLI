"""Core exceptions for TCODER."""


class TCODERBaseError(Exception):
    """Base exception class for TCODER errors."""
    pass


class ProviderError(TCODERBaseError):
    """Error related to providers (API errors, auth, etc.)."""
    pass


class ConfigError(TCODERBaseError):
    """Error related to configuration."""
    pass


class SecurityError(TCODERBaseError):
    """Security-related error."""
    pass


class AgentError(TCODERBaseError):
    """Error related to agent execution."""
    pass


class FileSystemError(TCODERBaseError):
    """Error related to filesystem operations."""
    pass
