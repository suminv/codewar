def maskify(cc):
    """Usually when you buy something, you're asked whether your credit card number, phone number or answer to your
    most secret question is still correct. However, since someone could look over your shoulder, you don't want that
    shown on your screen. Instead, we mask it.

    Your task is to write a function maskify, which changes all but the last four characters into '#'.

    """
    start = ''
    for i in cc[:-4]:
        if i:
            start += '#'
    return start + cc[-4:]


assert maskify("4556364607935616") == "############5616"
