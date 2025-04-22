def alias_gen(f_name, l_name):
    if not f_name[0].isalpha() or not l_name[0].isalpha():
        return "Your name must start with a letter from A - Z."

    first_name = FIRST_NAME.get(
        f_name[0].upper(), "Your name must start with a letter from A - Z."
    )
    surname = SURNAME.get(
        l_name[0].upper(), "Your name must start with a letter from A - Z."
    )

    return f"{first_name} {surname}"


FIRST_NAME = {"A": "Alpha", "B": "Beta", "C": "Cache"}
SURNAME = {"A": "Analogue", "B": "Bomb", "C": "Catalyst"}

print(alias_gen("Alpha", "Bomb"))
print(alias_gen("123abc", "Pinkman"))
