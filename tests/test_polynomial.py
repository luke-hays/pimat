import pytest
from pymath.polynomial import Polynomial

def test_add_two():
  f = Polynomial([1, 2, 3])
  g = Polynomial([-8, 17, 0, 5])
  assert f + g == Polynomial([-7, 19, 3, 5])

def test_evaluate_at():
  f = Polynomial([1, 2, 3])
  assert f(1) == 6
