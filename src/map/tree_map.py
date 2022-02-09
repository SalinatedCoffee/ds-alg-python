from src.tree.linkedbinary_tree import linkedbinary_tree
from src.map.map import map

class tree_map(linkedbinary_tree, map): # multiple inheritance, but map only implements _Item
    class Position(linkedbinary_tree.Position):
        def key(self):
            """Returns the key of the key-value pair referenced by the Position object."""
            return self.element()._key

        def value(self):
            """Returns the value of the key-value pair referenced by the Position object."""
            return self.element()._value

    # private utility methods

    def _subtree_search(self, p, k):
        """
        Searches the subtree rooted at p for key k and returns a Position of it if found.
        Returns the last touched key if search was unsuccessful.
        """
        if p.key() == k:
            return p
        elif p.key() > k and self.left(p) is not None:
            return self._subtree_search(self.left(p), k)
        elif p.key() < k and self.right(p) is not None:
            return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """Returns a Position for the first item of the subtree rooted at p."""
        current = p
        while self.left(current):
            current = self.left(current)
        return current

    def _subtree_last_position(self, p):
        """Returns a Position for the last item of the subtree rooted at p."""
        current = p
        while self.right(current):
            current = self.right(current)
        return current

    # public methods; returns None if search was unsuccessful

    def first(self):
        """Returns a Position for the first item in the tree."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Returns a Position for the last item in the tree."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Returns a Position for the item before the one at Position p."""
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            current = p
            parent = self.parent(p)
            while parent is not None and self.left(parent) == current:
                current = parent
                parent = self.parent(current)
            return parent

    def after(self, p):
        """Returns a Position for the item after the one at Position p."""
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            current = p
            parent = self.parent(p)
            while parent is not None and self.right(parent) == current:
                current = parent
                parent = self.parent(current)
            return parent

    def find_position(self, k):
        """Returns a Position for the item with key k."""
        if len(self) > 0:
            res = self._subtree_search(self.root(), k)
            if res.key() == k:
                return res
        return None

    def find_min(self):
        """Returns the key-value pair with smallest key."""
        res = self.first()
        return (res.key(), res.value()) if res is not None else None

    def find_max(self):
        """Returns the key-value pair with largest key."""
        res = self.last()
        return (res.key(), res.value()) if res is not None else None

    def find_ge(self, k):
        """Returns the key-value pair with key greater than or equal to k."""
        res = self._subtree_search(self.root(), k) if self.root() is not None else None
        if res is not None and res.key() < k:
            res = self.after(res)
        return (res.key(), res.value()) if res is not None else None

    def find_le(self, k):
        """Returns the key-value pair with key less than or equal to k."""
        res = self._subtree_search(self.root(), k) if self.root() is not None else None
        if res is not None and res.key() > k:
            res = self.before(res)
        return (res.key(), res.value()) if res is not None else None

    def find_range(self, l, h):
        """
        Generator that iterates through all key-value pairs where the keys are in the interval
        [l, h)
        """
        # set range for params passed as None
        if l is None:
            l = self.first().key()
        if h is None:
            h = self.last().key()
        # map is empty or invalid range was supplied
        if len(self) == 0 or l >= h:
            return
        current = self._subtree_search(self.root(), l) if self.root() is not None else None
        if current is not None and current.key() < l:
            current = self.after(current)
        while current and current.key() < h:
            yield (current.key(), current.value())
            current = self.after(current)

    def delete(self, p):
        """Deletes the item at Position p and updates the tree accordingly."""
        self._validate(p)
        # both children present, promote largest item of left subtree to position p
        if self.left(p) and self.right(p):
            r = self._subtree_last_position(self.left(p))
            self._replace(p, r.element())
            p = r
        self._delete(p)

    # magic method overrides

    def __getitem__(self, k):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None or p.key() != k:
            raise KeyError('Key error: ' + repr(k))
        return p.value()

    def __setitem__(self, k, v):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None:
            self._add_root(self._Item(k, v))
        elif p.key() != k:
            if k < p.key():
                self._add_left(p, self._Item(k, v))
            else:
                self._add_right(p, self._Item(k, v))
        else:
            p.element()._value = v

    def __delitem__(self, k):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None or p.key() != k:
            raise KeyError('Key error: ' + repr(k))
        else:
            self.delete(p)

    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current.key()
            current = self.after(current)
