def feast(beast: str, dish: str):
    beast_first_letter = beast.split()[0][0]
    beast_last_letter = beast.split()[-1][-1]
    dish_first_letter = dish.split()[0][0]
    dish_last_letter = dish.split()[-1][-1]
    return beast_first_letter == dish_first_letter and beast_last_letter == dish_last_letter


print(feast("great blue heron", "garlic naan"))
