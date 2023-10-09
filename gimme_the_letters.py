import string


def gimme_the_letters(sp):
    start_letter, end_letter = sp.split('-')
    if start_letter.isupper() and end_letter.isupper():
        start_letter_index = string.ascii_uppercase.index(start_letter)
        end_letter_index = string.ascii_uppercase.index(end_letter)
        result = ''.join(list(string.ascii_uppercase)[start_letter_index:end_letter_index + 1])
        return result
    else:
        start_letter_index = string.ascii_lowercase.index(start_letter)
        end_letter_index = string.ascii_lowercase.index(end_letter)
        result = ''.join(list(string.ascii_lowercase)[start_letter_index:end_letter_index + 1])
        return result


assert gimme_the_letters("a-z") == "abcdefghijklmnopqrstuvwxyz"
assert gimme_the_letters("Q-Z") == "QRSTUVWXYZ"
