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
            return None

        def __eq__(self, other):
            """Returns True if self and other represent the same position."""
            return None

        def __ne__(self, other):
            """Returns True if self and other does not represent the same position."""
            return None

    def _validate(self, p):
        """Returns node at position p if valid, raises error otherwise."""
        return None

    def _make_position(self, node):
        """Returns a Position object that corresponds to node."""
        return None

    def first(self):
        """Returns a Position object for the first node in the list."""
        return None

    def last(self):
        """Returns a Position object for the last node in the list."""
        return None

    def before(self, p):
        """Returns a Position object for the node before Position p."""
        return None

    def after(self, p):
        """Returns a Position object for the node after Position p."""
        return None

    def __iter__(self):
        """Forward iteration generator of current list."""
        yield None

    def insert_between(self, item, prev_ptr, next_ptr):
        """Inserts a new node between two positions and returns a Position object for that node."""
        return None

    def add_first(self, e):
        """Inserts a node with value e at the front of the list and returns its Position object."""
        return None

    def add_last(self, e):
        """Inserts a node with value e at the end of the list and returns its Position object."""
        return None
    
    def add_before(self, p, e):
        """Inserts a node with value e before the node at position p and returns its Position object."""
        return None

    def add_after(self, p, e):
        """Inserts a node with value e after the node at position p and returns its Position object."""
        return None
    
    def delete(self, p):
        """Removes the node at position p and returns its value."""
        return None

    def replace(self, p, e):
        """Replaces the value of the node at position p with e and returns the old value being replaced."""
        return None
    