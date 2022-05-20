import collections
import math
import string
from datetime import datetime


def abbrev_name(name):
    """Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
    The output should be two capital letters with a dot separating them.
    """
    first = name[0].upper()
    last = name.split(" ")[1][0].upper()

    return f"{first}.{last}"


abbrev_name("Sam Harris")


def square_sum(numbers):
    """
    Complete the square sum function so that it squares each number passed into it and then sums the results together.
    """
    result = []
    for i in numbers:
        result.append(i ** 2)

    return sum(result)


square_sum([1, 2])


def find_needle(haystack):
    """Can you find the needle in the haystack?

    Write a function findNeedle() that takes an array full of junk but containing one "needle"

    After your function finds the needle it should return a message (as a string) that says:

    "found the needle at position " plus the index it found the needle, so:"""

    for idx, word in enumerate(haystack):
        if word == "needle":
            return f"found the needle at position {idx}"


find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])


def invert(lst):
    """
    Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

    """
    result = []
    if len(lst) != 0:
        for dig in lst:
            if dig > 0:
                result.append(dig * -1)
            if dig < 0:
                result.append(abs(dig))
            if dig == 0:
                result.append(dig)
    else:
        return result
    return result


assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
assert invert([]) == []


def points(games):
    """Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

    For example: ["3:1", "2:2", "0:1", ...]

    Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

    if x>y - 3 points
    if x<y - 0 point
    if x=y - 1 point"""

    count = []
    x = games[0].split(":")[0]
    y = games[0].split(":")[1]

    for i in range(len(games)):
        x = games[i].split(":")[0]
        y = games[i].split(":")[1]
        if x > y:
            count.append(3)
        elif x < y:
            count.append(0)
        else:
            x == y
            count.append(1)
    # print(count)
    return sum(count)


assert (
           points(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"])
       ) == 30
assert (
           points(["1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4"])
       ) == 10
assert (
           points(["0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"])
       ) == 0
assert (
           points(["1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"])
       ) == 15
assert (
           points(["1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4"])
       ) == 12


def past(h, m, s):
    """
    Clock shows h hours, m minutes and s seconds after midnight.
    Your task is to write a function which returns the time since midnight in milliseconds.
    """
    return 3600000 * h + 60000 * m + s * 1000


assert (past(0, 1, 1)) == 61000
assert (past(1, 1, 1)) == 3661000
assert (past(0, 0, 0)) == 0
assert (past(1, 0, 1)) == 3601000
assert (past(1, 0, 0)) == 3600000


def sum_array(arr):
    """Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

    The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

    Mind the input validation."""

    if arr == None or len(arr) < 3:
        return 0
    else:
        return sum(sorted(arr)[1:-1])


def hero(bullets, dragons):
    """
    A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
    """
    if bullets // dragons == 2:
        return True
    return False


def filter_list(l):
    """In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out."""
    return [i for i in l if type(i) == int]


assert (filter_list([1, 2, "a", "b"])) == [1, 2]
assert (filter_list([1, "a", "b", 0, 15])) == [1, 0, 15]
assert (filter_list([1, 2, "aasf", "1", "123", 123])) == [1, 2, 123]


def count_sheeps(sheep):
    """
    Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
    """
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count


def DNA_strand(dna):
    result = ""
    if len(dna) == 0:
        return result
    else:
        for i in dna:
            if i == "A":
                result += "T"
            elif i == "T":
                result += "A"
            elif i == "C":
                result += "G"
            elif i == "G":
                result += "C"
        return result


assert (DNA_strand("AAAA")) == "TTTT"
assert (DNA_strand("ATTGC")) == "TAACG"
assert (DNA_strand("GTAT")) == "CATA"
assert (DNA_strand("AAGG")) == "TTCC"
assert (DNA_strand("CGCG")) == "GCGC"
assert (DNA_strand("ATTGC")) == "TAACG"


def nb_year(p0, percent, aug, p):
    """In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?"""
    nb_year = 0
    while p0 < p:
        p0 = p0 + int(p0 * (percent / 100)) + aug
        nb_year += 1
    return int(nb_year)


assert (nb_year(1500, 5, 100, 5000)) == 15


def count_positives_sum_negatives(arr):
    """
        Given an array of integers.
    Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
    If the input array is empty or null, return an empty array.
    """
    pos = 0
    neg = []
    if not arr:
        return []
    else:
        for i in arr:
            if i > 0:
                pos += 1
            elif i < 0:
                neg.append(i)
        return [pos, sum(neg)]


assert (
           count_positives_sum_negatives(
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
           )
       ) == [10, -65]
assert (
           count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])
       ) == [8, -50]
