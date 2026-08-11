# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]
### All sections: Added / Changed / Deprecated / Removed / Fixed / Security

## [0.1.0] - 2026-08-10'

### Added

- Docker Compose setup (api, worker, PostgreSQL, Redis)
- CI pipeline (lint + tests via GitHub Actions)
- Git workflow: `main`/`develop` protected branches, `feature/*`/`release/*`/`hotfix/*`
  conventions, PR template, CD workflow templates for staging/production

### Security

- Create SECURITY.md

## [Unreleased]

### Added

- Project scaffold: FastAPI + uv, layered structure (`api`/`services`/`repositories`/
  `models`/`schemas`/`core`/`workers`/`db`), health-check endpoint
