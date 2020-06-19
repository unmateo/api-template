# API Template

Dockerized FastAPI application ready for dev and prd environments.

## Features

- __Docker__ for local and production environments
- __pytest__ testing framework
- __precommit__ hooks for linting
- __SQLAlchemy__ for ORM features
- __PostgreSQL__ as local/prd DB
- __SQLite__ as test DB
- __VS Code__ config for remote container development
- __wdb + VS Code debugging__

## Commands

- Install hooks: `./scripts/install_hooks.sh`
- Build: `./scripts/build.sh`
- Test: `./scripts/test.sh`
- Run: `./scripts/run.sh`

## Debugging

- With [WDB](https://github.com/Kozea/wdb):

  1. Add this wherever you want to set up a breakpoint:
  ```python
    import wdb;wdb.set_trace()
  ```
  2. Execute the code normally
  3. Open any browser at _localhost:1984_ and start debugging

- With VsCode

  1. Open workspace in container using Remote-Container extension and provided config (devcontainer.json)
  2. Set your breakpoints by clicking any line number on any .py file
  3. Open /source/debug.py
  4. At VsCode debugging tab, click _Run and Debug_ button. This will open a debugging terminal with your app running on it and exposed at port 8001.
