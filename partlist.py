def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        left_part = " ".join(arr[:i])
        right_part = " ".join(arr[i:])
        result.append((left_part, right_part))
    return result


partlist(["I", "wish", "I", "hadn't", "come"])
