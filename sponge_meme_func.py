def sponge_meme(s):
    result = []
    for index, i in enumerate(s):
        if index % 2 == 0:
            result.append(i.upper())
        else:
            result.append(i.lower())
    return ''.join(result)


assert sponge_meme('stop Making spongebob Memes!') == 'StOp mAkInG SpOnGeBoB MeMeS!'
