from src.PyDSError import StackError

class LinkedListStack():
    class _Node:
        def __init__(self):
            self._value = None
            self._next = None

    def __init__(self):
        self._head = self._Node()
        self._size = 1
