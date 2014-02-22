

class Stack(object):
    """
    A first-in last-out data structure.

    A stack is guaranteed to always have at least 0 elements,
    and to always maintain the first-in first-out property.
    """
    def __init__(self):
        self._items = []

    @property
    def top(self):
        return self._items[-1]

    @property
    def empty(self):
        return len(self) == 0

    def item_at(self, pos):
        """Get the item at pos in the stack."""
        return self._items[pos]

    def push(self, item):
        '''S.push(object) -- push object on top.'''
        self._items.append(item)

    def pop(self):
        '''S.pop() -> item -- remove and return top item.
        Raises IndexError if stack is empty.
        '''
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop from empty stack")

    def __len__(self):
        return len(self._items)
