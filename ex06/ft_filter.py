def ft_filter(function, iterable):
    """
    It takes a function and an iterable and
    returns an iterable with only the elements
    where the function returns True.
    """
    return [item for item in iterable if function(item)]
