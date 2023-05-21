def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    """8 kyu Holiday VI - Shark Pontoon"""
    if dolphin:
        shark_speed = shark_speed / 2

    shark_time = shark_distance / shark_speed
    you_time = pontoon_distance / you_speed

    return 'Shark Bait!' if you_time > shark_time else 'Alive!'


assert (shark(12, 50, 4, 8, True)) == "Alive!"
assert (shark(7, 55, 4, 16, True)) == "Alive!"
assert (shark(24, 0, 4, 8, True)) == "Shark Bait!"


class Person:
