def find_average(nums: list):
    return sum(nums) / len(nums) if nums else 0


assert find_average([1, 3, 5, 7]) == 4
