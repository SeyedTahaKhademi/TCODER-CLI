from typing import List
from tcoder.core.models import Message


class MemoryManager:
    """Manages conversation history and memory."""

    def __init__(self, max_messages: int = 50):
        self.messages: List[Message] = []
        self.max_messages = max_messages

    def add_message(self, message: Message) -> None:
        """Add a new message to history."""
        self.messages.append(message)
        # Keep only recent messages to prevent token limit issues
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self) -> List[Message]:
        """Get all messages in history."""
        return self.messages.copy()

    def clear(self) -> None:
        """Clear all memory."""
        self.messages = []
