def spin_words(sentence):
    """Write a function that takes in a string of one or more words, and returns the same string, but with all
    five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist
    of only letters and spaces. Spaces will be included only when more than one word is present."""
    
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

print(spin_words("Welcome"))
print(spin_words("to"))
print(spin_words("to to to"))
print(spin_words("CodeWars"))
print(spin_words("Hey fellow warriors"))