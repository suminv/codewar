def row_weights(array):
    team_1_weight = sum(array[::2])
    team_2_weight = sum(array[1::2])

    return team_1_weight, team_2_weight


assert (row_weights([100, 50])) == (100, 50)
