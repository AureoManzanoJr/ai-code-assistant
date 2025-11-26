"""
Anthropic Claude provider implementation

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import os
from typing import Optional, List
from anthropic import AsyncAnthropic

from .base import BaseProvider


class AnthropicProvider(BaseProvider):
    """Anthropic Claude provider"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize Anthropic provider
        
        Args:
            api_key: Anthropic API key
            model: Model name (default: claude-3-opus-20240229)
        """
        api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Anthropic API key is required")
        
        super().__init__(api_key, model or "claude-3-opus-20240229")
        self.client = AsyncAnthropic(api_key=api_key)
    
    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ) -> str:
        """Generate text using Anthropic Claude"""
        messages = [{"role": "user", "content": prompt}]
        
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=messages,
        )
        
        return response.content[0].text
    
    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ):
        """Stream generate text using Anthropic Claude"""
        messages = [{"role": "user", "content": prompt}]
        
        stream = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=messages,
            stream=True,
        )
        
        async for chunk in stream:
            if hasattr(chunk, "delta") and chunk.delta.text:
                yield chunk.delta.text
            elif hasattr(chunk, "text"):
                yield chunk.text
    
    @classmethod
    def get_available_models(cls) -> List[str]:
        """Get available Anthropic models"""
        return [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ]

