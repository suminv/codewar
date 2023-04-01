def largest_pair_sum(numbers):
    """Given a sequence of numbers, find the largest pair sum in the sequence."""
    return sum(sorted(numbers)[-2:])


assert (largest_pair_sum([10, 14, 2, 23, 19])) == 42
assert (largest_pair_sum([-100, -29, -24, -19, 19])) == 0
assert (largest_pair_sum([1, 2, 3, 4, 6, -1, 2])) == 10
assert (largest_pair_sum([-10, -8, -16, -18, -19])) == -18
