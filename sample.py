def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r

count('aba')