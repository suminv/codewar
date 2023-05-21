def delete_nth(order, max_e):
    """Delete occurrences of an element if it occurs more than n times"""

    res = []

    for i in order:
        if res.count(i) < max_e:
            res.append(i)
    return res


assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
