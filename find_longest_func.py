def find_longest(string):
    return len(sorted(string.split(), key=len, reverse=True)[0])


assert (find_longest('The quick white fox jumped around the massive dog')) == 7
