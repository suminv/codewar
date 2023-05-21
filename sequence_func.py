def sequence(x):
    if x < 10:
        return [i for i in range(1, x + 1)]
    part1 = [i for i in range(10, x + 1)]
    part2 = [i for i in range(2, 10)]

    return ([1] + part1 + part2)


sequence(16)