assert (count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])) == [0, 0]
assert (count_positives_sum_negatives([])) == []


def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)

    # result = []
    # for i in list(str(num)):
    #     result.append(int(i)**2)
    # return int(''.join(map(str, result)))

    # return (''.join([str(int(i) ** 2) for i in list(str(num))]))


assert (square_digits(9119)) == 811181


def reverse_words(text):
    """Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained."""

    new_text = ""

    for word in text.split(" "):
        new_text += " " + word[::-1]

    return new_text.strip()


assert (
           reverse_words("The quick brown fox jumps over the lazy dog.")
       ) == "ehT kciuq nworb xof spmuj revo eht yzal .god"


def summation(num):
    """Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0."""

    result = 0
    for x in range(1, num + 1):
        result += x
    return result


assert (summation(8)) == 36
assert (summation(100)) == 5050


def solution(s):
    """Description:
    Complete the solution so that the function will break up camel casing, using a space between words.
    """
    cc = ""
    for i in s:
        if i.isupper():
            cc += " " + i
        else:
            cc += i
    return cc.strip()


assert (solution("breakCamelCase")) == "break Camel Case"


def get_planet_name(id):
    # This doesn't work; Fix it!
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id)


# print(get_planet_name(3))


def get_middle(s):
    """You are going to be given a word. Your job is to return the middle character of the word. If the word's length is
    odd, return the middle character. If the word's length is even, return the middle 2 characters.
    """
    if len(s) <= 0 or len(s) <= 2:
        return s
    elif len(s) % 2 == 0:
        middle = int(len(s) / 2)
        return s[middle - 1: middle + 1]
    else:
        return s[len(s) // 2]


assert (get_middle("test")) == "es"
assert (get_middle("testing")) == "t"
assert (get_middle("middle")) == "dd"
assert (get_middle("A")) == "A"
assert (get_middle("of")) == "of"


def alphabet_position(text):
    """In this kata you are required to, given a string, replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it."""
    alfa = "abcdefghijklmnopqrstuvwxyz"
    row_text = list("".join(c for c in text if c.isalpha()).lower())
    result = ""
    for character in row_text:
        number = ord(character) - 96
        result += " " + str(number)
    return result.strip()


assert (
           alphabet_position("The sunset sets at twelve o' clock.")
       ) == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def remove(s):
    return s[:-1] if s.endswith("!") else s
    # if s[-1] == '!':
    #     return s[:-1]
    # elif len(s) == 0:
    #     return s
    # else:
    #     return s


assert (remove("Hi! Hi!")) == "Hi! Hi"


def move_zeros(array):
    """Description:
    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
    """
    for i in array:  # traverse the array
        if i == 0:  # checks if 'i' is equal to 0
            array.remove(0)  # remove a 0 everytime we find one
            array.append(0)  # appends a 0 everytime we find one
    return array  # returns the updated array


assert (move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert (move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])) == [
    9,
    9,
    1,
    2,
    1,
    1,
    3,
    1,
    9,
    9,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
assert (move_zeros([0, 0])) == [0, 0]
assert (move_zeros([0])) == [0]
assert (move_zeros([])) == []


def lovefunc(flower1, flower2):
    """Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't."""

    return flower1 % 2 != flower2 % 2


assert (lovefunc(2, 2)) == False


def xo(s):
    # return s.lower().count('x') == s.lower().count('o')

    """Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char."""
    x = []
    ss = []
    for i in s.lower():
        if i == "x":
            x.append(i)
        if i == "o":
            ss.append(i)

    if len(x) == len(ss):
        return True
    return False


assert (xo("xxxxxoooxooo")) == True


def is_isogram(string):
    """An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case."""
    if len(string) == len(set(string.lower())):
        return True
    return False


assert (is_isogram("Dermatoglyphics")) == True
assert (is_isogram("aba")) == False
assert (is_isogram("moOse")) == False


def find_it(seq):
    """Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.
    """
    for i in seq:
        if seq.count(i) % 2 != 0:  # check odd number?
            return i


def find_uniq(arr):
    """There is an array with some numbers. All numbers are equal except for one. Try to find it!"""
    sort_arr = sorted(arr)
    if sort_arr[0] == sort_arr[1]:
        return sort_arr[-1]
    return sort_arr[0]


assert (find_uniq([1, 1, 1, 2, 1, 1])) == 2
assert (find_uniq([0, 0, 0.55, 0, 0])) == 0.55
assert (find_uniq([8, 8, 8, 8, 8, 8, 8, 7])) == 7


def digital_root(n):
    """Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer."""

    if len(str(n)) == 1:
        return n
    sum = 0
    for i in str(n):
        sum += int(i)
    return digital_root(sum)


assert (digital_root(493193)) == 2
assert (digital_root(16)) == 7


def is_square(n):
    if n < 0:
        return False
    return math.sqrt(n) % 1 == 0


assert (is_square(3)) == False
assert (is_square(-1)) == False
assert (is_square(25)) == True


def count_by(x, n):
    return [i for i in range(x, x * n + 1, x)]


assert (count_by(2, 5)) == [2, 4, 6, 8, 10]


def rps(p1, p2):
    """Let's play! You have to return which player won! In case of a draw return"""
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock":
        if p2 == "scissors":
            return "Player 1 won!"
        else:
            return "Player 2 won!"
    elif p1 == "paper":
        if p2 == "rock":
            return "Player 1 won!"
        else:
            return "Player 2 won!"
    elif p1 == "scissors":
        if p2 == "paper":
            return "Player 1 won!"
        else:
            return "Player 2 won!"


assert (rps("rock", "scissors")) == "Player 1 won!"
assert (rps("scissors", "rock")) == "Player 2 won!"


def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


def count_bits(n):
    """Description:
    Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

    Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
    """
    return bin(n).count("1")


assert (count_bits(77231418)) == 14
assert (count_bits(12525589)) == 11


def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)


