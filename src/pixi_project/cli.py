"""Command-line interface for the pixi-project."""

import typeguard
import typer

app = typer.Typer(help="Pixi Project CLI tool.")


@app.command()
def greet(
    name: str,
    count: int = typer.Option(1, "--count", "-c", help="Number of greetings."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output."),
) -> None:
    """Greet the user with a friendly message."""
    typeguard.check_type(count, int)
    typeguard.check_type(name, str)

    for _ in range(count):
        message = f"Hello, {name}!"
        if verbose:
            message += " It's nice to meet you!"
        typer.echo(message)


def main() -> None:
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
