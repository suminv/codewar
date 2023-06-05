import string


def find_missing_letter(chars):
    alphabet_lower_upper = list(string.ascii_letters)
    first_letter = chars[0]
    char_length = len(chars)
    start_index = alphabet_lower_upper.index(first_letter)
    alphabet = alphabet_lower_upper[start_index: start_index + char_length + 1]

    for letter in alphabet:
        if letter not in chars:
            return letter


assert (find_missing_letter(['a', 'b', 'c', 'd', 'f'])) == 'e'
assert (find_missing_letter(['O', 'Q', 'R', 'S'])) == 'P'
