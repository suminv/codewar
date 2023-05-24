websites = ['codewars' for i in range(1000)]

assert (len(websites)) == 1000
assert (type(websites)) == list
assert (list(set(websites)) == ["codewars"])
