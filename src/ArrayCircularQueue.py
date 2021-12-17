# TODO: impliment dynamic size adjustment (factor of 2 for size increase, factor of .5 for decrease)
# size should be decreased when elements are 1/4 of current capacity
from src.PyDSError import *

class ArrayCircularQueue():
    DEFAULT_INTERNAL_SIZE = 10

    def __init__(self, size=DEFAULT_INTERNAL_SIZE):
        self._data = [None] * size
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def _migrate(self, new_size):
        if new_size < self._size:
            raise MigrateSizeException("new internal size is smaller than number of current elements")
        temp = [None] * new_size
        for i in range(new_size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0
    
    def front(self):
        if not self._size:
            return None
        return self._data[self._front]

    def enqueue(self, item):
        if len(self) == len(self._data):
            raise QueueOverCapacityException("unable to enqueue item to full queue")
        self._data[(self._front + self._size) % len(self._data)] = item
        self._size += 1
    
    def dequeue(self):
        if not self._size:
            raise EmptyQueueException("unable to dequeue item from empty queue")
        temp = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return temp