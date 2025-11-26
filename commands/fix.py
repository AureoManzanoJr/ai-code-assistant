"""
Fix code command

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

from core.providers.factory import get_provider
from core.config import Config

console = Console()


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--auto-apply", is_flag=True, help="Automatically apply fixes")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def fix_command(path, auto_apply, provider, model):
    """
    🐛 Corrige bugs e erros no código
    
    Exemplos:
    
    \b
        ai-code fix main.py
        ai-code fix src/ --auto-apply
    """
    asyncio.run(_fix_code(path, auto_apply, provider, model))


async def _fix_code(path, auto_apply, provider, model):
    """Fix code"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = """You are an expert debugger. Fix bugs and errors in the given code.

Requirements:
- Identify all bugs and errors
- Fix them properly
- Maintain functionality
- Follow best practices
- Explain what was fixed"""
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            user_prompt = f"Fix all bugs and errors in the following code:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]🐛 Analisando {file_path.name}...[/cyan]")
            
            fixed = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            # Extract code from markdown if present
            if "```" in fixed:
                lines = fixed.split("```")
                for i, line in enumerate(lines):
                    if i % 2 == 1:  # Code blocks
                        fixed = line.split("\n", 1)[1] if "\n" in line else line
                        break
            
            if auto_apply:
                file_path.write_text(fixed, encoding="utf-8")
                console.print(f"[green]✅ Correções aplicadas em {file_path}[/green]")
            else:
                syntax = Syntax(fixed, "python", theme="monokai", line_numbers=True)
                console.print(Panel(syntax, title=f"[bold green]Código Corrigido: {file_path}[/bold green]", border_style="green"))
                console.print("[yellow]💡 Use --auto-apply para aplicar automaticamente[/yellow]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

