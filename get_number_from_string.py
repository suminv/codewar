import re


def get_number_from_string(st):
    return int(''.join(re.findall(r"\d", st)))



assert (get_number_from_string("$hell5o wor6ld")) == 56
