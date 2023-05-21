def combat(health, damage):
    """8 kyu Grasshopper - Terminal game combat function"""
    if health > damage:
        return health - damage
    return 0
