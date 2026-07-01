from datetime import datetime
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    """Roles for chat messages."""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class Message(BaseModel):
    """A single chat message."""
    role: MessageRole
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: dict[str, Any] = Field(default_factory=dict)


class ToolCall(BaseModel):
    """A tool call from the model."""
    id: str
    name: str
    arguments: dict[str, Any]


class ToolResult(BaseModel):
    """The result of a tool call."""
    id: str
    output: str
    success: bool
    error: str | None = None


class ProviderConfig(BaseModel):
    """Base configuration for providers."""
    api_key: str | None = None
    base_url: str | None = None
    model: str
    temperature: float = 0.7
    max_tokens: int = 4096
    timeout: int = 30


class ChatResponse(BaseModel):
    """Response from a provider chat completion."""
    content: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)
