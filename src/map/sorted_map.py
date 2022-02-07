from src.map.map import map

class sorted_map(map):
    """
    Simple map object that uses a sorted list to store data internally.
    Supports inexact searching on existing keys.
    """
    def _find_index(self, k, l, h):
        """
        Performs a binary search for k over the range [l, h] in self._table.
        If key k is found, returns the index for k.
        If key k is not found, but the range contains keys larger than k,
            returns index of the first item with larger key than k.
        If none of the keys in the range are larger than k, returns h + 1.
        """
        # if range is malformed, return high + 1
        if l > h:
            return h + 1
        m = (l + h) // 2
        if self._table[m]._key == k:
            return m
        elif self._table[m]._key < k:
            return self._find_index(k, m+1, h)
        return self._find_index(k, l, m-1)

    def __init__(self):
        # table will be sorted in ascending order
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        # if table is empty, self._find_index(k, 0, -1) -> 0
        i = self._find_index(k, 0, len(self._table)-1)
        if len(self._table) == i or self._table[i]._key != k:
            raise KeyError('Key error: ' + repr(k))
        return self._table[i]._value

    def __setitem__(self, k, v):
        i = self._find_index(k, 0, len(self._table)-1)
        if len(self._table) == i:
            self._table.append(self._Item(k, v))
        elif self._table[i]._key == k:
            self._table[i]._value = v
        else:
            self._table.insert(i, self._Item(k, v))

    def __delitem__(self, k):
        i = self._find_index(k, 0, len(self._table)-1)
        if len(self._table) == i or self._table[i]._key != k:
            raise KeyError('Key error: ' + repr(k))
        self._table.pop(i)

    def __iter__(self):
        """Iterate over all keys in the map."""
        for i in self._table:
            yield i._key

    def __reversed__(self):
        """Iterate over all keys in the map, in reverse order."""
        for i in reversed(self._table):
            yield i._key

    # access methods return None if no result was found

    def find_min(self):
        """Returns the key-value pair with the smallest key."""
        if len(self._table) == 0:
            return None
        else:
            return (self._table[0]._key, self._table[0]._value)

    def find_max(self):
        """Returns the key-value pair with the largest key."""
        if len(self._table) == 0:
            return None
        else:
            return (self._table[-1]._key, self._table[-1]._value)

    def find_ge(self, k):
        """Returns the key-value pair with key larger than or equal to k."""
        pass

    def find_lt(self, k):
        """Returns the key-value pair with key smaller than k."""
        pass

    def find_gt(self, k):
        """Returns the key-value pair with key greater than k."""
        pass

    def find_le(self, k):
        """Returns the key-value pair with key smaller than or equal to k."""
        pass

    def find_range(self, l, h):
        """
        Generator that iterates through all keys in range [l, h).
        If None is passed as a parameter for l, the iteration begins from the start of the table.
        (and vice versa for h)
        """
        pass
