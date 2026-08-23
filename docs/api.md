# foc-mlx

Field Oriented Control (FOC) python function reference.

Modules:

- [core](#core) – compute FOC core transforms.
- [sim](#sim) – simulate and visualize FOC waveforms.

## core

Field Oriented Control core transforms.

Functions:

- [clarke](#coreclarke) – Clarke Transform, power variant form.
- [duty_cycle](#coreduty_cycle) – convert phase voltage to duty cycle.
- [inv_clarke](#coreinv_clarke) – Inverse Clarke Transform, power variant form.
- [inv_park](#coreinv_park) – Inverse Park Transform.
- [park](#corepark) – Park Transform.
- [svm](#coresvm) – Space Vector Modulation (SVM).

Usage:

```python
from foc_mlx import clarke, duty_cycle, inv_clarke, inv_park, park, svm
from mlx.core import array
```

### core.clarke

```python
i_alpha, i_beta = clarke(i_a, i_b)
```

Clarke Transform, power variant form.

Transform 3-phase current into 2-phase orthogonal representation in stationary
reference frame, with alpha aligned to A-phase axis.

Parameters:

- `i_a: array` – A-phase current array.
- `i_b: array` – B-phase current array.

Returns:

- `i_alpha: array` – alpha current array, aligned to `i_a`.
- `i_beta: array` – beta current array.

Raises:

- `ValueError` – invalid array size.

### core.duty_cycle

```python
t = duty_cycle(v, v_bus)
```

Convert phase voltage to duty cycle.

Parameters:

- `v: array` – input voltage array.
- `v_bus: float` – bus voltage float.

Returns:

- `t: array` – duty cycle array.

Raises:

- `ValueError` – invalid array size or invalid bus voltage.

Notes:

- Input phase voltage `v` is signed.
- Output duty cycle `t` is between 0 and 1 (0.5 is zero output voltage).
- Absolute input voltages greater than `v_bus` are clipped.

### core.inv_clarke

```python
v_a, v_b, v_c = inv_clarke(v_alpha, v_beta)
```

Inverse Clarke Transform, power variant form.

Parameters:

- `v_alpha: array` – alpha voltage array.
- `v_beta: array` – beta voltage array.

Returns:

- `v_a: array` – A-phase voltage array.
- `v_b: array` – B-phase voltage array.
- `v_c: array` – C-phase voltage array.

Raises:

- `ValueError` – invalid array size.

### core.inv_park

```python
v_alpha, v_beta = inv_park(v_d, v_q, theta)
```

Inverse Park Transform.

Parameters:

- `v_d: array` – direct voltage array.
- `v_q: array` – quadrature voltage array.
- `theta: array` – motor electrical angle array in radian.

Returns:

- `v_alpha: array` – alpha voltage array.
- `v_beta: array` – beta voltage array.

Raises:

- `ValueError` – invalid array size.

### core.park

```python
i_d, i_q = park(i_alpha, i_beta, theta)
```

Park Transform.

Transform stationary alpha-beta frame to rotating DQ frame, given motor electrical angle.

Parameters:

- `i_alpha: array` – alpha current array.
- `i_beta: array` – beta current array.
- `theta: array` – motor electrical angle array in radian.

Returns:

- `i_d: array` – direct current array.
- `i_q: array` – quadrature current array.

Raises:

- `ValueError` – invalid array size.

### core.svm

```python
t_a, t_b, t_c = svm(v_a, v_b, v_c, v_bus)
```

Space Vector Modulation (SVM).

Shift phase voltages to minimize torque ripple and convert to duty cycle.

Parameters:

- `v_a: array` – A-phase voltage array.
- `v_b: array` – B-phase voltage array.
- `v_c: array` – C-phase voltage array.
- `v_bus: float` – bus voltage float.

Returns:

- `t_a: array` – A-phase duty cycle array.
- `t_b: array` – B-phase duty cycle array.
- `t_c: array` – C-phase duty cycle array.

Raises:

- `ValueError` – invalid array size.

## sim

Example script to simulate and plot FOC waveforms.

Functions:

- [control](#simcontrol) – simulate FOC waveforms.
- [plot](#simplot) – plot a DataFrame of waveforms.

Usage:

```python
from foc_mlx import control, plot
```

### sim.control

```python
df = control()
```

Simulate FOC waveforms.

Parameters:

- `v_bus: float` – bus voltage (Volt).
- `i_pk: float` – peak sensed current (Amp).
- `k_p: float` – gain (Volt/Amp).

Returns:

- `df: DataFrame` – DataFrame of FOC waveforms.

### sim.plot

```python
cht = plot(df)
cht.save("waveforms.html")
```

Plot FOC waveforms.

Parameters:

- `df: DataFrame` – DataFrame of FOC waveforms.

Returns:

- `cht: ConcatChart | HConcatChart` – line plot of waveforms.
