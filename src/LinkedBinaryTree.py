from src.BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class Position:
        def __init__(self, node):
            self._container = self
            self._node = node

        def element(self):
            return self._node._value

        def __eq__(self, other):
            pass

    class _Node:
        def __init__(self, value=None, parent=None, left=None, right=None):
            self._value = value
            self._parent = parent
            self._left = left
            self._right = right

    def add_root(self, p):
        pass

    def add_left(self, p, e):
        pass

    def add_right(self, p, e):
        pass

    def replace(self, p, e):
        pass

    def delete(self, p):
        pass

    def attach(self, p, T1, T2):
        pass



    def left(self, p):
        pass

    def right(self, p):
        pass



    def root(self):
        pass

    def parent(self, p):
        pass

    def num_children(self, p):
        pass

    def children(self, p):
        pass

    def __len__(self):
        pass
