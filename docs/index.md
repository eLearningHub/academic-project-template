# Pixi Project

```{toctree}
:maxdepth: 2
:hidden:

usage
api
contributing
Code of Conduct <codeofconduct>
License <license>
Changelog <changelog>
```

## Overview

Pixi Project is a template for creating Python projects with modern development practices.

## Features

- Packaging and dependency management with Poetry
- Test automation with Nox
- Linting with pre-commit and Flake8
- Continuous integration with GitHub Actions
- Documentation with Sphinx, MyST, and Read the Docs using the furo theme
- Automated uploads to PyPI and TestPyPI
- Automated release notes with Release Drafter
- Automated dependency updates with Dependabot
- Code formatting with Black and Prettier
- Import sorting with isort
- Testing with pytest
- Code coverage with Coverage.py
- Coverage reporting with Codecov
- Command-line interface with Typer
- Static type-checking with mypy
- Runtime type-checking with Typeguard
- Automated Python syntax upgrades with pyupgrade
- Security audit with Bandit and Safety
- Check documentation examples with xdoctest
- Generate API documentation with autodoc and napoleon
- Generate command-line reference with sphinx-click
- Manage project labels with GitHub Labeler

## Installation

```bash
pip install pixi-project
```

## Quick Start

```bash
pixi-project greet "Your Name"
``` 