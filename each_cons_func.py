def each_cons(lst, n):
    mas = []
    for i in range(len(lst) - n + 1):
        mas.append(lst[i:i + n])
    return mas


lst = [3, 5, 8, 13]

# assert (each_cons(lst, 2)) == [[3, 5, 8], [5, 8, 13]]
