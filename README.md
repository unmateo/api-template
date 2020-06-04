# API Template

Dockerized FastAPI application ready for dev and prd environments.

## Development

- __pytest__ testing framework
- __vscode__ config for coding inside container
- __precommit__ hooks for linting

## Production

Build:

`docker build . --no-cache -t api`

Run:

`docker run -d -p 8000:80 --name api api`
