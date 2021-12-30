"""Custom errors / exceptions for various data structures."""

class QueueError():
    """Custom errors / exceptions for ArrayCircularQueue and ArrayCircularDequeue."""
    class EmptyQueue(Exception):
        """Raised when attempting to dequeue item from already empty queue."""

    class MigrateSize(Exception):
        """Raised when internal resize target is smaller than number of elements in queue."""

class StackError():
    """Custom errors / exceptions for LinkedListStack."""
    class Generic(Exception):
        """Generic error for stack."""
