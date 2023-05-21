def how_many_light_sabers_do_you_own(name=""):
    """8 kyu How many lightsabers do you own?"""
    return 18 if name == "Zach" else 0


assert how_many_light_sabers_do_you_own("Zach") == 18
assert how_many_light_sabers_do_you_own() == 0
assert how_many_light_sabers_do_you_own("zach") == 0
