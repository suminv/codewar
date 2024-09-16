def encode(st):
    vowels = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    res = ''
    for i in st:
        if vowels.get(i):
            res += str(vowels.get(i))
        else:
            res += i
    return res


def decode(st):
    vowels = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    res = ''
    for i in st:
        if i.isdigit():
            res += list(vowels.keys())[list(vowels.values()).index(int(i))]
        else:
            res += i
    return res


assert (encode('hello')) == 'h2ll4'
assert (decode('h2ll4')) == 'hello'
