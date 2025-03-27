#!/bin/bash
docker system prune -af
docker volume prune -f
rm -rf __pycache__ .pytest_cache