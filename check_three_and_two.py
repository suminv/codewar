def check_three_and_two(array):
    unic_array = list(set(array))
    res = []
    for i in unic_array:
        res.append(array.count(i))

    if (sorted(res))[0] == 2 and (sorted(res))[1] == 3:
        return True
    return False



assert (check_three_and_two(["a", "a", "a", "b", "b"])) == True
assert (check_three_and_two(["a", "c", "a", "c", "b"])) == False
assert (check_three_and_two(['a', 'a', 'a', 'a', 'c'])) == False
