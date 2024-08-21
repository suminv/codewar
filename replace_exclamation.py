def replace_exclamation(st):
    vowel = "aeiouAEIOU"
    res = ""
    for i in st:
        if i in vowel:
            res += "!"
        else:
            res += i
    return res


assert replace_exclamation("ABCDE") == "!BCD!"
