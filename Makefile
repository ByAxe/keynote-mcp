# Keynote-MCP Makefile

.PHONY: help install install-dev test lint format clean build upload

# Default target
help: ## Show help
	@echo "Keynote-MCP Development Tools"
	@echo ""
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Installation
install: ## Install project dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .

install-all: install install-dev ## Install all dependencies

# Code quality
lint: ## Run linters
	@echo "Running flake8..."
	flake8 src/ tests/
	@echo "Running mypy..."
	mypy src/
	@echo "Running bandit..."
	bandit -r src/
	@echo "Running safety..."
	safety check

format: ## Format code
	@echo "Running black..."
	black src/ tests/
	@echo "Running isort..."
	isort src/ tests/

format-check: ## Check code formatting
	@echo "Checking black..."
	black --check src/ tests/
	@echo "Checking isort..."
	isort --check-only src/ tests/

# Testing
test: ## Run tests
	pytest tests/ -v

test-cov: ## Run tests with coverage report
	pytest tests/ -v --cov=keynote_mcp --cov-report=html --cov-report=term

test-unit: ## Run unit tests
	pytest tests/ -v -m "unit"

test-integration: ## Run integration tests
	pytest tests/ -v -m "integration"

# Build and publish
clean: ## Clean build files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build package
	python -m build

upload-test: build ## Upload to test PyPI
	twine upload --repository testpypi dist/*

upload: build ## Upload to PyPI
	twine upload dist/*

# Development
dev-setup: ## Set up development environment
	python -m venv .venv
	@echo "Run: source .venv/bin/activate"
	@echo "Then: make install-all"

server: ## Start MCP server
	python start_server.py

demo: ## Run demo
	python examples/basic_usage.py

# Checks
check-all: format-check lint test ## Run all checks

pre-commit: format lint test ## Pre-commit checks

# Version
version: ## Show version info
	@python -c "import keynote_mcp; print(f'Version: {keynote_mcp.__version__}')"

# Environment
env-check: ## Check environment
	@echo "Python version:"
	@python --version
	@echo "Virtual environment:"
	@which python
	@echo "Installed packages:"
	@pip list | grep -E "(keynote|mcp|aiohttp|pytest)"

# Git
git-clean: ## Clean git repository
	git clean -fd
	git reset --hard HEAD

# Project info
info: ## Show project info
	@echo "Project: Keynote-MCP"
	@echo "Description: MCP server for Apple Keynote automation"
	@echo "Version: $(shell python -c 'import keynote_mcp; print(keynote_mcp.__version__)')"
	@echo "Python: $(shell python --version)"
	@echo "Path: $(shell pwd)"
