def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)

    # result = []
    # for i in list(str(num)):
    #     result.append(int(i)**2)
    # return int(''.join(map(str, result)))

    # return (''.join([str(int(i) ** 2) for i in list(str(num))]))


assert (square_digits(9119)) == 811181
