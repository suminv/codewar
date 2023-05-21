def validate_pin_reg(pin):
    """
        \d only digits
        {} = number of digits with \d
        | = or
    """
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False
