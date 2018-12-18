import pytest
from interpolate import interpolate


def test_interpolate_empty():
    with pytest.raises(ValueError):
        interpolate([])


def test_interpolate_repeated_x_values():
    with pytest.raises(ValueError):
        interpolate([(1, 2), (1, 3)])


def test_interpolate_degree_0():
    assert interpolate([(1, 2)]).coefficients == [2]


def test_interpolate_degree_1():
    assert interpolate([(1, 2), (2, 3)]).coefficients == [1, 1]


def test_interpolate_degree_3():
    points = [(1, 1), (2, 0), (-3, 2), (4, 4)]

    interpolating_polynomial = interpolate(points)
    evaluations = [interpolating_polynomial.evaluateAt(x) for (x, _) in points]

    for (p, y) in zip(points, evaluations):
        assert p[1] == pytest.approx(y)
