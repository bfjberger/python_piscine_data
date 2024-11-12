
def ft_filter(iterable, function):
    '''see doc https://docs.python.org/3/library/functions.html#filter'''
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]
