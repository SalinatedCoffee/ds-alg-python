from src.PyDSError import QueueError
from src.DoublyLinkedList import DoublyLinkedList

class DoublyLinkedDeque(DoublyLinkedList):
    """Simple deque using a doubly linked list as internal storage."""
    def first(self):
        """Returns the value of the first item in the deque."""
        return None

    def last(self):
        """Returns the value of the last item in the deque."""
        return None
    
    def insert_first(self, item):
        """Inserts a new node at the front of the deque with item as its value."""
        return None

    def insert_last(self, item):
        """Inserts a new node at the end of the deque with item as its value."""
        return None

    def delete_first(self):
        """Removes the node at the front of the deque and returns its value."""
        return None

    def delete_last(self):
        """Removes the node at the end of the deque and returns its value."""
        return None
