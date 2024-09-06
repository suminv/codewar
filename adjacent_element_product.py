def adjacent_element_product(array):
    res = []
    for i in range(len(array) - 1):
        res.append(array[i] * array[i + 1])
    return max(res)


assert adjacent_element_product([5, 1, 2, 3, 1, 4]) == 6
