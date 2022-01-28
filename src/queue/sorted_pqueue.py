import src.queue.priority_queue as pqueue
import src.list.positional_list as plist
from src.exceptions.PyDSError import QueueError

class sorted_pqueue(pqueue.priority_queue):
    def _find_min(self):
        """Returns a Position of the item with smallest key."""
        pass

    def __init__(self):
        self._data = plist.positional_list()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        """Adds a key-value pair to the queue."""
        pass

    def min(self):
        """Returns, but does not remove, a tuple for the item with the smallest key."""
        pass

    def remove_min(self):
        """Removes the item with the smallest key and returns its tuple representation."""
        pass
