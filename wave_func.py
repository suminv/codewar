def wave(people):
    arr = []
    for i in range(len(people)):
        if people[i] != ' ':
            temp = people[:i].lower() + people[i:].capitalize()
            arr.append(temp)
    return arr


(wave(' gap '))
