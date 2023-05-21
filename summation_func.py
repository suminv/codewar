def summation(num):
    """Write a program that finds the summation of every number from 1 to num. The number will always be a positive
    integer greater than 0. """

    result = 0
    for x in range(1, num + 1):
        result += x
    return result


assert (summation(8)) == 36
assert (summation(100)) == 5050
