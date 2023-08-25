def bumps(road):
    return 'Car Dead' if road.count('n') > 15 else 'Woohoo!'


assert bumps("_nnnnnnn_n__n______nn__nn_nnn") == 'Car Dead'
assert bumps("__nn_nnnn__n_n___n____nn__nnn") == 'Woohoo!'
