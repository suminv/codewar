import math


def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        return (math.ceil(n / 5)) * 5


assert (round_to_next5(7)) == 10
