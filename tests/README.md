# Tests

Tests are organized around observable behavior. The primary seam is the public
application/use-case boundary backed by a temporary SQLite database. Domain
tests may run without a database, while Streamlit tests cover only minimal
presentation journeys and integration with application use cases.

Run the complete test entrypoint from the repository root:

```bash
uv run pytest
```
