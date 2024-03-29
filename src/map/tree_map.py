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

    def _relink(self, parent, child, make_left_child:bool):
        """Link child node to parent."""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """Rotate p above parent."""
        x = p._node
        y = p._parent
        z = y._parent
        if z is None:       # parent is root, configure x as new root
            self._root = x
            x._parent = None
        else:               # else, attach x to z in lieu of y
            self._relink(z, x, y == z._left)
        if x == y._left:
            # x was left child of y, attach right subtree of x as left child of y
            # and attach y as right subtree of x
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            # else, attach left subtree of x as right child of y
            # and attach y as left subtree of x
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        """Perform trinode restructure of Position x with ancestors."""
        y = self.parent(x)
        z = self.parent(y)
        # check if nodes are in a single-rotation configuration (connected to same sides)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x

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
            self._rebalance_access(res)
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
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    # magic method overrides

    def __getitem__(self, k):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None:       # tree empty
            raise KeyError('Key error: ' + repr(k))
        elif p.key() != k:  # no hit on search
            self._rebalance_access(p)
            raise KeyError('Key error: ' + repr(k))
        return p.value()

    def __setitem__(self, k, v):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None:
            p = self._add_root(self._Item(k, v))
        elif p.key() != k:
            if k < p.key():
                p = self._add_left(p, self._Item(k, v))
            else:
                p = self._add_right(p, self._Item(k, v))
        else:
            p.element()._value = v
            self._rebalance_access(p)
            return
        self._rebalance_insert(p)

    def __delitem__(self, k):
        p = self._subtree_search(self.root(), k) if self.root() is not None else None
        if p is None:       # tree empty
            raise KeyError('Key error: ' + repr(k))
        elif p.key() != k:  # no hit on search
            self._rebalance_access(p)
            raise KeyError('Key error: ' + repr(k))
        self.delete(p)

    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current.key()
            current = self.after(current)

    # rebalance hooks for balanced tree subclasses

    def _rebalance_access(self, p): pass

    def _rebalance_insert(self, p): pass

    def _rebalance_delete(self, p): pass
