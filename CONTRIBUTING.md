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

- polars for DataFrames;
- altair for plotting;
- pytest for testing;

To sync dependencies:

```sh
uv sync
```

> [!TIP]
> `uv sync` will also download python and create a virtual environment (if needed).

## Tool Setup

The following system tools are used to manage the codebase:

- mdformat to format markdown documents;
- ruff and ty to check python code.

To install tools:

```sh
uv tool install ruff
uv tool install ty
```

Tools are installed in the `$PATH` and most can detect a python virtual environment. This is handy for use across multiple projects and applications.

## Branch and Test

Create a new git branch to make changes to the repository:

```sh
git switch -c <your-branch-name>
```

Check your changes by running all tests on the codebase:

```sh
uv run ruff check
uv run ruff format
uv run ty check
uv run pytest --cov
```

If these all pass, push changes to the remote repository and follow the GitHub process to submit a PR for your branch.
