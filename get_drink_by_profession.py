def get_drink_by_profession(param:str):
    res = {
    'Jabroni': 'Patron Tequila',
    'School Counselor': 'Anything with Alcohol',
    'Programmer': 'Hipster Craft Beer',
    'Bike Gang Member': 'Moonshine',
    'Politician': 'Your tax dollars',
    'Rapper': 'Cristal'
    }
    param = param.lower().title()
    return res.get(param, 'Beer')


assert (get_drink_by_profession("jabrOni")) == "Patron Tequila", 'Test case "jabrOni" failed '
assert (get_drink_by_profession("Pug")) == "Beer", 'Test case "Pug" failed'
