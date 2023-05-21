def digitize(n):
    """Convert number to reversed array of digits
    https://www.codewars.com/kata/5583090cbe83f4fd8c000051/solutions/python
    """
    return list(map(int, str(n)[::-1]))
    # return [int(x) for x in str(n)[::-1]]


assert digitize(35231) == [1, 3, 2, 5, 3]
