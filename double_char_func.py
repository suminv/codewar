def double_char(s):
    """Double Char"""
    res = ''
    for i in s:
        res += i * 2
    return res

    # return ''.join(c * 2 for c in s)


assert double_char("String") == "SSttrriinngg"
