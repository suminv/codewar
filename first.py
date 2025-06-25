def first(seq, n=1):
    if n == 0:
        return []
    return seq[:n]


seq = ["a", "b", "c", "d", "e"]

assert first(seq) == ["a"]
assert first(seq, 0) == []
assert first(seq, 2) == ["a", "b"]
assert first(seq, 3) == ["a", "b", "c"]
