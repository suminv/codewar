def persistence(n):
    """Write a function, persistence, that takes in a positive parameter num and returns its
    multiplicative persistence, which is the number of times you must multiply the
    digits in num until you reach a single digit.
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    4 --> 0 (because 4 is already a one-digit number)
    """
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


assert (persistence(39)) == 3
assert (persistence(4)) == 0
assert (persistence(25)) == 2
assert (persistence(999)) == 4
