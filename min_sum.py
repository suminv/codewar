def min_sum(arr):
    arr.sort()
    min_sum = 0
    for i in range(len(arr) // 2):
        min_sum += arr[i] * arr[-i - 1]
    return min_sum


assert min_sum([5, 4, 2, 3]) == 22
