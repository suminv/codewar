def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    else:
        diamond_str = ""

        # Top half
        for i in range(1, n + 1, 2):
            diamond_str += ' ' * ((n - i) // 2) + '*' * i + '\n'

        # Bottom half
        for i in range(n - 2, 0, -2):
            diamond_str += ' ' * ((n - i) // 2) + '*' * i + '\n'

        return diamond_str


# Example usage
result = diamond(5)
print(result)

diamond(5)
