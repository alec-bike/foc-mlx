# Contributing

This document describes the steps to contribute to the `foc-mlx` codebase.

## Development Setup

Fork the `foc-mlx` repository on GitHub and clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd foc-mlx
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

Install pre-commit hooks[^2]:

```sh
prek install
```

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

Run all tests on the codebase:

```sh
prek -a
```

If the hooks all pass, push changes to the remote repository, then follow the GitHub process to submit a PR for your branch.

<!-- footnotes -->

[^2]: See `prek.toml` for configured hooks. When installed, these hooks are run at each commit on staged files.

[^1]: Tools are installed in the `$PATH` and most can detect a python virtual environment. This is handy for use across multiple projects and applications.
