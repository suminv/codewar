def two_oldest_ages(ages):
    return sorted(ages)[-2:]


assert two_oldest_ages([1, 5, 87, 45, 8, 8]) == [45, 87]
