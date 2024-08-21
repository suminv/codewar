import re

def is_digit(n):
    res = bool(re.fullmatch(r'\d', n))
    return res


assert (is_digit('a5')) is False
assert (is_digit('5'))  is True
assert (is_digit('12'))  is False
assert (is_digit(''))  is False
assert (is_digit('abc'))  is False
