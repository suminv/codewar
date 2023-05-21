def move_zeros(array):
    """Description: Write an algorithm that takes an array and moves all of the zeros to the end, preserving the
    order of the other elements.
    """
    for i in array:  # traverse the array
        if i == 0:  # checks if 'i' is equal to 0
            array.remove(0)  # remove a 0 everytime we find one
            array.append(0)  # appends a 0 everytime we find one
    return array  # returns the updated array


assert (move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert (move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) == [
    9,
    9,
    1,
    2,
    1,
    1,
    3,
    1,
    9,
    9,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
assert (move_zeros([0, 0])) == [0, 0]
assert (move_zeros([0])) == [0]
assert (move_zeros([])) == []
