def is_uppercase(inp):
    """Is the string uppercase?"""
    return inp == inp.upper()


assert is_uppercase("hello I AM DONALD") == False
assert is_uppercase("HELLO I AM DONALD") == True
assert is_uppercase("$%&") == True
