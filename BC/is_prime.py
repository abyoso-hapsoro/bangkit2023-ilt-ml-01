def is_prime(x):
  # initialize variable
  num = x
  flag = 0
  
  # 1 and 2 is a prime number
  if num == 1 or num == 2:
    return_string = "{} is a prime number".format(num)
  
  else:
    # checking if number is divisible
    for i in range(2, int((num + 1) / 2)):
      # if it's divisible then it's not a prime number
      if num % i == 0:
        return_string = "{} is not a prime number".format(num)
        flag = 1
        break
    
    # if it's not divisible then it's a prime number
    if flag == 0:
      return_string = "{} is a prime number".format(num)
  
  return return_string
