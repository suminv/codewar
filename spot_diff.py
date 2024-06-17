def spot_diff(s1, s2):
    res = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res.append(i)

    return res


assert (spot_diff('abcdefg', 'abcqetg')) == [3, 5]