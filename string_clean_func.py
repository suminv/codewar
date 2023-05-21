def string_clean(s):
    """
    Delete from string all digits.
    """
    res = ''

    for i in s:
        if not i.isdigit():
            res += i
    return res


assert string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!") == "Dsa cdsc csa!!! I Am cool!"
