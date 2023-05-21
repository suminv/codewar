def find_uniq(arr):
    """There is an array with some numbers. All numbers are equal except for one. Try to find it!"""
    sort_arr = sorted(arr)
    if sort_arr[0] == sort_arr[1]:
        return sort_arr[-1]
    return sort_arr[0]


assert (find_uniq([1, 1, 1, 2, 1, 1])) == 2
assert (find_uniq([0, 0, 0.55, 0, 0])) == 0.55
assert (find_uniq([8, 8, 8, 8, 8, 8, 8, 7])) == 7
