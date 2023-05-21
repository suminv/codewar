def flatten_and_sort(array):
    """7 kyu Flatten and sort an array"""
    return sorted(reduce(lambda a, b: a + b, array))


assert (flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])) == [1, 2, 3, 4, 5, 6, 100]
