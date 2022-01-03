from src.PyDSError import QueueError

class CircularLLQueue():
    class _Node:
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
        return None

    def enqueue(self, item):
        return None

    def dequeue(self):
        return None

    def rotate(self):
        return None