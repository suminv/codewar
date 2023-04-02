def multiple_of_index(arr):
    """Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
    """
    return [val for index, val in enumerate(arr) if index and val % index == 0]


assert multiple_of_index([22, -6, 32, 82, 9, 25]) == [-6, 32, 25]
