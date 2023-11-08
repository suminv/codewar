def to_camel_case(text):
    text = text.replace('-', ' ').replace('_', ' ').split(' ')
    res = []

    for i in text[1:]:
        res.append(i.title())
    res.insert(0, text[0])

    return ''.join(res)


assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
