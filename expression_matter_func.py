def expression_matter(a, b, c):
    """8 kyu Expressions Matter"""
    operations = [
        a * (b + c),
        a * b * c,
        a + b * c,
        (a + b) * c,
        a + b + c
    ]
    return max(operations)


assert expression_matter(2, 1, 2) == 6
assert expression_matter(2, 1, 1) == 4
