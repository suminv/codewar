def merge_arrays(arr1, arr2):
    """Merge two sorted arrays into one"""

    return sorted(set(arr1 + arr2))


assert merge_arrays([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]) == [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
