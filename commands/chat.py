"""
Interactive chat command

Desenvolvido por: Aureo Manzano Junior
Website: https://iadev.pro
Email: aureomanzano@icloud.com
"""

import click
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from core.providers.factory import get_provider
from core.config import Config

console = Console()


@click.command()
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def chat_command(provider, model):
    """
    💬 Chat interativo com IA
    
    Exemplos:
    
    \b
        ai-code chat
        ai-code chat --provider openai
    """
    asyncio.run(_chat(provider, model))


async def _chat(provider, model):
    """Interactive chat"""
    try:
        provider_instance = get_provider(provider, model=model)
        
        console.print(Panel(
            "[bold cyan]💬 Chat Interativo com IA[/bold cyan]\n\n"
            "Digite suas perguntas sobre código. Use 'exit' ou 'quit' para sair.",
            border_style="cyan"
        ))
        
        conversation_history = []
        
        while True:
            user_input = Prompt.ask("\n[bold cyan]Você[/bold cyan]")
            
            if user_input.lower() in ["exit", "quit", "sair"]:
                console.print("[yellow]👋 Até logo![/yellow]")
                break
            
            if not user_input.strip():
                continue
            
            console.print("[cyan]🤖 Pensando...[/cyan]")
            
            # Add to history
            conversation_history.append({"role": "user", "content": user_input})
            
            # Generate response
            response = await provider_instance.generate(
                user_input,
                system_prompt="You are a helpful coding assistant. Provide clear, concise, and accurate answers.",
                temperature=0.7,
            )
            
            # Add to history
            conversation_history.append({"role": "assistant", "content": response})
            
            # Display response
            console.print(Panel(
                response,
                title="[bold green]IA[/bold green]",
                border_style="green"
            ))
    
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Até logo![/yellow]")
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

