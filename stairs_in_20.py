def stairs_in_20(stairs):
    one_year = 0
    for weekday in stairs:
        for amount in weekday:
            one_year += amount
    return one_year * 20