assert (binary_array_to_number([0, 0, 0, 1])) == 1


def wave(people):
    arr = []
    for i in range(len(people)):
        if people[i] != ' ':
            temp = people[:i].lower() + people[i:].capitalize()
            arr.append(temp)
    return arr


(wave(' gap '))


def create_phone_number(n):
    '''Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.'''

    row_num = ''.join(map(str, n))

    return f'({row_num[:3]}) {row_num[3:6]}-{row_num[6:]}'


assert (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == '(123) 456-7890'


def duplicate_count(text):
    '''Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
    '''
    result = collections.Counter(text.lower())
    count = 0
    for i in result.values():
        if i > 1:
            count += 1
    return count


assert (duplicate_count("")) == 0
assert (duplicate_count("abcde")) == 0
assert (duplicate_count("abcdeaa")) == 1
assert (duplicate_count("abcdeaB")) == 2
assert (duplicate_count("Indivisibilities")) == 2


def even_or_odd(number):
    """Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd
    numbers. """
    return 'Even' if number % 2 == 0 else 'Odd'


def pig_it(text):
    '''Move the first letter of each word to the end of it, then add "ay" to    the end of the word. Leave punctuation marks untouched.'''

    pig_sentence = ''
    for word in text.split():
        if word in '!,.#$%^*?&':
            pig_sentence += word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence += pig_word + ' '

    return pig_sentence.strip(' ')


assert (pig_it('Hello world !')) == 'elloHay orldway !'


def pig_it_v2(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)


assert (pig_it_v2('Hello world !')) == 'elloHay orldway !'


def friend(x):
    '''Make a program that filters a list of strings and returns a list with only your friends name in it.
    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
    Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]'''
    return [i for i in x if len(i) == 4]


assert (friend(["Ryan", "Kieran", "Mark", ]) == ["Ryan", "Mark"])


def is_triangle(a, b, c):
    '''Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

    (In this case, all triangles must have surface greater than 0 to be accepted).'''
    return (a < b + c) and (b < a + c) and (c < a + b)


assert (is_triangle(1, 2, 2)) == True
assert (is_triangle(7, 2, 2)) == False
assert (is_triangle(1, 2, 3)) == False
assert (is_triangle(1, 3, 2)) == False


def two_sum(numbers, target):
    '''
    Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).

    For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

    The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).
    '''

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                return i, j


assert (two_sum([1, 2, 3], 4)) == (0, 2)


def unique_in_order(iterable):
    '''Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.'''
    res = []
    prev = None
    for i in iterable:
        if i != prev:
            res.append(i)
        prev = i
    return res


assert (unique_in_order('AAAABBBCCDAABBB')) == ['A', 'B', 'C', 'D', 'A', 'B']


def valid_parentheses(string):
    '''Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
    '''
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


assert valid_parentheses("()") == True
assert valid_parentheses(")(()))") == False
assert valid_parentheses("(") == False
assert valid_parentheses("(())((()())())") == True


def describe_the_shape(angles):
    '''(replace s with number of sides and d with the measure of the interior angles).
    Angle measure should be floored to the nearest integer.
    Number of sides will be tested from 0 to 180.'''

    if angles < 3:
        return 'this will be a line segment or a dot'
    else:
        return f'This shape has {angles} sides and each angle measures {int(180 * (angles - 2) / angles)}'


assert (describe_the_shape(3)) == "This shape has 3 sides and each angle measures 60"

assert (describe_the_shape(2)) == "this will be a line segment or a dot"
assert (describe_the_shape(1)) == "this will be a line segment or a dot"


def sequence(x):
    if x < 10:
        return [i for i in range(1, x + 1)]
    part1 = [i for i in range(10, x + 1)]
    part2 = [i for i in range(2, 10)]

    return ([1] + part1 + part2)


sequence(16)


def powers_of_two(n):
    '''Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
    '''
    res = []
    for i in range(0, n + 1):
        res.append(2 ** i)
    return res

    # return [2**x for x in range(n+1)]


assert powers_of_two(0) == [1]
assert powers_of_two(1) == [1, 2]


def filter_long_words(sentence, n):
    row = sentence.split(' ')
    res = []
    for i in res:
        print(len(i))
        if len(i) > n:
            res.append(i)
    # print(res)


# print(filter_long_words("The quick brown fox jumps over the lazy dog", 4)) 
# == ['quick', 'brown', 'jumps']


def swap(string_):
    '''Given a string, swap the case for each of the letters.
    e.g. CodEwArs --> cODeWaRS'''
    s = ''
    for i in string_:
        if i.isupper():
            s += i.lower()
        else:
            s += i.upper()
    return s

    # return string_.swapcase()


assert swap('HelloWorld') == 'hELLOwORLD'
assert swap('CodeWars') == 'cODEwARS'


def domain_name(url):
    '''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:'''
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


def remove_(integer_list, values_list):
    """
    Define a method/function that removes from a given array of integers all the values contained in a second array.
    Examples (input -> output):
    * [1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3] -> [2, 2, 4]
    """
    res = []
    for i in integer_list:
        if i not in values_list:
            res.append(i)
    return res

    # return [i for i in integer_list if i not in values_list]


integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]


