def show_sequence(n):
    if n > 0:
        dig = list(range(n + 1))
        total = sum(dig)
        res = '+'.join(map(str, dig))
        return f'{res} = {total}'
    elif n == 0:
        return f'{n}={n}'
    else:
        return f'{n}<0'


assert show_sequence(6) == "0+1+2+3+4+5+6 = 21"
