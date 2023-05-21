def xo(s):
    # return s.lower().count('x') == s.lower().count('o')

    """Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
    insensitive. The string can contain any char. """
    x = []
    ss = []
    for i in s.lower():
        if i == "x":
            x.append(i)
        if i == "o":
            ss.append(i)

    if len(x) == len(ss):
        return True
    return False


assert (xo("xxxxxoooxooo")) == True