# assert remove_(integer_list, values_list) == [2, 2, 4]


def accum(s):
    res = ''
    for idx, value in enumerate(list(s.lower()), start=1):
        res += value * idx + '-'
    return res.title()[:-1]


assert (accum("ZpglnRxqenU")) == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"


def meeting(rooms):
    """
    Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!
    In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).
    'X' --> busy
    'O' --> empty
    """
    if 'O' in rooms:
        return rooms.index('O')
    else:
        return 'None available!'


# return rooms.index("O") if "O" in rooms else "None available!"

#
# assert meeting(['X', 'X', 'O', 'X']) == 254
# assert meeting(['X', 'X', 'X']) == 'None available!'


def closest_multiple_10(i):
    """Given a number return the closest number to it that is divisible by 10."""
    return round(i / 10) * 10


assert closest_multiple_10(54) == 50


def sticky_calc(operation, val1, val2):
    """Description
    Frank just bought a new calculator. But, this is no normal calculator. This is a 'Sticky Calculator.
    Whenever you add add, subtract, multiply or divide two numbers the two numbers first stick together:
    For instance:
    50 + 12 becomes 5012
    and then the operation is carried out as usual:
    (5012) + 12 = 5024"""
    val1, val2 = round(val1), round(val2)
    sticky = int(str(val1) + str(val2))

    if operation == '+':
        return sticky + val2
    elif operation == '-':
        return sticky - val2
    elif operation == '*':
        return sticky * val2
    elif operation == '/':
        return sticky / val2


