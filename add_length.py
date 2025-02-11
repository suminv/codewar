def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]



assert add_length('apple ban') == ['apple 5', 'ban 3']
assert add_length('you will win') == ['you 3', 'will 4', 'win 3']