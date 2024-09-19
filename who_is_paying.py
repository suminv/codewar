def who_is_paying(name):
    result = []

    if len(name) <= 2:
        result.append(str(name))
    else:
        result.append(''.join(list(name)))
        result.append(''.join(list(name[:2])))
    return result


assert (who_is_paying("Mexico")) == ["Mexico", "Me"], "Test case 'Mexico' failed"
assert (who_is_paying("Me")) == ['Me'], "Test case 'Me' failed"
assert (who_is_paying("I")) == ['I'], "Test case 'I' failed"
