def create_array_of_tiers(n):

    res = []
    n = str(n)

    for i in range(1, len(n) + 1):
        res.append(n[:i])
    return res

assert (create_array_of_tiers(2017)) == ["2", "20", "201", "2017"]
