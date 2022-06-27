def angle(n):
    """7 kyu Sum of angles"""
    return (n - 2) * 180


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
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return "Hello {you}, my name is {me}".format(you=your_name, me=self.name)


joe = Person('Joe')
joe.greet('Kate')


def build_string(*args):
    """8kyu String Templates - Bug Fixing #5"""
    return "I like {}!".format(", ".join(args))


def greet():
    """8 kyu Function 1 - hello world"""
    return "hello world!"


def find_longest(string):
    return len(sorted(string.split(), key=len, reverse=True)[0])


assert (find_longest('The quick white fox jumped around the massive dog')) == 7


def find_average(numbers):
    """8 kyu Calculate average"""
    return sum(numbers) / len(numbers)
