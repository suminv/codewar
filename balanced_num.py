def balanced_num(number):
    number = list(str(number))
    length = len(number)

    if length % 2 == 0:
        middle_one = length // 2 - 1
        middle_two = length // 2 + 1
        left_part = number[:middle_one]
        right_part = number[middle_two:]

        if sum(map(int, left_part)) == sum(map(int, right_part)):
            return 'Balanced'
        else:
            return 'Not Balanced'

    else:
        middle = length // 2
        left_part = number[:middle]
        right_part = number[middle + 1:]

        if sum(map(int, left_part)) == sum(map(int, right_part)):
            return 'Balanced'
        else:
            return 'Not Balanced'


assert balanced_num(7) == 'Balanced', "Test case '7' failed"
assert balanced_num(432) == 'Not Balanced', "Test case '432' failed"
print('all test completed!')
