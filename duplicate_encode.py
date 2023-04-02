def duplicate_encode(word):
    """
    The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
    that character appears only once in the original string, or ")" if that character appears more than once in the
    original string. Ignore capitalization when determining if a character is a duplicate.
    """
    word = word.lower()
    res = ''
    for letter in word:
        if word.count(letter) == 1:
            res += '('
        else:
            res += ')'
    return res
    # return ''.join('(' if word.count(x) == 1 else ')' for x in word)


assert (duplicate_encode("din")) == "((("
assert (duplicate_encode("recede")) == "()()()"
