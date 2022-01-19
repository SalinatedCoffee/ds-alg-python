from src.exceptions.PyDSError import QueueError

class arraycircular_queue:
    """Simple dynamic size queue that internally uses a list."""
    DEFAULT_INTERNAL_SIZE = 10
    DEFAULT_SIZEUP_FACTOR = 2
    DEFAULT_SIZEDOWN_FACTOR = 2
    DEFAULT_SIZEDOWN_THRESHOLD = 4

    def __init__(self, size=DEFAULT_INTERNAL_SIZE):
        self._data = [None] * size
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def _migrate(self, new_size):
        """Internal method that resizes the internal list."""
        if new_size < self._size:
            raise QueueError.MigrateSize("new size is smaller than number of current elements")
        temp = [None] * new_size
        for i in range(new_size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

    def front(self):
        """Returns the item at the front of the queue. Returns None when queue is empty."""
        if not self._size:
            return None
        return self._data[self._front]

    def enqueue(self, item):
        """Enqueues item to the front of the queue."""
        if len(self) == len(self._data):
            self._migrate(len(self) * self.DEFAULT_SIZEUP_FACTOR)
        self._data[(self._front + self._size) % len(self._data)] = item
        self._size += 1

    def dequeue(self):
        """Removes the item fron the front of the queue and returns it."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item from empty queue")
        temp = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if self._size < len(self._data) // self.DEFAULT_SIZEDOWN_THRESHOLD:
            self._migrate(len(self._data) // self.DEFAULT_SIZEDOWN_FACTOR)

        return temp
