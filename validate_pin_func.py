def validate_pin(pin):
    """7 kyu Regex validate PIN code"""
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)
