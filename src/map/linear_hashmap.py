from src.map.hashmap import hashmap

class linear_hashmap(hashmap):
    """Simple hash map that internally uses open addressing (linear probing) to store data."""
    _AVAIL = object()   # sentinel object for evicted locations

    def _is_available(self, j):
        """Returns True if self._table[j] is available."""
        return not self._table[j] or self._table[j] is self._AVAIL

    def _find_slot(self, j, k):
        """
        Searches the table for key k in bucket j.
        Returns a tuple based on search results where (found:bool, index:int).
        If found == False, index will be the first available location for bucket j.
        Conversely, index will be the location of key k in the table.
        """
        available = None
        while True:
            if self._is_available(j):
                if not available:
                    available = j
                # None means end of cluster, so no match found
                if not self._table[j]:
                    return (False, available)
            elif self._table[j]._key == k:
                return (True, j)
            # assume hashmap._resize is working correctly, no sanity check
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, idx = self._find_slot(j, k)
        if not found:
            raise KeyError('Key error: ' + repr(k))
        return self._table[idx]._value

    def _bucket_setitem(self, j, k, v):
        found, idx = self._find_slot(j, k)
        if not found:
            self._table[idx] = self._Item(k, v)
            self._n += 1
        else:
            self._table[idx]._value = v

    def _bucket_delitem(self, j, k):
        found, idx = self._find_slot(j, k)
        if not found:
            raise KeyError('Key error: ' + repr(k))
        self._table[idx] = self._AVAIL

    def __iter__(self):
        """Iterates over all keys in the hash table."""
        for i in self._table:
            if isinstance(i, self._Item):
                yield i._key
