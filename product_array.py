def product_array(arr):
    total_product = 1
    for num in arr:
        total_product *= num

    prod = []
    for num in arr:
        prod.append(total_product // num)

    return prod


assert product_array([3, 27, 4, 2]) == [216, 24, 162, 324]
