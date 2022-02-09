from src.tree.linkedbinary_tree import linkedbinary_tree
from src.map.map import map

class tree_map(linkedbinary_tree, map):
    class Position(linkedbinary_tree.Position):
        def key(self):
            """Returns the key of the key-value pair referenced by the Position object."""
            pass

        def value(self):
            """Returns the value of the key-value pair referenced by the Position object."""
            pass

    # private utility methods

    def _subtree_search(self, p, k):
        """
        Searches the subtree rooted at p for key k and returns a Position of it if found.
        Returns the last touched key if search was unsuccessful.
        """
        pass

    def _subtree_first_position(self, p):
        """Returns a Position for the first item of the subtree rooted at p."""
        pass

    def _subtree_last_position(self, p):
        """Returns a Position for the last item of the subtree rooted at p."""
        pass

    # public methods; returns None if search was unsuccessful

    def first(self):
        """Returns a Position for the first item in the tree."""
        pass

    def last(self):
        """Returns a Position for the last item in the tree."""
        pass

    def before(self, p):
        """Returns a Position for the item before the one at Position p."""
        pass

    def after(self, p):
        """Returns a Position for the item after the one at Position p."""
        pass

    def find_position(self, k):
        """Returns a Position for the item with key k."""
        pass

    def find_min(self):
        """Returns the key-value pair with smallest key."""
        pass

    def find_max(self):
        """Returns the key-value pair with largest key."""
        pass

    def find_ge(self, k):
        """Returns the key-value pair with key greater than or equal to k."""
        pass

    def find_le(self, k):
        """Returns the key-value pair with key less than or equal to k."""
        pass

    def find_range(self, l, h):
        """
        Generator that iterates through all key-value pairs where the keys are in the interval
        [l, h)
        """
        pass

    def delete(self, p):
        """Deletes the item at Position p and updates the tree accordingly."""
        pass

    # magic method overrides

    def __getitem__(self, k):
        pass

    def __setitem__(self, k, v):
        pass

    def __delitem__(self, v):
        pass

    def __iter__(self):
        pass
