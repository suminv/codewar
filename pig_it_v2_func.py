def pig_it_v2(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)


assert (pig_it_v2('Hello world !')) == 'elloHay orldway !'
