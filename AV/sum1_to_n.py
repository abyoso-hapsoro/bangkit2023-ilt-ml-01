def sum1_to_n(n):
  """
  Calculate the sum of an arithmetic sequence from 1 to n.

  Args:
    n (int): last term in the sequence.
  
  Returns:
    The sum of 1 + 2 + ... + n.
  """
  total = 0
  for num in range(1, n + 1):
    total += num
  return total
