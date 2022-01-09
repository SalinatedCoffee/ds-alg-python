from src.DoublyLinkedList import DoublyLinkedList

class PositionalDLList(DoublyLinkedList):
    """Simple position-referenced list ADT that uses a doubly linked list internally."""
    class Position:
        """Position object that is used to reference nodes in the list."""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Returns value stored by node at current position."""
            return self._node._value

        def __eq__(self, other):
            """Returns True if self and other represent the same position."""
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            """Returns True if self and other does not represent the same position."""
            return not (self == other)

    def _validate(self, p):
        """Returns node at position p if valid, raises error otherwise."""
        if not isinstance(p, self.Position):
            raise TypeError("provided object is not of correct Position type")
        if p._container is not self:
            raise ValueError("provided Position does not belong to this list")
        if p._node._next is None:
            raise ValueError("provided Position is no longer valid")
        return p._node

    def _make_position(self, node):
        """
        Returns a Position object that corresponds to node.
        Returns None if given node is a sentinel node.
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Returns a Position object for the first node in the list."""
        return self._make_position(self._header._next)

    def last(self):
        """Returns a Position object for the last node in the list."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Returns a Position object for the node before Position p."""
        p = self._validate(p)
        return self._make_position(p._prev)

    def after(self, p):
        """Returns a Position object for the node after Position p."""
        p = self._validate(p)
        return self._make_position(p._next)

    def __iter__(self):
        """Forward iteration generator of current list."""
        current = self.first()
        while current is not None:
            yield current.element()
            current = self.after(current)

    def _insert_between(self, item, prev_ptr, next_ptr):
        """Inserts a new node between two nodes and returns a Position object for that node."""
        node = super()._insert_between(item, prev_ptr, next_ptr)
        return self._make_position(node)

    def add_first(self, e):
        """Inserts a node with value e at the front of the list and returns its Position object."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Inserts a node with value e at the end of the list and returns its Position object."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Inserts a node with value e before the node at position p and returns its Position object."""
        p = self._validate(p)
        return self._insert_between(e, p._prev, p)

    def add_after(self, p, e):
        """Inserts a node with value e after the node at position p and returns its Position object."""
        p = self._validate(p)
        return self._insert_between(e, p, p._next)
    
    def delete(self, p):
        """Removes the node at position p and returns its value."""
        p = self._validate(p)
        return self._delete_node(p)

    def replace(self, p, e):
        """Replaces the value of the node at position p with e and returns the old value being replaced."""
        p = self._validate(p)
        old_value = p._value
        p._value = e
        return old_value
    