def contamination(text, char):
    if len(text) == 0 or len(char) == 0:
        return ""
    return len(text) * char


assert contamination("abc", "z") == "zzz"
assert contamination("", "z") == ""
