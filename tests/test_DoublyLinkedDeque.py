import pytest
from src.DoublyLinkedDeque import DoublyLinkedDeque
from src.PyDSError import QueueError

@pytest.fixture(name='empty_dld')
def fixture_empty_dld():
    """pytest fixture for an empty deque."""
    return DoublyLinkedDeque()

def test_initialization(empty_dld):
    """Test object initialization."""
    assert len(empty_dld) == 0
    with pytest.raises(QueueError.EmptyQueue):
        empty_dld.delete_first()
    with pytest.raises(QueueError.EmptyQueue):
        empty_dld.delete_last()
    assert empty_dld.first() is None
    assert empty_dld.last() is None

def test_enqueue_dequeue(empty_dld):
    """Test item enqueue / dequeue."""
    empty_dld.insert_first(1)
    empty_dld.insert_first(3)
    empty_dld.insert_last(5)
    empty_dld.insert_last(7)
    assert len(empty_dld) == 4
    assert empty_dld.first() == 3
    assert empty_dld.last() == 7
    assert empty_dld.delete_first() == 3
    assert empty_dld.delete_last() == 7
    assert len(empty_dld) == 2
    assert empty_dld.first() == 1
    assert empty_dld.last() == 5
    empty_dld.delete_first()
    assert empty_dld.first() == 5
    assert empty_dld.last() == 5
    empty_dld.delete_last()
    assert len(empty_dld) == 0
