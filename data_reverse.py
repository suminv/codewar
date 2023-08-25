def data_reverse(data):
    chunks = []
    for i in range(0, len(data), 8):
        chunks.append(data[i:i + 8])

    res = []
    for i in chunks[::-1]:
        for m in i:
            res.append(m)
    return res


data_reverse([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0])
