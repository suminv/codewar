def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)


assert (binary_array_to_number([0, 0, 0, 1])) == 1
