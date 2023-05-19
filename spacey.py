def spacey(array):
    res = []
    counter = 0
    for i in range(len(array)):
        counter += 1
        res.append(''.join(array[0:counter]))
    return res


assert (spacey(['kevin', 'has', 'no', 'space'])) == ['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace']
