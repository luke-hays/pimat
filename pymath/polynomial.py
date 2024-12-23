from itertools import zip_longest

def _strip_trailing_values(L: list[any], val: any):
  '''Strips all trailing values from the end of a list
  
  Returns a slice of the list.
  '''
  if len(L) == 0:
    return L

  i = len(L) - 1
  while i >= 0 and L[i] == val:
    i -= 1

  return L[:i+1]

# Based off pimbook implementation
class Polynomial(object):
  '''Represents a polynomial as a list of coefficients with no trailing zeros.

  A degree zero polynomial is represented by an empty list of coefficients.
  This is provided as the variable ZERO_POLYNOMIAL.

  Polynomials override the basic arithmetic methods.
  '''

  def __init__(self, coefficients: list[int]):
    '''Create a new polynomial.
    
    The caller must provide a list of all coefficients of the polynomial, even zero.
    E.g., Polynomial([0, 1, 0, 2]) corresponds to f(x) = x + 2x^3
    '''
    self.coefficients = _strip_trailing_values(coefficients, 0)
    self.indeterminate = 'x'

  def __add__(self, other: list[int]):
    new_coefficients = [sum(x) for x in zip_longest(self, other, fillvalue=0.)]
    return Polynomial(new_coefficients)

  def __mul__(self, other: list[int]):
    new_coefficients = [0] * (len(self) + len(other) - 1)

    for i, a in enumerate(self):
      for j, b in enumerate(other):
        new_coefficients[i+j] += (a * b)

    return Polynomial(_strip_trailing_values(new_coefficients, 0))
  
  def __len__(self):
    '''len satisfies len(p) == 1 + degree(p)'''
    return len(self.coefficients)
  
  def __repr__(self):
    return ' + '.join([
        '%s %s^%d' % (a, self.indeterminate, i) 
        if i > 0 
        else '%s' % a for i, a in enumerate(self.coefficients)
      ])
  
  def __iter__(self):
    return iter(self.coefficients)

  def __neg__(self):
    return Polynomial([-a for a in self])

  def __sub__(self, other: list[int]):
    return self + (-other)

  def __call__(self, *args):
    return self.evaluate_at(args[0])

  def evaluate_at(self, x: int):
    '''Evaluate a polynomial at an input point

    Uses Horner's method, which evalues a poylnomial by minimizing the number of multiplications.
    '''
    result = 0

    for coeff in reversed(self.coefficients):
      result = (result * x) + coeff
    
    return result

ZERO_POLYNOMIAL = Polynomial([])

# Interpolating Polynomial
