def capitalize(s):
    """7 kyu Alternate capitalization"""
    res_odd = []
    for i in range(len(s)):
        if i % 2 == 0:
            res_odd.append(s[i].upper())
        else:
            res_odd.append(s[i])
    odd = ''.join(res_odd)
    even = odd.swapcase()

    return [odd, even]


assert capitalize('abc')
