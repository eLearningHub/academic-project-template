# Pixi Setup Guide

This guide explains how to set up the project using Pixi for dependency management instead of directly editing the pyproject.toml file.

## Installing Pixi

If you haven't installed Pixi yet, you can do so with:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

## Setting Up the Project

1. Initialize the project with Pixi:

```bash
pixi init
```

2. Add Python dependencies:

```bash
# Core dependencies
pixi add python-dotenv
pixi add typer
pixi add typeguard
```

3. Add development dependencies:

```bash
# Add development dependencies to the pyproject.toml
pixi add --pypi --feature dev pytest pytest-cov pytest-mock
pixi add --pypi --feature dev black isort flake8 mypy
pixi add --pypi --feature dev bandit safety pre-commit
pixi add --pypi --feature dev sphinx sphinx-click furo myst-parser
pixi add --pypi --feature dev xdoctest coverage pyupgrade nox
```

4. Create a task to install development dependencies:

```bash
# Add this to the [tool.pixi.tasks] section in pyproject.toml
install-dev = """
pip install pytest pytest-cov pytest-mock black isort flake8 mypy bandit safety pre-commit sphinx sphinx-click furo myst-parser xdoctest coverage pyupgrade nox
"""
```

5. Run the install-dev task to install the development dependencies:

```bash
pixi run install-dev
```

## Using Pixi for Development

- Run tests:
  ```bash
  pixi run test
  ```

- Format code:
  ```bash
  pixi run format
  ```

- Lint code:
  ```bash
  pixi run lint
  ```

- Type check:
  ```bash
  pixi run mypy
  ```

- Build documentation:
  ```bash
  pixi run docs
  ```

- Security check:
  ```bash
  pixi run security
  ```

## Adding New Dependencies

Always use the `pixi add` command to add new dependencies:

```bash
# Add a regular dependency
pixi add package_name

# Add a development dependency
pixi add --pypi --feature dev package_name
```

## Important Note

Do not edit pyproject.toml directly to add dependencies. Always use the `pixi add` command to ensure proper dependency resolution and environment management. Pixi will automatically update the pyproject.toml file with the appropriate configuration. 