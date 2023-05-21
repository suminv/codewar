def alternate(n, first_value, second_value):
    # res = []
    # for i in range(n):
    #     res.append(first_value)
    #     res.append(second_value)
    #
    # return res[0:n]
    return [[first_value, second_value][i % 2] for i in range(n)]


assert alternate(5, True, False) == [True, False, True, False, True]
