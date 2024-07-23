def get_larger_numbers(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            a[i] = b[i]
    return a


a = [13, 64, 15, 17, 88]
b = [23, 14, 53, 17, 80]

assert (get_larger_numbers(a, b)) == [23, 64, 53, 17, 88]
