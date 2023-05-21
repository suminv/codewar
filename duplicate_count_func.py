def duplicate_count(text):
    '''Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
    digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (
    both uppercase and lowercase) and numeric digits.
    '''
    result = collections.Counter(text.lower())
    count = 0
    for i in result.values():
        if i > 1:
            count += 1
    return count


assert (duplicate_count("")) == 0
assert (duplicate_count("abcde")) == 0
assert (duplicate_count("abcdeaa")) == 1
assert (duplicate_count("abcdeaB")) == 2
assert (duplicate_count("Indivisibilities")) == 2
