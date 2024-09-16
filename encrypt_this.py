def encrypt_this(text):
    result = []

    for word in text.split():
        if len(word) == 1:  # если слово состоит из одного символа
            result.append(str(ord(word[0])))
        elif len(word) == 2:  # если слово состоит из двух символов
            result.append(str(ord(word[0])) + word[1])
        else:  # для слов длиной 3 и более символов
            result.append(str(ord(word[0])) + word[-1] + word[2:-1] + word[1])

    return " ".join(result)


assert encrypt_this("Hello") == "72olle", "Test case 'Hello' failed"
assert encrypt_this("good") == "103doo", "Test case 'good' failed"
assert (encrypt_this("hello world") == "104olle 119drlo"), "Test case 'hello world' failed"

print("All tests passed!")
