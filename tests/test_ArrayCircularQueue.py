from _pytest._code.code import _PYTEST_DIR
import pytest
from src.ArrayCircularQueue import ArrayCircularQueue
from src.PyDSError import *

# could probably just do this inline but practice using fixtures
@pytest.fixture
def default_queue():
    return ArrayCircularQueue()


def test_enqueue_dequeue(default_queue):
    with pytest.raises(EmptyQueueException):
        default_queue.dequeue()

    assert default_queue.front() == None

    for i in range(10):
        default_queue.enqueue(i)

    with pytest.raises(QueueOverCapacityException):
        default_queue.enqueue(11)

    assert default_queue.dequeue() == 0