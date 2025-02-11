import math

def power_of_two(x):
    return math.log2(x).is_integer() if x > 0 else False




assert power_of_two(0) == False
assert power_of_two(1) == True
