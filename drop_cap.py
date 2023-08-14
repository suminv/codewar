def drop_cap(words):
    res = []
    for i in words.split(" "):
        if len(i) > 2:
            res.append(i.capitalize())
        else:
            res.append(i)
    return " ".join(res)


assert (drop_cap("apple of banana")) == "Apple of Banana"
assert (drop_cap("one   space")) == "One   Space"
