from src.exceptions.PyDSError import QueueError
from src.list.doublylinked_list import doublylinked_list

class doublylinked_deque(doublylinked_list):
    """Simple deque using a doubly linked list as internal storage."""
    def first(self):
        """Returns the value of the first item in the deque."""
        if not self._size:
            return None
        return self._header._next._value

    def last(self):
        """Returns the value of the last item in the deque."""
        if not self._size:
            return None
        return self._trailer._prev._value
    
    def insert_first(self, item):
        """Inserts a new node at the front of the deque with item as its value."""
        self._insert_between(item, self._header, self._header._next)

    def insert_last(self, item):
        """Inserts a new node at the end of the deque with item as its value."""
        self._insert_between(item, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Removes the node at the front of the deque and returns its value."""
        if not self._size:
            raise QueueError.EmptyQueue("unable to dequeue item from empty queue")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Removes the node at the end of the deque and returns its value."""
        if not self._size:
            raise QueueError.EmptyQueue("umable to dequeue item from empty queue")
        return self._delete_node(self._trailer._prev)
