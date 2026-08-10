# TaskGate

Task/Project Management API (mini-Trello/Jira) — a portfolio project built with FastAPI + PostgreSQL.

## Tech stack

- Python 3.12, FastAPI
- PostgreSQL 16, SQLAlchemy 2.0 (async), Alembic
- Redis + ARQ (background jobs, webhooks)
- uv — dependency manager

## Local setup

1. Copy `.env.example` to `.env` and **fill in real values** — `POSTGRES_USER`,
   `POSTGRES_PASSWORD`, `DATABASE_URL`, `JWT_SECRET_KEY`, etc. `.env` is
   gitignored and must never be committed. `docker-compose.yml` has no
   credentials of its own — it only reads `${POSTGRES_USER}` and similar
   from `.env`, so it will refuse to start without one:

   ```bash
   cp .env.example .env
   # then edit .env with real values
   ```

2. Start everything with Docker Compose:

   ```bash
   docker compose up --build
   ```

   > On Windows, the Postgres data directory is bind-mounted to `D:\DB\TaskGate_db`
   > on the host (see `docker-compose.yml`). Make sure the `D:` drive is shared
   > with Docker Desktop (Settings → Resources → File sharing) if you're on the
   > Hyper-V backend; with the WSL2 backend this works out of the box.

3. The API will be available at `http://localhost:8000`, docs at `http://localhost:8000/docs`.

## Development without Docker

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## Tests

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
```

## Project structure

```
app/
 ├── api/v1/        # routers
 ├── services/       # business logic
 ├── repositories/    # data access
 ├── models/           # SQLAlchemy models
 ├── schemas/           # Pydantic schemas
 ├── core/               # config, security, permissions
 ├── workers/             # ARQ tasks (webhooks, cron jobs)
 ├── db/                   # session, base model, migrations
 └── tests/
```

## Development status

The project is built in stages — see section 8 of the specification for the roadmap.
Current progress is tracked via issues/project board on GitHub.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the branching workflow (feature branches
per issue, PRs into `develop`, release branches into `main`).

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).

## License

Copyright (c) 2026 devsmish. All rights reserved. See [LICENSE](./LICENSE) — this code
is available for viewing only; use, copying, and modification without the author's
written permission are not allowed.
