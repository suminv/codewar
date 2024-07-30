def to_float_array(arr):
    return [float(i) for i in arr]


assert to_float_array(["1", "2", "3"]) == [1, 2, 3]
