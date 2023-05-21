def sticky_calc(operation, val1, val2):
    """Description
    Frank just bought a new calculator. But, this is no normal calculator. This is a 'Sticky Calculator.
    Whenever you add add, subtract, multiply or divide two numbers the two numbers first stick together:
    For instance:
    50 + 12 becomes 5012
    and then the operation is carried out as usual:
    (5012) + 12 = 5024"""
    val1, val2 = round(val1), round(val2)
    sticky = int(str(val1) + str(val2))

    if operation == '+':
        return sticky + val2
    elif operation == '-':
        return sticky - val2
    elif operation == '*':
        return sticky * val2
    elif operation == '/':
        return sticky / val2


assert sticky_calc('+', 4, 7) == 54
