# API Template

Dockerized FastAPI application ready for dev and prd environments.

## Features

- __pytest__ testing framework
- __vscode__ config for coding inside container
- __precommit__ hooks for linting
- __SQLAlchemy__ for ORM features
- __PostgreSQL__ as local/prd DB
- __SQLite__ as test DB

## Commands

Install hooks:

`./scripts/install_hooks.sh`

Build:

`./scripts/build.sh`

Test:

`./scripts/test.sh`

Run:

`./scripts/run.sh`
