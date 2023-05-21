def divisors(n):
    """7 kyu Count the divisors of a number"""
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)

    return len(res)


assert divisors(1) == 1
assert divisors(4) == 3
