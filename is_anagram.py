def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


assert (is_anagram("foefet", "toffee")) == True
assert (is_anagram("dumble", "bumble")) == False
