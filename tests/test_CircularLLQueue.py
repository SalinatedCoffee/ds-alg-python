import pytest
from src.CircularLLQueue import CircularLLQueue
from src.PyDSError import QueueError

@pytest.fixture(name='empty_queue')
def fixture_empty_queue():
    """pytest fixture for empty queue."""
    return CircularLLQueue()

def test_initialization(empty_queue):
    """Test object initialization."""
    with pytest.raises(QueueError.EmptyQueue):
        empty_queue.dequeue()
    assert empty_queue.front() is None
    assert len(empty_queue) == 0

def test_enqueue_dequeue(empty_queue):
    """Test basic enqueue / dequeue of items."""
    empty_queue.enqueue(3)
    empty_queue.enqueue(5)
    empty_queue.enqueue(7)
    assert len(empty_queue) == 3
    assert empty_queue.front() == 3
    empty_queue.dequeue()
    empty_queue.dequeue()
    assert empty_queue.dequeue() == 7
    assert len(empty_queue) == 0

def test_rotate(empty_queue):
    """Test basic queue rotation."""
    empty_queue.enqueue(3)
    empty_queue.enqueue(5)
    empty_queue.enqueue(7)
    empty_queue.enqueue(9)
    empty_queue.enqueue(11)
    assert len(empty_queue) == 5
    assert empty_queue.front() == 3
    empty_queue.rotate()
    assert empty_queue.front() == 5
    empty_queue.rotate()
    empty_queue.rotate()
    assert empty_queue.front() == 9

def test_comprehensive_operations(empty_queue):
    """Test item enqueue / dequeue combined with queue rotations."""
    empty_queue.enqueue(1)
    empty_queue.enqueue(3)
    empty_queue.enqueue(5)
    empty_queue.enqueue(7)
    assert len(empty_queue) == 4
    assert empty_queue.front() == 1
    empty_queue.rotate()
    empty_queue.rotate()
    assert empty_queue.front() == 5
    empty_queue.dequeue()
    empty_queue.rotate()
    assert empty_queue.front() == 1
    empty_queue.enqueue(2)
    empty_queue.enqueue(4)
    assert len(empty_queue) == 5
    for _ in range(3):
        empty_queue.rotate()
    assert empty_queue.front() == 2
    for _ in range(4):
        empty_queue.dequeue()
    assert empty_queue.front() == 7
