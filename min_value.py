def min_value(digits):
    sort_digits = (sorted(set(digits)))
    res = ''
    for digit in sort_digits:
        res += str(digit)
    return int(res)


assert min_value([1, 3, 1]) == 13
assert min_value([4, 7, 5, 7]) == 457
