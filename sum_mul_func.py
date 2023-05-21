def sum_mul(n, m):
    """Sum of Multiples"""
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'


assert sum_mul(2, 9) == 20
assert sum_mul(0, 0) == 'INVALID'
assert sum_mul(4, -7) == 'INVALID'
