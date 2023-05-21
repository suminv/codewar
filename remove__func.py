def remove_(integer_list, values_list):
    """
    Define a method/function that removes from a given array of integers all the values contained in a second array.
    Examples (input -> output):
    * [1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3] -> [2, 2, 4]
    """
    res = []
    for i in integer_list:
        if i not in values_list:
            res.append(i)
    return res

    # return [i for i in integer_list if i not in values_list]


integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]

# assert remove_(integer_list, values_list) == [2, 2, 4]
