# Contributing / Git workflow

This project follows a full Git Flow: `main` and `develop` as long-lived
protected branches, `feature/*` per issue, `release/*` for release
preparation, `hotfix/*` for urgent production fixes.

## Branches

| Branch | Purpose |
|---|---|
| `main` | Production-ready code only. **Protected** — no direct pushes, only merged via PR from `release/*` or `hotfix/*`. Every merge is tagged with a version and published as a GitHub Release. |
| `develop` | Integration branch, **default branch** of the repository. **Protected** — no direct pushes, only merged via PR from `feature/*`, `release/*` (back-merge) or `hotfix/*`. |
| `feature/<issue-number>-<short-slug>` | One branch per issue. Branched from `develop`, merged back into `develop` via PR. Example: `feature/145-jwt-refresh`. |
| `release/<version>` | Cut from `develop` when preparing a release (e.g. `release/v0.2.3`). Only version bump, changelog, README updates and last-minute fixes happen here — no new features. Merged into **both** `main` (tag + GitHub Release) and back into `develop`. |
| `hotfix/<version>` | For urgent fixes to something already in production. Branched from `main` (not `develop`!), merged into **both** `main` (new patch tag) and `develop`. |

## Day-to-day workflow (feature)

1. Pick or create a GitHub Issue (e.g. `#145 Add JWT refresh token support`).
2. Branch from `develop`:

   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/145-jwt-refresh
   ```

   (GitHub's "Create a branch" button on the issue page does this automatically
   and links the branch to the issue.)

3. Commit as you go:

   ```bash
   git add .
   git commit -m "Add refresh token model"
   git commit -m "Implement refresh endpoint"
   ```

4. Push and open a PR **into `develop`**:

   ```bash
   git push -u origin feature/145-jwt-refresh
   ```

   In the PR description, always include `Closes #145` (or `Fixes #145`) —
   the PR template reminds you. CI (lint + tests) must pass before merging.

5. Merge on GitHub. **Squash and merge** is the default for `feature/* → develop`
   — keeps `develop` history linear, one commit per feature. The issue closes
   automatically thanks to `Closes #145`.

6. Clean up locally:

   ```bash
   git branch -d feature/145-jwt-refresh
   git checkout develop
   git pull origin develop
   ```

   (The remote branch is deleted automatically by GitHub —
   see "Automatically delete head branches" in repo settings.)

## Releases

```bash
git checkout develop
git pull origin develop
git checkout -b release/v0.2.3
```

Update `README.md`, `CHANGELOG.md`, version strings, commit and push:

```bash
git add .
git commit -m "docs: update README and changelog for v0.2.3"
git push -u origin release/v0.2.3
```

Open **two** PRs from `release/v0.2.3`:

1. `release/v0.2.3 → main` — the actual production release. Merge using a
   regular **merge commit** (not squash — history and tags must stay intact).
2. `main → develop` — brings the changelog/README/version bump back into
   `develop`. Also a regular merge commit.

Both PRs must pass CI. After PR #1 is merged, tag the release:

```bash
git checkout main
git pull origin main
git tag -a v0.2.3 -m "Release v0.2.3: User Auth & Swagger Docs"
git push origin v0.2.3
```

Then GitHub → Releases → Draft a new release → pick the `v0.2.3` tag →
publish. Publishing the release is what triggers the production deploy
(see `.github/workflows/deploy-production.yml`).

Delete `release/v0.2.3` after both PRs are merged.

Finally, sync locally — no manual merging of `main` into `develop` needed,
GitHub already did it via PR #2:

```bash
git checkout develop
git pull origin develop
```

## Hotfixes

For an urgent bug found in production (`main`), branch from `main`, not
`develop` — `develop` may contain unfinished features you don't want to ship
early:

```bash
git checkout main
git pull origin main
git checkout -b hotfix/v0.2.4
# fix the bug, bump patch version
git push -u origin hotfix/v0.2.4
```

Same as a release: open two PRs (`hotfix/v0.2.4 → main` and `main → develop`),
merge both with a regular merge commit, tag `v0.2.4` on `main`, publish a
GitHub Release.

## Merge strategy summary

| PR direction | Strategy |
|---|---|
| `feature/* → develop` | Squash and merge |
| `release/* → main` | Merge commit |
| `hotfix/* → main` | Merge commit |
| `main → develop` | Merge commit |

Configure allowed merge types in Settings → General → Pull Requests to
enforce this (don't rely on remembering to pick the right button).

## Versioning

Semantic Versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking API changes
- **MINOR** — new backwards-compatible functionality
- **PATCH** — bugfixes only (including hotfixes)

## CI/CD

- `.github/workflows/ci.yml` — lint + tests, runs on every push to
  `main`/`develop`/`release/**` and on every PR into `main`/`develop`.
- `.github/workflows/build-image.yml` — reusable workflow that builds and
  pushes a Docker image to GHCR; called by the two deploy workflows below.
- `.github/workflows/deploy-staging.yml` — deploys to the `staging`
  environment on every push to `develop`.
- `.github/workflows/deploy-production.yml` — deploys to the `production`
  environment when a GitHub Release is published. The `production`
  environment should have "Required reviewers" enabled (Settings →
  Environments) so deploys wait for manual approval.

The actual deploy steps in both workflows are placeholders (`TODO`) until
target infrastructure is decided.

## Commit messages

No strict convention enforced yet — keep messages short and descriptive
(imperative mood, e.g. "Add JWT refresh endpoint").
