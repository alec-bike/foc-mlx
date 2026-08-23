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

The core transforms can be found in `src/foc_mlx/core.py`. Refer also to the python [API](docs/api.md) which documents all public functions.

## Examples

Calculate the Clarke transform:

```python
from mlx.core import linspace, sin, pi
from foc_mlx import clarke

theta = linspace(0, 2 * pi, 1000)  # electrical angle in rad
i_a = sin(theta)  # phase currents in Amp
i_b = sin(theta - 2 * pi / 3)
i_alpha, i_beta = clarke(i_a, i_b)
```

Simulate and plot the FOC waveforms:

```python
from foc_mlx import control, plot

df = control()
plot(df).save("foc_waveforms.html")
```

![FOC Waveforms.](docs/foc_waveforms.svg)

## Development

To test and develop the codebase, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- links -->

[1]: https://docs.astral.sh/uv/getting-started/installation
