# Contributing

## Branches

Use one branch per issue. When creating a branch manually, use:

```text
<type>/<ticket-or-description>
```

Examples:

```text
feat/MPJ-123-sales-flow
fix/MPJ-124-stock-boundary
docs/MPJ-125-domain-rules
```

Keep an existing issue branch name when the development environment provides
one. Linear is the source of issue identifiers. Agent pull requests must target
`develop`; keep `main` for releases and explicitly authorized hotfixes.

## Commits

Use Conventional Commits:

```text
<type>(<scope>): <imperative description>
```

Valid types are `feat`, `fix`, `docs`, `style`, `refactor`, `test`, and `chore`.
Keep the subject under 72 characters. Add a body for non-trivial changes and
explain why the change is needed rather than restating the diff.

Create commits at coherent milestones, not for every small edit. Never commit
secrets, generated build artifacts, local databases, installers, or failing
work. Dependency lockfiles are committed for reproducible environments.

## Pull Requests

Pull requests should be small, focused, and linked to their Linear issue. Agent
pull requests must target `develop`:

```bash
gh pr create --base develop
```

Use a Conventional Commit-style title:

```text
<type>(<scope>): <imperative description>
```

Include:

- A concise summary and motivation.
- The Linear issue link and Project context.
- The acceptance criteria and their status.
- Commands used for validation.
- Known risks, limitations, and follow-up work.

Run the complete validation gate before pushing. Review the complete diff
against `develop` before requesting review. Use Orca Linear to attach the PR,
post one completion comment, and move the issue to `In Review` when valid. Do
not merge a pull request while required checks are failing.

## Local Development

Use `uv` to create a reproducible Python environment once the project metadata
is available:

```bash
uv sync --locked --dev
```

Run the application locally with:

```bash
uv run streamlit run <streamlit-entrypoint>
```

Run the expected validation commands from the repository root:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy .
uv run pytest
```

Keep dependency metadata and its lockfile synchronized when dependencies change.
Do not edit lockfiles manually.

## Testing

Write behavior-focused tests before implementation when practical. Prefer the
application/use-case boundary backed by a temporary SQLite database. Test
user-visible outcomes such as totals, stock balances, debt balances, receipts,
and cancellation behavior instead of private helpers.

## Data And Security

- Never commit secrets, API keys, credentials, `.env` files, local SQLite
  databases, backups, generated installers, or build artifacts.
- Keep passwords outside source control.
- Use transactions for operations that change related sale, stock, debt, receipt,
  and cash state.
- Preserve historical prices and stock movements.
- Do not expose the local Streamlit server to the network without an explicit
  security decision.

## Scope

Do not add AI, cloud synchronization, automatic migration, fiscal integrations,
supplier purchasing workflows, or unrelated refactors without an explicit issue
and acceptance criteria.
