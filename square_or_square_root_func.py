def square_or_square_root(arr):
    from math import sqrt
    """https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python"""
    res = []
    for i in arr:
        if sqrt(i) % 1 == 0:
            res.append(round(sqrt(i)))
        else:
            res.append(i ** 2)

    return res


assert square_or_square_root([4, 3, 9, 7, 2, 1]) == [2, 9, 3, 49, 4, 1]
