def expanded_form(num):
    num_total = (str(num))
    res = ''
    for j, i in enumerate(num_total):
        if i != '0':
            res += ' + {}{}'.format(i, len(num_total[j + 1:]) * '0')

    return res.strip(' +')


assert (expanded_form(70304)) == '70000 + 300 + 4'
