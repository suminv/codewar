def no_space(x):
    """Remove String Spaces
    """
    return ''.join(x.split(' '))


assert no_space('8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB'
