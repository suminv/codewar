def find_children(dancing_brigade):
    """Where is my parent!?(cry)
    https://www.codewars.com/kata/58539230879867a8cd00011c/train/python
    """
    res = []
    for i in sorted(dancing_brigade.lower()):
        if i.upper() not in res:
            res.append(i.upper())
        else:
            res.append(i)

    return ''.join(res)


assert find_children("AaaaaZazzz") == "AaaaaaZzzz"
