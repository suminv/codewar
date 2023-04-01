def largest(n, xs):
    """Find the n highest elements in a list"""
    if n != 0:
        return sorted(xs)[-n:]
    return []


assert (largest(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == [9, 10]
assert (largest(3, [5, 1, 5, 2, 3, 1, 2, 3, 5])) == [5, 5, 5]
assert (largest(7, [9, 1, 50, 22, 3, 13, 2, 63, 5])) == [3, 5, 9, 13, 22, 50, 63]
