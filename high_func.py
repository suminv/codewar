def high(x):
    """Highest Scoring Word"""
    keys = []
    values = []

    for word in x.split():
        score = 0
        keys.append(word)

        for letter in word:
            score += (ord(letter)) - 96
        values.append(score)

    res = dict(zip(keys, values))
    max_Score = max(res.values())

    for k, v in res.items():
        if v == max_Score:
            return k


assert high('man i need a taxi up to ubud') == 'taxi'
