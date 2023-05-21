def sum_str(a, b):
    """Sum The Strings"""
    if a.isdigit() and b.isdigit():
        return str(int(a) + int(b))
    elif len(a) == 0 and len(b) == 0:
        return '0'
    elif len(a) == 0 and b.isdigit():
        return b
    elif len(b) == 0 and a.isdigit():
        return a


#   return str(int(a or 0) + int(b or 0))


assert (sum_str('481693', '202083')) == '683776'
assert sum_str("", "") == "0"
assert sum_str("9", "") == "9"
assert sum_str("", "5") == "5"
