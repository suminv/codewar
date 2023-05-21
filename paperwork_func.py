def paperwork(n, m):
    """8 kyu Beginner Series #1 School Paperwork"""
    if n < 0 or m < 0:
        return 0
    return n * m


assert paperwork(5, 5) == 25
assert paperwork(-5, 5) == 0
