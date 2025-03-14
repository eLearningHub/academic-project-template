# Usage

## Command Line Interface

Pixi Project provides a command-line interface with various commands.

### Greeting Command

The `greet` command allows you to greet a user:

```bash
pixi-project greet "World"
```

You can customize the greeting with options:

```bash
# Greet multiple times
pixi-project greet "World" --count 3

# Add extra verbosity
pixi-project greet "World" --verbose
```

## Python API

You can also use Pixi Project as a Python library:

```python
from pixi_project.cli import greet

# Call the greet function directly
greet("World", count=3, verbose=True)
``` 