def get_sum(a, b):
    """7 kyu Beginner Series #3 Sum of Numbers"""
    res = []
    if a == b:
        return a
    elif a < b:
        for i in range(a, b + 1):
            res.append(i)
        return sum(res)
    else:
        for i in range(b, a + 1):
            res.append(i)
        return sum(res)


assert (get_sum(0, 1)) == 1
assert (get_sum(0, -1)) == -1
