def disemvowel(string_):
    """Trolls are attacking your comment section!
    A common way to deal with this situation is to remove all the vowels from the trolls' comments, neutralizing
    the threat.
    Your task is to write a function that takes a string and return a new string with all vowels removed.
    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
    Note: for this kata y isn't considered a vowel."""

    vol = 'aeiouAEIOU'
    res = ''
    for letter in string_:
        if letter not in vol:
            res += letter
    return res


assert (disemvowel("This website is for losers LOL!")) == "Ths wbst s fr lsrs LL!"
