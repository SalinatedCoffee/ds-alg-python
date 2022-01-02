import pytest
from src.CircularLLQueue import CircularLLQueue
from src.PyDSError import QueueError

@pytest.fixture(name='empty_queue')
def fixture_empty_queue():
    return CircularLLQueue()

def test_initialization(empty_queue):
    with pytest.raises(QueueError.EmptyQueue):
        empty_queue.dequeue()
    assert empty_queue.front() is None
    assert len(empty_queue) == 0

def test_enqueue_dequeue(empty_queue):
    assert False

def test_rotate(empty_queue):
    assert False
