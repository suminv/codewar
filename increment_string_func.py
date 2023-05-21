def increment_string(strng):
    """ 5 kyu String incrementer"""
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


# "foobar002"


assert (increment_string("foobar001")) == "foobar002"
