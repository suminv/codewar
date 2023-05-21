def find_multiples(integer, limit):
    """https://www.codewars.com/kata/58ca658cc0d6401f2700045f/python"""
    return [i for i in range(integer, limit + 1) if i % integer == 0]


assert find_multiples(5, 25) == [5, 10, 15, 20, 25]
