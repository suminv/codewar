def duck_duck_goose(players, goose):
    idx = (goose - 1) % len(players)
    return players[idx].name
