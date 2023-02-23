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
