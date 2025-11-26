"""
Configuration management

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import os
import yaml
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration manager"""
    
    def __init__(self):
        """Initialize configuration"""
        self.config_dir = Path.home() / ".ai-code"
        self.config_file = self.config_dir / "config.yaml"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Default configuration
        self.defaults = {
            "provider": "openai",
            "model": "gpt-4-turbo-preview",
            "temperature": 0.7,
            "max_tokens": 2000,
            "default_language": "python",
            "theme": "dark",
        }
        
        # Load configuration
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f) or {}
                    # Merge with defaults
                    return {**self.defaults, **config}
            except Exception:
                return self.defaults.copy()
        return self.defaults.copy()
    
    def _save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                yaml.dump(self._config, f, default_flow_style=False)
        except Exception:
            pass
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        # Check environment variables first
        env_key = f"AI_CODE_{key.upper()}"
        env_value = os.getenv(env_key)
        if env_value:
            return env_value
        
        # Check config file
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self._config[key] = value
        self._save_config()
    
    def get_api_key(self) -> Optional[str]:
        """Get API key for current provider"""
        provider = self.get("provider", "openai")
        
        # Try environment variables first
        if provider == "openai":
            return os.getenv("OPENAI_API_KEY") or self.get("openai_key")
        elif provider == "anthropic":
            return os.getenv("ANTHROPIC_API_KEY") or self.get("anthropic_key")
        elif provider == "ollama":
            # Ollama doesn't need API key
            return None
        
        return None
    
    def show(self) -> Dict[str, Any]:
        """Show current configuration"""
        config = self._config.copy()
        # Don't show API keys
        for key in ["openai_key", "anthropic_key", "api_key"]:
            if key in config:
                config[key] = "***" if config[key] else None
        return config

