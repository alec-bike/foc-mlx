# foc-mlx – agent notes

`foc-mlx` – Python library of power-variant Field Oriented Control transforms (Clarke, Park, inverses, SVM, duty cycle) built on `mlx` (array library optimized for Apple Silicon).

## Layout

- `src/foc_mlx/core.py` – all implementations. `__init__.py` re-exports public functions through `__all__`, so add any new functions there too.
- `tests/test_foc.py` – pytest tests.
- `docs/api.md` – hand-written API reference. Keep in sync with `core.py` docstrings.
- `examples/transforms.py` – plot example (`altair`, `polars`).
- `.github/workflows/ci.yaml` – Linux CI.

## Commands – run from repo root

Use `uv`. Sync and setup dependencies (run once per fresh `.venv`):

```sh
uv sync
```

On Linux also run `uv pip install mlx-cpu`.

CI test commands (run to validate codebase changes):

```sh
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest
```

These mirror the CI tasks in `.github/workflows/ci.yaml`. Keep CI tasks, `CONTRIBUTING.md` and these commands consistent.

## Conventions

- Google-style docstrings.
- Inputs are validated up front and raise: `AttributeError` (wrong type); `ValueError` (empty or mismatched size, invalid bus voltage input).
- Tests that intentionally pass a wrong type use `# ty: ignore`.

## Working style

- When asked to "rescan", report only what changed or remains, and mark items already covered above.
- Prefer suggestions over edits for docs/config unless asked to change files.

## Token-efficient tool use

- Search with `rg -n` before reading. Read files with `offset`/`limit`, not whole.
- Never dump `uv.lock`, `.venv/` or `__pycache__/`. Use `git diff --stat`, then `git diff -- <path>` (exclude `uv.lock`).
- Cap command output – `| tail -30` or `grep` for errors/failures.
- Run independent reads/commands in one turn (or one `codemode` script that filters output). Chain CI checks in a single `bash` call with `tail`.
- Don't re-read a file after editing it. Don't re-run checks that already passed unless files changed.
- Keep answers short. Don't repeat large diffs or file contents back.
