"""Tests for the CLI module."""

from typer.testing import CliRunner

from pixi_project.cli import app


def test_app() -> None:
    """Test the main CLI entry point."""
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Greet the user with a friendly message." in result.output


def test_greet() -> None:
    """Test the greet command."""
    runner = CliRunner()
    result = runner.invoke(app, ["World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_greet_with_count() -> None:
    """Test the greet command with count option."""
    runner = CliRunner()
    result = runner.invoke(app, ["World", "--count", "3"])
    assert result.exit_code == 0
    assert result.output.count("Hello, World!") == 3


def test_greet_with_verbose() -> None:
    """Test the greet command with verbose option."""
    runner = CliRunner()
    result = runner.invoke(app, ["World", "--verbose"])
    assert result.exit_code == 0
    assert "Hello, World! It's nice to meet you!" in result.output
