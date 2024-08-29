from _typeshed import SupportsAdd
import re


def happy_g(st):
    if re.search(r'(?<!g)g(?!g)', st):
        return False
    return True



assert happy_g("gg0gg3gg0gg") is True
assert happy_g("ggg ggg g ggg") is False
