def is_valid_walk(walk):
    if (walk.count('n') == walk.count('s') and
            walk.count('e') == walk.count('w') and
            len(walk) == 10):
        return True
    return False


assert (is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) == True
assert (is_valid_walk(['w', 'w', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])) == False
assert (is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'])) == True
assert (is_valid_walk(['e', 'n', 'n', 'n', 'n', 'w', 's', 's', 's', 's'])) == True
assert (is_valid_walk(['w', 's', 'e', 'w', 's', 'e', 'n', 'w', 'e', 'n'])) == True
