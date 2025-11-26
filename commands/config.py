"""
Configuration command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from core.config import Config

console = Console()


@click.group()
def config_command():
    """⚙️ Gerencia configurações"""
    pass


@config_command.command()
@click.argument("key")
@click.argument("value")
def set(key, value):
    """Define um valor de configuração"""
    config = Config()
    config.set(key, value)
    console.print(f"[green]✅ {key} definido como: {value}[/green]")


@config_command.command()
@click.argument("key")
def get(key):
    """Obtém um valor de configuração"""
    config = Config()
    value = config.get(key)
    if value:
        console.print(f"[cyan]{key}: {value}[/cyan]")
    else:
        console.print(f"[yellow]⚠️  {key} não encontrado[/yellow]")


@config_command.command()
def show():
    """Mostra todas as configurações"""
    config = Config()
    settings = config.show()
    
    table = Table(title="Configurações", show_header=True, header_style="bold cyan")
    table.add_column("Chave", style="cyan")
    table.add_column("Valor", style="green")
    
    for key, value in settings.items():
        table.add_row(key, str(value))
    
    console.print(table)


@config_command.command()
@click.argument("provider")
@click.argument("api_key")
def set_provider(provider, api_key):
    """Configura provider e API key"""
    config = Config()
    config.set("provider", provider)
    
    if provider == "openai":
        config.set("openai_key", api_key)
    elif provider == "anthropic":
        config.set("anthropic_key", api_key)
    
    console.print(f"[green]✅ Provider {provider} configurado![/green]")

