def are_coprime(n, m):
    """7 kyu Coprime Validator"""
    while m > 0:
        n, m = m, n % m
    return n == 1


assert are_coprime(20, 27) == True
assert are_coprime(12, 39) == False
