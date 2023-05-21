def simple_multiplication(number):
    """8 kyu Simple multiplication"""
    # return number * 8 if number % 2 == 0 else number * 9
    if number % 2 == 0:
        return number * 8
    return number * 9
