def update_light(current):
    """ 8kyu Thinkful - Logic Drills: Traffic light"""
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


assert update_light('green') == 'yellow'
assert update_light('yellow') == 'red'
assert update_light('red') == 'green'
