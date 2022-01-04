import pytest
from src.DoublyLinkedDeque import DoublyLinkedDeque

@pytest.fixture(name='empty_dld')
def fixture_empty_dld():
    """pytest fixture for an empty deque."""
    return DoublyLinkedDeque()

def test_initialization(empty_dld):
    """Test object initialization."""
    assert False

def test_enqueue_dequeue(empty_dld):
    """Test item enqueue / dequeue."""
    assert False
