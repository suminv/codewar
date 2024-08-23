import re


def happy_g(st):
    return bool(re.search(r"gg", st))


assert happy_g("gg0gg3gg0gg") is True
assert happy_g("gg0gg3gg0gg") is False
