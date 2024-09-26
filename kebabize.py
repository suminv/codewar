def remove_digit(st: str) -> str:
    res = ''
    for i in st:
        if not i.isdigit():
            res += i
    return res


def kebabize(st):
    res = ''
    for i in remove_digit(st):
        if i.isupper():
            res += '-' + i.lower()
        else:
            res += i.lower()
    res.split('-')

    if res.startswith('-'):
        return res.removeprefix('-')
    return res


assert (kebabize('myCamelHas3Humps')) == 'my-camel-has-humps', 'Test case "myCamelHas3Humps" failed'
assert (kebabize('SOS')) == 's-o-s', 'Test case "SOS" failed'
