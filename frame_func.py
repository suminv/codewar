def frame(balls):
    """6 kyu Alex & snooker: points earned."""
    trd = re.findall(r'[A-Za-z]+|\d+', balls)
    return trd


balls = "R15Bk16YGBnBeP"
(frame(balls))
