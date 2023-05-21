def sort_array(source_array):
    """Sort the odd
    https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python"""
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
