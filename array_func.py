def array(string):
    return ' '.join(string.split(',')[1:-1]) or None


assert array('1,2,3,4') == '2 3'
assert array('1,2,3,4,5') == '2 3 4'
