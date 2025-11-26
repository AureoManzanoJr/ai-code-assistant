"""
Analyze code command

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
@click.option("--suggest-improvements", is_flag=True, help="Suggest improvements")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def analyze_command(path, suggest_improvements, provider, model):
    """
    🔍 Analisa código e fornece insights
    
    Exemplos:
    
    \b
        ai-code analyze main.py
        ai-code analyze src/ --suggest-improvements
    """
    asyncio.run(_analyze_code(path, suggest_improvements, provider, model))


async def _analyze_code(path, suggest_improvements, provider, model):
    """Analyze code"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = """You are an expert code analyst. Analyze code and provide insights.

Analyze:
- Code quality
- Performance issues
- Security concerns
- Best practices adherence
- Maintainability
- Complexity"""
    
    if suggest_improvements:
        system_prompt += "\n\nProvide specific improvement suggestions with examples."
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            user_prompt = f"Analyze the following code:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]🔍 Analisando {file_path.name}...[/cyan]")
            
            analysis = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            markdown = Markdown(analysis)
            console.print(Panel(markdown, title=f"[bold cyan]Análise: {file_path}[/bold cyan]", border_style="cyan"))
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

