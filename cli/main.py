"""
Main CLI entry point

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from core.config import Config
from commands import (
    generate_command,
    refactor_command,
    explain_command,
    test_command,
    translate_command,
    fix_command,
    docs_command,
    analyze_command,
    chat_command,
    review_command,
    config_command,
    web_command,
)

console = Console()


@click.group()
@click.version_option(version="1.0.0", prog_name="ai-code")
@click.option("--verbose", "-v", is_flag=True, help="Modo verbose")
@click.pass_context
def cli(ctx, verbose):
    """
    🤖 AI Code Assistant CLI
    
    Ferramenta poderosa para assistência de código com IA.
    
    Desenvolvido por: Aureo Manzano Junior (https://iadev.pro)
    """
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["config"] = Config()
    
    if not verbose:
        # Show welcome message
        welcome_text = Text()
        welcome_text.append("🤖 AI Code Assistant CLI\n\n", style="bold cyan")
        welcome_text.append("Desenvolvido por: ", style="dim")
        welcome_text.append("Aureo Manzano Junior", style="bold")
        welcome_text.append("\nWebsite: ", style="dim")
        welcome_text.append("https://iadev.pro", style="bold blue")
        
        console.print(Panel(welcome_text, border_style="cyan", title="Bem-vindo"))


# Register all commands
cli.add_command(generate_command)
cli.add_command(refactor_command)
cli.add_command(explain_command)
cli.add_command(test_command)
cli.add_command(translate_command)
cli.add_command(fix_command)
cli.add_command(docs_command)
cli.add_command(analyze_command)
cli.add_command(chat_command)
cli.add_command(review_command)
cli.add_command(config_command)
cli.add_command(web_command)


if __name__ == "__main__":
    cli()

