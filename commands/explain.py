"""
Explain code command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
import asyncio
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from core.providers.factory import get_provider
from core.config import Config

console = Console()


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--detailed", "-d", is_flag=True, help="Detailed explanation")
@click.option("--function", "-f", help="Explain specific function")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def explain_command(path, detailed, function, provider, model):
    """
    📖 Explica código de forma clara
    
    Exemplos:
    
    \b
        ai-code explain main.py
        ai-code explain code.py --detailed
        ai-code explain file.py --function calculate_total
    """
    asyncio.run(_explain(path, detailed, function, provider, model))


async def _explain(path, detailed, function, provider, model):
    """Explain code"""
    file_path = Path(path)
    
    if not file_path.exists():
        console.print(f"[red]❌ Arquivo não encontrado: {path}[/red]")
        return
    
    code = file_path.read_text(encoding="utf-8")
    
    system_prompt = """You are an expert code explainer. Explain code in a clear, concise, and educational way.

Focus on:
- What the code does
- How it works
- Key concepts and patterns
- Important details"""
    
    if detailed:
        system_prompt += "\n\nProvide a very detailed explanation, including edge cases and potential improvements."
    
    user_prompt = f"Explain the following code:\n\n```\n{code}\n```"
    
    if function:
        user_prompt += f"\n\nFocus on the function: {function}"
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        console.print(f"[cyan]🤖 Analisando código...[/cyan]")
        
        explanation = await provider_instance.generate(
            user_prompt,
            system_prompt=system_prompt,
            temperature=0.3,
        )
        
        markdown = Markdown(explanation)
        console.print(Panel(markdown, title="[bold cyan]Explicação do Código[/bold cyan]", border_style="cyan"))
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

