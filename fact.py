# factorial function
#
# Return the factorial of n
# fact(n) => n!

def fact(n): # recursive function
    if(n == 1): # if n == 1 return 1
        return 1
    else:
        return n * fact(n - 1) # multiplies each n with n - 1 until n == 1


def factorial(n): # while loop
    product = n
    while(n > 1):
        product = product * (n - 1)
        n = n - 1
    print product


def factfor(n): # for loop
    product = n
    for x in range(n):
        if x > 0:
            product = product * x
    return product
