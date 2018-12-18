from polynomial import strip_zeros, Polynomial


def test_strip_empty():
    assert strip_zeros([]) == []


def test_strip_single():
    assert strip_zeros([1, 2, 3, 1, 0]) == [1, 2, 3, 1]


def test_strip_many():
    assert strip_zeros([1, 2, 3, 0, 0, 0, 0]) == [1, 2, 3]


def test_polynomial_zero():
    assert Polynomial([0]).coefficients == []
    assert len(Polynomial([0])) == 0


def test_polynomial_repr():
    f = Polynomial([1, 2, 3])
    assert repr(f) == "1 + 2 x^1 + 3 x^2"


def test_polynomial_add():
    f = Polynomial([1, 2, 3])
    g = Polynomial([4, 5, 6])
    assert (f + g).coefficients == [5, 7, 9]


def test_polynomial_sub():
    f = Polynomial([1, 2, 3])
    g = Polynomial([4, 5, 6])
    assert (f - g).coefficients == [-3, -3, -3]


def test_polynomial_add_zero():
    f = Polynomial([1, 2, 3])
    g = Polynomial([0])
    assert (f + g).coefficients == [1, 2, 3]


def test_polynomial_negate():
    f = Polynomial([1, 2, 3])
    assert (-f).coefficients == [-1, -2, -3]


def test_polynomial_multiply():
    f = Polynomial([1, 2, 3])
    g = Polynomial([4, 5, 6])
    assert (f * g).coefficients == [4, 13, 28, 27, 18]


def test_polynomial_evaluate_at():
    f = Polynomial([1, 2, 3])
    assert (f(2)) == 1 + 4 + 12
