from collections import Counter


def highest_rank(arr):
    count = Counter(arr)
    max_freq = max(count.values())

    max_freq_elements = [num for num, freq in count.items() if freq == max_freq]

    return max(max_freq_elements)


assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
assert (highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10])) == 3
