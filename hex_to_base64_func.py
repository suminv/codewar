def hex_to_base64(hex: str) -> str:
    """6kyu Hex to base64 """
    decode = base64.b16decode(hex, casefold=True)
    encode = base64.b64encode(decode).decode('utf-8')
    return encode


def is_divisible(n, x, y):
    """8 kyu Is n divisible by x and y? """
    return n % x == 0 and n % y == 0


assert is_divisible(3, 2, 2) == False
assert is_divisible(12, 3, 4) == True
