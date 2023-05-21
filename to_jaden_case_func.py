def to_jaden_case(s: str):
    """Jaden Casing Strings"""
    return string.capwords(s)


quote = "How can mirrors be real if our eyes aren't real"
assert to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real"
