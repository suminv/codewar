def sum_pairs(ints, s):
    """
    https://www.codewars.com/kata/54d81488b981293527000c8f/train/python Given a list of integers and a single sum
    value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
    """

    d = set()
    for n in ints:
        if n in d:
            return [s - n, n]
        d.add(s - n)


l1 = [1, 4, 8, 7, 3, 15]
assert sum_pairs(l1, 8) == [1, 7]
