def check_for_factor(base, factor):
    return base % factor == 0


assert check_for_factor(10, 2) is True
assert check_for_factor(10, 3) is False
