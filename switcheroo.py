def switcheroo(s):
    res = ''
    for i in s:
        if i == 'a':
            res += 'b'
        elif i == 'b':
            res += 'a'
        elif i == 'c':
            res += 'c'
    return res


assert (switcheroo('abc')) == 'bac', 'Test case "abc" failed'
