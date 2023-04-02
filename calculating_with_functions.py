"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

"""


def zero(num=None):
    return 0 if num is None else int(num(0))


def one(num=None):
    return 1 if num is None else int(num(1))


def two(num=None):
    return 2 if num is None else int(num(2))


def three(num=None):
    return 3 if num is None else int(num(3))


def four(num=None):
    return 4 if num is None else int(num(4))


def five(num=None):
    return 5 if num is None else int(num(5))


def six(num=None):
    return 6 if num is None else int(num(6))


def seven(num=None):
    return 7 if num is None else int(num(7))


def eight(num=None):
    return 8 if num is None else int(num(8))


def nine(num=None):
    return 9 if num is None else int(num(9))


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


assert (seven(times(five()))) == 35
assert (four(plus(nine()))) == 13
assert (eight(minus(three()))) == 5
assert (six(divided_by(two()))) == 3
