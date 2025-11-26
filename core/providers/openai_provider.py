"""
OpenAI provider implementation

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import os
from typing import Optional, List
from openai import AsyncOpenAI

from .base import BaseProvider


class OpenAIProvider(BaseProvider):
    """OpenAI provider"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize OpenAI provider
        
        Args:
            api_key: OpenAI API key
            model: Model name (default: gpt-4-turbo-preview)
        """
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key is required")
        
        super().__init__(api_key, model or "gpt-4-turbo-preview")
        self.client = AsyncOpenAI(api_key=api_key)
    
    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ) -> str:
        """Generate text using OpenAI"""
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        return response.choices[0].message.content
    
    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ):
        """Stream generate text using OpenAI"""
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    @classmethod
    def get_available_models(cls) -> List[str]:
        """Get available OpenAI models"""
        return [
            "gpt-4-turbo-preview",
            "gpt-4",
            "gpt-3.5-turbo",
            "gpt-4-1106-preview",
        ]

