def duplicates(arr):
    """Given an array, find the duplicates in that array, and return a new array of those duplicates. The elements
    of the returned array should appear in the order when they first appeared as duplicates.
    Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., "1" != 1).
    """
    seen = []
    dups = []
    for char in arr:
        if char not in seen:
            seen.append(char)
        elif char not in dups:
            dups.append(char)

    return dups


assert (duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'])) == [4, 3, 1]
assert (duplicates([0, 1, 2, 3, 4, 5])) == []
assert (duplicates(['1', 2, 4, '4', 3, '3', 1, 5, 3, 3, 3, 3])) == [3]
assert (duplicates(['zut', 'alors', 1, 2, 4, 4, 3, 3, '1', 5, 3, 'zut'])) == [4, 3, 'zut']
assert (duplicates([])) == []
assert (duplicates(['no', 'duplicates', 'here'])) == []
