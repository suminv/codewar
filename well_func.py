def well(arr):
    """7 kyu Well of Ideas - Harder Version"""

    count = 0
    for i in arr:
        for n in i:
            if str(n).lower() == 'good':
                count += 1
    if count == 1 or count == 2:
        return 'Publish!'
    elif count > 2:
        return 'I smell a series!'
    return 'Fail!'


assert well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]) == 'Fail!'
assert well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]) == 'Publish!'
assert well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]) == 'I smell a series!'
