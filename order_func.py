def order(words):
    """ 6 kyu Your order, please"""
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
