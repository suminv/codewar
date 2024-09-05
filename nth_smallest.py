def nth_smallest(arr, pos):
    res = sorted(arr, reverse=True)
    return res[-pos]


assert nth_smallest([15,20,7,10,4,3],3) == 7
