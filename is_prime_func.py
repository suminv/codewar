def is_prime(num):
    """https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python"""
    if num <= 1:
        return False
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


class Add(int):
    """https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/python"""
