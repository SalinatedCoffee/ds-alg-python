from attr import dataclass
from src.PyDSError import *

class ArrayCircularDeque():
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
        if new_size < self._size:
            raise MigrateSizeException("new size is smaller than number of current elements")
        temp = [None] * new_size
        for i in range(new_size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

    def front(self):
        if not self._size:
            return None
        return self._data[self._front]

    def end(self):
        if not self._size:
            return None
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def add_front(self, item):
        if len(self) == len(self._data):
            self._migrate(len(self) * self.DEFAULT_SIZEUP_FACTOR)
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = item
        self._size += 1

    def add_end(self, item):
        if len(self) == len(self._data):
            self._migrate(len(self) * self.DEFAULT_SIZEUP_FACTOR)
        self._data[(self._front + len(self)) % len(self._data)] = item
        self._size += 1
    
    def remove_front(self):
        if not self._size:
            raise EmptyQueueException("unable to dequeue item from empty queue")
        temp = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        return temp

    def remove_end(self):
        if not self._size:
            raise EmptyQueueException("unable to dequeue item form empty queue")
        temp = self._data[(self._front + len(self) - 1) % len(self._data)]
        self._size -= 1
        return temp