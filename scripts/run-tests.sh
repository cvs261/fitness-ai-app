#!/bin/bash
echo "Running tests..."
source .venv/bin/activate
export FLASK_ENV=testing
pytest --color=yes
