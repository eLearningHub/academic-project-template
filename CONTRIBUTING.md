# Contributing to Pixi Project

Thank you for considering contributing to Pixi Project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

- Check if the bug has already been reported in the Issues section
- Use the bug report template when creating a new issue
- Include detailed steps to reproduce the bug
- Include any relevant logs or error messages

### Suggesting Enhancements

- Check if the enhancement has already been suggested in the Issues section
- Use the feature request template when creating a new issue
- Describe the feature in detail and why it would be valuable

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Run tests and ensure they pass
5. Update documentation if necessary
6. Submit a pull request

## Development Environment

You can use either Poetry or Pixi for dependency management.

### Using Poetry

```bash
# Clone the repository
git clone https://github.com/eLearningHub/pixi-template.git
cd pixi-template

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

### Using Pixi

```bash
# Clone the repository
git clone https://github.com/eLearningHub/pixi-template.git
cd pixi-template

# Install Pixi if you haven't already
curl -fsSL https://pixi.sh/install.sh | bash

# Install dependencies
pixi install

# Install development dependencies
pixi run install-dev

# Install pre-commit hooks
pixi run pre-commit install
```

> **Important**: When using Pixi, always add dependencies with `pixi add` commands instead of editing pyproject.toml directly. Use `pixi add [package]` for regular dependencies and `pixi add --pypi --feature dev [package]` for development dependencies. Pixi will automatically update the pyproject.toml file with the appropriate configuration. See [pixi_setup.md](pixi_setup.md) for more details.

## Testing

We use pytest for testing.

### Using Poetry

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src
```

### Using Pixi

```bash
# Run tests
pixi run test
```

### Using Nox

Nox provides isolated environments for testing:

```bash
# Install Nox
pip install nox

# Run tests
nox -s tests
```

## Code Style

We use Black for code formatting, isort for import sorting, and Flake8 for linting.

### Using Poetry

```bash
# Format code
poetry run black src tests

# Sort imports
poetry run isort src tests

# Lint code
poetry run flake8 src tests
```

### Using Pixi

```bash
# Format code
pixi run format

# Lint code
pixi run lint
```

### Using Nox

```bash
nox -s black
nox -s isort
nox -s lint
```

## Type Checking

We use mypy for static type checking:

### Using Poetry

```bash
poetry run mypy src tests
```

### Using Pixi

```bash
pixi run mypy
```

### Using Nox

```bash
nox -s mypy
```

## Documentation

We use Sphinx with MyST for documentation:

### Using Poetry

```bash
# Build documentation
cd docs
poetry run sphinx-build . _build
```

### Using Pixi

```bash
# Build documentation with Quarto
pixi run docs

# Build documentation with Sphinx
pixi run sdocs
```

### Using Nox

```bash
nox -s docs
```

## Adding Dependencies

### Using Poetry

```bash
# Add a regular dependency
poetry add package_name

# Add a development dependency
poetry add --group dev package_name
```

### Using Pixi

```bash
# Add a regular dependency
pixi add package_name

# Add a development dependency
pixi add --pypi --feature dev package_name
```

> **Important**: Do not edit pyproject.toml directly to add dependencies. Always use the appropriate package manager commands. Pixi will automatically update the pyproject.toml file with the appropriate configuration.

## Commit Messages

Please follow these guidelines for commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create a new GitHub release
4. The CI/CD pipeline will automatically publish to PyPI 