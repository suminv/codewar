def solve(s):
    """Simple string characters"""
    count_upper = 0
    count_lower = 0
    count_number = 0
    count_special = 0

    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i.isnumeric():
            count_number += 1
        elif i in string.punctuation:
            count_special += 1

    return [count_upper, count_lower, count_number, count_special]


assert solve("*'&ABCDabcde12345") == [4, 5, 5, 3]
