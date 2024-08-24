def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    mult = [i*i for i in array1]
    return (sorted(mult) == sorted(array2))



a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2)) # True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [231, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2)) # False
