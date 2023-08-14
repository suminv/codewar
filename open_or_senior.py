def open_or_senior(data):
    """To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet
    club, handicaps range from -2 to +26; the better the player the lower the handicap.
    """
    res = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res


assert open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]) == [
    "Open",
    "Senior",
    "Open",
    "Senior",
]
