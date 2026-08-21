# Field Oriented Control

The `foc-mlx` library implements power-variant Field Oriented Control core transforms (Park, Clarke) with Space Vector Modulation (SVM). It uses `mlx` for array operations that are optimized for Apple Silicon.

## Getting Started

Clone the `foc-mlx` repository:

```sh
git clone git@github.com:alec-bike/foc-mlx.git
cd motion
```

> [!TIP]
> This repository uses uv to manage dependencies. See [uv][1] for setup instructions.

Sync local dependencies:

```sh
uv sync
```

### Example

Calculate the Clarke transform:

```python
from mlx.core import linspace, sin, pi
from foc_mlx.core import clarke

theta = linspace(0, 2 * pi, 1000)  # electrical angle in rad
i_a = sin(theta)  # phase currents in Amp
i_b = sin(theta - 2 * pi / 3)
i_alpha, i_beta = clarke(i_a, i_b)
```

Simulate and plot the FOC waveforms:

```python
from foc_mlx.sim import control
from foc_mlx.plot import plot_df

df = control()
plot_df(df).save("foc_waveforms.html")
```

![FOC Waveforms.](docs/foc_waveforms.svg)

Refer to the [API](docs/api.md) documentation for the full python function reference.

## Development

To test and develop the codebase, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- links -->

[1]: https://docs.astral.sh/uv/getting-started/installation
