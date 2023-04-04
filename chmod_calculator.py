def chmod_calculator(perm):
    chmod = {
        'rwx': '7',
        'rw-': '6',
        'r-x': '5',
        'r--': '4',
        '-wx': '3',
        '-w-': '2',
        '--x': '1',
        '---': '0'
    }

    bits = ''

    for i in ('user', 'group', 'other'):
        if i in perm:
            bits += chmod[perm[i]]
        else:
            bits += '0'

    return bits


assert (chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'})) == "755"
assert (chmod_calculator({"user": 'rwx', "group": 'r--', "other": 'r--'})) == "744"
assert (chmod_calculator({"user": 'r-x', "group": 'r-x', "other": '---'})) == "550"
assert (chmod_calculator({"group": 'rwx'})) == "070"
assert (chmod_calculator({})) == "000"
