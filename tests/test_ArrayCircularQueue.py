from _pytest._code.code import _PYTEST_DIR
import pytest
from src.ArrayCircularQueue import ArrayCircularQueue
from src.PyDSError import *

# could probably just do this inline but practice using fixtures
@pytest.fixture
def default_queue():
    return ArrayCircularQueue()

def test_initialization(default_queue):
    assert default_queue.front() == None

def test_basic_enqueue_dequeue(default_queue):
    default_queue.enqueue(1)
    default_queue.enqueue(1337)
    assert default_queue.front() == 1
    assert default_queue.dequeue() == 1
    assert default_queue.front() == 1337
    assert default_queue.dequeue() == 1337

def test_dequeue_from_empty(default_queue):
    with pytest.raises(EmptyQueueException):
        default_queue.dequeue()

def test_internal_resize_up(default_queue):
    for i in range(11):
        default_queue.enqueue(i)

    assert len(default_queue) == 11

def test_internal_resize_down(default_queue):
    for i in range(10):
        default_queue.enqueue(i)

    for i in range(9):
        default_queue.dequeue()

    assert default_queue.front() == 9