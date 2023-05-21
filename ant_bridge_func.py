def ant_bridge(ants, terrain):
    """5 kyuAnt Bridge"""
    n_ants = len(ants)
    terrain = terrain.replace('-.', '..')
    terrain = terrain.replace('.-', '..')
    count = terrain.count('.') % n_ants

    return ants[-count:] + ants[:-count]
