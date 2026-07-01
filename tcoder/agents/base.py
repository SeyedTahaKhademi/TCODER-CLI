from abc import ABC, abstractmethod
from typing import Any, Dict, List

from tcoder.core.models import Message
from tcoder.providers import BaseProvider
from tcoder.tools import BaseTool


class BaseAgent(ABC):
    """Abstract base class for TCODER agents."""

    def __init__(self, provider: BaseProvider, tools: List[BaseTool] | None = None):
        self.provider = provider
        self.tools = tools or []

    @abstractmethod
    async def run(self, messages: List[Message], **kwargs: Any) -> Any:
        """Run the agent with given input messages."""
        pass
