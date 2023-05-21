def is_palindrome(s):
    """Write a function that checks if a given string (case insensitive) is a palindrome."""

    return s.lower() == s.lower()[::-1]


assert is_palindrome('aba') == True
assert is_palindrome('Abba') == True
assert is_palindrome('malam') == True
assert is_palindrome('walter') == False
