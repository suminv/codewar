def sort_gift_code(code):
    return ''.join(sorted(code))


assert sort_gift_code('abcdef') == 'abcdef'
assert sort_gift_code('pqksuvy') == 'kpqsuvy'
