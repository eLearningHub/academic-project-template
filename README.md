# Pixi Project Template

A template for creating a Python project with Pixi package manager.

## Features

- Modern Python project structure with Pixi
- Built-in testing with pytest
- Code formatting and linting with Ruff
- Documentation with MkDocs and Quarto
- CLI tool integration with Typer
- PowerPoint automation with python-pptx

## Requirements

- Python >= 3.11
- [Pixi](https://prefix.dev/docs/pixi/overview) package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/eLearningHub/pixi-template.git
cd pixi-template
```

2. Install dependencies using Pixi:
```bash
pixi install
pixi run install-quarto-extensions
```

## Development Tasks

The project includes several predefined tasks that can be run using `pixi run`:

- `test`: Run pytest test suite
  ```bash
  pixi run test
  ```

- `lint`: Check code with Ruff
  ```bash
  pixi run lint
  ```

- `format`: Format code with Ruff
  ```bash
  pixi run format
  ```

- `docs`: Build Quarto documentation
  ```bash
  pixi run docs
  ```

- `cli`: Run CLI tool
  ```bash
  pixi run cli
  ```

## Documentation

The project uses both MkDocs and Quarto for documentation:

1. Install Quarto extensions:
```bash
sudo apt-get install lmodern
pixi run install-quarto-extensions
```

2. Start documentation server:
```bash
pixi run docs
```

## Testing

Tests are written using pytest. Run the test suite with:

```bash
pixi run test
```

Test configuration is specified in `pyproject.toml` under `[tool.pytest.ini_options]`.

## Code Style

This project uses Ruff for code formatting and linting:

- Line length is set to 100 characters
- Enforces import sorting
- Checks for common bugs and code smells

Format your code with:
```bash
pixi run format
```

Check for issues with:
```bash
pixi run lint
```

## Dependencies

### Main Dependencies
- python-dotenv >= 1.0.0

### Development Dependencies
- pytest >= 8.3.4
- pytest-cov >= 6.0.0
- pytest-mock >= 3.14.0
- typer >= 0.15.1
- quarto >= 1.5.57
- deno >= 1.41.0
- python-pptx >= 1.0.2

## Project Structure

```
pixi-template/
├── src/
│   └── pixi_project/
│       └── cli.py
├── tests/
├── docs/
├── pyproject.toml
├── README.md
└── LICENSE
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## Contact

eLearning Hub - behzad@mechatronics3d.com