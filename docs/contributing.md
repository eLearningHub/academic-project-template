# Contributing

Thank you for considering contributing to Pixi Project!

## Development Environment

We use Poetry for dependency management. To set up your development environment:

```bash
# Clone the repository
git clone https://github.com/eLearningHub/pixi-template.git
cd pixi-template

# Install dependencies
poetry install

# Install pre-commit hooks
pre-commit install
```

## Testing

We use pytest for testing. Run the tests with:

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src
```

Alternatively, you can use Nox to run tests in isolated environments:

```bash
# Install Nox
pip install nox

# Run tests
nox -s tests
```

## Code Style

We use Black for code formatting, isort for import sorting, and Flake8 for linting.

```bash
# Format code
poetry run black src tests

# Sort imports
poetry run isort src tests

# Lint code
poetry run flake8 src tests
```

Or use Nox:

```bash
nox -s black
nox -s isort
nox -s lint
```

## Type Checking

We use mypy for static type checking:

```bash
poetry run mypy src tests
```

Or use Nox:

```bash
nox -s mypy
```

## Documentation

We use Sphinx with MyST for documentation:

```bash
# Build documentation
cd docs
poetry run sphinx-build . _build
```

Or use Nox:

```bash
nox -s docs
```

## Pull Request Process

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Run tests and linting
5. Submit a pull request

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create a new GitHub release
4. The CI/CD pipeline will automatically publish to PyPI 