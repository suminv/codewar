def prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


assert (prime_factors(8)) == [2, 2, 2]
