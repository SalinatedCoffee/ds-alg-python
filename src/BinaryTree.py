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
        """Returns the sibling of node at position p."""
        parent = self.parent(p)
        if not parent:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self, p):
        """Generator that yields the children (in L->R order) of node at position p."""
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)
