import pytest
import src.queue.sorted_pqueue as pqueue
from src.exceptions.PyDSError import QueueError

LIST_ITEMS = [(7, 'one'), (3, 'two'), (5, 'three'), (1, 'four'), (9, 'five')]

@pytest.fixture(name='empty_pqueue')
def fixture_empty_pqueue():
    return pqueue.sorted_pqueue()

def test_initialization(empty_pqueue):
    """Test object initialization."""
    assert len(empty_pqueue) == 0
    with pytest.raises(QueueError.EmptyQueue):
        empty_pqueue.min()
    with pytest.raises(QueueError.EmptyQueue):
        empty_pqueue.remove_min()

def test_add_items(empty_pqueue):
    """Test addition of items."""
    for n, i in enumerate(LIST_ITEMS):
        k, v = i
        empty_pqueue.add(k, v)
        assert len(empty_pqueue) == n + 1
    assert len(empty_pqueue) == len(LIST_ITEMS)

def test_remove_items(empty_pqueue):
    """Test removal of items."""
    for i in LIST_ITEMS:
        k, v = i
        empty_pqueue.add(k, v)
    empty_pqueue.remove_min()
    assert len(empty_pqueue) == len(LIST_ITEMS) - 1
    for i in range(len(LIST_ITEMS) - 1):
        empty_pqueue.remove_min()
    assert len(empty_pqueue) == 0

def test_find_min(empty_pqueue):
    """Test minimum key search."""
    for i in LIST_ITEMS:
        k, v = i
        empty_pqueue.add(k, v)
    assert empty_pqueue.min() == LIST_ITEMS[3]
    assert empty_pqueue.remove_min() == LIST_ITEMS[3]
    assert empty_pqueue.remove_min() == LIST_ITEMS[1]
    assert empty_pqueue.remove_min() == LIST_ITEMS[2]
    assert empty_pqueue.remove_min() == LIST_ITEMS[0]
    assert empty_pqueue.remove_min() == LIST_ITEMS[4]
