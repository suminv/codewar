def devisors(integer:int):
    res = []
    for i in range(2, integer):
        if integer % i == 0:
            res.append(i)
    if res:
        return res
    return f"{integer} is prime"


assert (devisors(15)) == [3, 5]
assert (devisors(24)) == [2, 3, 4, 6, 8, 12]
assert (devisors(13)) == "13 is prime"