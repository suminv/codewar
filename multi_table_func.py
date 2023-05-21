def multi_table(number):
    """8 kyu Multiplication table for number"""
    res = ''
    for i in range(1, 11):
        res += f'{i} * {number} = {i * number}\n'
    return res.strip()
