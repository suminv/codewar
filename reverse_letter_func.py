def reverse_letter(s):
    """7 kyu Simple Fun #176: Reverse Letter"""
    alpha = string.ascii_letters
    res = ''

    for letter in s:
        if letter in alpha:
            res += letter
    return res[::-1]


assert reverse_letter("krish21an") == "nahsirk"
