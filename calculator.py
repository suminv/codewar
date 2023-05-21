def calculator(x, y, op):
    valid_operators = ['+', '-', '*', '/']
    if isinstance(x, int) and isinstance(y, int) and op in valid_operators:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
    else:
        return "unknown value"


assert calculator(6, 2, '+') == 8
assert calculator(6, 2, '&') == 'unknown value'
assert calculator(6, '^', '&') == 'unknown value'
