def unique_in_order(iterable):
    """Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
    any elements with the same value next to each other and preserving the original order of elements. """
    res = []
    prev = None
    for i in iterable:
        if i != prev:
            res.append(i)
        prev = i
    return res


assert (unique_in_order('AAAABBBCCDAABBB')) == ['A', 'B', 'C', 'D', 'A', 'B']
