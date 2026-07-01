import httpx
from typing import AsyncIterator, Any

from tcoder.core.models import Message, ProviderConfig, ChatResponse, ToolCall
from tcoder.core.exceptions import ProviderError
from tcoder.providers.base import BaseProvider


class OpenAICompatibleProvider(BaseProvider):
    """Provider for OpenAI-compatible APIs (OpenAI, vLLM, LM Studio, etc.)."""

    name = "openai_compatible"
    display_name = "OpenAI Compatible"
    default_model = "gpt-4o"
    available_models = [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-4",
        "gpt-3.5-turbo",
    ]

    def __init__(self, config: ProviderConfig):
        super().__init__(config)
        self.client = httpx.AsyncClient(
            base_url=config.base_url or "https://api.openai.com/v1",
            timeout=config.timeout,
        )

    def _prepare_messages(self, messages: list[Message]) -> list[dict[str, Any]]:
        """Convert internal message format to OpenAI format."""
        return [
            {"role": msg.role.value, "content": msg.content}
            for msg in messages
        ]

    async def chat(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
        stream: bool = False,
    ) -> ChatResponse:
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.config.model,
            "messages": self._prepare_messages(messages),
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        if tools:
            payload["tools"] = tools

        try:
            response = await self.client.post(
                "/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

            choice = data["choices"][0]
            message = choice["message"]

            tool_calls = []
            if "tool_calls" in message and message["tool_calls"]:
                for tc in message["tool_calls"]:
                    tool_calls.append(
                        ToolCall(
                            id=tc["id"],
                            name=tc["function"]["name"],
                            arguments=tc["function"]["arguments"]
                        )
                    )

            return ChatResponse(
                content=message.get("content", ""),
                tool_calls=tool_calls,
                usage=data.get("usage", {}),
                metadata={"provider": self.name}
            )

        except httpx.HTTPError as e:
            raise ProviderError(f"HTTP error with provider: {e}") from e
        except (KeyError, IndexError) as e:
            raise ProviderError(f"Invalid response from provider: {e}") from e

    async def chat_stream(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
    ) -> AsyncIterator[str]:
        raise NotImplementedError("Streaming not implemented yet")

    @classmethod
    def get_available_models(cls) -> list[str]:
        return cls.available_models
