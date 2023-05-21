def sum_of_differences(arr):
    """8kyu Sum of differences in array"""
    arr.sort(reverse=True)

    sum = 0
    dif = 0
    for i in range(len(arr) - 1):
        dif = arr[i] - arr[i + 1]
        sum += dif
    return sum


assert sum_of_differences([1, 2, 10]) == 9
assert sum_of_differences([-3, -2, -1]) == 2
assert sum_of_differences([1, 1, 1, 1, 1]) == 0
