def stray(arr):
    first, last = list(set(arr))
    if arr.count(first) > 1:
        return last
    if arr.count(last) > 1:
        return first


assert stray([1, 1, 1, 1, 1, 1, 2]) == 2
