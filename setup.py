"""
Setup script for AI Code Assistant CLI

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="ai-code-assistant",
    version="1.0.0",
    author="Aureo Manzano Junior",
    author_email="aureomanzano@icloud.com",
    description="Ferramenta CLI poderosa para assistência de código com IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AureoManzanoJr/ai-code-assistant",
    project_urls={
        "Homepage": "https://github.com/AureoManzanoJr/ai-code-assistant",
        "Documentation": "https://github.com/AureoManzanoJr/ai-code-assistant#readme",
        "Bug Reports": "https://github.com/AureoManzanoJr/ai-code-assistant/issues",
        "Source": "https://github.com/AureoManzanoJr/ai-code-assistant",
        "Author Website": "https://iadev.pro",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "click>=8.1.0",
        "openai>=1.0.0",
        "anthropic>=0.7.0",
        "requests>=2.31.0",
        "pygments>=2.16.0",
        "rich>=13.7.0",
        "pyyaml>=6.0",
        "aiohttp>=3.9.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "web": [
            "fastapi>=0.104.0",
            "uvicorn>=0.24.0",
            "jinja2>=3.1.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-code=cli.main:cli",
        ],
    },
    keywords="ai, code-assistant, cli, openai, claude, code-generation, refactoring, testing, developer-tools",
    include_package_data=True,
    zip_safe=False,
)

