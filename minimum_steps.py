def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    total_sum = 0
    count = 0

    for num in numbers:
        total_sum += num
        if total_sum >= value:
            return count
        count += 1


assert (minimum_steps([4, 6, 3], 7)) == 1
