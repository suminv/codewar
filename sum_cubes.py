def sum_cubes(n):
    return sum(i**3 for i in range(n + 1))


assert (sum_cubes(10)) == 3025
