def problem(a):
    if isinstance(a, str):
        return "Error"
    return (a * 50) + 6


assert problem("hello") == "Error"
assert problem(1) == 56
