from src.BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    class _Node:
        __slots__ = '_value', '_parent', '_left', '_right'
        def __init__(self, value=None, parent=None, left=None, right=None):
            self._value = value
            self._parent = parent
            self._left = left
            self._right = right

    def _validate(self, p):
        """Returns true if Position p is a valid position within self."""
        pass

    def _make_position(self, node):
        """Returns a Position object corresponding to node."""
        if node is None:
            return None
        return self.Position(self, node)

    def __init__(self):
        self._root = None
        self._size = 0

    def _add_root(self, e):
        """
        Creates a node with value e, sets it as self's root, and returns a Position object corresponding to it.
        Raises an error if self is not empty(already has a root).
        """
        if self._size:
            raise ValueError('attempted to create root node for nonempty tree')
        self._root = self._Node(e)
        return self._make_position(self._root)


    def _add_left(self, p, e):
        """
        Creates a node with value e, sets it as the left child of the node at position p,
        and returns the corresponding Position object.
        Raises an error if the node at p already has a left child.
        """
        if p._node._left:
            raise ValueError('attempted to add node as left child when one already exists')
        p._node._left = self._Node(e, p._node)
        return self._make_position(p._node._left)

    def _add_right(self, p, e):
        """
        Creates a node with value e, sets it as the right child of the node at position p,
        and returns the corresponding Position object.
        Raises an error if the node at p already has a right child.
        """
        if p._node._right:
            raise ValueError('attempted to add node as right child when one already exists')
        p._node._right = self._Node(e, p._node)
        return self._make_position(p._node._right)

    def _replace(self, p, e):
        """Replaces the _value of the node at position p with e, and returns the previous value."""
        self._validate(p)
        old = p.element()
        p._node._value = e
        return old

    def _delete(self, p):
        """
        Removes node at position p, and attempts to reattach its ancestor to its parent.
        Raises an error if the node has two children.
        """
        self._validate(p)
        if p._node._left and p._node._right:
            raise ValueError('attempted to remove node with two children')

    def _attach(self, p, T1, T2):
        """
        Attatches two subtrees T1 and T2 to the node at position p as its children (L:T1, R:T2).
        Raises an error of node is not a leaf.
        """
        pass

    # override methods from BinaryTree

    def left(self, p):
        pass

    def right(self, p):
        pass

    # override methods from Tree

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        pass

    def num_children(self, p):
        pass

    def children(self, p):
        pass

    def __len__(self):
        return self._size
