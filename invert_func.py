def invert(lst):
    """
    Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
    become positives.

    """
    result = []
    if len(lst) != 0:
        for dig in lst:
            if dig > 0:
                result.append(dig * -1)
            if dig < 0:
                result.append(abs(dig))
            if dig == 0:
                result.append(dig)
    else:
        return result
    return result


assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
assert invert([]) == []
