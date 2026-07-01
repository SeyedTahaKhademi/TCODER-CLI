from typing import Any, List

from tcoder.core.models import Message, MessageRole
from tcoder.agents.base import BaseAgent
from tcoder.memory import MemoryManager


class ChatAgent(BaseAgent):
    """A basic conversational agent."""

    def __init__(self, provider, tools=None):
        super().__init__(provider, tools)
        self.memory = MemoryManager()

    async def run(self, messages: List[Message], **kwargs: Any):
        """Process messages and get a response from the provider."""
        # Combine any stored memory with input messages
        all_messages = self.memory.get_messages() + messages
        response = await self.provider.chat(all_messages)
        
        # Add input and response to memory
        for msg in messages:
            self.memory.add_message(msg)
        self.memory.add_message(Message(role=MessageRole.ASSISTANT, content=response.content))
        
        return response
