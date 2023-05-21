def quarter_of(month):
    return math.ceil(month / 3)


assert quarter_of(3) == 1
assert quarter_of(8) == 3
assert quarter_of(11) == 4
