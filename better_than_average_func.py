def better_than_average(class_points, your_points):
    """https://www.codewars.com/kata/5601409514fc93442500010b/train/python"""
    avg = sum(class_points) / len(class_points)
    if your_points > avg:
        return True
    return False
