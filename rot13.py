def rot13(message):
    rot13 = ''
    alphabit = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in message:
        if i in alphabit:
            rot13 += alphabit[alphabit.index(i) + 13]
        else:
            rot13 += i
    return rot13


assert rot13('test') == 'grfg'
