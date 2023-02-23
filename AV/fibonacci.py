def fibonacci(x):
  if x > 2:
    return fibonacci(x-1) + fibonacci(x-2)
  else:
    return 1
