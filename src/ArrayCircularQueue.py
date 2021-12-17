# TODO: rename to enqueue and dequeue, add method that returns first item without removing it
from src.PyDSError import *

class ArrayCircularQueue():
    def __init__(self, size=30):
        self._data = [None] * size
        self._front = 0
        self._size = 0
    
    def push(self, item):
        if self._size == len(self._data):
            raise QueueOverCapacityException("unable to push item to full queue")
        self._data[(self._front + self._size) % len(self._data)] = item
        self._size += 1
    
    def pop(self):
        if not self._size:
            raise EmptyQueueException("unable to pop item from empty queue")
        temp = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return temp