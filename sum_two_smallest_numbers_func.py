def sum_two_smallest_numbers(numbers):
    """7 kyu Sum of two lowest positive integers"""
    return sum(sorted(numbers)[:2])


assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
