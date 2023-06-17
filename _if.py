def _if(value, func1, func2):
    if value:
        return func1()
    else:
        return func2()
