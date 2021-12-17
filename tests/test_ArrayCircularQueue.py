from _pytest._code.code import _PYTEST_DIR
import pytest
from src.ArrayCircularQueue import ArrayCircularQueue
from src.PyDSError import *

# could probably just do this inline but practice using fixtures
@pytest.fixture
def queue_with_size_10():
    return ArrayCircularQueue(10)


def test_push_pop(queue_with_size_10):
    queue_test = queue_with_size_10
    with pytest.raises(EmptyQueueException):
        queue_test.dequeue()

    for i in range(10):
        queue_test.enqueue(i)

    with pytest.raises(QueueOverCapacityException):
        queue_test.dequeue(11)

    assert queue_test.pop() == 0