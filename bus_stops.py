def number(bus_stops):
    get_people = []
    get_off_people = []

    for i, v in enumerate(bus_stops):
        get_people.append(bus_stops[i][0])
        get_off_people.append(bus_stops[i][-1])

    return sum(get_people) - sum(get_off_people)


assert (number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])) == 17
