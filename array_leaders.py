def array_leaders(numbers):
    res = []
    for i, v in enumerate(numbers):
        if v > sum(numbers[i + 1:]):
            res.append(v)
    return res


assert array_leaders([16, 17, 4, 3, 5, 2]) == [17, 5, 2]
