"""
Ollama provider implementation (local models)

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import aiohttp
from typing import Optional, List

from .base import BaseProvider


class OllamaProvider(BaseProvider):
    """Ollama provider for local models"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None, base_url: str = "http://localhost:11434"):
        """
        Initialize Ollama provider
        
        Args:
            api_key: Not used for Ollama
            model: Model name (default: llama2)
            base_url: Ollama server URL
        """
        super().__init__(None, model or "llama2")
        self.base_url = base_url
    
    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ) -> str:
        """Generate text using Ollama"""
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise Exception(f"Ollama API error: {response.status}")
                
                data = await response.json()
                return data.get("response", "")
    
    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ):
        """Stream generate text using Ollama"""
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise Exception(f"Ollama API error: {response.status}")
                
                async for line in response.content:
                    if line:
                        import json
                        data = json.loads(line)
                        if "response" in data:
                            yield data["response"]
    
    @classmethod
    def get_available_models(cls) -> List[str]:
        """Get available Ollama models (common ones)"""
        return [
            "llama2",
            "codellama",
            "mistral",
            "neural-chat",
            "starling-lm",
        ]