assert sticky_calc('+', 4, 7) == 54


def gimme(input_array):
    """As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.
    The input to the function will be an array of three distinct numbers (Haskell: a tuple).
    For example:
    gimme([2, 3, 1]) => 0"""""

    middle = sorted(input_array)[1]
    return input_array.index(middle)


assert gimme([2, 3, 1]) == 0


def longest(a1, a2):
    """Take 2 strings s1 and s2 including only letters from ato z.
    Return a new sorted string, the longest possible,
    containing distinct letters - each taken only once - coming from s1 or s2.
    """
    result = set(a1 + a2)
    return ''.join(sorted(result))


assert longest("aretheyhere", "yestheyarehere") == "aehrsty"


def increment_string(strng):
    """Your job is to write a function which increments a string, to create a new string.
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string."""
    stock_digit = []
    stock_letter = ''
    for i in list(strng):
        if i.isdigit():
            stock_digit.append(int(i))
        # stock_letter += i

    # print(stock_letter)
    # print(stock_digit)

    # return strng


# assert increment_string("foo") == "foo1"
# assert increment_string("foobar001") == "foobar002"
# assert increment_string("foobar1") == "foobar2"


def maskify(cc):
    """Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

    Your task is to write a function maskify, which changes all but the last four characters into '#'.

    """
    start = ''
    for i in cc[:-4]:
        if i:
            start += '#'
    return start + cc[-4:]


assert maskify("4556364607935616") == "############5616"


def solution(string, ending):
    """Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd
    argument (also a string). """
    return string.endswith(ending)


assert solution('abcde', 'cde') == True
assert solution('abcde', 'abc') == False


def string_clean(s):
    """
    Delete from string all digits.
    """
    res = ''

    for i in s:
        if not i.isdigit():
            res += i
    return res


assert string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!") == "Dsa cdsc csa!!! I Am cool!"


def sum_pairs(ints, s):
    """
    https://www.codewars.com/kata/54d81488b981293527000c8f/train/python
    Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
    """

    d = set()
    for n in ints:
        if n in d:
            return [s - n, n]
        d.add(s - n)


l1 = [1, 4, 8, 7, 3, 15]
assert sum_pairs(l1, 8) == [1, 7]


def choose_best_sum(t, k, ls):
    from itertools import combinations
    """https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python"""
    try:
        return max(sum(i) for i in combinations(ls, k) if sum(i) <= t)
    except:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
assert (choose_best_sum(230, 4, xs)) == 230
assert (choose_best_sum(430, 5, xs)) == 430
assert (choose_best_sum(430, 8, xs)) is None


def is_prime(num):
    """https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python"""
    if num <= 1:
        return False
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


class Add(int):
    """https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/python"""

    def __call__(self, n):
        return Add(self + n)


def positive_sum(arr):
    """https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python"""
    return sum(i for i in arr if i > 0)


def opposite(number):
    """https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python"""
    return -number


