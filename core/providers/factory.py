"""
Provider factory

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

from typing import Optional
from core.config import Config
from .openai_provider import OpenAIProvider
from .anthropic_provider import AnthropicProvider
from .ollama_provider import OllamaProvider
from .base import BaseProvider


def get_provider(
    provider_name: Optional[str] = None,
    api_key: Optional[str] = None,
    model: Optional[str] = None,
) -> BaseProvider:
    """
    Get AI provider instance
    
    Args:
        provider_name: Provider name (openai, anthropic, ollama)
        api_key: API key (optional, will use config if not provided)
        model: Model name (optional, will use config if not provided)
        
    Returns:
        Provider instance
    """
    config = Config()
    
    provider_name = provider_name or config.get("provider", "openai")
    api_key = api_key or config.get_api_key()
    model = model or config.get("model")
    
    if provider_name == "openai":
        return OpenAIProvider(api_key=api_key, model=model)
    elif provider_name == "anthropic":
        return AnthropicProvider(api_key=api_key, model=model)
    elif provider_name == "ollama":
        return OllamaProvider(model=model)
    else:
        raise ValueError(f"Unknown provider: {provider_name}")

