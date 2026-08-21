"""Test foc core transforms."""

import pytest
from mlx.core import array, isclose, pi, sin, sqrt

from foc_mlx import clarke, duty_cycle, inv_clarke, inv_park, park, svm

ZERO = array(0)
ONE = array(1)
EMPTY = array([])
INV_SQRT2 = sqrt(array(0.5))


def test_clarke() -> None:
    """Test the Clarke transform."""
    theta = ZERO  # motor electrical angle, in radian
    i_a = sin(theta)  # phase currents
    i_b = sin(theta - 2 * pi / 3)
    i_alpha, i_beta = clarke(i_a, i_b)
    assert isclose(i_alpha, ZERO)
    assert isclose(i_beta, -ONE)

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = clarke(EMPTY, i_b)

    # ensure assertion error raised for mismatched size inputs
    with pytest.raises(ValueError):
        _ = clarke(array([0, 1]), i_b)


def test_park() -> None:
    """Test the Park transform."""
    theta = array(pi / 4.0)  # motor electrical angle, in radian
    i_alpha = ZERO  # transformed currents
    i_beta = -ONE
    i_d, i_q = park(i_alpha, i_beta, theta)
    assert isclose(i_d, -INV_SQRT2)
    assert isclose(i_q, -INV_SQRT2)

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = park(EMPTY, i_beta, theta)


def test_inv_clarke() -> None:
    """Test the Inverse Clarke transform."""
    v_alpha = -ONE  # transformed voltages
    v_beta = ZERO
    v_a, v_b, v_c = inv_clarke(v_alpha, v_beta)
    assert isclose(v_a, -ONE)
    assert isclose(v_b, array(0.5))
    assert isclose(v_c, array(0.5))

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = inv_clarke(EMPTY, v_beta)


def test_inv_park() -> None:
    """Test the Inverse Park transform."""
    theta = array(pi / 4)  # motor electrical angle, in radian
    v_d = ZERO  # DQ voltages
    v_q = ONE
    v_alpha, v_beta = inv_park(v_d, v_q, theta)
    assert isclose(v_alpha, -INV_SQRT2)
    assert isclose(v_beta, INV_SQRT2)

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = inv_park(EMPTY, v_q, theta)


def test_fwd_inv() -> None:
    """Test forward-inverse equivalence."""
    theta = ZERO  # motor electrical angle, in radian
    i_a = sin(theta)  # phase currents, in Amp
    i_b = sin(theta - 2 * pi / 3)
    i_c = -i_a - i_b
    i_alpha, i_beta = clarke(i_a, i_b)
    i_ao, i_bo, i_co = inv_clarke(i_alpha, i_beta)
    i_d, i_q = park(i_alpha, i_beta, theta)
    i_alphao, i_betao = inv_park(i_d, i_q, theta)

    # ensure forward/inverse computations yield the same values
    assert isclose(i_a, i_ao)
    assert isclose(i_b, i_bo)
    assert isclose(i_c, i_co)
    assert isclose(i_alpha, i_alphao)
    assert isclose(i_beta, i_betao)


def test_duty_cycle() -> None:
    """Test the duty cycle computation."""
    v_bus: float = 48  # bus voltage
    v_in = array(-24)  # input voltage
    t_out = duty_cycle(v_in, v_bus)
    assert isclose(t_out, array(0.25))

    # check clipping when v_in greater than v_bus
    v_in = array(50)  # input voltage above v_bus
    t_out = duty_cycle(v_in, v_bus)
    assert isclose(t_out, array(1.0))

    # ensure assertion error raised when v_bus is zero
    with pytest.raises(ValueError):
        _ = duty_cycle(v_in, 0)

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = duty_cycle(EMPTY, v_bus)


def test_svm() -> None:
    """Test the Space Vector Modulation function."""
    v_bus: float = 48  # bus voltage, in Volt
    v_pk: float = 16  # peak voltage, in Volt
    theta = array(pi / 6)  # motor electrical angle, in radian
    v_a = v_pk * sin(theta)  # phase voltages
    v_b = v_pk * sin(theta - 2 * pi / 3)
    v_c = v_pk * sin(theta - 4 * pi / 3)
    t_a, t_b, t_c = svm(v_a, v_b, v_c, v_bus)
    assert isclose(t_a, array(0.625))
    assert isclose(t_b, array(0.375))
    assert isclose(t_c, array(0.625))

    # ensure assertion error raised for empty input array
    with pytest.raises(ValueError):
        _ = svm(EMPTY, v_b, v_c, v_bus)