def find_smallest_int(arr):
    """https://www.codewars.com/kata/55a2d7ebe362935a210000b2/python"""
    return min(arr)


def better_than_average(class_points, your_points):
    """https://www.codewars.com/kata/5601409514fc93442500010b/train/python"""
    avg = sum(class_points) / len(class_points)
    if your_points > avg:
        return True
    return False


def century(year):
    """https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python"""
    from math import ceil

    return ceil(year / 100)


def square_or_square_root(arr):
    from math import sqrt
    """https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python"""
    res = []
    for i in arr:
        if sqrt(i) % 1 == 0:
            res.append(round(sqrt(i)))
        else:
            res.append(i ** 2)

    return res


assert square_or_square_root([4, 3, 9, 7, 2, 1]) == [2, 9, 3, 49, 4, 1]


def find_multiples(integer, limit):
    """https://www.codewars.com/kata/58ca658cc0d6401f2700045f/python"""
    return [i for i in range(integer, limit + 1) if i % integer == 0]


assert find_multiples(5, 25) == [5, 10, 15, 20, 25]


def mag_number(info, n):
    import math

    weapons = {
        'PT92': 17,
        'M4A1': 30,
        'M16A2': 30,
        'PSG1': 5,
    }
    return math.ceil(n * 3 / weapons[info])


assert mag_number('PT92', 6) == 2
assert mag_number('M4A1', 8) == 1
assert mag_number('PSG1', 31) == 19


def remove_every_other(my_list):
    res = []
    for i, val in enumerate(my_list):
        if i % 2 == 0:
            res.append(val)
    return res


assert remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) == ["Keep", "Keep", "Keep"]


def sum_dif(n):
    res = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return sum(res)
    # s = set(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


assert sum_dif(10) == 23


def square_area(A):
    p = A * 4 / (math.pi * 2)
    res = p * p
    return round(res, 2)


assert (square_area(2)) == 1.62


def digitize(n):
    """Convert number to reversed array of digits
    https://www.codewars.com/kata/5583090cbe83f4fd8c000051/solutions/python
    """
    return list(map(int, str(n)[::-1]))
    # return [int(x) for x in str(n)[::-1]]


assert digitize(35231) == [1, 3, 2, 5, 3]


def pipe_fix(nums):
    """Lario and Muigi Pipe Problem
    https://www.codewars.com/kata/56b29582461215098d00000f/train/python"""
    raw = sorted(nums)
    return [x for x in range(raw[0], raw[-1] + 1)]
    # return list(range(min(nums), max(nums)+1))


assert pipe_fix([1, 2, 3, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def to_freud(sentence):
    """Freudian translator
    https://www.codewars.com/kata/5713bc89c82eff33c60009f7/solutions/python
    """
    return (len(sentence.split()) * ' sex').strip()


assert (to_freud("This is a test")) == "sex sex sex sex"


def is_narcissistic(i):
    # s = len(str(i))
    # res = []
    # for x in str(i):
    #     res.append(int(x)**s)
    #
    # if sum(res) == i:
    #     return True
    # return False

    num = str(i)
    length = len(num)
    return sum(int(a) ** length for a in num) == i


assert is_narcissistic(1634) == True
assert is_narcissistic(825) == False


def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x


def count_sheep(n):
    # res = ''
    # for i in range(1, n+1):
    #     res += f'{i} sheep...'
    # return res

    return ''.join(f"{i} sheep..." for i in range(1, n + 1))


assert (count_sheep(3)) == '1 sheep...2 sheep...3 sheep...'


def vowel_indices(word):
    """Find the vowels"""
    vowels = ['a', 'e', 'u', 'i', 'o', 'y']

    res = []
    for idx, value in enumerate(word.lower(), start=1):
        if value in vowels:
            res.append(idx)
    return res

    # return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']


assert (vowel_indices("apple")) == [1, 5]
assert (vowel_indices("apple")) == [1, 5]
assert (vowel_indices("UNDISARMED")) == [1, 4, 6, 9]
assert vowel_indices('supercalifragilisticexpialidocious') == [2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 25, 27, 29, 31,
                                                               32, 33]


def solution(s):
    """Split Strings
    https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
    """
    res = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0, len(s), 2):
        res.append(s[i:i + 2])
    return res


assert solution("asdfads") == ['as', 'df', 'ad', 's_']


def sort_array(source_array):
    """Sort the odd
    https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python"""
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def no_space(x):
    """Remove String Spaces
    """
    return ''.join(x.split(' '))


assert no_space('8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB'


def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i != j:
            return j


assert first_non_consecutive([1, 2, 3, 4, 6, 7, 8]) == 6
assert first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]) is None
assert first_non_consecutive([4, 6, 7, 8, 9, 11]) == 6


