import pytest
from src.LinkedListQueue import LinkedListQueue
from src.PyDSError import QueueError

@pytest.fixture(name='empty_queue')
def fixture_empty_queue():
    """pytest fixture for empty linked list queue."""
    return LinkedListQueue()

def test_initialization(empty_queue):
    """Test object initialization."""
    with pytest.raises(QueueError.EmptyQueue):
        empty_queue.dequeue()
    assert empty_queue.front() is None
    assert len(empty_queue) == 0

def test_enqueue_dequeue(empty_queue):
    """Test enqueue / dequeue of items."""
    empty_queue.enqueue(3)
    empty_queue.enqueue(5)
    empty_queue.enqueue(7)
    assert len(empty_queue) == 3
    assert empty_queue.front() == 3
    empty_queue.dequeue()
    empty_queue.dequeue()
    assert len(empty_queue) == 1
    assert empty_queue.dequeue() == 7