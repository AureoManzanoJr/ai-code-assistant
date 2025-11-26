"""
Generate tests command

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
@click.option("--framework", "-f", default="pytest", help="Test framework (pytest, unittest, jest)")
@click.option("--coverage", "-c", is_flag=True, help="Include coverage")
@click.option("--output", "-o", type=click.Path(), help="Output directory")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def test_command(path, framework, coverage, output, provider, model):
    """
    🧪 Gera testes para código
    
    Exemplos:
    
    \b
        ai-code test main.py
        ai-code test src/ --framework pytest
        ai-code test code.py --coverage
    """
    asyncio.run(_generate_tests(path, framework, coverage, output, provider, model))


async def _generate_tests(path, framework, coverage, output, provider, model):
    """Generate tests"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = f"""You are an expert test writer. Generate comprehensive tests using {framework}.

Requirements:
- Write comprehensive test cases
- Cover edge cases
- Include positive and negative tests
- Follow {framework} best practices
- Make tests maintainable and readable"""
    
    if coverage:
        system_prompt += "\n\nAim for high code coverage (80%+)."
    
    try:
        provider_instance = get_provider(provider, model=model)
        output_dir = Path(output) if output else path_obj.parent / "tests"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            user_prompt = f"Generate {framework} tests for the following code:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]🧪 Gerando testes para {file_path.name}...[/cyan]")
            
            tests = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            # Extract code from markdown if present
            if "```" in tests:
                lines = tests.split("```")
                for i, line in enumerate(lines):
                    if i % 2 == 1:  # Code blocks
                        tests = line.split("\n", 1)[1] if "\n" in line else line
                        break
            
            test_file = output_dir / f"test_{file_path.stem}.py"
            test_file.write_text(tests, encoding="utf-8")
            
            syntax = Syntax(tests, "python", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title=f"[bold green]Testes Gerados: {test_file}[/bold green]", border_style="green"))
        
        console.print(f"[green]✅ Testes gerados em: {output_dir}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

