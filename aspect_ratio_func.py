import math


def aspect_ratio(x: int, y: int):
    """Aspect Ratio Cropping - Part 1"""
    return math.ceil(y * 16 / 9), y


assert aspect_ratio(640, 480) == (854, 480)
