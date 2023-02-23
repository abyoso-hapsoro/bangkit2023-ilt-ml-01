from math import pi

def greeting(name):
  return 'Hello, ' + name

def triangel_area(x, y):
  return 0.5*x*y

def square_area(x):
  return x**2

def rectangle_area(x, y):
  return x*x

def circel_area(x):
  return pi*x**2

def cube_volume(x):
  return 6*x**2

def geometric_sum(a, r, n):
  """
  Calculate the sum of a geometric sequence.

  Args:
    a (Union[int, float]): first term in the sequence.
    r (Union[int, float]): common ratio between terms.
    n (int): number of terms.

  Returns:
    The sum of a + a*r + ... + a*r**(n-1).
  """

  total, ratio = a, r
  for _ in range(1, n):
    total += a*ratio
    ratio *= r
  return total

def power(x, y):
  return x^y

def fibonacci(x):
  if x > 2:
    return fibonacci(x-1) + fibonacci(x-2)
  else:
    return 1

def signum(x):
  """
  Get the sign of a real number. See https://mathworld.wolfram.com/Sign.html for more information.

  Args:
    x (Union[int, float]): real number.

  Returns:
    The sign of x.
  """
  
  pass

def is_prime(x):
  pass
