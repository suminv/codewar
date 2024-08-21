def uefa_euro_2016(teams, score):
    if score[0] == score[1]:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'
    else:
        if score[0] > score[1]:
            return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!'

        return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'




print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))
# "At match Germany - Ukraine, Germany won!"))
