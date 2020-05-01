#! /usr/bin/env sh
echo "installing pre-commit hooks"
pre-commit install -c /app/docker/.pre-commit-config.yaml
