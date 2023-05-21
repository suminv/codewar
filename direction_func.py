def direction(facing, turn):
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return compass[(compass.index(facing) + turn // 45) % 8]


assert (direction("S", 180)) == "N"
assert (direction("SE", -45)) == "E"
assert (direction("W", 495)) == "NE"
