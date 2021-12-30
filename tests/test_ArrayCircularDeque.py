import pytest
from src.ArrayCircularDeque import ArrayCircularDeque
from src.PyDSError import QueueError

@pytest.fixture(name='default_deque')
def fixture_default_deque():
    """pytest fixture for default deque."""
    return ArrayCircularDeque()

def test_initialization(default_deque):
    """Test object initialization with default parameters."""
    assert default_deque.front() is None
    assert default_deque.end() is None

def test_add_remove_front(default_deque):
    """Test enqueue / dequeue items from front."""
    default_deque.add_front(1)
    default_deque.add_front(2)
    assert default_deque.front() == 2
    default_deque.remove_front()
    assert default_deque.front() == 1
    default_deque.remove_front()
    assert default_deque.front() is None

def test_dequeue_from_empty(default_deque):
    """Test dequeuing item from empty queue."""
    with pytest.raises(QueueError.EmptyQueue):
        default_deque.remove_front()

    with pytest.raises(QueueError.EmptyQueue):
        default_deque.remove_end()

def test_add_remove_end(default_deque):
    """Test enqueue / dequeue items from end."""
    default_deque.add_end(1)
    default_deque.add_end(2)
    assert default_deque.end() == 2
    default_deque.remove_end()
    assert default_deque.end() == 1
    default_deque.remove_end()
    assert default_deque.end() is None
def test_internal_resize_up(default_deque):
    """Test internal resize when queue is full."""
    for i in range(11):
        default_deque.add_end(i)
    assert default_deque.end() == 10

def test_internal_resize_down(default_deque):
    """Test internal resize when queue is smaller than specified threshold."""
    for i in range(10):
        default_deque.add_end(i)
    for i in range(9):
        default_deque.remove_end()
    assert default_deque.end() == 0

def test_bidirectional_add_remove(default_deque):
    """Test enqueue / dequeue from front / back simultaneously."""
    default_deque.add_front(1)
    default_deque.add_front(2)
    assert default_deque.front() == 2
    assert default_deque.end() == 1
    default_deque.add_end(3)
    assert default_deque.end() == 3
    default_deque.remove_front()
    default_deque.remove_end()
    assert default_deque.front() == 1
    assert default_deque.end() == 1
