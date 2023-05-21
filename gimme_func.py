def gimme(input_array):
    """As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of
    the numerical element that lies between the other two elements. The input to the function will be an array of
    three distinct numbers (Haskell: a tuple). For example: gimme([2, 3, 1]) => 0"" """

    middle = sorted(input_array)[1]
    return input_array.index(middle)


assert gimme([2, 3, 1]) == 0
