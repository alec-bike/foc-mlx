# Contributing

This document describes how to make changes to the `foc-mlx` project.

## Development Setup

> [!TIP]
> Ensure that [git-lfs][1] is installed and initialized.

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd foc-mlx
```

### Dependencies

Project dependencies are configured in `pyproject.toml`. The core dependency is `mlx`.

Development `dev` dependencies:

- `pytest` for regression testing;
- `ruff` and `ty` for python code checking;
- `altair` and `polars` for the example plots.

Sync all dependencies:

```sh
uv sync
```

## Branch and Test

Create a new git branch to make changes to the repository:

```sh
git switch -c <your-branch-name>
```

Check your changes by running the equivalent CI tests:

```sh
uv run ruff format --check
uv run ruff check
uv run ty check -v
uv run pytest
```

> [!TIP]
> For testing on Linux, the `mlx-cpu` dependency is also needed:
>
> ```sh
> uv pip install mlx-cpu
> ```

If these all pass, push your branch to the remote repository and follow the GitHub process to submit a PR.

<!-- links -->

[1]: https://git-lfs.com
