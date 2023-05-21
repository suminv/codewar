def powers_of_two(n):
    '''Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2
    with the exponent ranging from 0 to n ( inclusive ).
    '''
    res = []
    for i in range(0, n + 1):
        res.append(2 ** i)
    return res

    # return [2**x for x in range(n+1)]


assert powers_of_two(0) == [1]
assert powers_of_two(1) == [1, 2]
