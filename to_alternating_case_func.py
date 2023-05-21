def to_alternating_case(string: str):
    """altERnaTIng cAsE <=> ALTerNAtiNG CaSe"""
    res = []
    for letter in string:
        if letter == letter.upper():
            res.append(letter.lower())
        elif letter == letter.lower():
            res.append(letter.upper())

    return ''.join(res)
    # return string.swapcase()


assert to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E"
assert to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
