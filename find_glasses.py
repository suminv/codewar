import re


def find_glasses(lst):
    pattern = r'O-+O'
    result = [i for i, s in enumerate(lst) if re.search(pattern, s)]
    return result[0] if result else -1


assert (find_glasses(["OO", "wallet", "O##O", "O----O"])) == 3
