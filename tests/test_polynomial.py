import pytest
from math import ceil
from pimat.polynomial import Polynomial, interpolate

interpolation_test_data = [
  ([(1, 1)], [1]),
  ([(1, 1), (2, 0)], [1, 0]),
  ([(1, 1), (2, 4), (7, 9)], [1, 4, 9])
]

def test_polynomial_print():
  assert repr(Polynomial([1, 2, 3])) == '1 + 2 x^1 + 3 x^2'

def test_add_two_polynomials():
  f = Polynomial([1, 2, 3])
  g = Polynomial([-8, 17, 0, 5])
  assert f + g == Polynomial([-7, 19, 3, 5])

def test_subtract_two_polynomials():
  f = Polynomial([1, 2, 3])
  g = Polynomial([1, 3, 0])
  assert f - g == Polynomial([0, -1, 3])

def test_polynomial_negation():
  f = -Polynomial([1, -2, 3])
  assert f == Polynomial([-1, 2, -3])

def test_evaluate_at():
  f = Polynomial([1, 2, 3])
  assert f(1) == 6

def test_empty_interpolation_list():
  with pytest.raises(ValueError):
    interpolate([])

def test_non_unique_xs_interpolation():
  with pytest.raises(ValueError):
    interpolate([(1,1), (1, 2)])

@pytest.mark.parametrize('p,expected', interpolation_test_data)
def test_polynomial_interpolation(p, expected):
  f = interpolate(p)
  assert [ceil(f(xi)) for (xi, yi) in p] == expected
