def dig_pow(n, p):
    pow = [i for i in range(p, p + len(str(n)))]
    numbers = [int(i) for i in str(n)]
    res = [numbers[i] ** pow[i] for i in range(len(numbers))]
    if sum(res) % n != 0:
        return -1
    else:
        return sum(res) // n


assert (dig_pow(46288, 3)) == 51
assert (dig_pow(92, 1)) == -1
