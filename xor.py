def xor(a, b):
    if a == b:
        return False
    return True


assert xor(False, False) == False
assert xor(True, False) == True
assert xor(False, True) == True
assert xor(True, True) == False
