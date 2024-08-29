import re

def alphanumeric(password):
    """Not very secure"""
    res = re.match(r'^[\da-zA-Z]+$', password)
    if res:
        return True
    return False
