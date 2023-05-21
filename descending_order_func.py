def descending_order(num):
    """7 kyu Descending Order"""
    return int(''.join((sorted(str(num), reverse=True))))


assert descending_order(123456789) == 987654321
assert descending_order(1201) == 2110
