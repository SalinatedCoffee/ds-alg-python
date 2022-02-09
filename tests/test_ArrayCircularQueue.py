import pytest
from src.queue.arraycircular_queue import arraycircular_queue
from src.exceptions.PyDSError import QueueError

# could probably just do this inline but practice using fixtures
@pytest.fixture(name='default_queue')
def fixture_default_queue():
    """pytest fixture for default queue."""
    return arraycircular_queue()

def test_initialization(default_queue):
    """Test object initialization with default parameters."""
    assert default_queue.front() is None

def test_basic_enqueue_dequeue(default_queue):
    """Test enqueue / dequeue items."""
    default_queue.enqueue(1)
    default_queue.enqueue(1337)
    assert default_queue.front() == 1
    assert default_queue.dequeue() == 1
    assert default_queue.front() == 1337
    assert default_queue.dequeue() == 1337

def test_dequeue_from_empty(default_queue):
    """Test dequeuing item from empty queue."""
    with pytest.raises(QueueError.EmptyQueue):
        default_queue.dequeue()

def test_internal_resize_up(default_queue):
    """Test internal resize when queue is full."""
    for i in range(11):
        default_queue.enqueue(i)
    assert len(default_queue) == 11

def test_internal_resize_down(default_queue):
    """Test internal resize when queue is smaller than specified threshold."""
    for i in range(10):
        default_queue.enqueue(i)

    for i in range(9):
        default_queue.dequeue()
    assert default_queue.front() == 9
