def sumDig_nthTerm(initVal: int, patternL: list, nthTerm: int):
    """ 6kyu Reach Me and Sum my Digits """
    term_n = initVal + sum([patternL[n % len(patternL)] for n in range(nthTerm - 1)])
    return sum(list(map(int, str(term_n))))


assert sumDig_nthTerm(10, [2, 1, 3], 6) == 10
