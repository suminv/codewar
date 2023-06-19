def remove_smallest(numbers):
    if not numbers:
        return numbers
    else:
        new = numbers[:]
        new.remove(min(numbers))
    return new


assert (remove_smallest([1, 2, 3, 4, 5])) == [2, 3, 4, 5]
assert (remove_smallest([])) == []
assert (remove_smallest([2, 2, 1, 2, 1])) == [2, 2, 2, 1]
