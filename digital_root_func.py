def digital_root(n):
    """Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way
    until a single-digit number is produced. The input will be a non-negative integer. """

    if len(str(n)) == 1:
        return n
    sum = 0
    for i in str(n):
        sum += int(i)
    return digital_root(sum)


assert (digital_root(493193)) == 2
assert (digital_root(16)) == 7
