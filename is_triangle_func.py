def is_triangle(a, b, c):
    """Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can
    be built with the sides of given length and false in any other case.

    (In this case, all triangles must have surface greater than 0 to be accepted)."""
    return (a < b + c) and (b < a + c) and (c < a + b)


assert (is_triangle(1, 2, 2)) == True
assert (is_triangle(7, 2, 2)) == False
assert (is_triangle(1, 2, 3)) == False
assert (is_triangle(1, 3, 2)) == False
