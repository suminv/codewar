def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i != j:
            return j


assert first_non_consecutive([1, 2, 3, 4, 6, 7, 8]) == 6
assert first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]) is None
assert first_non_consecutive([4, 6, 7, 8, 9, 11]) == 6
