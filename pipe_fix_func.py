def pipe_fix(nums):
    """Lario and Muigi Pipe Problem
    https://www.codewars.com/kata/56b29582461215098d00000f/train/python"""
    raw = sorted(nums)
    return [x for x in range(raw[0], raw[-1] + 1)]
    # return list(range(min(nums), max(nums)+1))


assert pipe_fix([1, 2, 3, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
