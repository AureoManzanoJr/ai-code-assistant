"""
Refactor code command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
import asyncio
from pathlib import Path
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from core.providers.factory import get_provider
from core.config import Config

console = Console()


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--improve-performance", is_flag=True, help="Focus on performance improvements")
@click.option("--apply-best-practices", is_flag=True, help="Apply best practices")
@click.option("--preserve-style", is_flag=True, help="Preserve code style")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def refactor_command(path, improve_performance, apply_best_practices, preserve_style, output, provider, model):
    """
    🔧 Refatora código existente
    
    Exemplos:
    
    \b
        ai-code refactor main.py
        ai-code refactor src/ --improve-performance
        ai-code refactor code.py --apply-best-practices
    """
    asyncio.run(_refactor(path, improve_performance, apply_best_practices, preserve_style, output, provider, model))


async def _refactor(path, improve_performance, apply_best_practices, preserve_style, output, provider, model):
    """Refactor code"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    improvements = []
    if improve_performance:
        improvements.append("performance")
    if apply_best_practices:
        improvements.append("best practices")
    
    system_prompt = """You are an expert code refactoring assistant. Refactor the given code to make it:
- More maintainable
- More readable
- More efficient
- Following best practices
- Production-ready

Preserve functionality while improving code quality."""
    
    if preserve_style:
        system_prompt += "\n\nPreserve the existing code style and structure."
    
    if improvements:
        system_prompt += f"\n\nFocus on: {', '.join(improvements)}"
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Refatorando código...", total=len(files))
            
            for file_path in files:
                code = file_path.read_text(encoding="utf-8")
                
                user_prompt = f"Refactor the following code:\n\n```\n{code}\n```"
                
                refactored = await provider_instance.generate(
                    user_prompt,
                    system_prompt=system_prompt,
                    temperature=0.3,
                )
                
                # Extract code from markdown if present
                if "```" in refactored:
                    lines = refactored.split("```")
                    for i, line in enumerate(lines):
                        if i % 2 == 1:  # Code blocks
                            refactored = line.split("\n", 1)[1] if "\n" in line else line
                            break
                
                output_path = Path(output) if output else file_path
                output_path.write_text(refactored, encoding="utf-8")
                
                syntax = Syntax(refactored, "python", theme="monokai", line_numbers=True)
                console.print(Panel(syntax, title=f"[bold green]Refatorado: {file_path}[/bold green]", border_style="green"))
                
                progress.update(task, advance=1)
        
        console.print(f"[green]✅ {len(files)} arquivo(s) refatorado(s) com sucesso![/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

