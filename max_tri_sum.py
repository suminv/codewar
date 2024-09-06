def max_tri_sum(numbers):
    numbers = sorted(set(numbers), reverse=True)
    return sum(numbers[:3])


assert max_tri_sum([3, 2, 6, 8, 2, 3]) == 17
