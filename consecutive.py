def consecutive(arr):
    """
    Create the function consecutive(arr) that takes an array of integers and return the minimum number of integers
    needed to make the contents of arr consecutive from the lowest number to the highest number.

    For example:
    If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7)
    to make it a consecutive array of numbers from 4 to 8. Numbers in arr will be unique.
    """
    if arr:
        return len([x for x in range(min(arr), max(arr) + 1)]) - len(arr)
    else:
        return 0


assert (consecutive([4, 8, 6])) == 2
assert (consecutive([1, 2, 3, 4])) == 0
assert (consecutive([])) == 0
