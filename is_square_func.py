def is_square(n):
    if n < 0:
        return False
    return math.sqrt(n) % 1 == 0


assert (is_square(3)) == False
assert (is_square(-1)) == False
assert (is_square(25)) == True
