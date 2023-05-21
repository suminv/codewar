def is_narcissistic(i):
    # s = len(str(i))
    # res = []
    # for x in str(i):
    #     res.append(int(x)**s)
    #
    # if sum(res) == i:
    #     return True
    # return False

    num = str(i)
    length = len(num)
    return sum(int(a) ** length for a in num) == i


assert is_narcissistic(1634) == True
assert is_narcissistic(825) == False
