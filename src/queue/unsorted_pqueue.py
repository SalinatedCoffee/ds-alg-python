import src.queue.priority_queue as pqueue
import src.list.positional_list as plist
from src.exceptions.PyDSError import QueueError

class unsorted_pqueue(pqueue.priority_queue):
    """Priority queue that uses an unsorted linked list to store data."""
    def _find_min(self):
        """Returns a Position of the item with smallest key."""
        if not len(self):
            raise QueueError.EmptyQueue('Queue is empty')
        min = self._data.first()
        current = self._data.after(min)
        while current is not None:
            if min.element() > current.element():
                min = current
            current = self._data.after(current)
        
        return min

    def __init__(self):
        self._data = plist.positional_list()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        """Adds a key-value pair to the queue."""
        self._data.add_last(self._Item(k, v))

    def min(self):
        """Returns, but does not remove, a tuple for the item with the smallest key."""
        min = self._find_min().element()
        return (min._key, min._value)

    def remove_min(self):
        """Removes the item with the smallest key and returns its tuple representation."""
        min = self._find_min()
        ret = (min.element()._key, min.element()._value)
        self._data.delete(min)
        return ret
