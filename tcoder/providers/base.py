from abc import ABC, abstractmethod
from typing import AsyncIterator, Any

from tcoder.core.models import Message, ProviderConfig, ChatResponse, ToolCall


class BaseProvider(ABC):
    """Abstract base class for LLM providers."""

    name: str
    display_name: str
    default_model: str
    available_models: list[str]

    def __init__(self, config: ProviderConfig):
        self.config = config

    @abstractmethod
    async def chat(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
        stream: bool = False,
    ) -> ChatResponse:
        """Send a chat request to the provider and get a response."""
        pass

    @abstractmethod
    async def chat_stream(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
    ) -> AsyncIterator[str]:
        """Send a streaming chat request to the provider."""
        pass

    @classmethod
    @abstractmethod
    def get_available_models(cls) -> list[str]:
        """Get list of available models for this provider."""
        pass
