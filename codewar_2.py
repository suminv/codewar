import re
import string


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


def frame(balls):
    """6 kyu Alex & snooker: points earned."""
    trd = re.findall(r'[A-Za-z]+|\d+', balls)
    return trd


balls = "R15Bk16YGBnBeP"
(frame(balls))


def alphanumeric(password):
    """Not very secure"""
    res = re.match(r'^[\da-zA-Z]+$', password)
    if res:
        return True
    return False


def well(arr):
    """7 kyu Well of Ideas - Harder Version"""

    count = 0
    for i in arr:
        for n in i:
            if str(n).lower() == 'good':
                count += 1
    if count == 1 or count == 2:
        return 'Publish!'
    elif count > 2:
        return 'I smell a series!'
    return 'Fail!'


assert well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]) == 'Fail!'
assert well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]) == 'Publish!'
assert well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]) == 'I smell a series!'


def get_sum(a, b):
    """7 kyu Beginner Series #3 Sum of Numbers"""
    res = []
    if a == b:
        return a
    elif a < b:
        for i in range(a, b + 1):
            res.append(i)
        return sum(res)
    else:
        for i in range(b, a + 1):
            res.append(i)
        return sum(res)


assert (get_sum(0, 1)) == 1
assert (get_sum(0, -1)) == -1


def strCount(string, letter):
    """8 kyu All Star Code Challenge #18"""
    return string.count(letter)


def capitals(word):
    res = []
    for i, v in enumerate(word):
        if v.isupper():
            res.append(i)
    return res


assert (capitals('CodEWaRs')) == [0, 3, 4, 6]


def josephus(items, k):
    """5 kyu Josephus Permutation"""
    i, ys = 0, []
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        ys.append(items.pop(i))
    return ys


def sum_digits(number):
    """7 kyu Summing a number's digits"""
    return sum(int(digit) for digit in str(abs(number)))


assert sum_digits(10) == 1
assert sum_digits(99) == 18
assert sum_digits(-32) == 5


def validate_pin(pin):
    """7 kyu Regex validate PIN code"""
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


def validate_pin_reg(pin):
    """
        \d only digits
        {} = number of digits with \d
        | = or
    """
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False


def sequence_sum(begin_number, end_number, step):
    """7 kyu Sum of a sequence"""
    return sum(res for res in range(begin_number, end_number + 1, step))


assert sequence_sum(2, 6, 2) == 12
assert sequence_sum(16, 15, 3) == 0


def reverse_letter(s):
    """7 kyu Simple Fun #176: Reverse Letter"""
    alpha = string.ascii_letters
    res = ''

    for letter in s:
        if letter in alpha:
            res += letter
    return res[::-1]


assert reverse_letter("krish21an") == "nahsirk"


def increment_string(strng):
    """ 5 kyu String incrementer"""
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


# "foobar002"


assert (increment_string("foobar001")) == "foobar002"


def sort_by_length(arr):
    """7 kyu Sort array by string length"""
    return sorted(arr, key=len)


def combat(health, damage):
    """8 kyu Grasshopper - Terminal game combat function"""
    if health > damage:
        return health - damage
    return 0


def is_pangram(s):
    """6 kyu Detect Pangram"""
    del_symbol = '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    res = ''
    for i in s.lower():
        if i not in del_symbol:
            res += i
    return len(''.join(set(res))) == 26


assert is_pangram("The quick, brown fox jumps over the lazy dog!") is True
assert is_pangram("1bcdefghijklmnopqrstuvwxyz") is False


def dna_to_rna(dna):
    """8 kyu DNA to RNA Conversion"""
    if 'T' in dna:
        return dna.replace("T", 'U')
    return dna


"""8 kyu Grasshopper - Messi Goals"""
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


def sum_two_smallest_numbers(numbers):
    """7 kyu Sum of two lowest positive integers"""
    return sum(sorted(numbers)[:2])


assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19


def greet_2(name, owner):
    """8 kyu Grasshopper - Personalized Message"""
    return f'Hello guest' if name != owner else f'Hello boss'


def multi_table(number):
    """8 kyu Multiplication table for number"""
    res = ''
    for i in range(1, 11):
        res += f'{i} * {number} = {i * number}\n'
    return res.strip()


def remove_url_anchor(url):
    """7 kyu Remove anchor from URL"""
    return url.split('#')[0]


assert remove_url_anchor("www.codewars.com/katas/?page=1#about") == "www.codewars.com/katas/?page=1"


def likes(names):
    """6 kyu Who likes it?"""
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


assert likes(['Peter']) == 'Peter likes this'
assert likes([]) == 'no one likes this'
assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'
