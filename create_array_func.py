def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res


assert (create_array(4)) == [1, 2, 3, 4]
