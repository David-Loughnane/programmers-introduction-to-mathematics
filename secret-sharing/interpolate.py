from polynomial import Polynomial, ZERO
from typing import Sequence, Tuple


def single_term(points: Sequence[Tuple[float, float]], i: int) -> Polynomial:
    """Return one term of an interpolated polynomial."""
    theTerm = Polynomial([1.0])
    xi, yi = points[i]

    for j, p in enumerate(points):
        if j == i:
            continue

        xj = p[0]
        theTerm = theTerm * Polynomial([-xj / (xi - xj), 1.0 / (xi - xj)])

    return theTerm * Polynomial([yi])


def interpolate(points: Sequence[Tuple[float, float]]) -> Polynomial:
    """Return the unique degree n polynomial passing through the given n+1 points."""
    if len(points) == 0:
        raise ValueError('Must provide at least one point.')

    x_values = [p[0] for p in points]
    if len(set(x_values)) < len(x_values):
        raise ValueError('Not all x values are distinct.')

    terms = [single_term(points, i) for i in range(0, len(points))]
    return sum(terms, ZERO)
