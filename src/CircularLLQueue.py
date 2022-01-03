from src.PyDSError import QueueError

class CircularLLQueue():
    """Simple queue that supports right-to-left rotation operations."""
    class _Node:
        """Internal class used for internal cirular linked list."""
        __slots__ = '_value', '_next'
        def __init__(self, value=None, next_ptr=None):
            self._value = value
            self._next = next_ptr

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def front(self):
        """Returns the value of the first node in the queue."""
        if not self._size:
            return None
        return self._tail._next._value

    def enqueue(self, item):
        """Adds a node to the end of the queue with item as its value."""
        if not self._size:
            self._tail = self._Node(item)
            self._tail._next = self._tail
        else:
            temp = self._Node(item, self._tail._next)
            self._tail._next = temp
            self._tail = temp
        self._size += 1

    def dequeue(self):
        """Removes the first node in the queue and returns its value."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item from empty queue")
        temp = self._tail._next
        self._tail._next = temp._next
        self._size -= 1
        return temp._value

    def rotate(self):
        """Rotate the queue to the left by one item."""
        if self._size:
            self._tail = self._tail._next
