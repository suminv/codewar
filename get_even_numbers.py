def get_even_numbers(arr):
    return [x for x in arr if x % 2 == 0]


assert get_even_numbers([2, 4, 5, 6]) == [2, 4, 6]
