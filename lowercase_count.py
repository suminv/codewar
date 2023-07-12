def lowercase_count(strng):
    return sum(a.islower() for a in strng)


assert lowercase_count("abcABC123") == 3
