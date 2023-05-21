def choose_best_sum(t, k, ls):
    from itertools import combinations
    """https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python"""
    try:
        return max(sum(i) for i in combinations(ls, k) if sum(i) <= t)
    except:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
assert (choose_best_sum(230, 4, xs)) == 230
assert (choose_best_sum(430, 5, xs)) == 430
assert (choose_best_sum(430, 8, xs)) is None
