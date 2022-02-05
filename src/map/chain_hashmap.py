from src.map.hashmap import hashmap
from src.map.unsorted_map import unsorted_map

class chain_hashmap(hashmap):
    """
    Simple hash map that internally uses separate chaining to store data.
    The buckets utilize an unsorted table map as implemented in src.map.unsorted_map.
    """
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError('Key error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        bucket = self._table[j]
        if not bucket:
            self._table[j] = unsorted_map()
        new = k not in self._table[j]   # if k is not already in bucket
        self._table[j][k] = v
        if new:                         # new item is inserted, update size
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError('Key error: ' + repr(k))
        del self._table[j][k]

    def __iter__(self):
        for bucket in self._table:
            if isinstance(bucket, unsorted_map):
                # bucket is explicitly typechecked, ignore pylint error
                # pylint: disable-next=not-an-iterable
                for item in bucket:
                    yield item  # __iter__ of unsorted_map already yields keys, return directly
