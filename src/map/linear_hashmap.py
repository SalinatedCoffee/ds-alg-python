from src.map.hashmap import hashmap

class linear_hashmap(hashmap):
    """Simple hash map that internally uses open addressing (linear probing) to store data."""
    _AVAIL = object()   # sentinel object for evicted locations

    def _is_available(self, j):
        """Returns True if self._table[j] is available."""
        pass

    def _find_slot(self, j, k):
        """
        Searches the table for key k in bucket j.
        Returns a tuple based on search results where (found:bool, index:int).
        If found == False, index will be the first available location for bucket j.
        Conversely, index will be the location of key k in the table.
        """
        pass

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_delitem(self, j, k):
        pass

    def __iter__(self):
        pass
