from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseTool(ABC):
    """Abstract base class for tools that the AI can use."""

    name: str
    description: str
    parameters: Dict[str, Any]

    @abstractmethod
    async def run(self, **kwargs: Any) -> Any:
        """Run the tool with the given arguments."""
        pass

    def get_schema(self) -> Dict[str, Any]:
        """Get the OpenAI function calling schema for this tool."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }
