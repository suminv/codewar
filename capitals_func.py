def capitals(word):
    res = []
    for i, v in enumerate(word):
        if v.isupper():
            res.append(i)
    return res


assert (capitals('CodEWaRs')) == [0, 3, 4, 6]
