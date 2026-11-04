# AGENTS.md

`foc-mlx`: Python library of power-variant Field Oriented Control transforms (Clarke, Park, inverses, SVM, duty cycle) built on `mlx` (array library optimized for Apple Silicon).

## Layout

- `src/foc_mlx/core.py`: all implementations.
- `src/foc_mlx/__init__.py`: re-exports public functions via `__all__`.
- `tests/test_foc.py`: pytest tests.
- `docs/api.md`: hand-written API reference. Keep in sync with `core.py` docstrings, including `Raises`.
- `examples/transforms.py`: plot example (`altair`, `polars`).
- `.github/workflows/ci.yaml`: Linux CI.

## Commands

```sh
uv sync  # once per fresh .venv
uv lock --check
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest
```

These mirror CI. Keep `ci.yaml`, `CONTRIBUTING.md` and this list consistent. On Linux also run `uv pip install mlx-cpu`.

## Conventions

- Google-style docstrings (`Parameters:` / `Returns:` / `Raises:`), line length 100.
- Inputs are validated up front:
  - wrong type raises `AttributeError` (from the first `.size` access);
  - empty or mismatched size raises `ValueError`;
  - invalid input raises `ValueError`.
- Tests that pass a wrong type on purpose use `# ty: ignore`.
- `*.svg` stays in git-lfs.
- Leave `[tool.uv] preview-features = true`.

## Outstanding issues

- `.size` vs `.shape` validation (#13): same-count arrays with different shapes pass, and valid broadcasting is rejected.
- Test gaps: only `clarke` and `park` have wrong-type tests, and `svm` has no bad-`v_bus` test.
- CI: `ci.yaml` lacks `permissions: contents: read`.
