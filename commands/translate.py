"""
Translate code command

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
@click.option("--to", "-t", required=True, help="Target language (python, javascript, typescript, go, rust, etc)")
@click.option("--preserve-comments", is_flag=True, help="Preserve comments")
@click.option("--output", "-o", type=click.Path(), help="Output file/directory")
@click.option("--provider", "-p", help="AI provider")
@click.option("--model", "-m", help="Model name")
def translate_command(path, to, preserve_comments, output, provider, model):
    """
    🌍 Traduz código entre linguagens
    
    Exemplos:
    
    \b
        ai-code translate main.py --to javascript
        ai-code translate src/ --to typescript
        ai-code translate code.py --to go --preserve-comments
    """
    asyncio.run(_translate(path, to, preserve_comments, output, provider, model))


async def _translate(path, to, preserve_comments, output, provider, model):
    """Translate code"""
    path_obj = Path(path)
    
    if path_obj.is_file():
        files = [path_obj]
    else:
        files = list(path_obj.rglob("*.*"))
        files = [f for f in files if f.suffix in [".py", ".js", ".ts", ".go", ".rs", ".java", ".cpp"]]
    
    if not files:
        console.print("[red]❌ Nenhum arquivo encontrado[/red]")
        return
    
    system_prompt = f"""You are an expert code translator. Translate code from one programming language to {to}.

Requirements:
- Maintain functionality exactly
- Use idiomatic {to} code
- Follow {to} best practices
- Preserve logic and structure
- Handle language-specific features appropriately"""
    
    if preserve_comments:
        system_prompt += "\n\nPreserve all comments and documentation."
    
    try:
        provider_instance = get_provider(provider, model=model)
        
        for file_path in files:
            code = file_path.read_text(encoding="utf-8")
            
            # Detect source language from extension
            ext_to_lang = {
                ".py": "Python",
                ".js": "JavaScript",
                ".ts": "TypeScript",
                ".go": "Go",
                ".rs": "Rust",
                ".java": "Java",
                ".cpp": "C++",
            }
            source_lang = ext_to_lang.get(file_path.suffix, "the source language")
            
            user_prompt = f"Translate the following {source_lang} code to {to}:\n\n```\n{code}\n```"
            
            console.print(f"[cyan]🌍 Traduzindo {file_path.name} para {to}...[/cyan]")
            
            translated = await provider_instance.generate(
                user_prompt,
                system_prompt=system_prompt,
                temperature=0.3,
            )
            
            # Extract code from markdown if present
            if "```" in translated:
                lines = translated.split("```")
                for i, line in enumerate(lines):
                    if i % 2 == 1:  # Code blocks
                        translated = line.split("\n", 1)[1] if "\n" in line else line
                        break
            
            # Determine output file extension
            lang_to_ext = {
                "python": ".py",
                "javascript": ".js",
                "typescript": ".ts",
                "go": ".go",
                "rust": ".rs",
                "java": ".java",
                "cpp": ".cpp",
            }
            ext = lang_to_ext.get(to.lower(), ".txt")
            
            if output:
                output_path = Path(output)
                if output_path.is_dir():
                    output_file = output_path / f"{file_path.stem}{ext}"
                else:
                    output_file = output_path
            else:
                output_file = file_path.parent / f"{file_path.stem}_{to}{ext}"
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(translated, encoding="utf-8")
            
            syntax = Syntax(translated, to, theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title=f"[bold green]Traduzido: {output_file}[/bold green]", border_style="green"))
        
        console.print(f"[green]✅ Tradução concluída![/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Erro: {str(e)}[/red]")
        raise click.Abort()

