#!/bin/bash
echo "Running tests..."
source .venv/bin/activate
pytest --color=yes
