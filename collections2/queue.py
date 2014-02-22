"""
While a deque can do anything a queue can do and more, by limiting the number
of available actions we achieve two things:

- It becomes semantically clear how we intend to use a data-structure.

- We can strengthen the invariants.

A similar argument can be made for using a stack in place of a list.
"""
from collections import deque


class Queue(object):
    """
    A first-in first-out data structure.

    A queue is guaranteed to always have at least 0 elements, and to always
    maintain the first-in first-out property.

    """
    def __init__(self):
        self._items = deque()

    @property
    def top(self):
        return self._items[0]

    @property
    def empty(self):
        return len(self) == 0

    def push(self, item):
        '''Q.push(object) -- push object on back of queue.'''
        self._items.append(item)

    def pop(self):
        '''Q.pop() -> item -- remove and return first item.
        Raises IndexError if queue is empty.'''
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        while not self.empty:
            yield self.pop()
 
 
class Queue2(object):
    """
    A bounded first-in first-out (FIFO) data structure.
 
    A queue is guaranteed to always have at least 0 elements,
    and to always maintain the first-in first-out property.

    Based on http://www.cs.cmu.edu/~rwh/theses/okasaki.pdf
    """
    def __init__(self, size):
        # Maximum size of queue
        self.size = size
        # Holds the front elements in correct order
        self._forward = []
        # Holds the back elements in reverse order
        self._backward = []
 
    @property
    def top(self):
        """Check the top element."""
        return self._forward[0]
 
    @property
    def empty(self):
        """Check if the queue is empty."""
        return len(self) == 0
 
    def __restore_invariant(self):
        """
        Copy over backward to forward if forward becomes empty and reverse it.
        This ensures the queue can always successfully pop when it contains
        items. Note that though this would make the cost of popping O(n),
        the amortized cost is only O(1).
        """
        if len(self._forward) == 0:
            self._forward, self._backward = self._backward, []
            self._forward.reverse()
 
    def push(self, item):
        '''Q.push(object) -- push object on back of queue.'''
        if self.size == len(self):
            raise ValueError("queue is full")
        else:
            self._backward.append(item)
            self.__restore_invariant()
 
    def pop(self):
        '''Q.pop() -> item -- remove and return first item.
        Raises IndexError if queue is empty.'''
        res = self._forward.pop()
        self.__restore_invariant()
        return res
 
    def __len__(self):
        return len(self._forward) + len(self._backward)
 
    def __contains__(self, item):
        return item in self._forward or item in self._backward
