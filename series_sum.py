def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


assert series_sum(1) ==  "1.00"
assert series_sum(58) == "2.40"

