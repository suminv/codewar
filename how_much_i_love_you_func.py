def how_much_i_love_you(nb_petals):
    """ 8kyu I love you, a little , a lot, passionately ... not at all"""
    return ["not at all", "I love you", "a little", "a lot", "passionately", "madly"][nb_petals % 6]


assert how_much_i_love_you(7) == "I love you"
assert how_much_i_love_you(6) == "not at all"
