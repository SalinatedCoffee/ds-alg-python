import pytest
from src.ArrayCircularDeque import ArrayCircularDeque
from src.PyDSError import *

@pytest.fixture
def default_deque():
    return ArrayCircularDeque()

def test_initialization(default_deque):
    assert default_deque.front() == None
    assert default_deque.end() == None

def test_add_remove_front(default_deque):
    default_deque.add_front(1)
    default_deque.add_front(2)
    assert default_deque.front() == 2
    default_deque.remove_front()
    assert default_deque.front() == 1
    default_deque.remove_front()
    assert default_deque.front() == None

def test_add_remove_end(default_deque):
    default_deque.add_end(1)
    default_deque.add_end(2)
    assert default_deque.end() == 2
    default_deque.remove_end()
    assert default_deque.end() == 1
    default_deque.remove_end()
    assert default_deque.end() == None

def test_internal_resize_up(default_deque):
    for i in range(11):
        default_deque.add_end(i)
    assert default_deque.end() == 10

def test_internal_resize_down(default_deque):
    for i in range(10):
        default_deque.add_end(i)
    for i in range(9):
        default_deque.remove_end()
    assert default_deque.end() == 0