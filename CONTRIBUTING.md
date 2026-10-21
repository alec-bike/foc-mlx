# Contributing

This document describes how to make changes to the `foc-mlx` project.

## Development Setup

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd foc-mlx
```

### Dependencies

Project dependencies are configured in `pyproject.toml`. The core dependency is `mlx`.

Development dependencies:

- `pytest` for regression testing; and
- `poethepoet` for running tasks.

Sync all dependencies:

```sh
uv sync
```

Install `ruff` for python lint and format:

```sh
uv tool install ruff
```

## Branch and Test

Create a new git branch to make changes to the repository:

```sh
git switch -c <your-branch-name>
```

Check your changes by running CI tasks locally:

```sh
uv run poe ci
```

> [!TIP]
> For testing on Linux, the `mlx-cpu` dependency is also needed:
>
> ```sh
> uv pip install mlx-cpu
> ```

If these all pass, push your branch to the remote repository and follow the GitHub process to submit a PR.
