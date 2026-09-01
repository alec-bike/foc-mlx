# Field Oriented Control

The `foc-mlx` library implements power-variant Field Oriented Control core transforms (Park, Clarke) with Space Vector Modulation (SVM). It uses `mlx` for array operations that are optimized for Apple Silicon.

## Getting Started

Clone the `foc-mlx` repository:

```sh
git clone git@github.com:alec-bike/foc-mlx.git
cd foc-mlx
```

> [!TIP]
> This repository uses uv to manage dependencies. See [uv][1] for setup instructions.

Sync local dependencies:

```sh
uv sync
```

Refer to the python [API](docs/api.md) which documents `foc-mlx` public functions.

## Examples

Calculate the Clarke transform:

```python
from mlx.core import linspace, sin, pi
from foc_mlx import clarke

theta = linspace(0, 2 * pi, 1000)  # electrical angle in rad
i_a = sin(theta)  # phase currents in Amp
i_b = sin(theta - 2 * pi / 3)
i_alpha, i_beta = clarke(i_a, i_b)
print(i_alpha)
```

Plot FOC waveforms:

```sh
uv run examples/transforms.py
```

> [!TIP]
> Running the examples works best in an interactive notebook such as Colab or Jupyter.

![FOC Waveforms.](docs/foc_waveforms.svg)

## Next Steps

To contribute to the codebase, see [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- links -->

[1]: https://docs.astral.sh/uv/getting-started/installation
