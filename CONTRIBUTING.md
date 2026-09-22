# Contributing

This document describes the steps to contribute to the `foc-mlx` codebase.

## Development Setup

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd foc-mlx
```

Project dependencies are configured in `pyproject.toml`. The only core dependency is `mlx`.

Additional dev dependencies are:

- altair and polars for the example plots;
- ruff and ty for python linting and type checking;
- pytest for testing.

To sync dependencies:

```sh
uv sync
```

> [!TIP]
> `uv sync` will also download python and create a virtual environment (if needed).

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

If these all pass, push changes to the remote repository and follow the GitHub process to submit a PR for your branch.
