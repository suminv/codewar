def find_outlier(integers):
    odd = []
    even = []

    for i in integers:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)

    if len(odd) > len(even):
        return even[0]
    else:
        return odd[0]


assert (find_outlier([2, 2, 6, 8, 10, 3])) == 3
assert (find_outlier([160, 3, 1719, 19, 11, 13, -21])) == 160
