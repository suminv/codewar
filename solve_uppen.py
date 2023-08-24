def solve(s: str) -> str:
    stock_upper = 0
    stock_lower = 0
    for letter in s:
        if letter.isupper():
            stock_upper += 1
        if letter.islower():
            stock_lower += 1
    if stock_upper > stock_lower:
        return s.upper()
    elif stock_upper < stock_lower:
        return s.lower()
    return s.lower()


assert (solve("CODe")) == "CODE"
assert (solve("COde")) == "code"
assert (solve("Code")) == "code"
