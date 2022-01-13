from src.Tree import Tree

class BinaryTree(Tree):
    """Abstract base binary tree class."""
    def left(self, p):
        """Should return the left child of node at position p."""
        raise NotImplementedError()

    def right(self, p):
        """Should return the right child of node at position p."""
        raise NotImplementedError()

    def sibling(self, p):
        """Should return the sibling of node at position p."""
        raise NotImplementedError()
