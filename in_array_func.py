def in_array(array1, array2):
    """6 kyu Which are in?"""
    res = []
    for i in array1:
        for x in array2:
            if i in x:
                res.append(i)
    return sorted(set(res))


array1 = ["live", "arp", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
assert in_array(array1, array2) == ['arp', 'live', 'strong']
