# Contributing Guide

Thank you for your interest in Keynote-MCP! We welcome and appreciate all forms of contribution.

## How to Contribute

### Report Issues
- Use [GitHub Issues](https://github.com/ByAxe/keynote-mcp/issues) to report bugs
- Please include as much detail as possible:
  - macOS version
  - Python version
  - Keynote version
  - Error messages and steps to reproduce

### Feature Requests
- Use the "Feature Request" template in Issues
- Describe the feature you'd like in detail
- Explain the use case and value

### Code Contributions
1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## Development Setup

### 1. Clone the project
```bash
git clone https://github.com/ByAxe/keynote-mcp.git
cd keynote-mcp
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Configure environment variables
```bash
cp env.example .env
# Edit .env and set required environment variables
```

### 5. Run tests
```bash
pytest tests/
```

## Coding Standards

### Python Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation
- Line length should not exceed 88 characters
- Use meaningful variable and function names

### Code Formatting
We use the following tools for code formatting:
```bash
# Format code
black .

# Sort imports
isort .

# Lint
flake8 .

# Type checking
mypy src/
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_presentation.py

# Run with coverage
pytest --cov=src tests/
```

### Writing Tests
- Write unit tests for new features
- Place test files in the `tests/` directory
- Prefix test files with `test_`
- Use the pytest framework

## Commit Convention

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `style`: Code formatting changes
- `refactor`: Code refactoring
- `test`: Test-related changes
- `chore`: Build process or tooling changes

### Example
```
feat(unsplash): add image search functionality

- Implement Unsplash API integration
- Support keyword search
- Support image orientation filtering

Closes #123
```

## Pull Request Process

### Pre-submission Checklist
- [ ] Code passes all tests
- [ ] Code follows formatting standards
- [ ] Necessary tests have been added
- [ ] Related documentation has been updated
- [ ] Commit messages follow the convention

### PR Description
Please include in your PR:
- Brief description of changes
- Related Issue number
- Test instructions
- Screenshots (if applicable)

### Code Review
- All PRs require code review
- At least one maintainer approval is needed
- Automated tests must pass

## Community Guidelines

### Code of Conduct
- Respect all participants
- Use inclusive language
- Accept constructive criticism
- Focus on what's best for the community

### Communication
- Use GitHub Issues for public discussion
- Maintain a friendly and professional attitude
- Respond promptly to comments and feedback

## Contact

If you have any questions:

- Create a [GitHub Issue](https://github.com/ByAxe/keynote-mcp/issues)

Thank you for contributing! Every PR, Issue, and suggestion makes this project better.
