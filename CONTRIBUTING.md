# Contributing

This document describes the tools required to test the `foc-mlx` codebase.

## Development Setup

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd motion
```

Project dependencies are configured in `pyproject.toml`:

- mlx for array operations;
- altair and polars for plotting;
- pytest for testing;

To sync dependencies:

```sh
uv sync
```

> [!TIP]
> `uv sync` will also download python and create a virtual environment, if needed.

## Tool Setup

The following system tools[^1] are used to manage the codebase:

- prek to check for issues at commit;
- mdformat to format markdown documents;
- ruff and ty to check python code.

To install tools:

```sh
uv tool install prek
uv tool install mdformat -w mdformat-footnote -w mdformat-gfm
uv tool install ruff
uv tool install ty
```

## Branch and Test

Create a new git branch to make changes to the repository:

```sh
git switch -c <your-branch-name>
```

Install and test pre-commit hooks[^2]:

```sh
prek install
prek -a
```

If the hooks all pass then the changes can be pushed to the remote repository. Follow the usual GitHub PR process to merge changes.

<!-- footnotes -->

[^1]: Tools are installed in the `$PATH` and most can detect a python virtual environment. This is handy for use across multiple projects and applications.

[^2]: See `prek.toml` for configured hooks. When installed, pre-commit hooks are run at each commit on staged files.
