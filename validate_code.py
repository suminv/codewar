import re

def validate_code(code):
    return bool(re.match(r'[1-3]', str(code)))


assert validate_code(123) is True
assert validate_code(323) is True
assert validate_code(423) is False
