class priority_queue:
    """Abstract base priority queue class."""
    class _Item:
        """Internal class that represents a key-value pair."""
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key
