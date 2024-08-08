def div_con(x):
    int_list = []
    str_list = []

    for i in x:
        if isinstance(i, int):
            int_list.append(i)
        else:
            str_list.append(int(i))

    return sum(int_list) - sum(str_list)


assert (div_con([9, 3, '7', '3'])) == 2