def merge_arrays(arr1, arr2):
    """Merge two sorted arrays into one"""

    return sorted(set(arr1 + arr2))


assert merge_arrays([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]) == [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]


def usdcny(usd):
    """Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an
    integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'

    """
    return f"{(usd * 6.75):.2f} Chinese Yuan"


assert usdcny(465) == "3138.75 Chinese Yuan"


def aspect_ratio(x: int, y: int):
    """Aspect Ratio Cropping - Part 1"""
    return math.ceil(y * 16 / 9), y


assert aspect_ratio(640, 480) == (854, 480)


def pillars(num_pill, dist, width):
    """Pillars"""
    if num_pill < 2:
        return 0

    return num_pill * ((dist * 100) + width) - (width * 2) - (dist * 100)


assert pillars(2, 20, 25) == 2000
assert pillars(11, 15, 30) == 15270


def is_palindrome(s):
    """Write a function that checks if a given string (case insensitive) is a palindrome."""

    return s.lower() == s.lower()[::-1]


assert is_palindrome('aba') == True
assert is_palindrome('Abba') == True
assert is_palindrome('malam') == True
assert is_palindrome('walter') == False


def is_today(date):
    return date.date() == datetime.today().date()


assert is_today(datetime(2020, 10, 1, 1, 1, 1, 1)) == False


def each_cons(lst, n):
    mas = []
    for i in range(len(lst) - n + 1):
        mas.append(lst[i:i + n])
    return mas


lst = [3, 5, 8, 13]


# assert (each_cons(lst, 2)) == [[3, 5, 8], [5, 8, 13]]


def bingo(array):
    """Bingo ( Or Not )"""
    win = sorted([2, 9, 14, 7, 15])
    res = []
    alfa = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    for i in array:
        if i in win:
            res.append(i)
    if list(set(res)) == win:
        return 'WIN'
    return 'LOSE'


# return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"


assert bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]) == "LOSE"
assert bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]) == "WIN"


def solve(s):
    """Simple string characters"""
    count_upper = 0
    count_lower = 0
    count_number = 0
    count_special = 0

    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i.isnumeric():
            count_number += 1
        elif i in string.punctuation:
            count_special += 1

    return [count_upper, count_lower, count_number, count_special]


assert solve("*'&ABCDabcde12345") == [4, 5, 5, 3]


def find_difference(a, b):
    """Difference of Volumes of Cuboids"""
    return abs(math.prod(a) - math.prod(b))


assert find_difference([3, 2, 5], [1, 4, 4]) == 14


def double_char(s):
    """Double Char"""
    res = ''
    for i in s:
        res += i * 2
    return res

    # return ''.join(c * 2 for c in s)


assert double_char("String") == "SSttrriinngg"


def between(a, b):
    """What is between?"""
    return [res for res in range(a, b + 1)]

    # return list(range(a,b+1))


def delete_nth(order, max_e):
    """Delete occurrences of an element if it occurs more than n times"""

    res = []

    for i in order:
        if res.count(i) < max_e:
            res.append(i)
    return res


assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]


def define_suit(card):
    val = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
    }
    return val[card[-1]]


assert define_suit('3C') == 'clubs'
assert define_suit('3S') == 'spades'


