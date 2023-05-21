def create_phone_number(n):
    '''Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those
    numbers in the form of a phone number. '''

    row_num = ''.join(map(str, n))

    return f'({row_num[:3]}) {row_num[3:6]}-{row_num[6:]}'


assert (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == '(123) 456-7890'
