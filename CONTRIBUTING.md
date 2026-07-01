# Contributing to TCODER

We welcome contributions from everyone! Here are some guidelines to help you get started.

## Code of Conduct

Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue in our GitHub repository with:
- A clear and descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Your environment details (OS, Python version, TCODER version)

### Suggesting Features

We love feature suggestions! Please open an issue and describe:
- The use case for the feature
- How you imagine it working
- Any alternative solutions you considered

### Submitting Code

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Run the tests (`pytest`)
5. Format your code with `black` and `ruff`
6. Commit your changes (`git commit -am 'Add some feature'`)
7. Push to the branch (`git push origin feature/my-feature`)
8. Open a Pull Request

## Development Setup

1. Clone your fork
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -e .[dev]`
5. Install pre-commit hooks: `pre-commit install` (if we have them)

## Running Tests

```bash
pytest
```

## Code Style

- We use `black` for formatting
- We use `ruff` for linting
- We use `mypy` for type checking
