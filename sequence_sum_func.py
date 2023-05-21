def sequence_sum(begin_number, end_number, step):
    """7 kyu Sum of a sequence"""
    return sum(res for res in range(begin_number, end_number + 1, step))


assert sequence_sum(2, 6, 2) == 12
assert sequence_sum(16, 15, 3) == 0
