def dna_to_rna(dna):
    """8 kyu DNA to RNA Conversion"""
    if 'T' in dna:
        return dna.replace("T", 'U')
    return dna


"""8 kyu Grasshopper - Messi Goals"""
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
