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

  ratio, terms, first_term = r, n, a
  if ratio != 1:
    return (first_term(1-ratio**terms))/(1-ratio)
  return first_term*terms
