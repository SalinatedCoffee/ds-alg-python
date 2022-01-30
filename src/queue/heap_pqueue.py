import src.queue.priority_queue as pqueue
from src.exceptions.PyDSError import QueueError

class heap_pqueue(pqueue.priority_queue):
    def _parent(self):
        """Returns the index of the node's parent node."""
        #(i-1)//2
        pass

    def _left(self):
        """Returns the index of the node's left child."""
        # 2i+1
        pass

    def _right(self):
        """Returns the index of the node's right child."""
        # 2i+2
        pass

    def _has_left(self):
        """Returns True if the node has a left child."""
        pass

    def _has_right(self):
        """Returns True if the node has a right child."""
        pass

    def _swap(self, i, j):
        """Swaps items located at indicies i and j."""
        pass

    def _upheap(self):
        """Runs up-heap bubbling starting at the current node."""
        pass

    def _downheap(self):
        """Runs down-heap bubbling starting at the current node."""
        pass

    def __init__(self):
        pass

    def __len__(self):
        pass

    def add(self):
        """Adds a key-value pair to the queue."""
        pass

    def min(self):
        """Returns, but does not remove, a tuple for the item with the smallest key."""
        pass

    def remove_min(self):
        """Removes the item with the smallest key and returns its tuple representation."""
        pass
