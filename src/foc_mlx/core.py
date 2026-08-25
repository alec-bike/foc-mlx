"""Field Oriented Control core transforms.

Power variant forms of the Park/Clarke transforms and Space Vector Modulation.
"""

import mlx.core as mx
from mlx.core import array

SQRT3: array = mx.sqrt(array(3.0))


def clarke(i_a: array, i_b: array) -> tuple[array, array]:
    """Clarke Transform, power variant form.

    Transform 3-phase current into 2-phase orthogonal representation in stationary
    reference frame, with alpha aligned to A-phase axis.

    Parameters:
        i_a: A-phase current array.
        i_b: B-phase current array.

    Returns:
        i_alpha: alpha current array, aligned to `i_a`.
        i_beta: beta current array.

    Raises:
        ValueError: invalid array size.
    """
    if (i_a.size <= 0) or (i_a.size != i_b.size):
        msg = "Invalid array size."
        raise ValueError(msg)

    i_alpha = i_a  # alpha frame aligned with a-phase
    i_beta = (i_a + 2 * i_b) / SQRT3
    return i_alpha, i_beta


def park(i_alpha: array, i_beta: array, theta: array) -> tuple[array, array]:
    """Park Transform.

    Transform stationary alpha-beta frame to rotating DQ frame, given motor electrical angle.

    Parameters:
        i_alpha: alpha current array.
        i_beta: beta current array.
        theta: motor electrical angle array (radian).

    Returns:
        i_d: direct current array.
        i_q: quadrature current array.

    Raises:
        ValueError: invalid array size.
    """
    if (i_alpha.size <= 0) or (i_alpha.size != i_beta.size) or (i_beta.size != theta.size):
        msg = "Invalid array size."
        raise ValueError(msg)

    i_d = i_alpha * mx.cos(theta) + i_beta * mx.sin(theta)
    i_q = -i_alpha * mx.sin(theta) + i_beta * mx.cos(theta)
    return i_d, i_q


def inv_clarke(v_alpha: array, v_beta: array) -> tuple[array, array, array]:
    """Inverse Clarke Transform, power variant form.

    Parameters:
        v_alpha: alpha voltage array.
        v_beta: beta voltage array.

    Returns:
        v_a: A-phase voltage array.
        v_b: B-phase voltage array.
        v_c: C-phase voltage array.

    Raises:
        ValueError: invalid array size.
    """
    if (v_alpha.size <= 0) or (v_alpha.size != v_beta.size):
        msg = "Invalid array size."
        raise ValueError(msg)

    v_a = v_alpha
    v_b = (-v_alpha + SQRT3 * v_beta) / 2
    v_c = (-v_alpha - SQRT3 * v_beta) / 2
    return v_a, v_b, v_c


def inv_park(v_d: array, v_q: array, theta: array) -> tuple[array, array]:
    """Inverse Park Transform.

    Parameters:
        v_d: direct voltage array.
        v_q: quadrature voltage array.
        theta: motor electrical angle array (radian).

    Returns:
        v_alpha: alpha voltage array.
        v_beta: beta voltage array.

    Raises:
        ValueError: invalid array size.
    """
    if (v_d.size <= 0) or (v_d.size != v_q.size) or (v_q.size != theta.size):
        msg = "Invalid array size."
        raise ValueError(msg)

    v_alpha = v_d * mx.cos(theta) - v_q * mx.sin(theta)
    v_beta = v_d * mx.sin(theta) + v_q * mx.cos(theta)
    return v_alpha, v_beta


def svm(v_a: array, v_b: array, v_c: array, v_bus: float) -> tuple[array, array, array]:
    """Space Vector Modulation (SVM).

    Shift phase voltages to minimize torque ripple and convert to duty cycle.

    Parameters:
        v_a: A-phase voltage array.
        v_b: B-phase voltage array.
        v_c: C-phase voltage array.
        v_bus: bus voltage float.

    Returns:
        t_a: A-phase duty cycle array.
        t_b: B-phase duty cycle array.
        t_c: C-phase duty cycle array.

    Raises:
        ValueError: invalid array size.
    """
    if (v_a.size <= 0) or (v_a.size != v_b.size) or (v_b.size != v_c.size):
        msg = "Invalid array size."
        raise ValueError(msg)

    # calculate neutral-point voltages
    v = mx.stack([v_a, v_b, v_c])
    v_np = (mx.max(v, 0) + mx.min(v, 0)) / 2.0

    # shift voltages and convert to duty cycle
    t_a = duty_cycle(v_a - v_np, v_bus)
    t_b = duty_cycle(v_b - v_np, v_bus)
    t_c = duty_cycle(v_c - v_np, v_bus)

    return t_a, t_b, t_c


def duty_cycle(v: array, v_bus: float) -> array:
    """Convert phase voltage to duty cycle.

    Note:
        - Input phase voltage `v` is signed.
        - Output duty cycle `t` is between 0 and 1 (0.5 is zero output voltage).
        - Absolute input voltages greater than the bus voltage `v_bus` are clipped.

    Parameters:
        v: input voltage array.
        v_bus: bus voltage float.

    Returns:
        t: duty cycle array.

    Raises:
        ValueError: invalid array size or invalid bus voltage.
    """
    if v.size <= 0:
        msg = "Invalid array size."
        raise ValueError(msg)

    if v_bus <= 0:
        msg = "Invalid bus voltage."
        raise ValueError(msg)

    # shift input voltage and scale by bus voltage
    t = (1 + v / v_bus) / 2
    return mx.clip(t, 0, 1)  # clip to 0-1
