def is_digit(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


print(is_digit("s121210"))  # False
print(is_digit("-234.4"))  # True
