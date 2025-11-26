"""
Code review command

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
@click.option("--detailed", "-d", is_flag=True, help="Detailed review")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def review_command(path, detailed, provider, model):
    """
    🎯 Revisa código como um code review
    
    Exemplos:
    
    \b
        ai-code review main.py
        ai-code review pr/ --detailed
    """
    asyncio.run(_review_code(path, detailed, provider, model))


async def _review_code(path, detailed, provider, model):
    """Review code"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = """You are an expert code reviewer. Review code as if you were doing a pull request review.

Review:
- Code quality
- Best practices
- Potential bugs
- Performance issues
- Security concerns
- Maintainability
- Documentation
- Test coverage

Provide constructive feedback with specific examples."""
    
    if detailed:
        system_prompt += "\n\nProvide a very detailed review with line-by-line comments where appropriate."
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            user_prompt = f"Review the following code:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]🎯 Revisando {file_path.name}...[/cyan]")
            
            review = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            markdown = Markdown(review)
            console.print(Panel(markdown, title=f"[bold yellow]Code Review: {file_path}[/bold yellow]", border_style="yellow"))
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

