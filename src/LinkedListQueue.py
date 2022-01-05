#TODO: dequeue(): sanitize removed node with None for python GC
from src.PyDSError import QueueError

class LinkedListQueue:
    """Simple queue that internally uses a linked list."""
    class _Node:
        """Private class used for internal linked list."""
        __slots__ = '_value', '_next'

        def __init__(self, value=None, next_ptr=None):
            self._value = value
            self._next = next_ptr

    def __init__(self):
        """Head of linked list is the front of the queue, and vice versa."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def front(self):
        """Returns value of the node at the front of the queue."""
        if not self._size:
            return None
        return self._head._value

    def enqueue(self, item):
        """Adds a new node to the end of the queue with item as its value."""
        if not self._size:
            self._head = self._Node(item, None)
            self._tail = self._head
        else:
            self._tail._next = self._Node(item, None)
            self._tail = self._tail._next
        self._size += 1

    def dequeue(self):
        """Removes the node from the front of the queue and returns its value."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item from empty queue")
        temp = self._head._value
        self._head = self._head._next
        self._size -= 1
        return temp
