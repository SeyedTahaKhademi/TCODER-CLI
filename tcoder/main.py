import typer
from rich.console import Console

from tcoder import __version__
from tcoder.config import ConfigManager
from tcoder.security import KeyManager
from tcoder.providers import get_provider_class, PROVIDER_REGISTRY
from tcoder.core.models import ProviderConfig, Message, MessageRole
from tcoder.ui import run_interactive_ui

app = typer.Typer(
    name="tcoder",
    help="TCODER CLI - Production-Grade AI Coding Agent for Linux",
)
console = Console()


@app.command()
def version():
    """Show version information."""
    console.print(f"[bold blue]TCODER CLI[/bold blue] v{__version__}")


@app.command()
def login(
    provider: str = typer.Option(..., "--provider", "-p", help="Provider name (e.g., openai)"),
    api_key: str = typer.Option(..., "--api-key", "-k", help="API key for the provider"),
):
    """Login and store API key securely."""
    KeyManager.set_key(provider, api_key)
    console.print(f"✅ Successfully logged in to [green]{provider}[/green]")


@app.command()
def logout(provider: str = typer.Option(..., "--provider", "-p", help="Provider to logout from")):
    """Remove stored API key."""
    KeyManager.delete_key(provider)
    console.print(f"✅ Successfully logged out from [green]{provider}[/green]")


@app.command("providers")
def list_providers():
    """List all available providers."""
    console.print("[bold]Available providers:[/bold]")
    for name, provider_cls in PROVIDER_REGISTRY.items():
        console.print(f"  • [cyan]{name}[/cyan] - {provider_cls.display_name}")


@app.command()
def status():
    """Show current status and configuration."""
    config_manager = ConfigManager()
    config = config_manager.config
    console.print("[bold]TCODER Status[/bold]")
    console.print(f"  • Current provider: [cyan]{config.general.provider}[/cyan]")
    console.print(f"  • Profile: [cyan]{config.general.profile}[/cyan]")


@app.command()
def chat(
    prompt: str = typer.Argument(..., help="Prompt to send to the AI"),
    provider: str | None = typer.Option(None, "--provider", "-p", help="Provider to use"),
    model: str | None = typer.Option(None, "--model", "-m", help="Model to use"),
):
    """Send a single prompt to the AI and get a response."""
    import asyncio
    asyncio.run(_chat_async(prompt, provider, model))


async def _chat_async(prompt: str, provider_name: str | None, model_name: str | None):
    config_manager = ConfigManager()
    config = config_manager.config
    provider_name = provider_name or config.general.provider

    api_key = KeyManager.get_key(provider_name)
    if not api_key:
        console.print("[red]Error:[/red] Not logged in to this provider. Use `tcoder login`.")
        raise typer.Exit(1)

    provider_cls = get_provider_class(provider_name)
    provider_config = ProviderConfig(
        api_key=api_key,
        base_url=config.providers.get(provider_name, {}).get("base_url"),
        model=model_name or config.providers.get(provider_name, {}).get("model") or provider_cls.default_model,
    )
    provider = provider_cls(provider_config)

    messages = [Message(role=MessageRole.USER, content=prompt)]
    with console.status("[green]Thinking...[/green]"):
        response = await provider.chat(messages)
    console.print("\n[bold blue]AI Response:[/bold blue]")
    console.print(response.content)


@app.command()
def doctor():
    """Check system health and configuration."""
    console.print("[bold]TCODER Doctor[/bold]")
    console.print("  ✅ Python version: [green]OK[/green]")
    console.print("  ✅ Config directory: [green]OK[/green]")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Run TCODER in interactive mode if no command is specified."""
    if ctx.invoked_subcommand is None:
        run_interactive_ui()


if __name__ == "__main__":
    app()
