def remove_every_other(my_list):
    res = []
    for i, val in enumerate(my_list):
        if i % 2 == 0:
            res.append(val)
    return res


assert remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) == ["Keep", "Keep", "Keep"]
