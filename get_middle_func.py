def get_middle(s):
    """You are going to be given a word. Your job is to return the middle character of the word. If the word's length is
    odd, return the middle character. If the word's length is even, return the middle 2 characters.
    """
    if len(s) <= 0 or len(s) <= 2:
        return s
    elif len(s) % 2 == 0:
        middle = int(len(s) / 2)
        return s[middle - 1: middle + 1]
    else:
        return s[len(s) // 2]


assert (get_middle("test")) == "es"
assert (get_middle("testing")) == "t"
assert (get_middle("middle")) == "dd"
assert (get_middle("A")) == "A"
assert (get_middle("of")) == "of"
