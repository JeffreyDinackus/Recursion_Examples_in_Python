



def factorial(input):
  if input == 1:
    return 1

  return input * factorial(input - 1)



print(factorial(5))
# 120