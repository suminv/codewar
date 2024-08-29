def filter_string(st:str)->int:
    res = ''

    for i in st:
        if i.isdigit():
            res+=i

    return int(res)


assert filter_string('a1b2c3') == 123
