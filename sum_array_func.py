def sum_array(arr):
    """Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value,
    not by index! ).

    The highest or lowest element respectively is a single element at each edge, even if there are more than one with
    the same value.

    Mind the input validation."""

    if arr is None or len(arr) < 3:
        return 0
    else:
        return sum(sorted(arr)[1:-1])
