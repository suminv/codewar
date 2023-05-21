def bingo(array):
    """Bingo ( Or Not )"""
    win = sorted([2, 9, 14, 7, 15])
    res = []
    alfa = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    for i in array:
        if i in win:
            res.append(i)
    if list(set(res)) == win:
        return 'WIN'
    return 'LOSE'


# return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"


assert bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]) == "LOSE"
assert bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]) == "WIN"
