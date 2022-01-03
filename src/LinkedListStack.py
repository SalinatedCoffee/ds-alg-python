#TODO: pop(): sanitize removed node with None for python GC
from src.PyDSError import StackError

class LinkedListStack():
    """Simple stack that internally uses a linked list."""
    class _Node:
        """Private class used for internal linked list."""
        __slots__ = '_value', '_next'

        def __init__(self, value=None, next_ptr = None):
            self._value = value
            self._next = next_ptr

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def pop(self):
        """Removes the node at the head and returns its value."""
        if not self._size:
            raise StackError.EmptyStack("unable to pop item from empty stack")
        temp = self._head
        self._head = temp._next
        self._size -= 1
        return temp._value

    def push(self, item):
        """Adds a new node at the head with item as its value."""
        self._head = self._Node(item, self._head)
        self._size += 1

    def top(self):
        """Returns the value of the node at the head."""
        if not self._size:
            return None
        return self._head._value
