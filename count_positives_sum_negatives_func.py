def count_positives_sum_negatives(arr):
    """
    Given an array of integers. Return an array, where the first element is the count of positives numbers and the
    second element is sum of negative numbers. 0 is neither positive nor negative. If the input array is empty or
    null, return an empty array.
    """
    pos = 0
    neg = []
    if not arr:
        return []
    else:
        for i in arr:
            if i > 0:
                pos += 1
            elif i < 0:
                neg.append(i)
        return [pos, sum(neg)]


assert (
           count_positives_sum_negatives(
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
           )
       ) == [10, -65]
assert (
           count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])
       ) == [8, -50]
assert (count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])) == [0, 0]
assert (count_positives_sum_negatives([])) == []
