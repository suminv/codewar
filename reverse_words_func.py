def reverse_words(text):
    """Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
    string should be retained. """

    new_text = ""

    for word in text.split(" "):
        new_text += " " + word[::-1]

    return new_text.strip()


assert (
           reverse_words("The quick brown fox jumps over the lazy dog.")
       ) == "ehT kciuq nworb xof spmuj revo eht yzal .god"
