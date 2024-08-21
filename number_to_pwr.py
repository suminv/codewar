def number_to_pwr(number, p):
    n = 1
    for i in range(p):
        n *= number
    return n


print(number_to_pwr(10, 6))
