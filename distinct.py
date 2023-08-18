def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result


assert distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]
