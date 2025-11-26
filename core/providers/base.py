"""
Base provider interface

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class BaseProvider(ABC):
    """Base class for AI providers"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize provider
        
        Args:
            api_key: API key for the provider
            model: Model name to use
        """
        self.api_key = api_key
        self.model = model
    
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ) -> str:
        """
        Generate text from prompt
        
        Args:
            prompt: User prompt
            system_prompt: System prompt
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text
        """
        pass
    
    @abstractmethod
    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
    ):
        """
        Stream generate text from prompt
        
        Args:
            prompt: User prompt
            system_prompt: System prompt
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
            
        Yields:
            Generated text chunks
        """
        pass
    
    @classmethod
    @abstractmethod
    def get_available_models(cls) -> List[str]:
        """Get list of available models"""
        pass

