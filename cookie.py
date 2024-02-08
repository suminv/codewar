def cookie(x):
    names = {str: "Zach", int: "Monica", float: "Monica"}
    name = names.get(type(x), "the dog")
    return f"Who ate the last cookie? It was {name}!"


assert cookie("Ryan") == "Who ate the last cookie? It was Zach!"
assert cookie(2.3) == "Who ate the last cookie? It was Monica!"
assert cookie(26) == "Who ate the last cookie? It was Monica!"
assert cookie(True) == "Who ate the last cookie? It was the dog!"
