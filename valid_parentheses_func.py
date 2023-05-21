def valid_parentheses(string):
    """Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
    The function should return true if the string is valid, and false if it's invalid.
    """
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
