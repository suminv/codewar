def sum_digits(number):
    """7 kyu Summing a number's digits"""
    return sum(int(digit) for digit in str(abs(number)))


assert sum_digits(10) == 1
assert sum_digits(99) == 18
assert sum_digits(-32) == 5
