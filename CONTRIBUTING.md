# Contributing

This document describes the tools required to test the `foc-mlx` codebase.

## Development Setup

Fork the repository on `github.com`, then clone locally:

```sh
git clone git@github.com:YOUR-USERNAME/foc-mlx.git
cd motion
```

Sync local dependencies:

```sh
uv sync
```

Project dependencies are configured in `pyproject.toml`:

- mlx for array operations;
- altair and polars for plotting;
- pytest for testing;

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

To update:

```sh
uv self update
uv tool update --all
```

Install and test pre-commit hooks[^2]:

```sh
prek install
prek -a
```

> [!TIP]
> If the hooks all pass then the codebase is setup correctly.

<!-- footnotes -->

[^1]: Tools are installed in the `$PATH` and most can detect a python virtual environment. This is handy for use across multiple projects and applications.

[^2]: See `prek.toml` for configured hooks. By default, pre-commit hooks are run at each commit on staged files.
