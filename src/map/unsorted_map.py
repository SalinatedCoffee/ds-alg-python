from src.map.map import map

class unsorted_map(map):
    """Simple table map that uses an unsorted list for internal storage."""
    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for i in self._table:
            if i._key == k:
                return i._value
        raise KeyError('Key error: ' + repr(k))

    def __setitem__(self, k, v):
        for i in self._table:
            if i._key == k:
                i._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for n, i in enumerate(self._table):
            if i._key == k:
                self._table.pop(n)
                return
        raise KeyError('Key error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for i in self._table:
            yield i._key
