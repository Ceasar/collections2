"""
More functions for manipulating iterables.
"""
from itertools import chain, izip, islice


def flatten(*args):
    """
    Flatten a list of lists.

    >>> list(flatten([1, 2], [3, 4], {5, 6}))
    [1, 2, 3, 4, 5, 6]
    """
    return chain(*args)


def splice(x, i, y):
    """
    Splice one list into another.

    >>> list(splice([1, 2, 5, 6], 2, [3, 4]))
    [1, 2, 3, 4, 5, 6]
    """
    return chain(islice(x, 0, i), y, islice(x, i, len(x)))


def divide(list_, k):
    """
    Slice a list into pieces of length-k.

    >>> list(divide([1, 2, 3, 4, 5, 6], 2))
    [(1, 2), (3, 4), (5, 6)]
    >>> list(divide([1, 2, 3, 4, 5, 6, 7], 2))
    [(1, 2), (3, 4), (5, 6)]
    """
    return izip(*[iter(list_)] * k)


def enumerate2(iterable, reverse_counts=False, reverse_values=False):
    """
    Enumerate a reversed iterable.

    >>> items = ['a', 'b', 'c']
    >>> list(enumerate2(items))
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> list(enumerate2(items, reverse_counts=True))
    [(2, 'a'), (1, 'b'), (0, 'c')]
    >>> list(enumerate2(items, reverse_values=True))
    [(0, 'c'), (1, 'b'), (2, 'a')]
    >>> list(enumerate2(items, reverse_counts=True, reverse_values=True))
    [(2, 'c'), (1, 'b'), (0, 'a')]
    """
    if reverse_counts:
        if reverse_values:
            return izip(reversed(xrange(len(iterable))), reversed(iterable))
        else:
            return izip(reversed(xrange(len(iterable))), iterable)
    else:
        if reverse_values:
            return izip(xrange(len(iterable)), reversed(iterable))
        else:
            return enumerate(iterable)
