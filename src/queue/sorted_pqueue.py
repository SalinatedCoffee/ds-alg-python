import src.queue.priority_queue as pqueue
import src.list.positional_list as plist
from src.exceptions.PyDSError import QueueError

class sorted_pqueue(pqueue.priority_queue):
    """Priority queue that uses a sorted linked list to store data."""
    def _find_min(self):
        """Returns a Position of the item with smallest key."""
        # return first item, since list is in ascending order
        if not len(self):
            raise QueueError.EmptyQueue('Queue is empty')
        return self._data.first()

    def __init__(self):
        self._data = plist.positional_list()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        """Adds a key-value pair to the queue."""
        item = self._Item(k, v)
        current = self._data.last()
        while current and current.element() > item:
            current = self._data.before(current)
        if not current:
            self._data.add_first(item)
        else:
            self._data.add_after(current, item)

    def min(self):
        """Returns, but does not remove, a tuple for the item with the smallest key."""
        min = self._find_min().element()
        return (min._key, min._value)

    def remove_min(self):
        """Removes the item with the smallest key and returns its tuple representation."""
        min = self._find_min()
        temp = min.element()
        self._data.delete(min)
        return (temp._key, temp._value)
