def productFib(prod):
    # prod: an integer representing the product of two Fibonacci numbers
    # returns: a list of the form [F(n), F(n+1), boolean] where F(n) and F(n+1) are consecutive Fibonacci numbers and boolean is True if F(n) * F(n+1) == prod and False otherwise

    # initialize the first two Fibonacci numbers
    a = 0 # F(0)
    b = 1 # F(1)

    # loop until the product of a and b is greater than or equal to prod
    while a * b < prod:
        # update a and b using the Fibonacci recurrence relation
        a, b = b, a + b

    # check if the product of a and b is equal to prod
    if a * b == prod:
        # return the result with True
        return [a, b, True]
    else:
        # return the result with False
        return [a, b, False]


assert productFib(5895) == [89, 144, False]
