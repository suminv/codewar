def sum_dif(n):
    res = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return sum(res)
    # s = set(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


assert sum_dif(10) == 23
