from random import randrange
from src.map.map import map

_LOAD_FACTOR_THRESHOLD = 0.5 # Resize the table array when this load factor is reached
_RESIZE_FACTOR = 2   # Resize the table array by this constant

class hashmap(map):
    """Custom abstract base class for hashmap-like data structures."""
    def __init__(self, capacity=11, prime=109345121):
        self._table = capacity * [None]
        self._n = 0
        self._prime = prime
        self._scale = 1 + randrange(prime-1)
        self._shift = randrange(prime)
    
    def _hash_function(self, k):
        """
        Compute the hash of key k and map it to the table array using the Multiply-Add-and-Divide method.
        [(ai+b) mod p] mod N
        p = Arbitrary prime number (self._prime)
        a = Random integer in the range [0, p-1] (self._scale)
        b = Random integer in the range [0, p] (self._shift)
        N = Size of the bucket array (len(self._table))
        i = Hash generated from key k (hash(k))
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > int(len(self._table) * _LOAD_FACTOR_THRESHOLD):
            self._resize(_RESIZE_FACTOR * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        """Resizes self._table to size c."""
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    def _bucket_getitem(self, j, k):
        """
        Searches bucket j for an item with key k and returns the value of the item.
        Raises an error if the item is not found.
        """
        raise NotImplementedError()

    def _bucket_setitem(self, j, k, v):
        """
        If item with key k already exists in bucket j, overwrites the item's value with v.
        If item does not exist, insert a new item with key k and value v.
        """
        raise NotImplementedError()

    def _bucket_delitem(self, j, k):
        """
        Searches bucket j for an item with key k and deletes the item.
        Raises an error if the item is not found.
        """
        raise NotImplementedError()

    def __iter__(self):
        """Generator that iterates through all keys in the hashmap."""
        raise NotImplementedError()
