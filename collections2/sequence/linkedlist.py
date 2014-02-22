'''A stack cargo, supporting push and pop implementations.
 
Implemented using a linked list. Technically, not necessary since Python's list
supports pop and append, but marking a list as a stack can be linguistically
simpler, especially when iterating.'''
 
 
class Node(object):
    def __init__(self, cargo, left, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
 
 
class DoubleLinkedList(object):
    '''
    A stack cargo, supporting push and pop implementations.
 
    >>> ll = DoubleLinkedList()
    >>> ll.empty
    True
    >>> ll.append(1)
    >>> ll.append(2)
    >>> ll.right
    2
    >>> ll.pop()
    2
    >>> ll.pop()
    1
    '''
 
    def __init__(self, items=None):
        self._right = None
        self._left = None
        if items is not None:
            for item in items:
                self.append(item)
 
    @property
    def right(self):
        assert not self.empty, 'head of empty list'
        return self._right.cargo
 
    @property
    def left(self):
        assert not self.empty, 'head of empty list'
        return self._left.cargo
 
    @property
    def empty(self):
        """Check if the list is empty."""
        return self._right is None
 
    def append(self, cargo):
        '''S.append(cargo) -- push cargo on top.'''
        node = Node(cargo, self._right, None)
        if self.empty:
            self._left = node
        self._right = node
 
    def appendleft(self, cargo):
        '''S.append(cargo) -- push cargo on top.'''
        node = Node(cargo, None, self._left)
        if self.empty:
            self._right = node
        self._left = node
 
    def pop(self):
        assert not self.empty, 'pop from empty list'
        self._right, cargo = self._right.left, self._right.cargo
        return cargo
 
    def popleft(self):
        assert not self.empty, 'pop from empty list'
        self._left, cargo = self._left.right, self._left.cargo
        return cargo
 
    def reverse(self):
        self._right.left, current = None, self._right.left
        if current is not None:
            left, current.left = current.left, self._right
            while left is not None:
                left.left, current, left = current, left, left.left
            self._right = current
 
    def __iter__(self):
        node = self._right
        while node:
            yield node.cargo
            node = node.left
 
    def insert_after(self, lead, cargo):
        for node in self:
            if node.cargo == lead:
                lead.left = Node(cargo, lead.left)
                return True
        return False
 
    def remove(self, cargo):
        '''L.remove(value) -- remove first occurence of value.
        Raises ValueError if the value is not present.'''
        for node in self:
            if node.left.cargo == cargo:
                node.left = node.left.left
                return
        raise ValueError('list.remove(x): x not in list')
 
 
class LinkedList(object):
    '''
    A stack cargo, supporting push and pop implementations.
 
    >>> ll = LinkedList()
    >>> ll.empty
    True
    >>> ll.push(1)
    >>> ll.push(2)
    >>> ll.head
    2
    >>> ll.pop()
    2
    >>> ll.pop()
    1
    '''
 
    def __init__(self):
        self._head = None
 
    @property
    def head(self):
        '''
        S.peek() -> item -- return top item.
        Raises IndexError if stack is empty.
        '''
        assert not self.empty, 'peek at empty list'
        return self._head.cargo
 
    @property
    def empty(self):
        """Check if the list is empty."""
        return self._head is None
 
    def push(self, cargo):
        '''S.push(cargo) -- push cargo on top.'''
        self._head = Node(cargo, self._head)
 
    def pop(self):
        '''
        S.pop() -> item -- remove and return top item.
        Raised IndexError if stack is empty.
        '''
        assert not self.empty, 'pop from empty list'
        self._head, cargo = self._head.left, self._head.cargo
        return cargo
 
    def reverse(self):
        self._head.left, current = None, self._head.left
        if current is not None:
            left, current.left = current.left, self._head
            while left is not None:
                left.left, current, left = current, left, left.left
            self._head = current
 
    def __iter__(self):
        node = self._head
        while node:
            yield node.cargo
            node = node.left
 
    def insert_after(self, lead, cargo):
        for node in self:
            if node.cargo == lead:
                lead.left = Node(cargo, lead.left)
                return True
        return False
 
    def remove(self, cargo):
        '''L.remove(value) -- remove first occurence of value.
        Raises ValueError if the value is not present.'''
        for node in self:
            if node.left.cargo == cargo:
                node.left = node.left.left
                return
        raise ValueError('list.remove(x): x not in list')
