"""
Web interface command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
from rich.console import Console
from rich.panel import Panel

console = Console()


@click.command()
@click.option("--port", "-p", default=8080, help="Porta do servidor")
@click.option("--host", "-h", default="127.0.0.1", help="Host do servidor")
def web_command(port, host):
    """
    🌐 Inicia interface web
    
    Exemplos:
    
    \b
        ai-code web
        ai-code web --port 3000
    """
    try:
        console.print(Panel(
            f"[bold cyan]🌐 Iniciando interface web...[/bold cyan]\n\n"
            f"Acesse: http://{host}:{port}\n\n"
            "Pressione Ctrl+C para parar o servidor.",
            border_style="cyan"
        ))
        
        # Import here to avoid dependency if web extras not installed
        try:
            from web.server import start_server
            start_server(host=host, port=port)
        except ImportError:
            console.print("[red]❌ Interface web não disponível. Instale com: pip install ai-code-assistant[web][/red]")
            console.print("[yellow]💡 Ou instale manualmente: pip install fastapi uvicorn jinja2[/yellow]")
    
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Servidor parado[/yellow]")
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

