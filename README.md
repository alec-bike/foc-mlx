# Field Oriented Control

The `foc-mlx` python library implements the power-variant Field Oriented Control core transforms (Park, Clarke) with Space Vector Modulation (SVM). It uses `mlx` for array operations optimized for Apple Silicon.

## Getting Started

Clone the `foc-mlx` repository:

```sh
git clone git@github.com:alec-bike/foc-mlx.git
cd foc-mlx
```

> [!TIP]
> This repository uses `uv` to manage dependencies. See [uv][1] for setup instructions.

Sync all local dependencies:

```sh
uv sync
```

Run the example script to generate FOC waveforms:

```sh
uv run examples/transforms.py
```

![FOC Waveforms.](docs/transforms.svg)

## Next Steps

Look through the [Function Reference](docs/api.md) which describes the `foc-mlx` python API.

An example of using the API to calculate the Clarke transform:

```python
from mlx.core import linspace, sin, pi
from foc_mlx import clarke

theta = linspace(0, 2 * pi, 1000)  # electrical angle in rad
i_a = sin(theta)  # phase currents in Amp
i_b = sin(theta - 2 * pi / 3)
i_alpha, i_beta = clarke(i_a, i_b)
print(i_alpha)
```

## Development

To develop and test the codebase, see [Contributing](CONTRIBUTING.md).

<!-- links -->

[1]: https://docs.astral.sh/uv/getting-started/installation
