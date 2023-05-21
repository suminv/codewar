def vowel_indices(word):
    """Find the vowels"""
    vowels = ['a', 'e', 'u', 'i', 'o', 'y']

    res = []
    for idx, value in enumerate(word.lower(), start=1):
        if value in vowels:
            res.append(idx)
    return res

    # return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']


assert (vowel_indices("apple")) == [1, 5]
assert (vowel_indices("apple")) == [1, 5]
assert (vowel_indices("UNDISARMED")) == [1, 4, 6, 9]
assert vowel_indices('supercalifragilisticexpialidocious') == [2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 25, 27, 29, 31,
                                                               32, 33]
