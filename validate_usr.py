import re


def validate_usr(username):
    """
    Write a simple regex to validate a username. Allowed characters are:
    lowercase letters,
    numbers,
    underscore
    Length should be between 4 and 16 characters (both included).
    """
    return bool(re.match(r'^[0-9a-z_]{4,16}$', username))


assert (validate_usr('Hsddsa')) == False
assert (validate_usr('dsddsa1')) == True
