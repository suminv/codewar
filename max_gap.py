def max_gap(numbers):
    sorted_numbers = sorted(numbers)

    max_difference = 0
    for i in range(1, len(sorted_numbers)):
        difference = sorted_numbers[i] - sorted_numbers[i - 1]
        if difference > max_difference:
            max_difference = difference

    return max_difference


assert max_gap([13, 10, 2, 9, 5]) == 4
