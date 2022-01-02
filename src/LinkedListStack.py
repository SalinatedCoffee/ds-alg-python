from src.PyDSError import StackError

class LinkedListStack():
    class _Node:
        def __init__(self, value=None, next = None):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def pop(self):
        if not self._size:
            raise StackError.EmptyStack("unable to pop item from empty stack")
        temp = self._head
        self._head = temp._next
        self._size -= 1
        return temp._value

    def push(self, item):
        temp = self._Node(item, self._head)
        self._head = temp
        self._size += 1

    def top(self):
        if not self._size:
            return None
        return self._head._value