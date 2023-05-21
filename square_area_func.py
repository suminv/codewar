def square_area(A):
    p = A * 4 / (math.pi * 2)
    res = p * p
    return round(res, 2)


assert (square_area(2)) == 1.62
