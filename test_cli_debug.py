"""Debug script for the CLI."""

from typer.testing import CliRunner

from pixi_project.cli import app


def main():
    """Run the tests."""
    runner = CliRunner()

    # Test the main CLI entry point
    result = runner.invoke(app, ["--help"])
    print(f"Exit code: {result.exit_code}")
    print(f"Output: {result.output}")

    # Test the greet command
    result = runner.invoke(app, ["greet", "World"])
    print(f"Exit code: {result.exit_code}")
    print(f"Output: {result.output}")


if __name__ == "__main__":
    main()
