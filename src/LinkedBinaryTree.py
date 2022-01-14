from src.BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Simple binary tree data structure that is internally structured with linked nodes."""
    class Position:
        """Object that represents the position of a node."""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Returns the value of the node represented by self."""
            return self._node._value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    class _Node:
        """Internal node object."""
        __slots__ = '_value', '_parent', '_left', '_right'
        def __init__(self, value=None, parent=None, left=None, right=None):
            self._value = value
            self._parent = parent
            self._left = left
            self._right = right

    def _validate(self, p) -> _Node:
        """Returns node at position p if it is a valid position within self."""
        if not isinstance(p, self.Position):
            raise TypeError('object is not of type Position')
        if p._container is not self:
            raise ValueError('Position object does not belong to this tree')
        if not self.is_root(p) and p._node._parent is None:
            raise ValueError('this Position object is no longer valid')
        return p._node

    def _make_position(self, node):
        """Returns a Position object corresponding to node."""
        return self.Position(self, node) if node is not None else None

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
        self._size = 1
        return self._make_position(self._root)


    def _add_left(self, p, e):
        """
        Creates a node with value e, sets it as the left child of the node at position p,
        and returns the corresponding Position object.
        Raises an error if the node at p already has a left child.
        """
        node = self._validate(p)
        if node._left:
            raise ValueError('attempted to add node as left child when one already exists')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Creates a node with value e, sets it as the right child of the node at position p,
        and returns the corresponding Position object.
        Raises an error if the node at p already has a right child.
        """
        node = self._validate(p)
        if node._right:
            raise ValueError('attempted to add node as right child when one already exists')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replaces the _value of the node at position p with e, and returns the previous value."""
        node = self._validate(p)
        old = p.element()
        node._value = e
        return old

    def _delete(self, p):
        """
        Removes node at position p, and attempts to reattach its ancestor to its parent.
        Returns the value of node at position p.
        Raises an error if the node has two children.
        """
        node = self._validate(p)
        if node._left and node._right:
            raise ValueError('attempted to remove node with two children')
        child = node._left if node._left else node._right
        if child:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            if node is node._parent._left:
                node._parent._left = child
            else:
                node._parent._right = child
        temp = p.element()
        node._value = node._parent = node._left = node._right = None
        self._size -= 1
        return temp

    def _attach(self, p, T1, T2):
        """
        Attatches two subtrees T1 and T2 to the node at position p as its children (L:T1, R:T2).
        Raises an error if node is not a leaf.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('attempted to attach subtrees to non-leaf node')
        if not type(self) is type(T1) is type(T2):
            raise TypeError('subtrees must be the same type as the tree being attached to')
        if len(T1):
            T1.root()._node._parent = node
            node._left = T1.root()._node
            self._size += len(T1)
            T1._size = 0
            T1._root = None
        if len(T2):
            T2.root()._node._parent = node
            node._right = T2.root()._node
            self._size += len(T2)
            T2._size = 0
            T2._root = None

    # override methods from BinaryTree

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    # override methods from Tree

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        node = self._validate(p)
        children = 0
        if node._left:
            children += 1
        if node._right:
            children += 1
        return children

    def __len__(self):
        return self._size
