def pig_it(text):
    '''Move the first letter of each word to the end of it, then add "ay" to    the end of the word. Leave
    punctuation marks untouched. '''

    pig_sentence = ''
    for word in text.split():
        if word in '!,.#$%^*?&':
            pig_sentence += word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence += pig_word + ' '

    return pig_sentence.strip(' ')


assert (pig_it('Hello world !')) == 'elloHay orldway !'
