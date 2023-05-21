def mag_number(info, n):
    import math

    weapons = {
        'PT92': 17,
        'M4A1': 30,
        'M16A2': 30,
        'PSG1': 5,
    }
    return math.ceil(n * 3 / weapons[info])


assert mag_number('PT92', 6) == 2
assert mag_number('M4A1', 8) == 1
assert mag_number('PSG1', 31) == 19
