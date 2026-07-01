from tcoder.providers.base import BaseProvider
from tcoder.providers.openai_compatible import OpenAICompatibleProvider


PROVIDER_REGISTRY: dict[str, type[BaseProvider]] = {
    "openai": OpenAICompatibleProvider,
    "openai_compatible": OpenAICompatibleProvider,
    "vllm": OpenAICompatibleProvider,
    "lm_studio": OpenAICompatibleProvider,
    "groq": OpenAICompatibleProvider,
    "deepseek": OpenAICompatibleProvider,
    "mistral": OpenAICompatibleProvider,
}


def get_provider_class(provider_name: str) -> type[BaseProvider]:
    """Get the provider class for a given provider name."""
    if provider_name not in PROVIDER_REGISTRY:
        raise ValueError(f"Unknown provider: {provider_name}")
    return PROVIDER_REGISTRY[provider_name]