def sum_str(a, b):
    """Sum The Strings"""
    if a.isdigit() and b.isdigit():
        return str(int(a) + int(b))
    elif len(a) == 0 and len(b) == 0:
        return '0'
    elif len(a) == 0 and b.isdigit():
        return b
    elif len(b) == 0 and a.isdigit():
        return a


#   return str(int(a or 0) + int(b or 0))


assert (sum_str('481693', '202083')) == '683776'
assert sum_str("", "") == "0"
assert sum_str("9", "") == "9"
assert sum_str("", "5") == "5"


def dont_give_me_five(start, end):
    """Don't give me five!"""
    res = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            res += 1
    return res
    # return sum('5' not in str(i) for i in range(start, end + 1))


assert dont_give_me_five(1, 9) == 8
assert dont_give_me_five(4, 17) == 12


def high(x):
    """Highest Scoring Word"""
    keys = []
    values = []

    for word in x.split():
        score = 0
        keys.append(word)

        for letter in word:
            score += (ord(letter)) - 96
        values.append(score)

    res = dict(zip(keys, values))
    max_Score = max(res.values())

    for k, v in res.items():
        if v == max_Score:
            return k


assert high('man i need a taxi up to ubud') == 'taxi'


def find_children(dancing_brigade):
    """Where is my parent!?(cry)
    https://www.codewars.com/kata/58539230879867a8cd00011c/train/python
    """
    res = []
    for i in sorted(dancing_brigade.lower()):
        if i.upper() not in res:
            res.append(i.upper())
        else:
            res.append(i)

    return ''.join(res)


assert find_children("AaaaaZazzz") == "AaaaaaZzzz"


def hex_to_dec(s):
    """Hex to Decimal"""
    return int(s, 16)


assert hex_to_dec("10") == 16


def to_alternating_case(string: str):
    """altERnaTIng cAsE <=> ALTerNAtiNG CaSe"""
    res = []
    for letter in string:
        if letter == letter.upper():
            res.append(letter.lower())
        elif letter == letter.lower():
            res.append(letter.upper())

    return ''.join(res)
    # return string.swapcase()


assert to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E"
assert to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE"


def to_jaden_case(s: str):
    """Jaden Casing Strings"""
    return string.capwords(s)


quote = "How can mirrors be real if our eyes aren't real"
assert to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real"


def solution(nums=None):
    """Sort Numbers"""
    if nums is None:
        return []
    return [i for i in sorted(nums)]


assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]


# assert (solution(None)) == []


def direction(facing, turn):
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return compass[(compass.index(facing) + turn // 45) % 8]


assert (direction("S", 180)) == "N"
assert (direction("SE", -45)) == "E"
assert (direction("W", 495)) == "NE"


def sum_mul(n, m):
    """Sum of Multiples"""
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'


assert sum_mul(2, 9) == 20
assert sum_mul(0, 0) == 'INVALID'
assert sum_mul(4, -7) == 'INVALID'


def reverseWords(str):
    """Reversed Words"""
    return " ".join(str.split(" ")[::-1])


assert reverseWords("The greatest victory is that which requires no battle") == "battle no requires which that is " \
                                                                                "victory greatest The"


def remove(s):
    return s.strip('!')


assert remove("Hi! Hi!") == "Hi! Hi"


def weather_info(temperature):
    c = convert_to_celsius(temperature)
    if c < 0:
        return f'{c} is freezing temperature'
    else:
        return f'{c} is above freezing temperature'


def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)


assert weather_info(50) == '10.0 is above freezing temperature'
assert weather_info(23) == '-5.0 is freezing temperature'


def greet(language):
    dic = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    if language in dic:
        return dic[language]
    else:
        return 'Welcome'


assert (greet('english')) == 'Welcome'
assert (greet('dutch')) == 'Welkom'
assert (greet('IP_ADDRESS_INVALID')) == 'Welcome'


def is_uppercase(inp):
    """Is the string uppercase?"""
    return inp == inp.upper()



assert is_uppercase("hello I AM DONALD") == False
assert is_uppercase("HELLO I AM DONALD") == True
assert is_uppercase("$%&") == True
