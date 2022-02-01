import src.queue.priority_queue as pqueue
from src.exceptions.PyDSError import QueueError

class heap_pqueue(pqueue.priority_queue):
    """Simple priority queue that uses an array-based heap(list) for internal storage."""
    def _parent(self, i):
        """Returns the index of the node's parent node."""
        return (i - 1) // 2

    def _left(self, i):
        """Returns the index of the node's left child."""
        return 2 * i + 1

    def _right(self, i):
        """Returns the index of the node's right child."""
        return 2 + i + 2

    def _has_left(self, i):
        """Returns True if the node has a left child."""
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        """Returns True if the node has a right child."""
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        """Swaps items located at indicies i and j."""
        # private method, so assumes valid indicies
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        """Runs up-heap bubbling starting at the current node."""
        if i == 0:
            return
        parent = self._parent(i)
        if self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, i):
        """Runs down-heap bubbling starting at the current node."""
        # if both children exists, compare current key with one with smaller key
        # if only left exists, compare current key with that
        # if heap prop is not satisfied swap nodes and recursively run downheap
        if self._has_left(i):
            left = self._left(i)
            min = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[min] > self._data[right]:
                    min = right
            if self._data[min] < self._data[i]:
                self._swap(min, i)
                self._downheap(min)
                
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        """Adds a key-value pair to the queue."""
        self._data.append(self._Item(k, v))
        self._upheap(len(self._data) - 1)

    def min(self):
        """Returns, but does not remove, a tuple for the item with the smallest key."""
        if not len(self):
            raise QueueError.EmptyQueue('Priority queue is empty')
        ret = self._data[0]
        return (ret._key, ret._value)

    def remove_min(self):
        """Removes the item with the smallest key and returns its tuple representation."""
        # modify this method for in-place heapsort
        if not len(self):
            raise QueueError.EmptyQueue('Priotity queue is empty')
        self._swap(0, len(self) - 1)
        ret = self._data.pop()
        self._downheap(0)
        return (ret._key, ret._value)
