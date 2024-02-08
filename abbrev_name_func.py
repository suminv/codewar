def abbrev_name(name):
    """Write a function to convert a name into initials. This kata strictly takes two words with one space in between
    them. The output should be two capital letters with a dot separating them.
    """
    first = name[0].upper()
    last = name.split(" ")[1][0].upper()

    return f"{first}.{last}"


print(abbrev_name("Sam Harris"))
