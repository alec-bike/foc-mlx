# Contributing

This document describes how to contribute to the `foc-mlx` project.

## Development Setup

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd foc-mlx
```

### Dependencies

Project dependencies are configured in `pyproject.toml`. The core dependency is `mlx`.

Development dependencies for testing and CI:

- `ruff` and `ty` for linting and type-checking; and
- `pytest` for regression testing.

Optionally dependencies used by the example script:

- `altair` and `polars` for plotting.

To sync all dependencies:

```sh
uv sync --all-groups
```

## Branch and Test

Create a new git branch to make changes to the repository:

```sh
git switch -c <your-branch-name>
```

Check your changes by running CI tests locally:

```sh
uv run ruff check
uv run ruff format
uv run ty check
uv run pytest
```

> [!TIP]
> For testing on Linux, the `mlx-cpu` dependency is also needed:
>
> ```sh
> uv pip install mlx-cpu
> ```

If these all pass, push your branch to the remote repository and follow the GitHub process to submit a PR.
