def find_it(seq):
    """Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.
    """
    for i in seq:
        if seq.count(i) % 2 != 0:  # check odd number?
            return i
