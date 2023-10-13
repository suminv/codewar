def max_product(lst, n_largest_elements):
    max_elements = sorted(lst, reverse=True)[:n_largest_elements]
    res = 1
    for el in max_elements:
        res *= el
    return res


assert max_product([4, 3, 5], 2) == 20
