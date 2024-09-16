def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True


def minimum_number(numbers):
    numbers_sum = sum(numbers)
    count = 0
    while not is_prime(numbers_sum + count):
        count += 1
    return count


assert (minimum_number([50, 39, 49, 6, 17, 28])) == 2
assert (minimum_number([2, 12, 8, 4, 6])) == 5
