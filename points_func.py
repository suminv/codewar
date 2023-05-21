def points(games):
    """Our football team finished the championship. The result of each match look like "x:y". Results of all matches
    are recorded in the collection.

    For example: ["3:1", "2:2", "0:1", ...]

    Write a function that takes such collection and counts the points of our team in the championship. Rules for
    counting points for each match:

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
