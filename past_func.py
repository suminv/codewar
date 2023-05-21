def past(h, m, s):
    """
    Clock shows h hours, m minutes and s seconds after midnight.
    Your task is to write a function which returns the time since midnight in milliseconds.
    """
    return 3600000 * h + 60000 * m + s * 1000


assert (past(0, 1, 1)) == 61000
assert (past(1, 1, 1)) == 3661000
assert (past(0, 0, 0)) == 0
assert (past(1, 0, 1)) == 3601000
assert (past(1, 0, 0)) == 3600000
