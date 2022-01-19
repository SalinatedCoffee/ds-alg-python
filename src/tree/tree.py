class tree:
    """Abstract base tree class."""
    class Position:
        """Nested position class that represents a position within the tree object."""
        def element(self):
            """Should return the value of the node represented by self."""
            raise NotImplementedError()

        def __eq__(self, other):
            """Should return True if Position other represents the same location."""
            raise NotImplementedError()

        def __ne__(self, other):
            """Should return True if Position other does not represent the same location."""
            raise not (self == other)

    def root(self):
        """Should return the root node of self."""
        raise NotImplementedError()

    def parent(self, p):
        """Should return the parent node of node represented by Position p."""
        raise NotImplementedError()

    def num_children(self, p):
        """Should return the number of children of the node represented by Position p."""
        raise NotImplementedError()

    def children(self, p):
        """Should return an iterable containing all child nodes of node at Position p."""
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def is_root(self, p):
        """Returns True if the node at Position p is the root of Tree self."""
        return self.root() == p

    def is_leaf(self, p):
        """Returns True if the node at Position p is a leaf of Tree self."""
        return self.num_children(p) == 0
