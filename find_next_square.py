import math


def find_next_square(sq):
    if not math.sqrt(sq).is_integer():
        return -1
    else:
        return (math.sqrt(sq) + 1) ** 2


assert (find_next_square(121)) == 144
assert (find_next_square(342786627)) == -1
