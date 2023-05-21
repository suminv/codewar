def is_isogram(string):
    """An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
    determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
    Ignore letter case. """
    if len(string) == len(set(string.lower())):
        return True
    return False


assert (is_isogram("Dermatoglyphics")) == True
assert (is_isogram("aba")) == False
assert (is_isogram("moOse")) == False
