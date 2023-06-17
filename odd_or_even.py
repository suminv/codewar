def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


assert (odd_or_even([0, 1, 2])) == "odd"
assert (odd_or_even([0, 1, 2, 3])) == "even"
