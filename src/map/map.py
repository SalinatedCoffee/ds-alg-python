from collections.abc import MutableMapping

class map(MutableMapping):
    """Custom abstract base class for map-like data structures."""
    class _Item:
        """Nested class that represents a key-value pair."""
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return self._key != other._key

        def __lt__(self, other):
            return self._key < other._key
