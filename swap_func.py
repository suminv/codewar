def swap(string_):
    """Given a string, swap the case for each of the letters.
    e.g. CodEwArs --> cODeWaRS"""
    s = ''
    for i in string_:
        if i.isupper():
            s += i.lower()
        else:
            s += i.upper()
    return s

    # return string_.swapcase()


assert swap('HelloWorld') == 'hELLOwORLD'
assert swap('CodeWars') == 'cODEwARS'
