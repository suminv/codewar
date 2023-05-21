def dont_give_me_five(start, end):
    """Don't give me five!"""
    res = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            res += 1
    return res
    # return sum('5' not in str(i) for i in range(start, end + 1))


assert dont_give_me_five(1, 9) == 8
assert dont_give_me_five(4, 17) == 12
