def to_freud(sentence):
    """Freudian translator
    https://www.codewars.com/kata/5713bc89c82eff33c60009f7/solutions/python
    """
    return (len(sentence.split()) * ' sex').strip()


assert (to_freud("This is a test")) == "sex sex sex sex"
