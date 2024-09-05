def reverse(st:str):
    return ' '.join(st.split(' ')[::-1])


assert reverse('Hello World') == 'World Hello'
