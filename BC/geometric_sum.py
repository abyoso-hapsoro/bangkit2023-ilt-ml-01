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

    first_term, common_ratio, num_terms = a, r, n
    numerator = first_term * (1 - common_ratio ** num_terms)
    denominator = 1 - common_ratio
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = num_terms * first_term
    return result
