def closest_multiple_10(i):
    """Given a number return the closest number to it that is divisible by 10."""
    return round(i / 10) * 10


assert closest_multiple_10(54) == 50
