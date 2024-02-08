def accum(s):
    res = ""
    for idx, value in enumerate(list(s.lower()), start=1):
        res += value * idx + "-"
    return res.title()[:-1]


assert (
           accum("ZpglnRxqenU")
       ) == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
