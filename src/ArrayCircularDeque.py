from src.PyDSError import QueueError

class ArrayCircularDeque():
    """Simple dynamic size deque that internally uses a list."""
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
        """Returns the item at the front of the deque. Returns None when deque is empty."""
        if not self._size:
            return None
        return self._data[self._front]

    def end(self):
        """Returns the item at the end of the deque. Returns None when deque is empty."""
        if not self._size:
            return None
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def add_front(self, item):
        """Adds item to the front of the deque."""
        if len(self) == len(self._data):
            self._migrate(len(self) * self.DEFAULT_SIZEUP_FACTOR)
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = item
        self._size += 1

    def add_end(self, item):
        """Adds item to the end of the deque."""
        if len(self) == len(self._data):
            self._migrate(len(self) * self.DEFAULT_SIZEUP_FACTOR)
        self._data[(self._front + len(self)) % len(self._data)] = item
        self._size += 1

    def remove_front(self):
        """Removes the item at the front of the deque and returns it."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item from empty queue")
        temp = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < len(self._data) // self.DEFAULT_SIZEDOWN_THRESHOLD and \
            self._size > self.DEFAULT_INTERNAL_SIZE:
            self._migrate(len(self._data) // self.DEFAULT_SIZEDOWN_FACTOR)
        return temp

    def remove_end(self):
        """Removes the item at the end of the deque and returns it."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item form empty queue")
        temp = self._data[(self._front + len(self) - 1) % len(self._data)]
        self._size -= 1
        if self._size < len(self._data) // self.DEFAULT_SIZEDOWN_THRESHOLD and \
            self._size > self.DEFAULT_INTERNAL_SIZE:
            self._migrate(len(self._data) // self.DEFAULT_SIZEDOWN_FACTOR)
        return temp
