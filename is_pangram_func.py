def is_pangram(s):
    """6 kyu Detect Pangram"""
    del_symbol = '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    res = ''
    for i in s.lower():
        if i not in del_symbol:
            res += i
    return len(''.join(set(res))) == 26


assert is_pangram("The quick, brown fox jumps over the lazy dog!") is True
assert is_pangram("1bc
