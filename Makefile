# Makefile

# Variables
PYTHON=python3
POETRY=poetry

.PHONY: help install lint test clean setup

help:
	@echo "Commands:"
	@echo "  setup   : Set up the development environment."
	@echo "  install : Install project dependencies."
	@echo "  lint    : Run flake8 linter."
	@echo "  test    : Run pytest tests."
	@echo "  clean   : Clean up temporary files."

setup:
	@bash scripts/setup_dev_environment.sh

install:
	@$(POETRY) install

lint:
	@$(POETRY) run flake8 .

test:
	@$(POETRY) run pytest

clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

