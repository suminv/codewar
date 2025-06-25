def find_longest(arr: list[int]) -> int:
    converted = [str(i) for i in arr]
    return int(max(converted, key=len))


assert (find_longest([3, 40000, 100])) == 40000
