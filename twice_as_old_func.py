def twice_as_old(dad_years_old, son_years_old):
    """8 kyu Twice as old"""
    return abs(dad_years_old - (son_years_old * 2))


assert twice_as_old(36, 7) == 22
assert twice_as_old(55, 30) == 5
