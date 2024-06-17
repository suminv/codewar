def basic_op(operator, value1, value2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Division by zero error'  # Optional handling for division by zero
    }
    
    if operator in operations:
        return operations[operator](value1, value2)
    else:
        return 'Invalid operator'