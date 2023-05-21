def find_difference(a, b):
    """Difference of Volumes of Cuboids"""
    return abs(math.prod(a) - math.prod(b))


assert find_difference([3, 2, 5], [1, 4, 4]) == 14
