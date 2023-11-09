






# def fib(current, prev, prevprev,num):
#   print(current)
#   if num == 0:
#     return ""
#   if num == 1:
#     return "0"
#   elif num == 2:
#     num -=2
#     return "0 1"
#   else: 
    
#     current = prev+prevprev
#     prev = current
#     prevprev = prev
    
#   num -=1
  
#   return str(fib(current, prev, prevprev,num))





# arr = []
# print(fib(0,1,0, 6))


def Fibonacci(n):
 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
 
# Driver Program
print(Fibonacci(9))