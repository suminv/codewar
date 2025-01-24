
def split_and_merge(string_, separator):
    return ' '.join([separator.join(list(word)) for word in string_.split()])



assert split_and_merge("My name is John"," ") ==  "M y n a m e i s J o h n"
assert split_and_merge("My name is John","-") == "M-y n-a-m-e i-s J-o-h-n"
