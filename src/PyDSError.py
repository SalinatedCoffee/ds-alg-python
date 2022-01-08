"""Custom errors / exceptions for various data structures."""

class QueueError():
    """Custom errors / exceptions for queue objects."""
    class EmptyQueue(Exception):
        """Raised when attempting to dequeue item from already empty queue."""

    class MigrateSize(Exception):
        """Raised when internal resize target is smaller than number of elements in queue."""

class StackError():
    """Custom errors / exceptions for stack objects."""
    class EmptyStack(Exception):
        """Raised when attempting to pop item from already empty queue."""

class ListError():
    """Custom errors / exceptions for list objects."""
    class EmptyList(Exception):
        """Raised when attempting to remove item from already empty list."""