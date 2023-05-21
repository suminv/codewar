def solution(nums=None):
    """Sort Numbers"""
    if nums is None:
        return []
    return [i for i in sorted(nums)]


assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]

# assert (solution(None)) == []
