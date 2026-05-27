#!/bin/bash

# Exit if any command fails
set -e

VENV_DIR=".venv"
VENV_PIP="$VENV_DIR/bin/pip"

# Check if virtual environment already exists
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv "$VENV_DIR"
else
  echo "Virtual environment already exists!"
fi

echo "Installing Dependencies..."
"$VENV_PIP" install --upgrade pip
"$VENV_PIP" install black==25.1.0 pre-commit==4.2.0 flake8==7.2.0 mypy==1.16.0 isort==6.0.1

"$VENV_DIR/bin/pre-commit" install

echo "Static analysis env is set up and ready to use!"