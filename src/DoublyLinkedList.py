class DoublyLinkedList():
    class _Node:
        __slots__ = '_value', '_prev', '_next'
        def __init__(self, value=None, prev_ptr=None, next_ptr=None):
            self._value = value
            self._prev = prev_ptr
            self._next = next_ptr
    
    def __init__(self):
        self._temp = None
