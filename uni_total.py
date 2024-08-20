def uni_total(s):
    res = []
    for i in s:
        res.append(ord(i))
    return sum(res)


assert (uni_total('aaa')) == 291
