def check(a, x):
    return x in a


assert check([1, 2, 3, 4, 5], 5) == True
assert check(["hello", "world", "kata"], "map") == False
