class DoublyLinkedList:
    """Simple doubly linked list class intended for internal use."""
    class _Node:
        """Internal node class."""
        __slots__ = '_value', '_prev', '_next'
        def __init__(self, value=None, prev_ptr=None, next_ptr=None):
            self._value = value
            self._prev = prev_ptr
            self._next = next_ptr

    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def insert_between(self, item, prev_ptr, next_ptr):
        """
        Given references to two adjacent nodes, insert new node between them with item as its value.
        Assumes the two nodes are adjacent, and are in correct order.
        Returns the newly created node.
        """
        temp = self._Node(item, prev_ptr, next_ptr)
        prev_ptr._next = temp
        next_ptr._prev = temp
        self._size += 1
        return temp

    def delete_node(self, node):
        """Removes the node from the linked list and returns it."""
        node._prev._next = node._next
        node._next._prev = node._prev
        value = node._value
        node._value = node._prev = node._next = None
        self._size -= 1
        return value
