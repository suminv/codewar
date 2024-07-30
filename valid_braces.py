def is_valid_braces(s):
    # Создаем словарь для сопоставления закрывающих скобок с открывающими
    matching_braces = {")": "(", "]": "[", "}": "{"}
    # Создаем пустой стек
    stack = []

    for char in s:
        if char in matching_braces.values():
            # Если символ - открывающая скобка, добавляем его в стек
            stack.append(char)
        elif char in matching_braces.keys():
            # Если символ - закрывающая скобка
            if stack == [] or stack.pop() != matching_braces[char]:
                # Если стек пуст или верхний элемент стека не соответствует закрывающей скобке
                return False
        else:
            # Если символ не является скобкой (по условию задачи это не должно происходить)
            return False

    # Проверяем, пуст ли стек (все открывающие скобки должны быть закрыты)
    return stack == []


assert (is_valid_braces("(){}[]")) == True
assert (is_valid_braces("([{}])")) == True
assert (is_valid_braces("(}")) == False
assert (is_valid_braces("[(])")) == False
assert (is_valid_braces("[({})](]")) == False
