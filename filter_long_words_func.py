def filter_long_words(sentence, n):
    row = sentence.split(' ')
    res = []
    for i in res:
        print(len(i))
        if len(i) > n:
            res.append(i)
    # print(res)

# print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))
# == ['quick', 'brown', 'jumps']
