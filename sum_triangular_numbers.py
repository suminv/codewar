def sum_triangular_numbers(n):
    res = []
    for i in range(1, n + 1):
        res.append((1 / 2) * i * (i + 1))

    return sum(res)


assert sum_triangular_numbers(6) == 56
assert sum_triangular_numbers(-291) == 0
