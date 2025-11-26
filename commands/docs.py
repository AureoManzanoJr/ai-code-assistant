"""
Generate documentation command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
import asyncio
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from core.providers.factory import get_provider
from core.config import Config

console = Console()


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--format", "-f", default="markdown", help="Output format (markdown, html, rst)")
@click.option("--output", "-o", type=click.Path(), help="Output file/directory")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def docs_command(path, format, output, provider, model):
    """
    📝 Gera documentação automática
    
    Exemplos:
    
    \b
        ai-code docs main.py
        ai-code docs src/ --format markdown
    """
    asyncio.run(_generate_docs(path, format, output, provider, model))


async def _generate_docs(path, format, output, provider, model):
    """Generate documentation"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.py")) + list(path_obj.rglob("*.js")) + list(path_obj.rglob("*.ts"))
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = f"""You are an expert technical writer. Generate comprehensive documentation in {format} format.

Requirements:
- Document all functions, classes, and modules
- Include parameter descriptions
- Include return value descriptions
- Include usage examples
- Make it clear and comprehensive
- Follow {format} formatting standards"""
    
    try:
        provider_instance = get_provider(provider, model=model)
        output_dir = Path(output) if output else path_obj.parent / "docs"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            user_prompt = f"Generate {format} documentation for the following code:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]📝 Gerando documentação para {file_path.name}...[/cyan]")
            
            docs = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            ext = {
                "markdown": ".md",
                "html": ".html",
                "rst": ".rst",
            }.get(format.lower(), ".md")
            
            doc_file = output_dir / f"{file_path.stem}{ext}"
            doc_file.write_text(docs, encoding="utf-8")
            
            markdown = Markdown(docs)
            console.print(Panel(markdown, title=f"[bold green]Documentação: {doc_file}[/bold green]", border_style="green"))
        
        console.print(f"[green]✅ Documentação gerada em: {output_dir}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

