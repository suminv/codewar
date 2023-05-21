def count_sheep(n):
    # res = ''
    # for i in range(1, n+1):
    #     res += f'{i} sheep...'
    # return res

    return ''.join(f"{i} sheep..." for i in range(1, n + 1))


assert (count_sheep(3)) == '1 sheep...2 sheep...3 sheep...'
