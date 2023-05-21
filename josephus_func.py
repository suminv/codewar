def josephus(items, k):
    """5 kyu Josephus Permutation"""
    i, ys = 0, []
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        ys.append(items.pop(i))
    return ys
