"""
Generate code command

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
@click.argument("description", required=True)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
@click.option("--language", "-l", help="Programming language")
@click.option("--context", "-c", help="Additional context")
@click.option("--provider", "-p", help="AI provider (openai, anthropic, ollama)")
@click.option("--model", "-m", help="Model name")
@click.option("--stream", "-s", is_flag=True, help="Stream output")
def generate_command(description, output, language, context, provider, model, stream):
    """
    🎨 Gera código a partir de uma descrição
    
    Exemplos:
    
    \b
        ai-code generate "função que calcula fibonacci"
        ai-code generate "API REST em Flask" --output app.py
        ai-code generate "componente React" --language javascript
    """
    asyncio.run(_generate(description, output, language, context, provider, model, stream))


async def _generate(description, output, language, context, provider, model, stream):
    """Generate code"""
    config = Config()
    
    language = language or config.get("default_language", "python")
    
    system_prompt = f"""You are an expert {language} developer. Generate clean, well-documented, and production-ready code.

Requirements:
- Write clean and readable code
- Include proper error handling
- Add comments where necessary
- Follow best practices for {language}
- Make the code production-ready"""

    user_prompt = f"Generate {language} code for: {description}"
    
    if context:
        user_prompt += f"\n\nContext: {context}"
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        console.print(f"[cyan]🤖 Gerando código com {provider_instance.__class__.__name__}...[/cyan]")
        
        if stream:
            code = ""
            console.print("\n[bold green]Código gerado:[/bold green]\n")
            async for chunk in provider_instance.stream_generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.7,
            ):
                code += chunk
                console.print(chunk, end="")
            console.print("\n")
        else:
            code = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.7,
            )
            
            # Display code with syntax highlighting
            syntax = Syntax(code, language, theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title="[bold green]Código Gerado[/bold green]", border_style="green"))
        
        # Save to file if output specified
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(code, encoding="utf-8")
            console.print(f"[green]✅ Código salvo em: {output_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

