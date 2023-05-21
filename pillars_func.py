def pillars(num_pill, dist, width):
    """Pillars"""
    if num_pill < 2:
        return 0

    return num_pill * ((dist * 100) + width) - (width * 2) - (dist * 100)


assert pillars(2, 20, 25) == 2000
assert pillars(11, 15, 30) == 15270
