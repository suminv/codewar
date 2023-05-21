def count_by(x, n):
    return [i for i in range(x, x * n + 1, x)]


assert (count_by(2, 5)) == [2, 4, 6, 8, 10]
