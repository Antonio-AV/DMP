# Project Architecture

## Module Boundaries

| Module | Responsibility | May depend on | Must not depend on |
| --- | --- | --- | --- |
| `dmp.domain` | Entities, value objects, statuses, and business rules | Python standard library and other domain modules | `streamlit`, `dmp.ui`, or SQLite adapters |
| `dmp.application` | Use cases and ports for external dependencies | `dmp.domain` and Python standard library | `streamlit` or concrete SQLite code |
| `dmp.data` | SQLite connection, repositories, and versioned migrations | `dmp.domain`, application ports, and `sqlite3` | `streamlit` and UI state |
| `dmp.ui` | Streamlit entrypoint, pages, and presentation state | `dmp.application` and concrete data adapters for composition | Business rules implemented in widgets |
| `tests` | Behavior-focused tests at public boundaries | Application, domain, data, and minimal UI integration | Production-only test doubles that bypass behavior |

The intended dependency direction is:

```text
dmp.ui -> dmp.application -> dmp.domain
   |              |
   +----------> dmp.data
```

The application layer defines the interfaces it needs from persistence. The
data layer implements those interfaces with local SQLite. This keeps use cases
independent from both Streamlit and the storage mechanism.

## Offline-First Data Flow

- SQLite is the only persistence technology for business state.
- SQLite access uses Python's standard-library `sqlite3` module.
- The database file stays on the Windows computer and is not committed to Git.
- The Streamlit session may contain transient presentation state such as the
  active cart; persisted business state belongs to SQLite.
- No remote API, cloud service, or network dependency is part of the local
  application path.

Transactions for changes that affect related business records belong in the
data/application implementation of each use case, not in UI callbacks.

## Entrypoints

- Local application: `src/dmp/ui/app.py`, launched with
  `uv run streamlit run src/dmp/ui/app.py --server.address localhost`.
- Test suite: `tests/`, launched from the repository root with `uv run pytest`.

The reproducible environment and quality commands are intentionally deferred to
MPJ-50. GitHub Actions are intentionally deferred to MPJ-52.
