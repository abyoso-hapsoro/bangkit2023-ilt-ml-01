def is_prime(x):
  # initialize variable
    num = x
    flag = 0

    if num < 2:
        # special case, 1 is not a prime number
        if num == 1:
            return_string = "{} is not a prime number".format(num)

        # return invalid if input is 0 or negative number
        else : 
            return_string = "Input is 0 or negative number"

        return return_string
  
    # checking if number is divisible 
    for i in range(2, int(num / 2) + 1):
    
        # if it's divisible then it's not a prime number
        if num % i == 0:
            return_string = "{} is not a prime number".format(num)
            flag = 1
            break
    
    # if it's not divisible then it's a prime number
    if flag == 0:
        return_string = "{} is a prime number".format(num)
  
    return return_string
