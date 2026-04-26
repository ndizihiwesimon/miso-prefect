# miso-prefect

A lightweight Prefect project with a single greeting flow, deployment config, and local smoke tests.

## Overview

This repository contains a small Prefect flow in `main.py` and a `prefect.yaml` deployment that targets the local `miso` process work pool.

## Getting Started

Create a virtual environment and install the project dependencies:

```bash
uv sync --python 3.11
```

Run the flow directly:

```bash
.venv/bin/python main.py
```

Run the tests:

```bash
.venv/bin/python -m unittest discover -s tests
```

## Deployment

Start a local Prefect server in one terminal:

```bash
.venv/bin/prefect server start --host 127.0.0.1
```

Start a worker for the configured process work pool in another terminal:

```bash
PREFECT_API_URL=http://127.0.0.1:4200/api .venv/bin/prefect worker start --pool miso
```

Register the deployment and trigger a run:

```bash
PREFECT_API_URL=http://127.0.0.1:4200/api .venv/bin/prefect deploy
PREFECT_API_URL=http://127.0.0.1:4200/api .venv/bin/prefect deployment run 'main/main-deployment'
```

## Development

- Keep flows modular and reusable.
- Store configuration in environment variables where possible.
- Add tests for flow logic and tasks.
- Create feature branches using `feature/feature-name`.
- Open pull requests into `dev`, then open a second pull request from `dev` into `main`.

## License

MIT LICENSE
