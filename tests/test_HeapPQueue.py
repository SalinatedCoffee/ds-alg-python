import pytest
import src.queue.heap_pqueue as pqueue
from src.exceptions.PyDSError import QueueError

@pytest.fixture(name='empty_pqueue')
def fixture_empty_pqueue():
    """pytest fixture that returns a new heap_pqueue object."""
    return pqueue.heap_pqueue()

@pytest.fixture(name='sample_pqueue')
def fixture_sample_pqueue():
    """pytest fixture that returns a binary tree constructed without triggering heap bubbling."""
    # insert nodes in this exact order to construct tree without triggering node swaps
    sample_tuples = [(4, 'C'), (5, 'A'), (6, 'Z'), (15, 'K'), (9, 'F'), (7, 'Q'), (20, 'B'), \
                    (16, 'X'), (25, 'J'), (14, 'E'), (12, 'H'), (11, 'S'), (13, 'W')]
    heap = pqueue.heap_pqueue()
    for i in sample_tuples:
        heap.add(i[0], i[1])
    if len(heap) != len(sample_tuples):
        raise Exception('Failed to construct tree')
    return heap

def test_initialization(empty_pqueue):
    """Tests object instantiation."""
    assert len(empty_pqueue) == 0
    with pytest.raises(QueueError.EmptyQueue):
        empty_pqueue.min()
    with pytest.raises(QueueError.EmptyQueue):
        empty_pqueue.remove_min()

def test_add_to_empty(empty_pqueue):
    """Tests the addition of items to an empty priority queue."""
    empty_pqueue.add(1, 'A')
    empty_pqueue.add(2, 'B')
    empty_pqueue.add(3, 'C')
    assert len(empty_pqueue) == 3
    assert empty_pqueue.min() == (1, 'A')

def test_remove_single(empty_pqueue):
    """Tests removing from a priority queue of size 1."""
    empty_pqueue.add(1, 'A')
    assert empty_pqueue.remove_min() == (1, 'A')
    assert len(empty_pqueue) == 0
    with pytest.raises(QueueError.EmptyQueue):
        empty_pqueue.min()

def test_upheap(sample_pqueue):
    """Tests the behavior of internal up-heap bubbling."""
    init_size = len(sample_pqueue)
    sample_pqueue.add(2, 'T')
    assert sample_pqueue.min() == (2, 'T')
    sample_pqueue.add(1, 'Y')
    assert sample_pqueue.min() == (1, 'Y')
    assert init_size + 2 == len(sample_pqueue)

def test_downheap(sample_pqueue):
    """Tests the behavior of internal down-heap bubbling."""
    init_size = len(sample_pqueue)
    assert sample_pqueue.remove_min() == (4, 'C')
    assert sample_pqueue.remove_min() == (5, 'A')
    assert init_size - 2 == len(sample_pqueue)
