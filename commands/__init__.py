"""
CLI Commands

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

from .generate import generate_command
from .refactor import refactor_command
from .explain import explain_command
from .test import test_command
from .translate import translate_command
from .fix import fix_command
from .docs import docs_command
from .analyze import analyze_command
from .chat import chat_command
from .review import review_command
from .config import config_command
from .web import web_command

__all__ = [
    "generate_command",
    "refactor_command",
    "explain_command",
    "test_command",
    "translate_command",
    "fix_command",
    "docs_command",
    "analyze_command",
    "chat_command",
    "review_command",
    "config_command",
    "web_command",
]

