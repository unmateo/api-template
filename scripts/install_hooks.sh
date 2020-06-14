#! /usr/bin/env sh
echo "installing pre-commit hooks"
docker-compose run api pre-commit install -c /app/docker/.pre-commit-config.yaml
