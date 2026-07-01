from datetime import datetime
import pytest
from tcoder.core.models import Message, MessageRole, ProviderConfig, ChatResponse


def test_message_creation():
    """Test creating a Message instance."""
    msg = Message(role=MessageRole.USER, content="Hello, world!")
    assert msg.role == MessageRole.USER
    assert msg.content == "Hello, world!"
    assert isinstance(msg.timestamp, datetime)


def test_provider_config():
    """Test ProviderConfig model."""
    config = ProviderConfig(model="gpt-4o")
    assert config.model == "gpt-4o"
    assert config.temperature == 0.7


def test_chat_response():
    """Test ChatResponse model."""
    resp = ChatResponse(content="Hi there!")
    assert resp.content == "Hi there!"
    assert resp.tool_calls == []
