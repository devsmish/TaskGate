# TaskGate

Task/Project Management API (mini-Trello/Jira) — a portfolio project built with FastAPI + PostgreSQL.

## Tech stack

- Python 3.12, FastAPI
- PostgreSQL 16, SQLAlchemy 2.0 (async), Alembic
- Redis + ARQ (background jobs, webhooks)
- uv — dependency manager

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

## License

Copyright (c) 2026 devsmish. All rights reserved. See [LICENSE](./LICENSE) — this code
is available for viewing only; use, copying, and modification without the author's
written permission are not allowed.
