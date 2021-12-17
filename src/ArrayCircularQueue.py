# TODO: rename to enqueue and dequeue, add method that returns first item without removing it
# impliment dynamic size adjustment (factor of 2 for size increase, factor of .5 for decrease)
# size should be decreased when elements are 1/4 of current capacity
from src.PyDSError import *

class ArrayCircularQueue():
    def __init__(self, size=30):
        self._data = [None] * size
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size
    
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